from big_ol_pile_of_manim_imports import *

class Covered(Scene):
    def construct(self):
        topics = VGroup(
            TextMobject("What sound is"),
            TextMobject("The creation of sounds"),
            TextMobject("How sound travels"),
            TextMobject("The frequency of sounds")
        )

        for topic in topics:
            dot = Dot(color=BLUE)
            dot.next_to(topic, LEFT)
            topic.add(dot)
        topics.arrange_submobjects(
            DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF
        )
        self.add(topics)
        self.wait(3)
        for i in range(len(topics)):
            self.play(
                topics[i + 1:].set_fill, {"opacity": 0.25},
                topics[:i].set_fill, {"opacity": 0.25},
                topics[i].set_fill, {"opacity": 1},
            )
            self.wait(2)

        self.play(topics.set_fill, {"opacity": 1})
        self.wait(2)
