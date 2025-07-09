from manim import (
    DARK_BLUE,
    DEGREES,
    DOWN,
    GREEN,
    IN,
    LEFT,
    ORANGE,
    OUT,
    RED,
    RIGHT,
    UP,
    Create,
    Cube,
    Dot,
    Dot3D,
    DrawBorderThenFill,
    FadeOut,
    NumberPlane,
    Point,
    Scene,
    Square,
    ThreeDAxes,
    ThreeDScene,
    TracedPath,
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


class MosquitoCube(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=90 * DEGREES)
        axes = ThreeDAxes()

        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(axes)

        cube = Cube(fill_opacity=0.25, stroke_width=1.0, side_length=4)
        self.play(DrawBorderThenFill(cube))
        self.stop_ambient_camera_rotation()
        self.wait(1)
        dot_a = Dot3D(color=DARK_BLUE, radius=0.045)
        corner_b = Point((DOWN + RIGHT + OUT) * cube.side_length / 2)
        corner_a = Point((UP + LEFT + IN) * cube.side_length / 2)
        dot_a.move_to(corner_a)
        self.play(Create(dot_a))
        dotPath = TracedPath(dot_a.get_center, stroke_color=RED)
        self.add(dotPath)
        self.play(dot_a.animate.move_to(corner_b))
        self.play(FadeOut(dot_a, dotPath))

        self.wait(5)
