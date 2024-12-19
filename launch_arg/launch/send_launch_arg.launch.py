import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory


def generate_launch_description():
    recv_launch_arg = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory("launch_arg"), "launch", "recv_launch_arg.launch.py")]
        ),
        launch_arguments={"launch_arg": "Hello there!"}.items(),
    )

    return LaunchDescription(
        [
            recv_launch_arg,
        ]
    )
