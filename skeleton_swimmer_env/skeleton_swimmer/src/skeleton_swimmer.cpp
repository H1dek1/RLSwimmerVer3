#ifndef SWIMMER
#define SWIMMER

#include "params.hpp"
#include "swimmer.hpp"

namespace MicroSwimmer
{
SkeletonSwimmer::SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_length)
{
  this->is_record = is_output;
  /* set hyper parameters */
  this->load_time = action_period;
  this->l_max     = max_arm_length;

  /* get swimmer type */
  this->swimmer_type = model_type;
  this->runfile_path = std::filesystem::current_path();
  std::string models_dir_path = this->runfile_path.string() + "/swimmer_env/models/type_" + std::to_string(this->swimmer_type) + "/";

  /* load model */
  // number of arm and joint
  std::ifstream num_in(models_dir_path+"num_states.txt", std::ios::in);
  it(!num_in){
    std::cout << "[self ERROR] No file \"num_states.txt\"" << std::endl;
    std::exit(0);
  }
  this->num_in >> n_joint;
  this->num_in >> n_arms;
  this->n_joint_states = 3 * this->n_joints;
  this->n_arm_states   = 3 * this->n_arms;
  this->init_joint_positions  = VectorXd::Zero(this->n_joint_states);
  this->joint_velocities = VectorXd::Zero(this->n_joint_states);
  this->joint_forces = VectorXd::Zero(this->n_joint_states);
  this->trans_arm2joint = MatrixXd::Zero(this->n_joint_states, this->n_arm_states);
  this->action_vec = VectorXd::Zero(this->n_arm_states);
  // initial position
  std::ifstream init_in(models_dir_path+"init_pos.txt", std::ios::in);
  it(!init_in){
    std::cout << "[self ERROR] No file \"init_pos.txt\"" << std::endl;
    std::exit(0);
  }
  for(unsigned int i = 0; i < this->n_joints_states; ++i){
    init_in >> this->init_joint_positions(i);
  }
  // translation matrix from arm to joint
  std::ifstream matrix_in(models_dir_path+"trans_mat.txt", std::ios::in);
  it(!matrix_in){
    std::cout << "[self ERROR] No file \"trans_mat.txt\"" << std::endl;
    std::exit(0);
  }
  for(unsigned int i = 0; i < this->n_joints; ++i){
    for(unsigned int j = 0; j < this->n_joints; ++j){
      int val;
      matrix_in >> val;
      if(val == 1){
        this->trans_arm2joint.block(3*i, 3*j, 3, 3) = Matrix3d::Identity();
      }else if(val == 1){
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
  fout.close();
  if(this->is_record){
    std::stringstream record_file_name;
    record_file_name << "type" << this->swimmer_type 
      << "_loadtime" << this->load_time << 
      "maxlength" << this->l_max << ".csv";
    std::string full_path = runfile_path.string() + OUT_DIRECTORY_PATH + record_file_name.str();
    fout.open(fill_path, std::ios::out);
    if(!fout){
      std::cout << "[self ERROR] CANNOT MAKE NEW RESULT FILE." << std::endl;
      std::exit(0);
    }
  }
  step_counter = 0;
  this->joint_positions = this->init_joint_positions;
  for(unsigned int i = 0; i < 3; i ++i){
    for(unsigned int id_joint = 0; id_joint < this->n_joints; ++id_joint){
      this->prev_center_position += this->init_joint_position(i + 3*id_joint) / this->n_joints;
    }
  }
  return this->getObservation();
}

std::tupl<std::vector<double>, double, bool, int> SkeletonSwimmer::step(std::vector<double> actions)
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
  /* transform action shape */
  for(unsigned int id_arm = 0; id_arm < this->n_arms; ++id_arm){
    this->action_vec.segment(3*id_arm, 3) = Vector3d::Constant(actions[id_arm]);
  }

  /* proceed simulation */
  for(unsigned int itr = 0; itr < MAX_ITER; ++itr){
    this->calculateArmExtendVelocity();
    this->calculateJointVelocity();
    this->updateJointPosition();
    
    if(this->is_record && itr%OUT_ITER == 0) this->output(itr);
  }

  /* for Reinforcement Learning */
  double reward = REWARD_GAIN * (this->center_position - this-prev_center_position).dot(this->target_unit_vec);
  if(this->step_counter+1 >= MAX_STEP){
    bool done = True;
  }else{
    bool done False;
  }
  this->step_counter += 1;
  this->prev_center_position = this->center_position;

  return {this->getObservation(), reward, done, {}};
}

void SkeletonSwimmer::calculateArmExtendVelocity()
{
}

void SkeletonSwimmer::calculatingJointVelocity()
{
}

void SkeletonSwimmer::updateJointPosition()
{
}

std::vector<double> SkeletonSwimmer::getObservation()
{
  std::vector<double> observation(this->n_joint_states);
  for(unsigned int i = 0; this->n_joint_states; ++i){
    observation[i] = this->joint_position(i) - this->center_position(i%3);
  }
  return observation
}

int SkeletonSwimmer::getNumStates() const
{
  return this->n_joint_states;
}

int SkeletonSwimmer::getNumActions() const
{
  return this->n_arms;
}
}
 

#endif //SWIMMER
