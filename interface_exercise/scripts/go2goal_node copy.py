#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
import math
from interface_exercise.control import go2goal

class GoToGoal():
    def __init__(self):
        self.pose = None
        self.goal = None
        self.period = 0.05
    def update(self,pose,goal,Kv=1.0,Kw=5.0):
        p = [pose[0],pose[1]]
        q = [math.cos(pose[2]),math.sin(pose[2])]
        return go2goal(p,q,goal,1.0,5.0)

class GoToGoalROSInterface():
    def __init__(self):
        self.controller = GoToGoal()
        self.node = Node('controller')
        # ADD CODE HERE
        pass
    def pose_sub_callback(self,msg:Pose):
        # ADD CODE HERE
        pass
    def goal_sub_callback(self,msg:Point):
        # ADD CODE HERE
        pass
    def timer_callback(self):
        # ADD CODE HERE
        pass

# Implemented as a sub-class of a (ROS)Node.
class GoToGoalNode(Node):
    def __init__(self):
        super().__init__('controller')
        self.pose_msg = None
        self.goal_msg = None
        self.period = 0.05
        
        self.cmd_vel_pub = self.create_publisher(Twist,'cmd_vel',10)
        self.pose_sub = self.create_subscription(Pose,'pose',self.pose_sub_callback,10)
        self.goal_sub = self.create_subscription(Point,'goal',self.goal_sub_callback,10)
        self.create_timer(self.period,self.timer_callback)
    def pose_sub_callback(self,msg:Pose):
        self.pose_msg = msg
    def goal_sub_callback(self,msg:Point):
        self.goal_msg = msg
    def timer_callback(self):
        if self.goal_msg and self.pose_msg:
            p = [self.pose_msg.x,self.pose_msg.y]
            p_goal = [self.goal_msg.x,self.goal_msg.y]
            q = [math.cos(self.pose_msg.theta),math.sin(self.pose_msg.theta)]
            v,w = go2goal(p,q,p_goal,1.0,5.0)
            cmd_vel_msg = Twist()
            cmd_vel_msg.linear.x = v
            cmd_vel_msg.angular.z = w
            self.cmd_vel_pub.publish(cmd_vel_msg)
def main(args=None):
    rclpy.init(args=args)
    node = GoToGoalNode()
    rclpy.spin(node)
    node.destroy_node()
    #interface = GoToGoalROSInterface()
    #rclpy.spin(interface.node)
    #interface.node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
