import rclpy
import rclpy.node


class LaunchArgNode(rclpy.node.Node):
    def __init__(self):
        super().__init__("launch_arg_node")

        self.declare_parameter("launch_arg")

        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        launch_arg = self.get_parameter("launch_arg").get_parameter_value().string_value

        self.get_logger().info(launch_arg)


def main():
    rclpy.init()
    node = LaunchArgNode()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
