from manim import (
    BLUE,
    GREEN,
    Circle,
    DrawBorderThenFill,
    FadeOut,
    Indicate,
    ReplacementTransform,
    Scene,
    Square,
)


class Test(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.play(FadeOut(blue_circle))
