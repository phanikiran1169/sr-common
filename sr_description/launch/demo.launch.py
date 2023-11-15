import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare, ExecutableInPackage
from launch_ros.descriptions import ParameterValue


def generate_launch_description():

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                 "robot_description":
                    ParameterValue(Command([ExecutableInPackage("xacro", "xacro"), " ",
                            PathJoinSubstitution(
                            [FindPackageShare("sr_description"),
                             "robots/sr_hand.urdf.xacro"]), 
                    ]), value_type=str)},
            ]),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            parameters=[
                {"source_list": ["published_joints"]}],
            ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen"
        )
    ])