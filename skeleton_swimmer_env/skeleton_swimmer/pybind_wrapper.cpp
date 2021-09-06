#include <eigen3/Eigen/Dense>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include "skeleton_swimmer.hpp"

namespace py = pybind11;

PYBIND11_MODULE(skeleton_swimmer, m) {
  py::class_<MicroSwimmer::SkeletonSwimmer>(m, "SkeletonSwimmer")
    .def(py::init<int, bool, double, double>())
    .def("getNumStates", &MicroSwimmer::SkeletonSwimmer::getNumStates)
    .def("getNumActions", &MicroSwimmer::SkeletonSwimmer::getNumActions)
    .def("reset", &MicroSwimmer::SkeletonSwimmer::reset)
    .def("step", &MicroSwimmer::SkeletonSwimmer::step);
}
