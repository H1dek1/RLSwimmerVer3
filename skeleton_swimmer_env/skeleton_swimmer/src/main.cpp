#include "skeleton_swimmer.hpp"
#include <eigen3/Eigen/Core>

int main(void){
  bool output_flag = true;
  int model_type = 10;
  double action_period = 10.0;
  double max_arm_length = 1.5;
  MicroSwimmer::SkeletonSwimmer swimmer(
      model_type, 
      output_flag, 
      action_period, 
      max_arm_length
      );
  std::vector<double> obs = swimmer.reset();
  std::cout << "Reset" << std::endl;
  for(auto x : obs){
    std::cout << x << ", ";
  }
  std::cout << std::endl;
  Eigen::VectorXd actions(2);
  actions << 0.5, -0.5;
  auto [obs2, reward, done, info] = swimmer.step(actions);
  std::cout << "Step" << std::endl;
  for(auto x : obs2){
    std::cout << x << ", ";
  }
  std::cout << std::endl;
  std::cout << "Reward = " << reward << std::endl;
  std::cout << std::endl;

  return 0;
}
