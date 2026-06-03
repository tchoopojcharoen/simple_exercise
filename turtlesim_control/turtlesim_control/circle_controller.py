#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CircleController(Node):
    def __init__(self):
        super().__init__('circle_controller')

        self.pub = self.create_publisher( Twist, '/turtle1/cmd_vel',10 )

        self.timer = self.create_timer(0.1, self.timer_callback)

        self.get_logger().info('Circle controller node has started.')

    def timer_callback(self):
        msg = Twist()

        msg.linear.x = 2.0
        msg.angular.z = 1.0

        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = CircleController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
