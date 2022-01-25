#ifndef SWIMMER
#define SWIMMER

#include "params.hpp"
#include "skeleton_swimmer.hpp"

namespace MicroSwimmer
{
using namespace Eigen;

SkeletonSwimmer::SkeletonSwimmer(int model_type, bool on_record=false, double action_interval=0.5, double max_arm_length=1.5, double displacement_gain=1.0, double energy_gain=1.0, bool consider_energy=false, bool random_init_states=false) : 
  ON_RECORD(          on_record                                  ), 
  DISPLACEMENT_GAIN(  displacement_gain                          ), 
  ENERGY_GAIN(        energy_gain                                ), 
  CONSIDER_ENERGY(    consider_energy                            ), 
  RANDOM_INIT_STATES( random_init_states                         ), 
  ACTION_INTERVAL(    action_interval                            ), 
  L_MAX(              max_arm_length                             ), 
  SWIMMER_TYPE(       model_type                                 ),
  RUNFILE_PATH(       std::filesystem::current_path()            ),
  MAX_STEP(           static_cast<int>(MAX_TIME/action_interval) ),
  MAX_ITER(           static_cast<int>(action_interval/DT)       )
{
  std::string models_dir_path = this->RUNFILE_PATH.string() + MODEL_LOAD_PATH + "/type_" + std::to_string(this->SWIMMER_TYPE) + "/";

  /* load number of spheres and arms */
  std::ifstream num_in(models_dir_path+"num_states.txt", std::ios::in);
  if(!num_in){
    std::cout << "[self ERROR] No file \"num_states.txt\"" << std::endl;
    std::exit(0);
  }
  num_in >> this->n_spheres;
  num_in >> this->n_arms;
  this->n_sphere_states = 3 * this->n_spheres;
  this->n_arm_states    = 3 * this->n_arms;
  this->init_sphere_positions = VectorXd::Zero(this->n_sphere_states);
  this->incident_matrix_arm2sph    = MatrixXd::Zero(this->n_sphere_states, this->n_arm_states);

  /* load initial positions */
  std::ifstream init_in(models_dir_path+"init_pos.txt", std::ios::in);
  if(!init_in){
    std::cout << "[self ERROR] No file \"init_pos.txt\"" << std::endl;
    std::exit(0);
  }
  for(size_t id_sphere = 0; id_sphere < this->n_spheres; ++id_sphere){
    for(unsigned int id_dim = 0; id_dim < 3; ++id_dim){
      init_in >> this->init_sphere_positions(3*id_sphere + id_dim);
    }
  }
  // std::cout << this->init_sphere_positions.transpose() << std::endl;

  // set gravity point to zero point
  Vector3d centroid_pos = Vector3d::Zero();
  for(size_t id_sphere = 0; id_sphere < this->n_spheres; ++id_sphere){
    centroid_pos(0) += this->init_sphere_positions(3*id_sphere + 0);
    centroid_pos(1) += this->init_sphere_positions(3*id_sphere + 1);
    centroid_pos(2) += this->init_sphere_positions(3*id_sphere + 2);
  }
  centroid_pos /= this->n_spheres;
  
  for(size_t id_sphere = 0; id_sphere < this->n_spheres; ++id_sphere){
    this->init_sphere_positions.segment(3*id_sphere, 3) -= centroid_pos;
  }
  // std::cout << this->init_sphere_positions.transpose() << std::endl;

  /* load connection information matrix */
  std::ifstream matrix_in(models_dir_path+"incidence_matrix.txt", std::ios::in);
  if(!matrix_in){
    std::cout << "[self ERROR] No file \"incidence_matrix.txt\"" << std::endl;
    std::exit(0);
  }
  for(size_t i = 0; i < this->n_spheres; ++i){
    for(size_t j = 0; j < this->n_arms; ++j){
      int val;
      matrix_in >> val;
      if(val == 1){
        this->incident_matrix_arm2sph.block(3*i, 3*j, 3, 3) = Matrix3d::Identity();
      }else if(val == -1){
        this->incident_matrix_arm2sph.block(3*i, 3*j, 3, 3) = -Matrix3d::Identity();
      }
    }
  }
  this->target_unit_vec = Vector3d::UnitX();

  // For Quaternion
  std::ostringstream dim_oss;
  dim_oss << this->SWIMMER_TYPE;
  auto dim_iss = std::istringstream(
      dim_oss.str().substr(0, 1)
      );
  dim_iss >> this->swimmer_dim;
}

SkeletonSwimmer::~SkeletonSwimmer()
{
  if(fout.is_open()){
    fout.close();
  }
}

//std::vector<double> SkeletonSwimmer::reset()
VectorXd SkeletonSwimmer::reset()
{
  /* Set record file */
  if(fout.is_open()){
    fout.close();
  }
  if(this->ON_RECORD){
    std::stringstream record_file_name;
    if(this->CONSIDER_ENERGY == true){
      record_file_name << "type" << this->SWIMMER_TYPE
        << "_radius" << A
        << "_interval" << this->ACTION_INTERVAL
        << "_maxlength" << this->L_MAX 
        << "_withEnergy" 
        << ".csv";
    }else{
      record_file_name << "type" << this->SWIMMER_TYPE
        << "_radius" << A
        << "_interval" << this->ACTION_INTERVAL
        << "_maxlength" << this->L_MAX 
        << "_withoutEnergy"
        << ".csv";
    }
    std::string full_path = RUNFILE_PATH.string() + OUT_DIRECTORY_PATH + record_file_name.str();
    fout.open(full_path, std::ios::out);
    if(!fout){
      std::cout << "[self ERROR] CANNOT MAKE NEW RESULT FILE." << std::endl;
      std::exit(0);
    }
    /* Header */
    fout << "Time" << ",";
    for(size_t id_sph = 0; id_sph < this->n_spheres; ++id_sph){
      fout << "sphere_pos_" << id_sph << "_x" << ",";
      fout << "sphere_pos_" << id_sph << "_y" << ",";
      fout << "sphere_pos_" << id_sph << "_z" << ",";
    }
    for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
      fout << "arm_force_" << id_arm << ",";
      fout << "input_action_" << id_arm << ",";
      fout << "arm_energy_consumption_" << id_arm << ",";
    }
    for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
      fout << "arm_length_" << id_arm << ",";
    }
    fout << "head_direction_x,head_direction_y,head_direction_z" << std::endl;
  }

  /* Reset All Variables */
  this->step_counter       = 0;
  this->total_itr          = 0;
  this->input_actions      = VectorXd::Zero(this->n_arms);
  this->arm_lengths        = VectorXd::Ones(this->n_arms);
  this->arm_forces         = VectorXd::Zero(this->n_arm_states);
  this->output_energy_consumption = VectorXd::Zero(this->n_arms);
  this->step_energy_consumption = VectorXd::Zero(this->n_arms);
  this->sphere_velocities  = VectorXd::Zero(this->n_sphere_states);

  this->sphere_positions = this->init_sphere_positions;
  /* Rotate initial position */
  if (this->RANDOM_INIT_STATES) {
    // Define random
    std::mt19937 mt(this->rnd());
    std::uniform_real_distribution<> rand_2pi(0.0, 2.0*M_PI);
    // construct Quaternion
    if (this->swimmer_dim > 1) {
      quats.emplace_back(
          AngleAxisd(rand_2pi(mt), Vector3d::UnitZ())
          );
      if (this->swimmer_dim > 2) {
        quats.emplace_back(
            AngleAxisd(rand_2pi(mt), Vector3d::UnitY())
            );
        quats.emplace_back(
            AngleAxisd(rand_2pi(mt), Vector3d::UnitX())
            );
      }
    }
    Quaterniond total_quat = Quaterniond::Identity();
    for (int idx = quats.size()-1; idx >= 0; --idx) {
      total_quat *= quats[idx];
    }
    // Rotate each sphere
    for (size_t id_sph = 0; id_sph < this->n_spheres; ++id_sph) {
      this->sphere_positions.segment(3*id_sph, 3) = total_quat * this->sphere_positions.segment(3*id_sph, 3);
    }
  }



  this->updateCenterPosition();
  this->prev_center_position = this->center_position;

  return this->getObservation();
}

std::tuple<VectorXd, double, bool, std::unordered_map<std::string, VectorXd>> 
SkeletonSwimmer::step(const VectorXd actions)
{
  /* check input action size */
  if(static_cast<size_t>(actions.rows()) != this->n_arms){
    std::cout << "[self ERROR] The action size is wrong" << std::endl;
    std::exit(0);
  }
  /* check input action values */
  for(size_t i = 0; i < this->n_arms; ++i){
    if(std::abs(actions(i)) > 1.0){
      std::cout << "[self ERROR] The value is out of range" << std::endl;
      std::exit(0);
    }
  }
  this->input_actions = actions;
  this->step_energy_consumption = VectorXd::Zero(this->n_arms);

  /* Iteration */
  for(unsigned int itr = 0; itr < this->MAX_ITER; ++itr){
    if(this->ON_RECORD && this->total_itr%OUT_ITER == 0){
      this->output(); // using this->total_itr
    }
    this->miniStep(this->input_actions);
    this->total_itr += 1;
  }
  this->updateCenterPosition();

  /* Judgement for finish */
  bool done = false;
  if(this->step_counter >= this->MAX_STEP-1){
    done = true;
  }

  /* Rward */
  Vector3d displacement = this->center_position - this->prev_center_position;
  double displacement_reward = this->DISPLACEMENT_GAIN  * displacement.dot(this->target_unit_vec);

  double reward;
  if(this->CONSIDER_ENERGY){
    double energy_penalty = this->ENERGY_GAIN * this->step_energy_consumption.sum();
    reward = 2.0 * displacement_reward / (1.0 + energy_penalty);
    // reward = tanh( 0.01 * displacement_reward / (0.00000000 + energy_penalty) );
    // reward = 0.1 * displacement_reward / (0.00000001 + energy_penalty);

  }else{
    reward = displacement_reward;
  }

  /* Additional information */
  std::unordered_map<std::string, VectorXd> info;
  info["center"] = this->center_position;
  info["displacement"] = displacement;
  info["energy_consumption"] = this->step_energy_consumption;
  info["head_direction"] = (this->sphere_positions.segment(0, 3) - this->center_position).normalized();

  /* update counter */
  this->step_counter += 1;
  /* update center position */
  this->prev_center_position = this->center_position;

  return {this->getObservation(), reward, done, info};
}

void SkeletonSwimmer::miniStep(const VectorXd actions)
{
  /* Arm Vector (3m x 1) */
  VectorXd arm_vector = this->incident_matrix_arm2sph.transpose() * this->sphere_positions;

  /* Arm length and direction */
  auto [arm_lengths, arm_directions] = this->splitLengthAndDirection(arm_vector, this->n_arms);
  this->arm_lengths = arm_lengths;

  /* Translational Matrix */
  MatrixXd arm2sph = this->incident_matrix_arm2sph * arm_directions;

  /* Stokeslet */
  auto stokeslet = this->calculateStokeslet(this->sphere_positions, this->n_spheres);

  /* Clipping ArmExtensile velocity */
  auto clipped_actions = this->clipActions(actions, this->arm_lengths);

  /* calculate sphere velocity */
  MatrixXd trans_mat = arm2sph.transpose() * stokeslet * arm2sph;
  if(trans_mat.determinant() == 0.0){
    std::cout << "[self ERROR] Translational Matrix is Singuler" << std::endl;
    std::cout << "Cannot invert Matrix" << std::endl;
    std::exit(0);
  }
  this->arm_forces = trans_mat.inverse() * clipped_actions;
  this->sphere_velocities = stokeslet * arm2sph * this->arm_forces;

  /* update positions */
  this->sphere_positions += this->sphere_velocities * DT;

  /* calculate Energy Consumption */
  VectorXd energy_consumption = (this->arm_forces.array() * clipped_actions.array() * DT).abs();
  this->output_energy_consumption += energy_consumption;
  this->step_energy_consumption   += energy_consumption;
}

VectorXd SkeletonSwimmer::clipActions(const VectorXd actions, const VectorXd lengths) const
{
  VectorXd clipped_actions = actions;
  for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
    if(lengths(id_arm) > this->L_MAX){
      clipped_actions(id_arm) = std::min(0.0, actions(id_arm));
    }else if(lengths(id_arm) < L_MIN){
      clipped_actions(id_arm) = std::max(0.0, actions(id_arm));
    }
  }

  return clipped_actions;
}

std::tuple<VectorXd, MatrixXd> SkeletonSwimmer::splitLengthAndDirection(VectorXd vector, size_t n_split) const
{
  MatrixXd direction_mat = MatrixXd::Zero(3*n_split, n_split);
  VectorXd length_vec(n_split);

  for(size_t id_arm = 0; id_arm < n_split; ++id_arm){
    VectorXd one_vec = vector.segment(3*id_arm, 3);
    length_vec(id_arm) = one_vec.norm();
    direction_mat.block(3*id_arm, id_arm, 3, 1) = one_vec.normalized();
  }

  return{length_vec, direction_mat};
}

MatrixXd SkeletonSwimmer::calculateStokeslet(const VectorXd positions, const size_t n_sph) const
{
  MatrixXd stokeslet = MatrixXd::Zero(3*n_sph, 3*n_sph);
  for(size_t id_target = 0; id_target < n_sph; ++id_target){
    Vector3d target_pos = positions.segment(3*id_target, 3);
    for(size_t id_to = 0; id_to < n_sph; ++id_to){
      if(id_target == id_to){
        stokeslet.block(3*id_target, 3*id_to, 3, 3) = COEF_SELF * Matrix3d::Identity();
      }else{
        Vector3d rel_vec = positions.segment(3*id_to, 3) - target_pos;
        double inverted_norm = 1.0 / rel_vec.norm();
        double inverted_norm3 = std::pow(inverted_norm, 3);
        stokeslet.block(3*id_target, 3*id_to, 3, 3) = COEF_OTHER * (
            (Matrix3d::Identity()*inverted_norm) 
            + (rel_vec*rel_vec.transpose()*inverted_norm3)
            );
      }
    }
  }

  return stokeslet;
}

void SkeletonSwimmer::output()
{
  fout << this->total_itr*DT << ",";
  for(size_t id_sph = 0; id_sph < this->n_spheres; ++id_sph){
    fout << this->sphere_positions(3*id_sph + 0) << ",";
    fout << this->sphere_positions(3*id_sph + 1) << ",";
    fout << this->sphere_positions(3*id_sph + 2) << ",";
  }
  for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
    fout << this->arm_forces(id_arm) << ",";
    fout << this->input_actions(id_arm) << ",";
    fout << this->output_energy_consumption(id_arm) << ",";
  }
  for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
    fout << this->arm_lengths(id_arm) << ",";
  }
  Vector3d head_direction = (this->sphere_positions.segment(0, 3) - this->center_position).normalized();
  fout << head_direction(0) << ","
       << head_direction(1) << ","
       << head_direction(2) << std::endl;
  // fout << std::endl;
  this->output_energy_consumption = VectorXd::Zero(this->n_arms);
}

VectorXd SkeletonSwimmer::getObservation() const
{
  VectorXd rel_pos = this->sphere_positions;
  for(size_t id_sphere = 0; id_sphere < this->n_spheres; ++id_sphere){
    rel_pos.segment(3*id_sphere, 3) -= this->center_position;
  }
  return rel_pos;
}

void SkeletonSwimmer::updateCenterPosition()
{
  this->center_position = Vector3d::Zero();
  for(size_t id_sphere = 0; id_sphere < this->n_spheres; ++id_sphere){
    this->center_position(0) += this->sphere_positions(3*id_sphere + 0);
    this->center_position(1) += this->sphere_positions(3*id_sphere + 1);
    this->center_position(2) += this->sphere_positions(3*id_sphere + 2);
  }
  this->center_position /= this->n_spheres;
}

size_t SkeletonSwimmer::getNumStates() const
{
  return this->n_sphere_states;
}

size_t SkeletonSwimmer::getNumActions() const
{
  return this->n_arms;
}
}

#endif //SWIMMER
