import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                'mapping_launch.py'
            )
        ),

        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                'navigation_launch.py'
            )
        ),
    ])

