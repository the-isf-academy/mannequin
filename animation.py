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
from parts import draw_tail, draw_face, draw_cat, draw_frame
from time import sleep
from static import default_settings

def rotate(drawing_function, settings, delay=0.02):
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
            print(frame_settings['leg_hip_angle'])
        sleep(delay)

# Prepares settings for an animation. The helpers `interpolate` and `mirror``
# are used to create ranges of values for different settings. Basically, we want
# a range that slides from the first value to the last value and back, so that
# we can create a smooth loop of action. For example, the head should tilt
# forward and then back again. Try messing around with the values to create
# different actions!

if __name__ == '__main__':
    settings = default_settings()
    hideturtle()
    settings['leg_hip_angle'] = mirror(interpolate(-30, -60, 10))
    settings['CIRCLE_RAD'] = mirror(interpolate(10, 50, 10))
    rotate(draw_frame, settings)
