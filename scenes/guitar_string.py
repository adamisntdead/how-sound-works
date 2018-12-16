from big_ol_pile_of_manim_imports import *
import numpy as np


class String(Scene):

    def construct(self):
        title = TextMobject("A Guitar String")
        title.scale(2)
        title.to_edge(UP)

        rectangle = ScreenRectangle(height = 4)
        self.play(Write(title), run_time = 3)
        self.play(ShowCreation(rectangle))
        self.wait(6)
        self.play(FadeOut(rectangle))
        self.wait(3)

class Demo(GraphScene):
    CONFIG = {
        "x_min": -np.pi / 2,
        "x_max": np.pi / 2,
        "y_min": -10,
        "y_max": 10,
        "x_axis_label": "",
        "y_axis_label": "",
        "graph_origin": ORIGIN,
        "function": lambda x: np.cos(x),
        "function_opposite": lambda x: -np.cos(x),
        "function_color" : BLUE,
        "axes_color": BLACK,
    }

    def construct(self):
        title = TextMobject("A Guitar String")
        title.scale(2)
        title.to_edge(UP)
        self.add(title)

        self.setup_axes(animate=False)

        func_graph = self.get_graph(lambda x: 0, self.function_color)
        self.play(ShowCreation(func_graph))
        
        self.wait(4)

        for _ in range(15):
            self.play(Transform(func_graph, self.get_graph(self.function_opposite, self.function_color)), run_time=0.5)
            self.play(Transform(func_graph, self.get_graph(self.function, self.function_color)), run_time=0.5)
        
        self.play(Transform(func_graph, self.get_graph(lambda x: 0, self.function_color)))
        self.wait(2)
        self.play(FadeOut(func_graph), FadeOut(title))
        self.wait(1)