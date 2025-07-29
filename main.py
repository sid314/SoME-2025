from manim import (
    AnimationGroup,
    Axes,
    BLUE,
    BraceBetweenPoints,
    Create,
    Cube,
    DARK_BLUE,
    DEGREES,
    DOWN,
    Dot,
    Dot3D,
    DrawBorderThenFill,
    FadeIn,
    FadeOut,
    GREEN,
    GREY,
    IN,
    Indicate,
    LEFT,
    Line,
    MathTex,
    NumberPlane,
    ORANGE,
    OUT,
    PI,
    PINK,
    Point,
    RED,
    RIGHT,
    Rectangle,
    Rotate,
    Scene,
    Square,
    Tex,
    Text,
    ThreeDAxes,
    ThreeDScene,
    TracedPath,
    Transform,
    UL,
    UP,
    UR,
    Unwrite,
    VGroup,
    Write,
    YELLOW,
)


def write_unwrite(scene: Scene, text: str, wait: int = 0):
    tex = Tex(text)
    scene.play(Write(tex))
    if wait > 0:
        scene.wait(wait)

    scene.play(Unwrite(tex))


def write_unwrite_three_d(scene: ThreeDScene, text: str, wait: int = 0):
    tex = Tex(text)
    scene.add_fixed_in_frame_mobjects(tex)
    tex.to_corner(UL)

    scene.play(Write(tex))
    if wait > 0:
        scene.wait(wait)
    scene.play(Unwrite(tex))


def write(scene: Scene, tex: Tex):
    scene.play(Write(tex))


def unwrite(scene: Scene, tex: Tex):
    scene.play(Write(tex))


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
        axes = ThreeDAxes(x_length=axis_length, y_length=axis_length, z_length=7)
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
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
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
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
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
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
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
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
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
            dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=2)
            self.add(dotPath)
        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(DOWN + ((-10 + 2 * x) / 10.0 * RIGHT))
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
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
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
            Rotate(square_left, angle=-90 * DEGREES, axis=UP, about_point=[-1, 0, 0]),
            Rotate(square_right, angle=-90 * DEGREES, axis=DOWN, about_point=[1, 0, 0]),
            Rotate(square_up, angle=-90 * DEGREES, axis=RIGHT, about_point=[0, 1, 0]),
            Rotate(square_down, angle=-90 * DEGREES, axis=LEFT, about_point=[0, -1, 0]),
            # square_top.animate.move_to(4 * RIGHT),
            Rotate(square_top, angle=-90 * DEGREES, axis=DOWN, about_point=[0, 0, -1]),
        ]
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))
        self.play(
            Rotate(square_top, angle=-90 * DEGREES, axis=UP, about_point=[3, 0, 0]),
        )

        self.wait(5)


class Cuboid_Unfold(ThreeDScene):
    def construct(self):
        a = 1.0
        b = 1.4
        c = 1.2
        self.move_camera(50 * DEGREES)
        self.camera.set_zoom(1)
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        base = Rectangle(width=a, height=b, stroke_width=2)

        top = base.copy().shift(c * OUT).set_color(BLUE)

        right = Rectangle(width=c, height=b, color=GREEN, stroke_width=2)
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=90 * DEGREES, axis=DOWN, about_point=(a / 2) * RIGHT)

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
            Rotate(left, angle=-90 * DEGREES, axis=UP, about_point=[-a / 2, 0, 0]),
            Rotate(right, angle=-90 * DEGREES, axis=DOWN, about_point=[a / 2, 0, 0]),
            Rotate(up, angle=-90 * DEGREES, axis=RIGHT, about_point=[0, b / 2, 0]),
            Rotate(down, angle=-90 * DEGREES, axis=LEFT, about_point=[0, -b / 2, 0]),
            Rotate(top, angle=-90 * DEGREES, axis=DOWN, about_point=[0, 0, -a / 2]),
        ]
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))
        self.play(
            Rotate(top, angle=-90 * DEGREES, axis=UP, about_point=[c + (a / 2), 0, 0]),
        )

        self.wait(5)


class Cuboid_Ant_Paths(ThreeDScene):
    def construct(self):
        a = 1.0
        b = 1.4
        c = 1.2
        self.move_camera(50 * DEGREES)
        self.camera.set_zoom(1.2)
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        base = Rectangle(width=a, height=b, stroke_width=0.5, stroke_color=ORANGE)

        top = base.copy().shift(c * OUT)

        right = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=90 * DEGREES, axis=DOWN, about_point=(a / 2) * RIGHT)

        left = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=90 * DEGREES, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=90 * DEGREES, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
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
        self.begin_ambient_camera_rotation(-0.5)

        dotlist = []
        for _ in range(11):
            dotlist.append(Dot(a / 2 * LEFT + b / 2 * UP, radius=0))
        for dot in dotlist:
            dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=2)
            self.add(dotPath)

        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(
                    b / 2 * DOWN + ((-10 + 2 * x) / 10.0 * RIGHT * a / 2)
                )
            )
        self.play(AnimationGroup(*first_moves, lag_ratio=0.3))
        second_moves = []
        for dot in dotlist:
            second_moves.append(
                dot.animate.move_to(a / 2 * RIGHT + b / 2 * DOWN + c * OUT)
            )
        self.play(AnimationGroup(*second_moves, lag_ratio=0.3))
        self.wait(1)


class Cuboid_Ant_Paths_Optimum(ThreeDScene):
    def construct(self):
        a = 2.5
        b = 3.5
        c = 1.5
        self.move_camera(theta=-7.13726219, phi=0.85266463)
        # self.camera.set_zoom(0.5)
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
        axes_label = axes.get_axis_labels(x_label="x", y_label="y")
        self.add(axes, axes_label)
        base = Rectangle(width=a, height=b, stroke_width=0.5, stroke_color=ORANGE)
        top = base.copy().shift(c * OUT)

        right = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=PI / 2, axis=DOWN, about_point=(a / 2) * RIGHT)

        left = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=PI / 2, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=PI / 2, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
        down.shift((-(c + b) / 2) * UP)
        down.rotate(angle=PI / 2, axis=LEFT, about_point=(b / 2) * DOWN)
        # cube = VGroup(base, top, left, right, up, down)
        fade_ins = [
            FadeIn(base),
            FadeIn(top),
            FadeIn(up),
            FadeIn(left),
            FadeIn(down),
            FadeIn(right),
        ]
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        # self.begin_ambient_camera_rotation(-0.1)

        up_right = base.get_corner(UP + RIGHT)
        up_left = base.get_corner(UP + LEFT)
        # up_left_top = top.get_corner(UP + LEFT)
        down_left = base.get_corner(DOWN + LEFT)
        down_left_dummy = (-a / 2, (b / 2) - c, 0)

        # self.add(Dot(up_right))
        # self.add(Dot(up_left))
        # self.add(Dot(up_left_top))
        # print(c)
        # print("side-length", Line(up_left, up_left_top).get_length())
        # print("side-length-dummy", Line(up_left, down_left_dummy).get_length())
        # self.add(Dot(down_left))
        # self.add(Dot(down_left_dummy))

        brace_a = BraceBetweenPoints(up_left, up_right, direction=UP)
        a_text = brace_a.get_tex("a")
        self.play(FadeIn(a_text, brace_a))

        brace_b = BraceBetweenPoints(up_left, down_left, direction=LEFT)
        b_text = brace_b.get_tex("b")
        self.play(FadeIn(b_text, brace_b))

        brace_c = BraceBetweenPoints(up_left, down_left_dummy, direction=LEFT)
        brace_c.rotate(PI / -2, about_point=up_left, axis=RIGHT)
        c_text = brace_c.get_tex("c")
        c_text.rotate(PI / 2, about_point=(-a / 2, b / 2, c / 2), axis=RIGHT)
        self.play(FadeIn(c_text, brace_c))

        # braces_and_text = VGroup(brace_a, brace_b, brace_c, a_text, b_text, c_text)

        dotlist = []
        for _ in range(11):
            dotlist.append(Dot(a / 2 * LEFT + b / 2 * UP, radius=0))
        dotpaths = []
        for dot in dotlist:
            dotPath = TracedPath(dot.get_center, stroke_color=BLUE, stroke_width=2)
            dotpaths.append(dotPath)
            self.add(dotPath)

        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(
                    b / 2 * DOWN + ((-10 + 2 * x) / 10.0 * RIGHT * a / 2)
                )
            )
        self.play(AnimationGroup(*first_moves, lag_ratio=0.1))
        second_moves = []
        for dot in dotlist:
            second_moves.append(
                dot.animate.move_to(a / 2 * RIGHT + b / 2 * DOWN + c * OUT)
            )
        self.play(AnimationGroup(*second_moves, lag_ratio=0.1))
        self.interactive_embed()
        # self.play(FadeOut(braces_and_text))
        # self.play(FadeOut(*dotpaths, lag_ratio=0.1))
        # self.play(FadeOut(cube))
        self.wait(1)


class Final(ThreeDScene):
    def construct(self):
        camera_speed = -0.2
        stroke_width_shapes = 0.5
        stroke_width_paths = 2
        dot_radius = 0.0
        center = 0 * (RIGHT + UP + OUT)

        a = 2.0
        b = 2.0
        c = 2.0
        # Hello
        t1 = Text("Hello.")
        self.play(Write(t1))
        self.play(Unwrite(t1))
        t1 = Tex("Have you ever wondered what is the best way ")
        t2 = Tex("to move from one diagonally opposite corner").next_to(
            t1, direction=DOWN
        )
        t3 = Tex("of a cube to the other?").next_to(t2, direction=DOWN)
        t4 = AnimationGroup(Write(t1), Write(t2), Write(t3), lag_ratio=0.7)
        self.play(t4)
        t4 = AnimationGroup(Unwrite(t1), Unwrite(t2), Unwrite(t3), lag_ratio=0.1)
        self.play(t4)
        t1 = Tex("It's easy enough if you are a mosquito.")
        self.play(Write(t1))
        t2 = Tex("You just fly across.")
        t2.next_to(t1, direction=DOWN)
        self.play(Write(t2))
        self.play(FadeOut(t1, t2))
        # mosquito
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(camera_speed)
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
        axes_label = axes.get_axis_labels(x_label="x", y_label="y")
        base = Rectangle(
            width=a, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        top = base.copy().shift(c * OUT)

        right = Rectangle(
            width=c, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=PI / 2, axis=DOWN, about_point=(a / 2) * RIGHT)

        left = Rectangle(
            width=c, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=PI / 2, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(
            width=a, height=c, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=PI / 2, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(
            width=a, height=c, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        down.shift((-(c + b) / 2) * UP)
        down.rotate(angle=PI / 2, axis=LEFT, about_point=(b / 2) * DOWN)

        dot_position_start = a / 2 * RIGHT + b / 2 * DOWN
        dot_position_mid = -dot_position_start
        dot_postition_mid_optimum = a / 2 * LEFT
        dot_position_end = dot_position_mid + c * OUT
        dot = Dot(dot_position_start, radius=dot_radius)
        self.add(dot)
        fade_ins = [
            FadeIn(axes),
            FadeIn(axes_label),
            FadeIn(base),
            FadeIn(top),
            FadeIn(up),
            FadeIn(left),
            FadeIn(down),
            FadeIn(right),
        ]

        dotPath = TracedPath(
            dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
        )
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(dot_position_end))
        self.stop_ambient_camera_rotation()
        # measure mosquito
        self.move_camera(PI / 4, -PI / 4, zoom=0.7)
        self.play(FadeOut(axes, axes_label))
        t1 = Tex(
            "Lets measure how much you travelled \\\\ by using the Pythagoras' Theorem. "
        ).set_stroke(width=0.5)
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))

        up_right = base.get_corner(UP + RIGHT)
        up_left = base.get_corner(UP + LEFT)
        # up_left_top = top.get_corner(UP + LEFT)
        down_left = base.get_corner(DOWN + LEFT)
        down_right = base.get_corner(DOWN + RIGHT)
        down_left_dummy = (-a / 2, (b / 2) - c, 0)
        brace_a = BraceBetweenPoints(up_left, up_right, direction=UP)
        a_text = brace_a.get_tex(f"{(a * 2)} unit")
        self.play(FadeIn(a_text, brace_a))

        brace_b = BraceBetweenPoints(up_left, down_left, direction=LEFT)
        b_text = brace_b.get_tex(f"{(b * 2)} unit")
        self.play(FadeIn(b_text, brace_b))

        brace_c = BraceBetweenPoints(up_left, down_left_dummy, direction=LEFT)
        brace_c.rotate(PI / -2, about_point=up_left, axis=RIGHT)
        c_text = brace_c.get_tex(f"{(c * 2)} unit")
        c_text.rotate(PI / 2, about_point=(-a / 2, b / 2, c / 2), axis=RIGHT)
        self.play(FadeIn(c_text, brace_c))

        brace_d = BraceBetweenPoints(up_left, down_right)
        d_text = brace_d.get_tex("4\\sqrt{2} unit").next_to(brace_d, direction=DOWN)

        self.play(
            FadeOut(
                base,
                top,
                up,
                down,
                left,
                right,
                dot,
                dotPath,
                brace_a,
                brace_b,
                brace_c,
                a_text,
                b_text,
                c_text,
                t1,
            )
        )
        # mosquito measure calculation
        self.move_camera(0, -PI / 2, zoom=1.0)
        t3 = Tex("Distance travelled (d) = ").move_to(center)
        t4 = MathTex("\\sqrt{4^2+4^2+4^2}").next_to(t3)
        t5 = MathTex("4\\sqrt{3}").next_to(t3)
        self.play(AnimationGroup(Write(t3), Write(t4), lag_ratio=1))
        self.play(Transform(t4, t5))
        t6 = MathTex("\\textrm{Distance travelled (d)} \\approx ").move_to(center)
        t5 = MathTex("6.928").next_to(t3)
        self.play(Transform(t3, t6), Transform(t4, t5))
        self.play(Unwrite(t3))
        self.play(t4.animate.move_to(center))
        self.play(Unwrite(t4))
        t1 = Tex("Not bad.")
        t2 = Tex("Infact, this is the shortest path possible").next_to(
            t1, direction=DOWN
        )
        self.play(AnimationGroup(Write(t1), Write(t2), lag_ratio=1))
        self.play(AnimationGroup(Unwrite(t1), Unwrite(t2), lag_ratio=0.1))

        # ant naive
        t1 = Tex("But what if you are an ant?")
        self.play(Write(t1))
        self.play(Unwrite(t1))
        t1 = Tex("Your first instinct maybe to go across and up.")
        t2 = Tex("Something like this:")
        t2.next_to(t1, direction=DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(FadeOut(t1), FadeOut(t2))
        # ant naive move
        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(-0.2)
        self.add(axes, axes_label)
        dot.move_to(dot_position_start)
        self.add(dot)
        fade_ins = [
            FadeIn(base),
            FadeIn(top),
            FadeIn(up),
            FadeIn(left),
            FadeIn(down),
            FadeIn(right),
            FadeIn(axes),
            FadeIn(axes_label),
        ]

        dotPath = TracedPath(
            dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
        )
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(dot_position_mid))
        self.wait(1)

        self.play(dot.animate.move_to(dot_position_end))
        self.stop_ambient_camera_rotation()

        # ant naive measure

        self.move_camera(PI / 4, -PI / 4)
        self.move_camera(zoom=0.7)
        t1 = Tex("Lets measure again ")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(FadeOut(axes), FadeOut(axes_label), Write(t1))
        self.play(FadeIn(brace_c), FadeIn(c_text), FadeIn(brace_d), FadeIn(d_text))
        self.wait(2)
        self.play(
            FadeOut(
                base,
                top,
                up,
                down,
                left,
                right,
                dot,
                dotPath,
                brace_c,
                brace_d,
                d_text,
                c_text,
                t1,
            )
        )

        # ant naive calculation
        self.move_camera(0, -PI / 2, zoom=1.0)
        t3 = Tex("Distance travelled (d) = ").move_to(center)
        t4 = MathTex("\\sqrt{4^2+4^2} +4").next_to(t3)
        t5 = MathTex("4(\\sqrt{2}+1)").next_to(t3)
        self.play(AnimationGroup(Write(t3), Write(t4), lag_ratio=1))
        self.play(Transform(t4, t5))
        t6 = MathTex("\\textrm{Distance travelled (d)} \\approx ").move_to(center)
        t5 = MathTex("9.657").next_to(t3)
        self.play(Transform(t3, t6), Transform(t4, t5))
        self.play(Unwrite(t3))
        self.play(t4.animate.move_to(center))
        self.play(Unwrite(t4))

        # ant naive different paths
        t1 = Tex("Hmmm, but there were many other paths \\\\ you could have chosen.")
        self.play(Write(t1))
        self.play(FadeOut(t1))

        self.move_camera(50 * DEGREES)
        self.begin_ambient_camera_rotation(0.2)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        # ant naive different paths move
        dotlist = []
        for _ in range(11):
            dotlist.append(Dot(a / 2 * LEFT + b / 2 * UP, radius=0))
        dotpaths = []
        for dot in dotlist:
            dotPath = TracedPath(
                dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
            )
            dotpaths.append(dotPath)
            self.add(dotPath)

        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(
                    b / 2 * DOWN + ((-10 + 2 * x) / 10.0 * RIGHT * a / 2)
                )
            )
        self.play(AnimationGroup(*first_moves, lag_ratio=0.1))
        second_moves = []
        for dot in dotlist:
            second_moves.append(
                dot.animate.move_to(a / 2 * RIGHT + b / 2 * DOWN + c * OUT)
            )
        self.play(AnimationGroup(*second_moves, lag_ratio=0.1))
        self.wait(2)
        self.stop_ambient_camera_rotation()
        # cube unfold first text
        self.move_camera(PI / 4, -PI / 4)
        self.move_camera(zoom=0.7)
        t1 = Tex("But how do we know which is the shortest path?")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        self.play(Unwrite(t1))
        t2 = Tex("Let's start by unfolding this cube.")
        self.add_fixed_in_frame_mobjects(t2)
        t2.to_corner(UL)
        self.play(Write(t2))

        # cube unfold first move

        self.play(FadeOut(*dotpaths, lag_ratio=0.1))
        rotations = [
            Rotate(left, angle=-90 * DEGREES, axis=UP, about_point=[-a / 2, 0, 0]),
            Rotate(right, angle=-90 * DEGREES, axis=DOWN, about_point=[a / 2, 0, 0]),
            Rotate(up, angle=-90 * DEGREES, axis=RIGHT, about_point=[0, b / 2, 0]),
            Rotate(down, angle=-90 * DEGREES, axis=LEFT, about_point=[0, -b / 2, 0]),
            Rotate(top, angle=-90 * DEGREES, axis=DOWN, about_point=[0, 0, -a / 2]),
        ]
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))
        self.play(
            Rotate(top, angle=-90 * DEGREES, axis=UP, about_point=[c + (a / 2), 0, 0]),
        )
        self.play(Unwrite(t2))
        t1 = Tex("Let's mark the starting and ending positions.")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        start_dot = Dot()

        start_dot.move_to(dot_position_start)
        corner_end = top.get_corner(UP + RIGHT)
        end_dot = Dot()
        end_dot.move_to(corner_end)
        self.play(FadeIn(start_dot, end_dot))
        self.play(Unwrite(t1))
        t1 = Tex("The shortest path is a straight line!")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        self.play(Unwrite(t1))
        t1 = Tex("Notice that the ant crosses the bottom edge at its midpoint.")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))

        dotPath = TracedPath(
            start_dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
        )
        self.add(dotPath)
        self.play(start_dot.animate.move_to(end_dot))
        self.play(FadeOut(start_dot, end_dot), Unwrite(t1))
        t1 = Tex("Let's measure again!")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))

        corner_top_down_right = top.get_corner(DOWN + RIGHT)

        brace_d = BraceBetweenPoints(dot_position_start, corner_top_down_right)
        d_text = brace_d.get_tex(f"{(a + c) * 2} units")
        brace_e = BraceBetweenPoints(corner_top_down_right, corner_end)
        e_text = brace_e.get_tex(f"{b * 2} units")
        self.play(FadeIn(brace_d, d_text, brace_e, e_text))
        self.play(
            FadeOut(
                base,
                top,
                up,
                down,
                left,
                right,
                brace_d,
                d_text,
                brace_e,
                e_text,
                dotPath,
                axes,
                axes_label,
                t1,
            )
        )
        self.move_camera(0, -PI / 2, zoom=1.0)
        self.wait(1)
        t3 = Tex("Distance travelled (d) = ").move_to(center)
        t4 = MathTex("\\sqrt{8^2+4^2}").next_to(t3)
        t5 = MathTex("\\sqrt{80}").next_to(t3)
        self.play(AnimationGroup(Write(t3), Write(t4), lag_ratio=1))
        self.wait(0.5)
        self.play(Transform(t4, t5))
        self.wait(0.5)
        t6 = MathTex("\\textrm{Distance travelled (d)} \\approx ").move_to(center)
        t5 = MathTex("8.944").next_to(t3)
        self.play(Transform(t3, t6), Transform(t4, t5))
        self.wait(0.5)
        self.play(Unwrite(t3))
        self.wait(0.5)
        self.play(t4.animate.move_to(center))
        self.play(Unwrite(t4))
        t1 = Tex("Hmmm, better.")
        self.play(Write(t1))
        self.play(Unwrite(t1))
        t1 = Tex("Lets see this in 3D")
        self.play(Write(t1))
        self.play(FadeOut(t1))
        self.move_camera(PI / 4, -PI / 4)
        self.move_camera(zoom=1)
        base = Rectangle(
            width=a, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        top = base.copy().shift(c * OUT)

        right = Rectangle(
            width=c, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=PI / 2, axis=DOWN, about_point=(a / 2) * RIGHT)

        left = Rectangle(
            width=c, height=b, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=PI / 2, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(
            width=a, height=c, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=PI / 2, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(
            width=a, height=c, stroke_width=stroke_width_shapes, stroke_color=ORANGE
        )
        down.shift((-(c + b) / 2) * UP)
        down.rotate(angle=PI / 2, axis=LEFT, about_point=(b / 2) * DOWN)

        fade_ins = [
            FadeIn(base),
            FadeIn(top),
            FadeIn(up),
            FadeIn(left),
            FadeIn(down),
            FadeIn(right),
            FadeIn(axes),
            FadeIn(axes_label),
        ]

        dot.move_to(dot_position_start)
        self.add(dot)
        dotPath = TracedPath(
            dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
        )
        self.add(dotPath)
        self.play(AnimationGroup(*fade_ins, lag_ratio=0.1))
        self.play(dot.animate.move_to(dot_postition_mid_optimum))
        self.wait(1)
        self.play(dot.animate.move_to(dot_position_end))
        self.wait(1)
        self.move_camera(zoom=0.7)
        t1 = Tex("Notice how it again passes through the midpoint")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        self.wait(1)
        self.play(FadeOut(t1))
        self.play(
            FadeOut(base, top, up, down, left, right, dot, dotPath, axes, axes_label)
        )
        self.move_camera(0, -PI / 2)

        t1 = Tex("But what if the ant had to go across a rectangle.")
        t2 = Tex("There are again many different paths").next_to(t1, direction=DOWN)
        t3 = Tex(
            "and going through the edge of the midpoint may not be the best solution"
        ).next_to(t2, direction=DOWN)
        t4 = AnimationGroup(Write(t1), Write(t2), Write(t3), lag_ratio=0.7)
        self.play(t4)
        t4 = AnimationGroup(FadeOut(t1), FadeOut(t2), FadeOut(t3), lag_ratio=0.1)
        self.play(t4)
        a = 1.0
        b = 1.4
        c = 1.2
        self.move_camera(50 * DEGREES)
        self.camera.set_zoom(1.2)
        axes = Axes(x_length=16, y_length=16, x_range=[-16, 16], y_range=[-16, 16])
        self.add(axes)
        base = Rectangle(width=a, height=b, stroke_width=0.5, stroke_color=ORANGE)

        top = base.copy().shift(c * OUT)

        right = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        right.shift(((c + a) / 2) * RIGHT)
        right.rotate(angle=90 * DEGREES, axis=DOWN, about_point=(a / 2) * RIGHT)

        left = Rectangle(width=c, height=b, stroke_width=0.5, stroke_color=ORANGE)
        left.shift((-(c + a) / 2) * RIGHT)
        left.rotate(angle=90 * DEGREES, axis=UP, about_point=(a / 2) * LEFT)

        up = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
        up.shift(((c + b) / 2) * UP)
        up.rotate(angle=90 * DEGREES, axis=RIGHT, about_point=(b / 2) * UP)

        down = Rectangle(width=a, height=c, stroke_width=0.5, stroke_color=ORANGE)
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
        self.begin_ambient_camera_rotation(camera_speed)
        dotlist = []
        for _ in range(11):
            dotlist.append(Dot(a / 2 * LEFT + b / 2 * UP, radius=0))
        dotpaths = []
        for dot in dotlist:
            dotPath = TracedPath(
                dot.get_center, stroke_color=BLUE, stroke_width=stroke_width_paths
            )
            dotpaths.append(dotPath)
            self.add(dotPath)

        first_moves = []
        for x in range(11):
            first_moves.append(
                dotlist[x].animate.move_to(
                    b / 2 * DOWN + ((-10 + 2 * x) / 10.0 * RIGHT * a / 2)
                )
            )
        self.play(AnimationGroup(*first_moves, lag_ratio=0.1))
        second_moves = []
        for dot in dotlist:
            second_moves.append(
                dot.animate.move_to(a / 2 * RIGHT + b / 2 * DOWN + c * OUT)
            )
        self.play(AnimationGroup(*second_moves, lag_ratio=0.1))
        self.wait(1)
        self.play(FadeOut(*dotpaths, lag_ratio=0.1))

        self.stop_ambient_camera_rotation()

        self.move_camera(PI / 4, -PI / 4)
        self.move_camera(zoom=1.5)

        up_right = base.get_corner(UP + RIGHT)
        up_left = base.get_corner(UP + LEFT)
        # up_left_top = top.get_corner(UP + LEFT)
        down_left = base.get_corner(DOWN + LEFT)
        down_left_dummy = (-a / 2, (b / 2) - c, 0)

        t1 = Tex("Let's label the sides")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        brace_a = BraceBetweenPoints(up_left, up_right, direction=UP)
        a_text = brace_a.get_tex("a")
        self.play(FadeIn(a_text, brace_a))

        brace_b = BraceBetweenPoints(up_left, down_left, direction=LEFT)
        b_text = brace_b.get_tex("b")
        self.play(FadeIn(b_text, brace_b))

        brace_c = BraceBetweenPoints(up_left, down_left_dummy, direction=LEFT)
        brace_c.rotate(PI / -2, about_point=up_left, axis=RIGHT)
        c_text = brace_c.get_tex("c")
        c_text.rotate(PI / 2, about_point=(-a / 2, b / 2, c / 2), axis=RIGHT)
        self.play(FadeIn(c_text, brace_c))
        self.play(Unwrite(t1))
        t1 = Tex("Now let's again unfold it")
        self.add_fixed_in_frame_mobjects(t1)
        t1.to_corner(UL)
        self.play(Write(t1))
        self.play(Unwrite(t1))
        # self.play(FadeOut(brace_a, a_text, brace_b, b_text, brace_c, c_text))
        # self.begin_ambient_camera_rotation(0.2)

        rotations = [
            Rotate(left, angle=-90 * DEGREES, axis=UP, about_point=[-a / 2, 0, 0]),
            Rotate(right, angle=-90 * DEGREES, axis=DOWN, about_point=[a / 2, 0, 0]),
            Rotate(up, angle=-90 * DEGREES, axis=RIGHT, about_point=[0, b / 2, 0]),
            Rotate(down, angle=-90 * DEGREES, axis=LEFT, about_point=[0, -b / 2, 0]),
            Rotate(top, angle=-90 * DEGREES, axis=DOWN, about_point=[0, 0, -a / 2]),
        ]
        down_left_top = top.get_corner(DOWN + LEFT)
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))

        self.play(
            Rotate(top, angle=-90 * DEGREES, axis=UP, about_point=[c + (a / 2), 0, 0]),
        )
        # put this code AFTER rotations
        up_right_top = top.get_corner(UP + RIGHT)
        up_left_top = top.get_corner(UP + LEFT)
        down_left = base.get_corner(DOWN + LEFT)
        down_right = base.get_corner(DOWN + RIGHT)
        down_left_top = top.get_corner(DOWN + LEFT)
        start_dot = Dot(down_left, radius=dot_radius)
        end_dot = Dot(up_left_top, radius=dot_radius)

        brace_f = BraceBetweenPoints(down_right, down_left_top)
        f_text = brace_f.get_tex("c")
        self.play(
            Transform(brace_c, brace_f),
            Transform(c_text, f_text),
        )
        # down_left_dummy = (-a / 2, (b / 2) - c, 0)
        #
        # self.add(Dot(up_left_top, color=GREEN))
        # self.add(Dot(down_left, color=YELLOW))
        # self.add(Dot(down_right, color=PINK))
        # self.add(Dot(up_right_top))
        X = (b * a) / (c + a)

        pass_point = (((-a / 2) + c), X - (b / 2), 0)
        self.play(FadeIn(start_dot, end_dot))
        self.add(Dot(pass_point, color=BLUE, radius=dot_radius))
        dotPath = TracedPath(start_dot.get_center, stroke_color=RED)
        self.add(dotPath)
        self.play(start_dot.animate.move_to(end_dot))
        self.play(FadeOut(axes, axes_label))
        write_unwrite_three_d(
            self, "Notice how again the shortest path is a staight line"
        )
        write_unwrite_three_d(
            self,
            "Let's mark the distance of the point on the bottom edge \\\\ where the dot crosses it from the bottom right \\\\ corner as l",
            wait=2,
        )

        brace_g = BraceBetweenPoints(down_right, pass_point)
        g_text = brace_g.get_tex(("l"))
        self.play(FadeIn(brace_g, g_text))
        write_unwrite_three_d(self, "Now how do we find this l?")

        rotations = [
            Rotate(left, angle=90 * DEGREES, axis=UP, about_point=[-a / 2, 0, 0]),
            Rotate(right, angle=90 * DEGREES, axis=DOWN, about_point=[a / 2, 0, 0]),
            Rotate(up, angle=90 * DEGREES, axis=RIGHT, about_point=[0, b / 2, 0]),
            Rotate(down, angle=90 * DEGREES, axis=LEFT, about_point=[0, -b / 2, 0]),
        ]
        down_left_top = top.get_corner(DOWN + LEFT)
        self.play(
            FadeOut(
                a_text,
                b_text,
                g_text,
                brace_a,
                brace_b,
                brace_g,
                f_text,
                brace_f,
                c_text,
                brace_c,
                dotPath,
            )
        )
        self.play(AnimationGroup(*rotations, lag_ratio=0.1))

        self.play(
            Rotate(top, angle=90 * DEGREES, axis=DOWN, about_point=[0, 0, -a / 2]),
        )
        self.play(Rotate(top, angle=90 * DEGREES, axis=UP, about_point=[-a / 2, 0, c]))
        write_unwrite_three_d(self, "Here we will find it out using differntiation")
        dot_radius = 0.05

        pass_point = ((a / 2), X - (b / 2), 0)
        pass_point_dot = Dot(pass_point, radius=dot_radius)
        self.add(pass_point_dot)

        start_dot = Dot(down_left, radius=dot_radius)
        self.add(start_dot)
        end_dot = Dot(top.get_corner(UP + RIGHT))
        self.add(end_dot)

        write_unwrite_three_d(self, "Now watch carefully how the ant moves")
        dotPath1 = TracedPath(start_dot.get_center, stroke_color=RED)
        self.add(dotPath1)
        self.play(start_dot.animate.move_to(pass_point))
        self.play(FadeOut(start_dot))

        write_unwrite_three_d(self, "Let's call this length $l_1$")
        self.play(Indicate(dotPath1))

        tex1 = MathTex("l_1 = ?")
        self.add_fixed_in_frame_mobjects(tex1)
        tex1.to_edge(RIGHT)
        self.play(FadeIn(tex1))
        dotPath2 = TracedPath(pass_point_dot.get_center, stroke_color=YELLOW)
        self.add(dotPath2)
        self.play(pass_point_dot.animate.move_to(end_dot))

        write_unwrite_three_d(self, "And this length $l_2$")

        tex3 = MathTex("l_2 = ?")
        self.add_fixed_in_frame_mobjects(tex3)
        tex3.next_to(tex1, direction=DOWN)
        self.play(FadeIn(tex3))
        self.play(Indicate(dotPath2))
        write_unwrite_three_d(self, "We have to minimise $l_1+l_2$")

        write_unwrite_three_d(
            self, "Let's find out $l_1$ and $l_2$ in terms of the sides and l"
        )
        self.play(
            tex1.animate.shift(DOWN * 2 + LEFT * 2),
            tex3.animate.shift(DOWN * 2 + LEFT * 2),
        )
        a_line = Line(down_right, down_left)
        a_line.set_stroke(color=PINK, width=2)
        x_line = Line(down_right, pass_point)
        x_line.set_stroke(color=PINK, width=2)
        l1_line = Line(down_left, pass_point)
        l1_line.set_stroke(color=BLUE, width=2)
        self.play(FadeIn(a_line, x_line, l1_line))

        aline_copy = a_line.copy()
        xline_copy = x_line.copy()
        l1line_copy = l1_line.copy()

        br1 = Tex("a")
        br1.scale(0.5)
        br2 = Tex("x")
        br2.scale(0.5)
        br3 = MathTex("l_1")
        br3.scale(0.5)

        tr1 = VGroup(
            aline_copy,
            xline_copy,
            l1line_copy,
            br1,
            br2,
            br3,
        )
        self.add_fixed_in_frame_mobjects(tr1)
        aline_copy.to_corner(UR)
        aline_copy.shift(X * DOWN)
        xline_copy.to_corner(UR)
        l1line_copy.to_corner(UR)
        br1.next_to(aline_copy, direction=DOWN)
        br2.next_to(xline_copy)
        br3.next_to(l1line_copy, direction=UP)

        # self.play(FadeIn(tr1))

        tr1.shift(LEFT * 2 + DOWN * 2)
        self.play(tr1.animate.scale(1.5))

        write_unwrite_three_d(self, "Now $l_1$ comes out to this")

        tex2 = MathTex("l_1 = \\sqrt{a^2+c^2}")
        self.add_fixed_in_frame_mobjects(tex2)
        tex2.to_edge(RIGHT)
        tex2.shift(2 * DOWN + 2 * LEFT)
        self.play(FadeOut(tex1), FadeIn(tex2))
        self.play(FadeOut(tr1, a_line, x_line, l1_line))

        pass_point_top = ((a / 2), X - (b / 2), c)
        up_right_top = top.get_corner(UP + RIGHT)
        a_line = Line(pass_point, pass_point_top)
        a_line.set_stroke(color=PINK, width=2)
        x_line = Line(pass_point_top, up_right_top)
        x_line.set_stroke(color=PINK, width=2)
        l1_line = Line(pass_point, up_right_top)
        l1_line.set_stroke(color=BLUE, width=2)
        self.play(FadeIn(a_line, x_line, l1_line))
        write_unwrite_three_d(self, "Similarly $l_2$ comes out to this")

        tex4 = MathTex("l_2 = \\sqrt{c^2+(b-x)^2}")
        self.add_fixed_in_frame_mobjects(tex4)
        tex4.to_edge(RIGHT)
        tex4.next_to(tex2, direction=DOWN)
        self.play(FadeOut(tex3), FadeIn(tex4))
        self.play(
            FadeOut(
                a_line,
                x_line,
                l1_line,
                tex4,
                tex2,
                top,
                base,
                right,
                left,
                up,
                down,
                end_dot,
                pass_point_dot,
                dotPath2,
            )
        )
        self.move_camera(0, -PI / 2, zoom=1.0)
        t1 = MathTex("l")
        t2 = MathTex("= l_1+l_2")
        t2.next_to(t1)
        t3 = MathTex("= \\sqrt{a^2+x^2} + \\sqrt{c^2+(b-x)^2} ")
        t3.next_to(t2, direction=DOWN)
        t3.shift(RIGHT * 2)
        self.play(Write(t1), Write(t2), (Write(t3)))
        self.play(FadeOut(t2), t1.animate.shift(2.5 * LEFT), t3.animate.move_to(t2))
        self.play(VGroup(t1, t3).animate.shift(2 * DOWN))
        write_unwrite(self, "Now let's differentiate l\\\\ with respect to x")
        t4 = MathTex("\\frac{dl}{dx}")
        t5 = MathTex("=\\frac{d}{dx}(\\sqrt{a^2+x^2} + \\sqrt{c^2+(b-x)^2})")
        self.play(Transform(t1, t4))
        self.play(t1.animate.shift(4 * LEFT))

        self.play(Transform(t3, t5), t1.animate.shift(LEFT))
        t6 = MathTex(
            "= \\frac{d}{dx}(\\sqrt{a^2+x^2})+\\frac{d}{dx}(\\sqrt{c^2+(b-x)^2})"
        )
        self.play(Transform(t3, t6))
        t7 = MathTex(
            "=\\frac{2x}{2\\sqrt{a^2+x^2}} - \\frac{2(b-x)}{2\\sqrt{c^2+(b-x)^2}}"
        )

        self.play(Transform(t3, t7), t1.animate.shift(RIGHT))
        self.play(VGroup(t3, t1).animate.shift(DOWN))
        write_unwrite(self, "Now we set the derivative to zero")

        self.play(VGroup(t3, t1).animate.shift(UP))
        self.play(FadeOut(t1), t3.animate.shift(LEFT))
        self.play(
            Transform(
                t3,
                MathTex(
                    "\\frac{2x}{2\\sqrt{a^2+x^2}} - \\frac{2(b-x)}{2\\sqrt{c^2+(b-x)^2}}=0"
                ),
            )
        )
        waittime = 0.5
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex(
                    "\\frac{2x}{2\\sqrt{a^2+x^2}} = \\frac{2(b-x)}{2\\sqrt{c^2+(b-x)^2}}"
                ),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x\\sqrt{(c^2+(b-x)^2)} = (b-x)\\sqrt{(a^2+x^2)}"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x^2(c^2+(b-x)^2) = (b-x)^2(a^2+x^2)"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex(
                    "x^2c^2+x^2b^2+x^4-2bx^3=b^2a^2+x^2b^2+x^2a^2+x^4-2a^2bx-2bx^3",
                ),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x^2c^2 -x^2a^2 +2a^2bx -b^2a^2 = 0"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x^2c^2 -a^2(x^2 -2bx +b^2 ) = 0"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x^2c^2 - = a^2(x^2 -2bx +b^2 )"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x^2c^2  = a^2(x - b)^2"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("xc  = \\pm a(x - b)"),
            )
        )
        self.wait(waittime)
        t1 = Tex("Think about why we used the root with the negative sign")
        t1.to_corner(UL)

        self.play(
            Transform(
                t3,
                MathTex("xc  = -a(x-b)"),
            ),
            Write(t1),
        )
        self.play(Unwrite(t1))
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("xc  = -ax  +ab"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x(c+a)  = ab"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x  = \\frac{ab}{a+c}"),
            )
        )
        t1 = Tex("Let's see if this works for a cube.\\\\")
        t1.to_corner(UL)
        self.play(Write(t1))
        self.play(
            Transform(
                t3,
                MathTex("x  = \\frac{a.a}{a+a}"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x  = \\frac{a^2}{2a}"),
            )
        )
        self.wait(waittime)
        self.play(
            Transform(
                t3,
                MathTex("x  = \\frac{a}{2}"),
            )
        )
        self.play(Unwrite(t1))

        self.play(FadeOut(t3))
        write_unwrite(self, "Hmmm, so far so good")
        write_unwrite(self, "Let's verify this geometrically for a cuboid")
        self.wait(5)
