import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='navigation2',
            executable='your_navigation_node',
            name='navigation_node',
            output='screen',
            parameters=[{'your_navigation_params'}]
        ),
        # Adicione outros nós necessários para a navegação
    ])

