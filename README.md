[![PyPI version](https://img.shields.io/pypi/v/manim-main-function)](https://pypi.org/project/manim-main-function/)
![License](https://img.shields.io/pypi/l/manim-main-function)


# About this Project

This project is a Python Module that let you use manim using a python API instead of the command line.
Pressing the green run button in your IDE will render the scene or show the last frame of the scene.

# Installation

Install the package with pip:
```
   pip install manim-main-function
```

# Usage

**Please make sure you have manim installed and running on your machine**

To use the module, you just need to let your scene inherit from the `ManinMainFunctions` class.
This class provides a set of functions that allow you to render the scene using the main function instead of the command line.

Below is are two examples of how to use the Module.

```python
import manim as m
# import ManinMainFunctions
from manim_main_function.mmf import ManinMainFunction


# Add 'ManinMainFunctions' to your scene class to enable the main function
class ShowLastFrameExample(ManinMainFunction, m.Scene):

    def construct(self):
        my_text = m.Text("Hello World", color=m.BLUE)

        self.add(my_text)


if __name__ == '__main__':
    # You can now render Manim Scenes using the main function instead of the command line!
    ShowLastFrameExample.show_last_frame()
```

```python
import manim as m
# import ManinMainFunctions
from manim_main_function.mmf import ManinMainFunction


# Add 'ManinMainFunctions' to your scene class to enable the main function
class ShowLastFrameExample(ManinMainFunction, m.Scene):

    def construct(self):
        my_text = m.Text("Hello World", color=m.BLUE)

        self.play(
            m.FadeIn(my_text)
        )


if __name__ == '__main__':
    # You can now render Manim Scenes using the main function instead of the command line!
    ShowLastFrameExample.render_video_medium()  # renders the video with the -pqm flags

    # Feel free to uncomment the following lines to render the video with different quality settings:
    # 
    # ShowLastFrameExample.render_video_low() # renders the video with the -pql flags
    # ShowLastFrameExample.render_video_high() # renders the video with the -pqh flags
    # ShowLastFrameExample.render_video_4k() # renders the video with the -pqk flags
    # ShowLastFrameExample.render_video_4k_without_cache() # renders the video with the -pqk flags and without cache (--disable_caching flag)


```
## Available Functions
- `render_video_low()`: Renders the video with the -pql flags
- `render_video_medium()`: Renders the video with the -pqm flags
- `render_video_high()`: Renders the video with the -pqh flags
- `render_video_4k()`: Renders the video with the -pqk flags
- `render_video_4k_without_cache()`: Renders the video with the -pqk flags and without cache (--disable_caching flag)
- `show_last_frame()`: Shows the last frame of the scene