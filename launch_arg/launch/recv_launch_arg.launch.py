import launch
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    launch_arg = DeclareLaunchArgument(
        "launch_arg",
        default_value="Hello world",
    )

    launch_arg_node = Node(
        package="launch_arg",
        executable="launch_arg_node",
        name="launch_arg_node",
        output="screen",
        parameters=[{"launch_arg": LaunchConfiguration("launch_arg")}],
    )
    return launch.LaunchDescription([launch_arg, launch_arg_node])
