# Animation
# By Chris Proctor
# -----------------
# This module animates the mannequin. This would normally be a really tricky 
# thing to do, but because the project is nicely decomposed into its parts, 
# it's pretty easy.

# Note: This module is completely optional. If you do decide to play with it, 
# on't expect understand everything that's happening here. Instead, try playing
# around with the settings at the bottom to see what happens. 

from turtle import clear, hideturtle
from helpers import no_delay, generate_animation_settings, mirror, interpolate
from main import default_settings
from body_parts import draw_body
from time import sleep

def animate(drawing_function, settings, delay=0.02):
    """
    Draws an animation by looping through values of settings, clearing the
    screen, and calling `drawing_function` with the settings for that frame. 
    Each value in settings should either be a single value (like 10) or a 
    list of values (like [10, 11, 12, 13, 14, 13, 12, 11, 10]). If a setting
    is a single value, that won't ever change. If it's a list of values, each 
    frame will get a value by looping through that list forever.
    """
    for frame_settings in generate_animation_settings(settings):
        with no_delay():
            clear()
            drawing_function(frame_settings)
        sleep(delay)

# Prepares settings for an animation. The helpers `interpolate` and mirror` 
# are used to create the 
#

if __name__ == '__main__':
    settings = default_settings()
    settings['head_angle'] = mirror(interpolate(-30, 30, 10))
    settings['back_arm_shoulder_angle'] = mirror(interpolate(-45, 45, 10))
    settings['front_arm_shoulder_angle'] = mirror(interpolate(45, -45, 10))
    settings['back_arm_elbow_angle'] = mirror(interpolate(-90, -30, 10))
    settings['front_arm_elbow_angle'] = mirror(interpolate(-30, -90, 10))
    settings['back_leg_hip_angle'] = mirror(interpolate(-30, 30, 10))
    settings['back_leg_knee_angle'] = mirror(interpolate(0, 30, 10))
    settings['front_leg_hip_angle'] = mirror(interpolate(30, -30, 10))
    settings['front_leg_knee_angle'] = mirror(interpolate(30, 0, 10))
    hideturtle()
    animate(draw_body, settings)
