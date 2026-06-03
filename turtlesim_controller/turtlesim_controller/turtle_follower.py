#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleFollower(Node):
    def __init__(self):
        super().__init__('turtle_follower')

        self.leader_pose = None
        self.follower_pose = None

        self.desired_distance = 1.0

        self.leader_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.leader_pose_callback,
            10
        )

        self.follower_sub = self.create_subscription(
            Pose,
            '/turtle2/pose',
            self.follower_pose_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10
        )

        self.timer = self.create_timer(0.1, self.control_loop)

        self.get_logger().info('Turtle follower node has started.')

    def leader_pose_callback(self, msg):
        self.leader_pose = msg

    def follower_pose_callback(self, msg):
        self.follower_pose = msg

    def normalize_angle(self, angle):
        while angle > math.pi:
            angle -= 2.0 * math.pi
        while angle < -math.pi:
            angle += 2.0 * math.pi
        return angle

    def control_loop(self):
        if self.leader_pose is None or self.follower_pose is None:
            return

        dx = self.leader_pose.x - self.follower_pose.x
        dy = self.leader_pose.y - self.follower_pose.y

        distance = math.sqrt(dx**2 + dy**2)
        desired_heading = math.atan2(dy, dx)

        angle_error = self.normalize_angle(
            desired_heading - self.follower_pose.theta
        )

        cmd = Twist()

        k_linear = 1.5
        k_angular = 4.0

        distance_error = distance - self.desired_distance

        if distance_error > 0.05:
            cmd.linear.x = k_linear * distance_error
            cmd.angular.z = k_angular * angle_error
        else:
            cmd.linear.x = 0.0
            cmd.angular.z = k_angular * angle_error

        max_linear_speed = 2.0
        max_angular_speed = 4.0

        cmd.linear.x = max(min(cmd.linear.x, max_linear_speed), 0.0)
        cmd.angular.z = max(min(cmd.angular.z, max_angular_speed), -max_angular_speed)

        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)

    node = TurtleFollower()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()