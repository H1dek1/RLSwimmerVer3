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
    std::tuple<VectorXd, double, bool, std::map<std::string, VectorXd>>
      step(const VectorXd actions);

    /* Getter */
    size_t getNumStates() const;
    size_t getNumActions() const;

  public:
    /* Constructor & Destuctor */
    SkeletonSwimmer(int model_type, bool is_output, double action_period, double max_arm_lengh);
    ~SkeletonSwimmer();

  /* Private Member Functions */
  private:
    VectorXd getObservation() const;
    void     output();
    void     updateCenterPosition();
    void     miniStep(const VectorXd actions);
    MatrixXd calculateStokeslet(const VectorXd positions, const size_t n_sph) const;
    VectorXd clipActions(const VectorXd actions, const VectorXd lengths) const;
    std::tuple<VectorXd, MatrixXd> 
      splitLengthAndDirection(const VectorXd vector, const size_t n_split) const;

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

    /* initial sphere positions : 3n */
    VectorXd init_sphere_positions;
    /* sphere positions : 3n */
    VectorXd sphere_positions;
    /* sphere velocities : 3n */
    VectorXd sphere_velocities;
    /* Connection Matrix from arm to sphere : 3m x 3n*/
    MatrixXd connection_arm2sph;
    /* input arm actions : m */
    VectorXd input_actions;
    /* arm lengths : m */
    VectorXd arm_lengths;
    /* arm force vectors : 3m */
    VectorXd arm_forces;

    /* center position : 3 */
    Vector3d center_position;
    /* previous center position : 3 */
    Vector3d prev_center_position;
    /* target unit vector : 3 */
    Vector3d target_unit_vec;

  private:
    std::ofstream fout;
    const std::filesystem::path RUNFILE_PATH;
};
}

#endif //SWIMMER_H
