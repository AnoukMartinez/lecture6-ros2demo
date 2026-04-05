import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 

class CircleMotion(Node):
    def __init__(self):
        super().__init__('circle_motion')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Circle Motion Publihser started! Publishing to /cmd_vel')
    
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.3
        msg.angular.z = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}'
        )

def main(args=None):
    rclpy.init(args=args)
    circle_motion_publisher = CircleMotion()
    rclpy.spin(circle_motion_publisher)
    # circle_motion_publisher.destroy_node() # not in the readme for some reason...
    rclpy.shutdown()