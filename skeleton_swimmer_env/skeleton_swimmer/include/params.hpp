#ifndef PARAMS_H
#define PARAMS_H
#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <tuple>
#include <fstream>
#include <sstream>
#include <filesystem>
#include <eigen3/Eigen/Dense>

namespace MicroSwimmer {
  /* swimmer setting */
  // max length of each arm required less than 2
  constexpr double L_MAX = 1.5;
  // sphere radius required less than 0.5
  constexpr double A = 0.3;
  // max time of 1 episode
  constexpr double MAX_TIME = 1000;
  // the period to change input value
  constexpr double LOAD_TIME = 10;
  // reward gain
  constexpr double REWARD_GAIN = 30.0;

  /* output settings */
  // interval of output state
  constexpr double OUTPUT_INTERVAL = 1.0e-1;
  // output directory path
  const std::string OUT_DIRECTORY_PATH = "/sim/result/";

  /* simulation */
  // update interval
  constexpr double DT = 1.0e-2;

  /* iteration setting */
  const int MAX_STEP = int(MAX_TIME / LOAD_TIME);
  const int MAX_ITER = int(LOAD_TIME / DT);
  const int OUT_ITER = int(OUTPUT_INTERVAL / DT);
}
  

#endif //PARAMS_H
