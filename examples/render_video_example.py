import manim as m
from manin_main_function.mmf import ManinMainFunctions


class ShowLastFrameExample(ManinMainFunctions, m.Scene):

    def construct(self):
        my_text = m.Text("Hello World", color=m.BLUE)

        self.play(
            m.FadeIn(my_text)
        )


if __name__ == '__main__':
    # You can now render Manim Scenes using the main function instead of the command line!
    ShowLastFrameExample.render_video_medium() # renders the video with the -pqm flags

    # Feel free to uncomment the following lines to render the video with different quality settings:
    #
    # ShowLastFrameExample.render_video_low() # renders the video with the -pql flags
    # ShowLastFrameExample.render_video_high() # renders the video with the -pqh flags
    # ShowLastFrameExample.render_video_4k() # renders the video with the -pqk flags
    # ShowLastFrameExample.render_video_4k_without_cache() # renders the video with the -pqk flags and without cache (--disable_caching flag)

