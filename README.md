# Mannequin

By Chris Proctor

Mannequin is a package that draws a stick-figure body. The body's position can be controlled using a `dict` of settings, 
as shown in `main.py`:

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

If you want to put the body into other poses, start with the default settings and then update what you want:

    settings = default_settings()
    settings['head_angle'] = 30
    with no_delay():
        draw_body(settings)
    input("Press enter to continue...")

## Other modules
`main.py` is really short because most of the work is done in other modules. Here's a quick descrption of what 
lives where:

- `body_parts` contains constants defining the size and shape of different body parts, and functions to draw 
  all the body parts.
- `shapes` contains functions for the basic shapes used by `body_parts`. The basic `rectangle` starts drawing 
  from one corner of the rectangle, which is not always convenient. 
- `helpers` contains a mishmash of low-level helpers. Some, like `fly` and `no_delay`, are already familiar. 
  Of particular note is `restore_state_when_finished`, which puts the turtle back where she started after a code
  block runs. This is useful because we have agreed that our drawing functions should always return the turtle
  to where she started.
- `animation` brings the mannequin to life. Since we can completely control the mannequin's position using a
  dict of settings, we can animate the mannequin by gradually changing the values of different settings, and then 
  re-drawing the picture. 
