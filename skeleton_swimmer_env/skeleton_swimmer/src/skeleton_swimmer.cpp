#ifndef SWIMMER
#define SWIMMER

#include "params.hpp"
#include "skeleton_swimmer.hpp"

#define DEBUG true

namespace MicroSwimmer
{
using namespace Eigen;

SkeletonSwimmer::SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_length) : 
  is_record(is_output), 
  load_time(action_period), 
  l_max(max_arm_length), 
  swimmer_type(model_type),
  runfile_path(std::filesystem::current_path())
{
  std::string models_dir_path = this->runfile_path.string() + "/../../models/type_" + std::to_string(this->swimmer_type) + "/";

  /* load model */
  // set number of arm and joint
  std::ifstream num_in(models_dir_path+"num_states.txt", std::ios::in);
  if(!num_in){
    std::cout << "[self ERROR] No file \"num_states.txt\"" << std::endl;
    std::exit(0);
  }
  num_in >> n_joints;
  num_in >> n_arms;
  this->n_joint_states = 3 * this->n_joints;
  this->n_arm_states   = 3 * this->n_arms;
  this->init_joint_positions = VectorXd::Zero(this->n_joint_states);
  this->joint_velocities     = VectorXd::Zero(this->n_joint_states);
  this->joint_forces         = VectorXd::Zero(this->n_joint_states);
  this->trans_arm2joint      = MatrixXd::Zero(this->n_joint_states, this->n_arm_states);
  this->action_vec           = VectorXd::Zero(this->n_arm_states);
  // initial position
  std::ifstream init_in(models_dir_path+"init_pos.txt", std::ios::in);
  if(!init_in){
    std::cout << "[self ERROR] No file \"init_pos.txt\"" << std::endl;
    std::exit(0);
  }
  for(size_t i = 0; i < this->n_joint_states; ++i){
    init_in >> this->init_joint_positions(i);
  }
  // translation matrix from arm to joint
  std::ifstream matrix_in(models_dir_path+"trans_mat.txt", std::ios::in);
  if(!matrix_in){
    std::cout << "[self ERROR] No file \"trans_mat.txt\"" << std::endl;
    std::exit(0);
  }
  for(size_t i = 0; i < this->n_joints; ++i){
    for(size_t j = 0; j < this->n_arms; ++j){
      int val;
      matrix_in >> val;
      if(val == 1){
        this->trans_arm2joint.block(3*i, 3*j, 3, 3) = Matrix3d::Identity();
      }else if(val == -1){
        this->trans_arm2joint.block(3*i, 3*j, 3, 3) = -Matrix3d::Identity();
      }
    }
  }
  this->target_unit_vec = Vector3d::UnitX();
}

SkeletonSwimmer::~SkeletonSwimmer()
{
  fout.close();
}

std::vector<double> SkeletonSwimmer::reset()
{
  /* Set record file */
  if(fout.is_open()){
    fout.close();
  }
  if(this->is_record){
    std::stringstream record_file_name;
    record_file_name << "type" << this->swimmer_type 
      << "_loadtime" << this->load_time << 
      "_maxlength" << this->l_max << ".csv";
    std::string full_path = runfile_path.string() + OUT_DIRECTORY_PATH + record_file_name.str();
    fout.open(full_path, std::ios::out);
    if(!fout){
      std::cout << "[self ERROR] CANNOT MAKE NEW RESULT FILE." << std::endl;
      std::exit(0);
    }
  }
  /* Initialize All States */
  this->step_counter = 0;
  this->total_itr    = 0;
  this->joint_positions = this->init_joint_positions;
  this->updateCenterPosition();
  this->prev_center_position = this->center_position;
  return this->getObservation();
}

std::tuple<std::vector<double>, double, bool, int> 
SkeletonSwimmer::step(const std::vector<double> actions)
{
  /* check input action */
  if(actions.size() != this->n_arms){
    std::cout << "[self ERROR] The action size is wrong" << std::endl;
    std::exit(0);
  }
  for(auto const& action : actions){
    if(std::abs(action) > 1.0){
      std::cout << "[self ERROR] The value is out of range" << std::endl;
      std::exit(0);
    }
  }
  /* Iteration */
  //for(unsigned int itr = 0; itr < MAX_ITER; ++itr){
  for(unsigned int itr = 0; itr < 1; ++itr){
    this->miniStep(actions);
    if(this->is_record && this->total_itr%OUT_ITER == 0){
      this->output(); // using this->total_itr
    }
  }

  /* for Reinforcement Learning */
  double reward = REWARD_GAIN * (this->center_position - this->prev_center_position).dot(this->target_unit_vec);

  bool done = false;
  if(this->step_counter > MAX_STEP){
    done = true;
  }
  this->step_counter += 1;
  this->prev_center_position = this->center_position;

  return {this->getObservation(), reward, done, {}};
}

void SkeletonSwimmer::miniStep(const std::vector<double> actions)
{
  if(DEBUG){
  std::cout << "X" << std::endl;
  std::cout << this->joint_positions.transpose() << std::endl;
  }

  /* Arm Vector (3m x 1) */
  VectorXd arm_vector = this->trans_arm2joint.transpose() * this->joint_positions;
  if(DEBUG){
  std::cout << "Arm Vector" << std::endl;
  std::cout << arm_vector.transpose() << std::endl;
  }

  /* Arm length and direction */
  //auto [arm_lengths, arm_directions] = this->splitLengthAndDirection(arm_vector);
  this->splitLengthAndDirection(arm_vector);

}
//std::tuple<VectorXd, MatrixXd> SkeletonSwimmer::splitLengthAndDirection(VectorXd vector)
void SkeletonSwimmer::splitLengthAndDirection(VectorXd vector)
{
  std::cout << "In split function " << std::endl;
  for(size_t id_arm = 0; id_arm < this->n_arms; ++id_arm){
    VectorXd one_vec = vector.segment(3*id_arm, 3);
    std::cout << one_vec.transpose() << std::endl;
  }
  //return{length_vec, direction_vec}
}

void SkeletonSwimmer::output()
{
}

std::vector<double> SkeletonSwimmer::getObservation()
{
  std::vector<double> observation(this->n_joint_states);
  // FIXME
  for(unsigned int i = 0; i < this->n_joint_states; ++i){
    observation[i] = this->joint_positions(i) - this->center_position(i%3);
  }
  return observation;
}

void SkeletonSwimmer::updateCenterPosition()
{
  this->center_position = Vector3d::Zero();
  for(size_t id_joint = 0; id_joint < this->n_joints; ++id_joint){
    this->center_position(0) += this->joint_positions(3*id_joint + 0);
    this->center_position(1) += this->joint_positions(3*id_joint + 1);
    this->center_position(2) += this->joint_positions(3*id_joint + 2);
  }
  this->center_position /= this->n_joints;
}

size_t SkeletonSwimmer::getNumStates() const
{
  return this->n_joint_states;
}

size_t SkeletonSwimmer::getNumActions() const
{
  return this->n_arms;
}
}

#endif //SWIMMER
