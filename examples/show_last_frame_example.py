import manim as m
from manim_main_function.mmf import ManinMainFunction


class ShowLastFrameExample(ManinMainFunction, m.Scene):

    def construct(self):
        my_text = m.Text("Hello World", color=m.BLUE)

        self.add(my_text)


if __name__ == '__main__':
    # You can now render Manim Scenes using the main function instead of the command line!
    ShowLastFrameExample.show_last_frame()
