import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource, FrontendLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition, UnlessCondition
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit


def generate_launch_description():
    zedx_left_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('zed_wrapper'), 'launch'), 
                                        '/zed_camera.launch.py']),
        launch_arguments={
            'camera_name': LaunchConfiguration('zedx_left_camera_name'),
            'camera_model': LaunchConfiguration('zedx_left_camera_model'),
            'serial_number': LaunchConfiguration('zedx_left_serial_number')
            }.items(),
    )

    zedx_right_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('zed_wrapper'), 'launch'), 
                                        '/zed_camera.launch.py']),
        launch_arguments={
            'camera_name': LaunchConfiguration('zedx_right_camera_name'),
            'camera_model': LaunchConfiguration('zedx_right_camera_model'),
            'serial_number': LaunchConfiguration('zedx_right_serial_number')
            }.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument('zedx_left_camera_name', 
                              default_value='zedx/left', 
                              description='zedx_left_camera_name'
        ),

        DeclareLaunchArgument('zedx_left_camera_model', 
                              default_value='zedx', 
                              description='zedx_left_camera_model'
        ),

        DeclareLaunchArgument('zedx_left_serial_number', 
                              default_value='45656860', 
                              description='zedx_left_serial_number'
        ),

        DeclareLaunchArgument('zedx_right_camera_name', 
                              default_value='zedx/right', 
                              description='zedx_right_camera_name'
        ),

        DeclareLaunchArgument('zedx_right_camera_model', 
                              default_value='zedx', 
                              description='zedx_right_camera_model'
        ),

        DeclareLaunchArgument('zedx_right_serial_number', 
                              default_value='40051193', 
                              description='zedx_right_serial_number'
        ),
        
        zedx_left_launch,
        zedx_right_launch,
    ])