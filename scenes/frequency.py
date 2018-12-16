from big_ol_pile_of_manim_imports import *

class Frequency(GraphScene):
    CONFIG = {
        "x_min" : -4 * np.pi,
        "x_max" : 4 * np.pi,
        "y_min" : -2,
        "y_max" : 2,
        "x_axis_label": None,
        "y_axis_label": None,
        "graph_origin" : ORIGIN ,
        "function_color" : WHITE ,
        "axes_color" : BLUE
    }

    def construct(self):
        self.graph()

    def title(self):
        title = TextMobject("Sound travels in waves.", tex_to_color_map={"waves.": RED})
        title.scale(2)

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

    def graph(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_title = TextMobject("440Hz", tex_to_color_map={"440Hz": RED})
        graph_title.to_edge(UP)
        self.play(Write(graph_title))

        self.play(ShowCreation(func_graph))
        self.wait(3)

        graph_title_2 = TextMobject("880Hz", tex_to_color_map={"880Hz": RED})
        graph_title_2.to_edge(UP)
        func_graph_2=self.get_graph(self.func_to_graph2, self.function_color)

        self.play(Transform(graph_title, graph_title_2), Transform(func_graph, func_graph_2))
        self.wait(3)
        self.play(FadeOut(func_graph), FadeOut(self.x_axis), FadeOut(self.y_axis))
        self.wait()

        new = graph_title_2
        new.scale(3)
        new.center()

        self.play(Transform(graph_title, new))
        self.wait(3)
        self.play(Transform(graph_title, TextMobject("Hz", tex_to_color_map={"Hz": RED}).scale(3).center()))
        self.wait(3)
        self.play(Transform(graph_title, TextMobject("Hertz", tex_to_color_map={"Hertz": RED}).scale(3).center()))
        self.wait(3)
        
        FadeOut(graph_title)

    def func_to_graph(self,x):
        return np.sin(x)

    def func_to_graph2(self, x):
        return np.sin(2 * x)
