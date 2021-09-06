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
  // min length of each arm must be 1
  constexpr double L_MIN = 1.0;
  // sphere radius required less than 0.5
  constexpr double A = 0.3;
  // max time of 1 episode
  constexpr double MAX_TIME = 1000;
  // reward gain
  constexpr double REWARD_GAIN = 30.0;

  /* output settings */
  // interval of output state
  constexpr double OUTPUT_INTERVAL = 1.0e-1;
  // output directory path
  const std::string OUT_DIRECTORY_PATH = "/sim/result/";

  /* simulation */
  // update interval
  constexpr double DT = 1.0e-3;

  /* iteration setting */
  const int OUT_ITER = int(OUTPUT_INTERVAL / DT);

  /* Coefficient of Stokeslet */
  const     double COEF1 = 1 / (6*M_PI*A);
  constexpr double COEF2 = 1 / (8*M_PI);
}
  

#endif //PARAMS_H
