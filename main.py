from manim import (
    GREEN,
    ORANGE,
    PURPLE,
    RED,
    RIGHT,
    UP,
    Circle,
    Dot,
    NumberPlane,
    Point,
    Scene,
    Square,
)


class Test(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        # next to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(red_dot, green_dot)
        # shift
        s = Square(color=ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)
