from big_ol_pile_of_manim_imports import *


class Definition(Scene):
    def construct(self):
        text = TextMobject("""
        Travelling vibrations that can be heard when \\\\
        they reach a person or an animal's ear.
        """, tex_to_color_map={"vibrations": RED, "heard": GREEN})
        # text = TextMobject(" .", )
        text.scale(2)
        text.set_width(FRAME_WIDTH - 1)
        self.play(FadeIn(text, submobject_mode = "lagged_start", rate_func = None, lag_factor = 4, run_time = 5))
        self.wait(3)