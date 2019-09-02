from turtle import forward, right, left, back, circle, begin_fill, end_fill
from helpers import fly

def rectangle(width, height):
    """
    Draws a rectangle, starting with the width and turning right
    """
    begin_fill()
    for side in [width, height, width, height]:
        forward(side)
        right(90)
    end_fill()

def rectangle_from_center(width, height):
    """
    Draws a rectangle, but from the center. The turtle's starting direction
    points in the direction of the width.
    """
    left(90)
    fly(height/2)
    right(90)
    fly(-width/2)
    rectangle(width, height)
    fly(width/2)
    right(90)
    fly(height/2)
    left(90)

def rectangle_from_side_edge(width, height):
    """
    Draws a rectangle, but from the center of the side edge 
    (the middle of width), with the turtle facing the direction
    the rectangle will be drawn.
    """
    left(90)
    back(width / 2)
    rectangle(width, height)
    forward(width / 2)
    right(90)
