cmake_minimum_required(VERSION 3.9)
project(skeleton_swimmer VERSION 0.1.0)
enable_language(CXX)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../)
#message("${CMAKE_CURRENT_SOURCE_DIR}")

add_subdirectory(pybind11)
#add_subdirectory(module)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include/)
add_library(skeleton_swimmer_src
  src/skeleton_swimmer.cpp)
pybind11_add_module(skeleton_swimmer pybind_wrapper.cpp)
target_link_libraries(skeleton_swimmer PRIVATE skeleton_swimmer_src)
