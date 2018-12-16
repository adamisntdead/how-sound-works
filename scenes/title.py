from big_ol_pile_of_manim_imports import *

class Title(Scene):
    def construct(self):
        title = TextMobject("How Does Sound Work?", tex_to_color_map={"Sound": BLUE})
        title.scale(2)
        self.play(Write(title), run_time = 3)
        self.wait(5)
        self.play(FadeOut(title))