#ifndef SWIMMER_H
#define SWIMMER_H
#include "params.hpp"

namespace MicroSwimmer
{
using namspace Eigen;

class SkeletonSwimmer
{
  /* Member functions */
  public:
    std::vector<double> reset();
    std::tuple<std::vector<double>, double, bool, int>
      step(std::vector<double> actions);
  public:
    SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_lengh);
    ~SkeletonSwimmer();

    int getNumStates() const;
    int getNumActions() const;

  private:
    std::vector<double> getObservations() const;
    void output(int itr);
    void calculateArmExtendVelocity();
    void calculateJointVelocity();
    void updateJointPosition();

  /* Member variables */
  private:
    bool is_record;
    int step_counter;
    int swimmer_type;
    double load_time;
    double l_max;

    int n_joints;
    int n_arms;
    int n_states;
    int n_joint_states;
    int n_arm_states;

    VectorXd action_vec;
    VectorXd init_joint_positions;
    VectorXd joint_positions;
    VectorXd joint_velocities;
    VectorXd joint_forces;
    MatrixXd trans_arm2joint;

    Vector3d center_position;
    Vector3d prev_center_position;
    Vector3d target_unit_vec;

  private:
    std::ofstream fout;
    std::filesystem::path runfile_path;
}
}

#endif //SWIMMER_H
