cmake_minimum_required(VERSION 3.8)
project(sr_robot_msgs)

set(MSG_DEPS
  std_msgs
  builtin_interfaces
  sensor_msgs
  geometry_msgs
  actionlib_msgs
  moveit_msgs
)

find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(actionlib_msgs REQUIRED)
find_package(moveit_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/ActuatorStatistics.msg"
  "msg/AuxSpiData.msg"
  "msg/BiotacAll.msg"
  "msg/Biotac.msg"
  # "msg/cartesian_data.msg"
  # "msg/cartesian_position.msg"
  # "msg/command.msg"
  # "msg/config.msg"
  # "msg/contrlr.msg"
  "msg/ControllerStatistics.msg"
  "msg/ControlType.msg"
  "msg/EthercatDebug.msg"
  "msg/FromMotorDataType.msg"
  "msg/GraspArray.msg"
  "msg/JointControllerState.msg"
  # "msg/joint.msg"
  "msg/JointMusclePositionControllerState.msg"
  "msg/JointMuscleValveControllerCommand.msg"
  "msg/JointMuscleValveControllerState.msg"
  # "msg/joints_data.msg"
  "msg/JointStatistics.msg"
  "msg/MechanismStatistics.msg"
  "msg/MidProxDataAll.msg"
  "msg/MidProxData.msg"
  "msg/MotorSystemControls.msg"
  "msg/MSTReading.msg"
  # "msg/reverseKinematics.msg"
  # "msg/sendupdate.msg"
  "msg/ShadowPST.msg"
  "msg/TactileArray.msg"
  "msg/Tactile.msg"
  "msg/UBI0All.msg"
  "msg/UBI0.msg"
  "msg/MSTSensor.msg"
  "msg/MSTFinger.msg"
  "msg/MSTPalm.msg"
  "msg/ShadowContactStateStamped.msg"
  "msg/WrenchWithModelGroupName.msg"
  "msg/WrenchArray.msg"
  "msg/HybridControllerStatus.msg"
  "srv/ChangeControlType.srv"
  "srv/ChangeMotorSystemControls.srv"
  "srv/ForceController.srv"
  "srv/GetSegmentedLine.srv"
  # "srv/is_hand_occupied.srv"
  "srv/ManualSelfTest.srv"
  "srv/NullifyDemand.srv"
  "srv/RobotTeachMode.srv"
  "srv/SetDebugData.srv"
  "srv/SetEffortControllerGains.srv"
  "srv/SetMixedPositionVelocityPidGains.srv"
  "srv/SetPidGains.srv"
  "srv/SimpleMotorFlasher.srv"
  # "srv/which_fingers_are_touching.srv"
  "srv/GetFastGraspFromBoundingBox.srv"
  "srv/PlanTrajectoryFromList.srv"
  "srv/PlanTrajectoryFromPrefix.srv"
  "srv/PlanNamedTrajectory.srv"
  "srv/ExecutePlannedTrajectory.srv"
  "srv/ListNamedTrajectories.srv"
  "srv/SetTeachMode.srv"
  "srv/SetImuScale.srv"
  "action/Grasp.action"
  "action/PlanGrasp.action"
  DEPENDENCIES ${MSG_DEPS}
)

rosidl_get_typesupport_target(cpp_typesupport_target
  ${PROJECT_NAME} rosidl_typesupport_cpp)

# target_link_libraries(publish_address_book "${cpp_typesupport_target}")

# ament_export_dependencies(${MSG_DEPS})
ament_export_dependencies(rosidl_default_runtime)

ament_package()
