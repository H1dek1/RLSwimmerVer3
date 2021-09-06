cmake_minimum_required(VERSION 2.8)
project(skeleton_swimmer)
enable_language(CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "-O3 -Wall -fopenmp")


add_library(skeleton_swimmer
  STATIC
    skeleton_swimmer.cpp
  )

target_include_directories(skeleton_swimmer
  PUBLIC ../include
  )
add_executable(run main.cpp)
target_link_libraries(run skeleton_swimmer)
