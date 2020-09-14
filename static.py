# Drawing project
# Author: Your name

from helpers import no_delay
from parts import draw_frame
from turtle import *

def default_settings():
    return {
        'leg_hip_angle': -30,
        'CAT_WIDTH': 200,
        'CAT_HEIGHT': 100,
        'TAIL_WIDTH': 20,
        'TAIL_LENGTH':70,
        'STAR_WIDTH':200,
        'STAR_LENGTH':170,
        'CIRCLE_RAD':50
    }

if __name__ == '__main__':
    settings = default_settings()
    with no_delay():
        draw_frame(settings)
        input()
