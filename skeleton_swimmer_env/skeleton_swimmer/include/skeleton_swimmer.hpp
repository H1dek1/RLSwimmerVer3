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
    VectorXd reset();
    std::tuple<VectorXd, double, bool, int>
      step(const VectorXd actions);
  public:
    /* Constructor & Destuctor */
    SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_lengh);
    ~SkeletonSwimmer();
    /* Getter */
    size_t getNumStates() const;
    size_t getNumActions() const;

  /* Private Member Functions */
  private:
    VectorXd getObservation();
    void output();
    void updateCenterPosition();
    void miniStep(const VectorXd actions);
    std::tuple<VectorXd, MatrixXd> splitLengthAndDirection(const VectorXd vector, const size_t n_split) const;
    MatrixXd calculateStokeslet(const VectorXd positions, const size_t n_sph) const;
    VectorXd clipActions(const VectorXd actions, const VectorXd lengths) const;

  /* Member variables */
  private:
    const bool   IS_RECORD;
    const int    SWIMMER_TYPE;
    const double LOAD_TIME;
    const double L_MAX;
    const size_t MAX_STEP;
    const size_t MAX_ITER;
    unsigned int step_counter;
    unsigned int total_itr;

    size_t n_spheres; // n
    size_t n_arms;   // m
    size_t n_sphere_states; // 3n
    size_t n_arm_states;   // 3m

    /* Extended actions */
    VectorXd action_vec;
    /* initial sphere position */
    VectorXd init_sphere_positions;
    VectorXd sphere_positions;
    VectorXd sphere_velocities;
    VectorXd arm_forces;
    MatrixXd connection_arm2sph;
    VectorXd input_actions;
    VectorXd arm_lengths;

    Vector3d center_position;
    Vector3d prev_center_position;
    Vector3d target_unit_vec;

  private:
    std::ofstream fout;
    const std::filesystem::path RUNFILE_PATH;
};
}

#endif //SWIMMER_H
