import launch
import launch_ros.actions
import launch_testing

import pytest

import test_joy_twist


@pytest.mark.rostest
def generate_test_description():
    teleop_node = launch_ros.actions.Node(
        package='dyno_teleop_ros2',
        executable='teleop_joy_node',
        parameters=[{
            'axis_linear.x': 1,
            'axis_linear.y': 2,
            'axis_angular.yaw': 0,
            'scale_linear.x': 1.0,
            'scale_linear.y': 4.0,
            'scale_angular.yaw': 3.0,
            'enable_button': 0,
        }],
    )

    return launch.LaunchDescription([
            teleop_node,
            launch_testing.actions.ReadyToTest(),
        ]), locals()


class HolonomicJoy(test_joy_twist.TestJoyTwist):

    def setUp(self):
        super().setUp()
        self.joy_msg['axes'] = [0.3, 0.4, 0.5]
        self.joy_msg['buttons'] = [1]
        self.expect_cmd_vel['linear']['x'] = 0.4
        self.expect_cmd_vel['linear']['y'] = 2.0
        self.expect_cmd_vel['angular']['z'] = 0.9
