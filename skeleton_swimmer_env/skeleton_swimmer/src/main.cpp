#include "skeleton_swimmer.hpp"

int main(void){
  bool output_flag = false;
  int model_type = 10;
  double action_period = 1.0;
  double max_arm_length = 1.2;
  MicroSwimmer::SkeletonSwimmer swimmer(model_type, output_flag, action_period, max_arm_length);
  std::vector<double> obs = swimmer.reset();
  std::cout << "In main" << std::endl;
  for(auto x : obs){
    std::cout << x << ", ";
  }
  std::cout << std::endl;
  std::vector<double> actions{0.5, 0.5};
  auto [obs2, reward, done, info] = swimmer.step(actions);
  //for(auto x : obs2){
  //  std::cout << x << ", ";
  //}
  //std::cout << std::endl;
  return 0;
}
