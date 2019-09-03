# Drawing project
# Author: Your name

from helpers import no_delay
from body_parts import draw_body

def default_settings():
    return {
        'head_angle': 10,
        'front_arm_shoulder_angle': 45,
        'front_arm_elbow_angle': -90,
        'back_arm_shoulder_angle': -45,
        'back_arm_elbow_angle': -90,
        'front_leg_hip_angle': 30,
        'front_leg_knee_angle': 0,
        'back_leg_hip_angle': -30,
        'back_leg_knee_angle': 30
    }

if __name__ == '__main__':
    settings = default_settings()
    with no_delay():
        draw_body(settings)
    input("Press enter to continue...")
