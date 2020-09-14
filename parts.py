# Body Parts
# By Chris Proctor
# --------------------------------------
# This module draws parts. There are a bunch of constants defining the size and
# shape of body parts, and then functions that do the drawing.

from turtle import *
from helpers import fly, restore_state_when_finished, update_position
from shapes import rectangle, rectangle_from_center, rectangle_from_side_edge

# When variables are written in all-capital letters, it's a signal to programmers
# that they will be treated as constants--they will never change. It's very common
# to list out constants like this at the beginning of a program. It makes the code
# much easier to understand, and also makes it easier to change in the future.
CAT_WIDTH = 200
CAT_HEIGHT = 100
CAT_COLOR = "brown"

LEG_ORIGIN = [100, 25]
LEG_COLOR = "brown"

def draw_frame(settings):
    """
    Draws the whole frame, using the turtle's position as the body center position
    and using the turtle's current heading as pointing "forward", out from the
    body's torso.

    The order in which we draw body parts matters, because we fill in all the rectangles
    and want closer things to get drawn over things that are further back.
    """
    draw_cat(settings)
    draw_face(settings)
    draw_tail(settings)

def draw_cat(settings):
    with restore_state_when_finished():
        fillcolor(CAT_COLOR)
        goto(0,0)
        rectangle_from_center(settings['CAT_WIDTH'], settings['CAT_HEIGHT'])

def draw_face(settings):
    with restore_state_when_finished():
        penup()
        goto(-100, 25)
        pendown()
        begin_fill()
        circle(settings['CIRCLE_RAD'])
        end_fill()
        penup()

def draw_tail(settings):
    with restore_state_when_finished():
        fillcolor(LEG_COLOR)
        penup()
        goto(100, 50)
        pendown()
        right(90)
        tail_angle = settings['leg_hip_angle']
        right(tail_angle)
        rectangle(settings['TAIL_LENGTH'], settings['TAIL_WIDTH'])
        penup()


def draw_star(settings):
    "Draws a star"
    with restore_state_when_finished():
        color('red', 'yellow')
        begin_fill()
        while True:
            forward(settings["STAR_WIDTH"])
            left(settings["STAR_LENGTH"])
            if abs(pos()) < 1:
                break
        end_fill()
