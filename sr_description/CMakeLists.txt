cmake_minimum_required(VERSION 3.5)
project(sr_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY hand/
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/hand)

install(DIRECTORY meshes/
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/meshes)

install(DIRECTORY loaders/
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/loaders)

install(DIRECTORY robots/
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/robots)

install(DIRECTORY other/
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME}/other)

install(FILES launch/demo.launch.py
   DESTINATION ${CMAKE_INSTALL_PREFIX}/share/${PROJECT_NAME})

ament_package()