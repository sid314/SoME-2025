from manim import (
    BLUE,
    DARK_BLUE,
    DEGREES,
    DOWN,
    GREEN,
    GREY,
    IN,
    LEFT,
    ORANGE,
    OUT,
    PINK,
    RED,
    RIGHT,
    UP,
    YELLOW,
    AnimationGroup,
    Axes,
    Create,
    Cube,
    Dot,
    Dot3D,
    DrawBorderThenFill,
    FadeIn,
    FadeOut,
    NumberPlane,
    Point,
    Rectangle,
    Rotate,
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


class AntRandom(ThreeDScene):
    def construct(self):
        axis_length = 10
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        axes = ThreeDAxes(x_length=axis_length,
                          y_length=axis_length, z_length=7)
        label = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        self.add(label)

        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(axes)

        cube = Cube(fill_opacity=0.5, stroke_width=1.0, side_length=4)
        self.play(DrawBorderThenFill(cube))
        self.add(cube)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        # Down and up -y axis
        # Left Right -x axis
        # In out -z axis
        y = 0.5
        dot_a = Dot3D(color=GREEN, radius=0.045)
        corner_b = Point((DOWN + RIGHT + OUT) * cube.side_length / 2)
        corner_c = Point((RIGHT + y * UP + IN) * cube.side_length / 2)
        corner_a = Point((UP + LEFT + IN) * cube.side_length / 2)
        dot_a.move_to(corner_a)
        self.play(Create(dot_a))
        dotPath = TracedPath(dot_a.get_center, stroke_color=GREY)
        self.add(dotPath)
        self.play(dot_a.animate.move_to(corner_c))
        self.play(dot_a.animate.move_to(corner_b))
        self.play(FadeOut(dot_a, dotPath))

        self.wait(5)


class MosquitoTwo(ThreeDScene):
    def construct(self):
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(-0.4)
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        square_base = Square()
        square_top = square_base.copy().shift(2 * OUT)
        square_right = (
            square_base.copy()
            .shift(2 * RIGHT)
            .rotate(angle=90 * DEGREES, axis=DOWN, about_point=RIGHT)
        )
        square_left = (
            square_base.copy()
            .shift(2 * LEFT)
            .rotate(angle=90 * DEGREES, axis=UP, about_point=LEFT)
        )
        square_up = (
            square_base.copy()
            .shift(2 * UP)
            .rotate(angle=90 * DEGREES, axis=RIGHT, about_point=UP)
        )
        square_down = (
            square_base.copy()
            .shift(2 * DOWN)
            .rotate(angle=90 * DEGREES, axis=LEFT, about_point=DOWN)
        )
        dot = Dot3D(LEFT + UP)
        self.add(dot)
        fade_ins = [
            FadeIn(square_base),
            FadeIn(square_top),
            FadeIn(square_up),
            FadeIn(square_left),
            FadeIn(square_down),
            FadeIn(square_right),
        ]

        dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=5)
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(RIGHT + DOWN + 2 * OUT))
        self.wait(5)


class NaiveAnt(ThreeDScene):
    def construct(self):
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(-0.4)
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        square_base = Square(stroke_width=2)
        square_top = square_base.copy().shift(2 * OUT)
        square_right = (
            square_base.copy()
            .shift(2 * RIGHT)
            .rotate(angle=90 * DEGREES, axis=DOWN, about_point=RIGHT)
        )
        square_left = (
            square_base.copy()
            .shift(2 * LEFT)
            .rotate(angle=90 * DEGREES, axis=UP, about_point=LEFT)
        )
        square_up = (
            square_base.copy()
            .shift(2 * UP)
            .rotate(angle=90 * DEGREES, axis=RIGHT, about_point=UP)
        )
        square_down = (
            square_base.copy()
            .shift(2 * DOWN)
            .rotate(angle=90 * DEGREES, axis=LEFT, about_point=DOWN)
        )
        dot = Dot3D(LEFT + UP)
        self.add(dot)
        fade_ins = [
            FadeIn(square_base),
            FadeIn(square_top),
            FadeIn(square_up),
            FadeIn(square_left),
            FadeIn(square_down),
            FadeIn(square_right),
        ]

        dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=5)
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(RIGHT + DOWN))
        self.wait(1)

        self.play(dot.animate.move_to(RIGHT + DOWN + 2 * OUT))
        self.wait(5)


class OptimalAnt(ThreeDScene):
    def construct(self):
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(-0.4)
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        square_base = Square(stroke_width=2)
        square_top = square_base.copy().shift(2 * OUT)
        square_right = (
            square_base.copy()
            .shift(2 * RIGHT)
            .rotate(angle=90 * DEGREES, axis=DOWN, about_point=RIGHT)
        )
        square_left = (
            square_base.copy()
            .shift(2 * LEFT)
            .rotate(angle=90 * DEGREES, axis=UP, about_point=LEFT)
        )
        square_up = (
            square_base.copy()
            .shift(2 * UP)
            .rotate(angle=90 * DEGREES, axis=RIGHT, about_point=UP)
        )
        square_down = (
            square_base.copy()
            .shift(2 * DOWN)
            .rotate(angle=90 * DEGREES, axis=LEFT, about_point=DOWN)
        )
        dot = Dot3D(LEFT + UP)
        self.add(dot)
        fade_ins = [
            FadeIn(square_base),
            FadeIn(square_top),
            FadeIn(square_up),
            FadeIn(square_left),
            FadeIn(square_down),
            FadeIn(square_right),
        ]

        dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=5)
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(DOWN))
        self.wait(1)

        self.play(dot.animate.move_to(RIGHT + DOWN + 2 * OUT))
        self.wait(5)


class AntPaths(ThreeDScene):
    def construct(self):
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(-0.4)
        Dot3D.set_default(resolution=(2, 2))
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        square_base = Square(stroke_width=0.5, stroke_color=ORANGE)
        square_top = square_base.copy().shift(2 * OUT)
        square_right = (
            square_base.copy()
            .shift(2 * RIGHT)
            .rotate(angle=90 * DEGREES, axis=DOWN, about_point=RIGHT)
        )
        square_left = (
            square_base.copy()
            .shift(2 * LEFT)
            .rotate(angle=90 * DEGREES, axis=UP, about_point=LEFT)
        )
        square_up = (
            square_base.copy()
            .shift(2 * UP)
            .rotate(angle=90 * DEGREES, axis=RIGHT, about_point=UP)
        )
        square_down = (
            square_base.copy()
            .shift(2 * DOWN)
            .rotate(angle=90 * DEGREES, axis=LEFT, about_point=DOWN)
        )
        dotlist = []
        for _ in range(11):
            dotlist.append(Dot(LEFT + UP, radius=0))
        for dot in dotlist:
            dotPath = TracedPath(
                dot.get_center, stroke_color=BLUE, stroke_width=2)
            self.add(dotPath)
        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(
                    DOWN + ((-10 + 2 * x) / 10.0 * RIGHT))
            )
        fade_ins = [
            FadeIn(square_base),
            FadeIn(square_top),
            FadeIn(square_up),
            FadeIn(square_left),
            FadeIn(square_down),
            FadeIn(square_right),
        ]

        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(AnimationGroup(*first_moves, lag_ratio=0.1))
        self.wait(1)
        second_moves = []
        for dot in dotlist:
            second_moves.append(dot.animate.move_to(RIGHT + DOWN + 2 * OUT))
        self.play(AnimationGroup(*second_moves, lag_ratio=0.1))

        self.wait(2)


class Cube_Unfold(ThreeDScene):
    def construct(self):
        self.move_camera(50 * DEGREES)
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        square_base = Square()
        square_top = square_base.copy().shift(2 * OUT).set_color(BLUE)
        square_right = (
            square_base.copy()
            .shift(2 * RIGHT)
            .rotate(angle=90 * DEGREES, axis=DOWN, about_point=RIGHT)
            .set_color(GREEN)
        )
        square_left = (
            square_base.copy()
            .shift(2 * LEFT)
            .rotate(angle=90 * DEGREES, axis=UP, about_point=LEFT)
            .set_color(RED)
        )
        square_up = (
            square_base.copy()
            .shift(2 * UP)
            .rotate(angle=90 * DEGREES, axis=RIGHT, about_point=UP)
            .set_color(YELLOW)
        )
        square_down = (
            square_base.copy()
            .shift(2 * DOWN)
            .rotate(angle=90 * DEGREES, axis=LEFT, about_point=DOWN)
            .set_color(PINK)
        )
        fade_ins = [
            FadeIn(square_base),
            FadeIn(square_top),
            FadeIn(square_up),
            FadeIn(square_left),
            FadeIn(square_down),
            FadeIn(square_right),
        ]

        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.begin_ambient_camera_rotation(0.2)
        rotations = [
            Rotate(square_left, angle=-90 * DEGREES,
                   axis=UP, about_point=[-1, 0, 0]),
            Rotate(square_right, angle=-90 * DEGREES,
                   axis=DOWN, about_point=[1, 0, 0]),
            Rotate(square_up, angle=-90 * DEGREES,
                   axis=RIGHT, about_point=[0, 1, 0]),
            Rotate(square_down, angle=-90 * DEGREES,
                   axis=LEFT, about_point=[0, -1, 0]),
            # square_top.animate.move_to(4 * RIGHT),
            Rotate(square_top, angle=-90 * DEGREES,
                   axis=DOWN, about_point=[0, 0, -1]),
        ]
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))
        self.play(
            Rotate(square_top, angle=-90 * DEGREES,
                   axis=UP, about_point=[3, 0, 0]),
        )

        self.wait(5)


class Cuboid_Unfold(ThreeDScene):
    def construct(self):
        a = 1.0
        b = 1.4
        c = 1.2
        self.move_camera(50 * DEGREES)
        self.camera.set_zoom(1)
        axes = Axes(x_length=16, y_length=16,
                    x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        base = Rectangle(width=a, height=b, stroke_width=2)

        top = base.copy().shift(c * OUT).set_color(BLUE)

        right = Rectangle(width=c, height=b, color=GREEN, stroke_width=2)
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=90 * DEGREES, axis=DOWN,
                     about_point=(a / 2) * RIGHT)

        left = Rectangle(width=c, height=b, color=RED, stroke_width=2)
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=90 * DEGREES, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(width=a, height=c, color=YELLOW, stroke_width=2)
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=90 * DEGREES, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(width=a, height=c, color=PINK, stroke_width=2)
        down.shift((-(c + b) / 2) * UP)
        down.rotate(angle=90 * DEGREES, axis=LEFT, about_point=(b / 2) * DOWN)
        fade_ins = [
            FadeIn(base),
            FadeIn(top),
            FadeIn(up),
            FadeIn(left),
            FadeIn(down),
            FadeIn(right),
        ]
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.begin_ambient_camera_rotation(0.2)
        rotations = [
            Rotate(left, angle=-90 * DEGREES, axis=UP,
                   about_point=[-a / 2, 0, 0]),
            Rotate(right, angle=-90 * DEGREES,
                   axis=DOWN, about_point=[a / 2, 0, 0]),
            Rotate(up, angle=-90 * DEGREES, axis=RIGHT,
                   about_point=[0, b / 2, 0]),
            Rotate(down, angle=-90 * DEGREES, axis=LEFT,
                   about_point=[0, -b / 2, 0]),
            Rotate(top, angle=-90 * DEGREES, axis=DOWN,
                   about_point=[0, 0, -a / 2]),
        ]
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))
        self.play(
            Rotate(top, angle=-90 * DEGREES, axis=UP,
                   about_point=[c + (a / 2), 0, 0]),
        )

        self.wait(5)
