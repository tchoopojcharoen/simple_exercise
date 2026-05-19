import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from turtlesim_controller.control_law import compute_go_to_goal_control

class GoToGoalNode(Node):
    def __init__(self, namespace='turtle1'):
        super().__init__('turtlesim_go_to_goal')

        # attributed of classes (local variables)
        
        # Controller parameters
        
        # Publisher(s) 
        # Subscriber(s)
        # Timer (for loops if any)

    # def something_callback(self,msg, other_args):
    #    pass
    # def timer_callback(self):
    #   pass

def main(args=None):
    rclpy.init(args=args)

    node = GoToGoalNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()