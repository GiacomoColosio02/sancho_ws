import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloNode(Node):
    def __init__(self):
        super().__init__('hello_node')
        self.publisher_ = self.create_publisher(String, 'sancho_greeting', 10)
        self.timer = self.create_timer(1.0, self.publish_greeting)
        self.counter = 0
        self.get_logger().info('Hello node started')

    def publish_greeting(self):
        msg = String()
        msg.data = f'Ciao SANCHO! Messaggio numero {self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pubblicato: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()