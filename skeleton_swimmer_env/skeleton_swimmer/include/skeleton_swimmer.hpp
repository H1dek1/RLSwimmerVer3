#ifndef SWIMMER_H
#define SWIMMER_H
#include "params.hpp"

namespace MicroSwimmer
{
using namespace Eigen;

class SkeletonSwimmer
{
  /* Public Member Functions */
  public:
    std::vector<double> reset();
    std::tuple<std::vector<double>, double, bool, int>
      step(const std::vector<double> actions);
  public:
    /* Constructor & Destuctor */
    SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_lengh);
    ~SkeletonSwimmer();
    /* Getter */
    size_t getNumStates() const;
    size_t getNumActions() const;

  /* Private Member Functions */
  private:
    std::vector<double> getObservation();
    void output();
    void updateCenterPosition();
    void miniStep(const std::vector<double> actions);
    //std::tuple<VectorXd, MatrixXd> splitLengthAndDirection(VectorXd vector);
    void splitLengthAndDirection(VectorXd vector);

  /* Member variables */
  private:
    const bool   is_record;
    const int    swimmer_type;
    const double load_time;
    const double l_max;
    unsigned int step_counter;
    unsigned int total_itr;

    size_t n_joints; // n
    size_t n_arms;   // m
    size_t n_joint_states; // 3n
    size_t n_arm_states;   // 3m

    /* Extended actions */
    VectorXd action_vec;
    /* initial joint position */
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
    const std::filesystem::path runfile_path;
};
}

#endif //SWIMMER_H
