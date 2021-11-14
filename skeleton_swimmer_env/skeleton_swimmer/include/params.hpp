#ifndef PARAMS_H
#define PARAMS_H
#include <iostream>
#include <string>
#include <vector>
#include <array>
#include <tuple>
#include <map>
#include <fstream>
#include <sstream>
#include <filesystem>
#include <Eigen/Dense>

namespace MicroSwimmer {
  /* swimmer parameters */
  // min length of each arm must be 1
  constexpr double L_MIN = 1.0;
  // sphere radius required less than 0.5
  constexpr double A = 0.1;
  // Coefficients of Stokeslet
  constexpr double COEF_SELF  = 1 / (6*M_PI*A);
  constexpr double COEF_OTHER = 1 / (8*M_PI);

  /* simulation parameters*/
  // update interval
  constexpr double DT = 1.0e-3;
  // max time of 1 episode
  constexpr double MAX_TIME = 1000;

  /* Reinforcement Learning parameters */
  // reward gain
  constexpr double REWARD_GAIN = 1000.0;

  /* output parameters */
  // output directory path
  const std::string OUT_DIRECTORY_PATH = "/sim/result/";
  // interval of output state
  constexpr double OUTPUT_INTERVAL = 1.0e-1;
  constexpr int    OUT_ITER = static_cast<int>(OUTPUT_INTERVAL / DT);

  /* model loading directory */
  const std::string MODEL_LOAD_PATH = "/skeleton_swimmer_env/models/";

}
  

#endif //PARAMS_H
