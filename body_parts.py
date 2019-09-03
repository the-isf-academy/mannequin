# Body Parts
# By Chris Proctor
# --------------------------------------
# This module draws body parts. There are a bunch of constants defining the size and
# shape of body parts, and then functions that do the drawing. 

from turtle import right, left, back, fillcolor
from helpers import fly, restore_state_when_finished, update_position
from shapes import rectangle, rectangle_from_center, rectangle_from_side_edge

# When variables are written in all-capital letters, it's a signal to programmers
# that they will be treated as constants--they will never change. It's very common
# to list out constants like this at the beginning of a program. It makes the code
# much easier to understand, and also makes it easier to change in the future. 
TORSO_WIDTH = 40
TORSO_HEIGHT = 100
TORSO_COLOR = "grey"

LEG_ORIGIN = [0, -50]
UPPER_LEG_WIDTH = 30
UPPER_LEG_LENGTH = 60
LOWER_LEG_WIDTH = 20
LOWER_LEG_LENGTH = 50
FOOT_WIDTH = 20
FOOT_LENGTH = 40
LEG_COLOR = "brown"

ARM_ORIGIN = [0, 35]
UPPER_ARM_WIDTH = 20
UPPER_ARM_LENGTH = 50
LOWER_ARM_WIDTH = 20
LOWER_ARM_LENGTH = 40
HAND_WIDTH = 20
HAND_LENGTH = 20
ARM_COLOR = "brown"

HEAD_ORIGIN = [5, 80]
HEAD_WIDTH = 35
HEAD_HEIGHT = 45
HEAD_COLOR = "grey"
    
def draw_body(settings):
    """
    Draws the whole body, using the turtle's position as the body center position
    and using the turtle's current heading as pointing "forward", out from the
    body's torso.

    The order in which we draw body parts matters, because we fill in all the rectangles
    and want closer things to get drawn over things that are further back.
    """
    draw_arm(settings, 'back')
    draw_leg(settings, 'back')
    draw_torso()
    draw_head(settings)
    draw_leg(settings, 'front')
    draw_arm(settings, 'front')

def draw_leg(settings, which_leg):
    """
    Draws a leg, starting with the upper leg, then the lower leg, and finally the foot.
    """
    fillcolor(LEG_COLOR)
    with restore_state_when_finished():
        update_position(LEG_ORIGIN)
        right(90)
        hip_angle = settings[which_leg + '_leg_hip_angle']
        right(hip_angle)
        rectangle_from_side_edge(UPPER_LEG_WIDTH, UPPER_LEG_LENGTH)
        fly(UPPER_LEG_LENGTH)
        knee_angle = settings[which_leg + '_leg_knee_angle']
        right(knee_angle)
        rectangle_from_side_edge(LOWER_LEG_WIDTH, LOWER_LEG_LENGTH)
        fly(LOWER_LEG_LENGTH)
        left(90)
        back(LOWER_LEG_WIDTH / 2)
        rectangle_from_side_edge(FOOT_WIDTH, FOOT_LENGTH)
        
def draw_arm(settings, which_arm):
    """
    Draws an arm, starting with the upper arm, then the lower arm, and finally the hand
    """
    fillcolor(ARM_COLOR)
    with restore_state_when_finished():
        update_position(ARM_ORIGIN)
        right(90)
        shoulder_angle = settings[which_arm + '_arm_shoulder_angle']
        right(shoulder_angle)
        rectangle_from_side_edge(UPPER_ARM_WIDTH, UPPER_ARM_LENGTH)
        fly(UPPER_ARM_LENGTH)
        elbow_angle = settings[which_arm + '_arm_elbow_angle']
        right(elbow_angle)
        rectangle_from_side_edge(LOWER_ARM_WIDTH, LOWER_ARM_LENGTH)
        fly(LOWER_ARM_LENGTH)
        left(45)
        rectangle(HAND_WIDTH, HAND_LENGTH)
        
def draw_torso():
    "Draws the torso"
    fillcolor(TORSO_COLOR)
    rectangle_from_center(TORSO_WIDTH, TORSO_HEIGHT)

def draw_head(settings):
    "Draws the head"
    fillcolor(HEAD_COLOR)
    with restore_state_when_finished():
        update_position(HEAD_ORIGIN)
        right(settings['head_angle'])
        rectangle_from_center(HEAD_WIDTH, HEAD_HEIGHT)
    
   
