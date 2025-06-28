from manim import (
    PINK,
    Axes,
    Scene,
)


class Test(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x) * (x - 2) * (x + 2), color=PINK)
        area = ax.get_area(curve, x_range=(-2, 0))
        self.add(ax, curve, area)
