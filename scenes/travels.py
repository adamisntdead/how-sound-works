from big_ol_pile_of_manim_imports import *
import numpy as np

class IntroToSound(Scene):
    CONFIG = {
        "A_frequency" : 2.1,
        "A_color" : BLUE
    }

    def construct(self):
        self.add_speaker()
        self.play_A440()
        self.wait(3)
        self.play(FadeOut(self.speaker))
        self.wait(1)

    def add_speaker(self):
        speaker = SVGMobject(file_name = "speaker")
        speaker.set_fill(opacity = 0.8)
        self.speaker = speaker

        self.play(FadeIn(speaker))
        self.wait(3)

    def play_A440(self):
        self.broadcast()
        self.wait(0.75)
        you_arrow = Arrow(np.array([3, -2, 0]), np.array([3, 0, 0]), color=RED)
        you = TextMobject("Gas Molecules")
        you.next_to(you_arrow, DOWN)
        self.play(
            FadeInAndShiftFromDirection(you, LEFT),
            GrowArrow(you_arrow),
        )
        self.broadcast()
        self.wait(0.75)
        self.broadcast()
        self.wait(0.75)
        self.broadcast()
        self.wait(0.75)
        self.play(FadeOut(you_arrow), FadeOut(you))


    def broadcast(self, *added_anims, **kwargs):
        self.play(self.get_broadcast_animation(**kwargs), *added_anims)

    def get_broadcast_animation(self, **kwargs):
        kwargs["run_time"] = kwargs.get("run_time", 5)
        kwargs["n_circles"] = kwargs.get("n_circles", 10)
        return Broadcast(self.speaker[1], **kwargs)
