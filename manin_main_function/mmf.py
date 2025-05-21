import manim as m

import os
import inspect
from pathlib import Path
from manin_main_function.logger import log


class ManinMainFunctions(m.Scene):

    @classmethod
    def get_file_path(cls) -> Path:
        return Path(inspect.getfile(cls)).resolve()

    @classmethod
    def render_video_low(cls):
        flags = "-pql"
        scene = cls.__name__
        file_path = cls.get_file_path()

        terminal_cmd = f"manim {file_path} {scene} {flags}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")

    @classmethod
    def render_video_medium(cls):
        flags = "-pqm"
        scene = cls.__name__
        file_path = cls.get_file_path()

        terminal_cmd = f"manim {file_path} {scene} {flags}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")

    @classmethod
    def render_video_high(cls):
        flags = "-pqh"
        scene = cls.__name__
        file_path = cls.get_file_path()

        terminal_cmd = f"manim {file_path} {scene} {flags}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")

    @classmethod
    def render_video_4k(cls):
        flags = "-pqk"
        scene = cls.__name__
        file_path = cls.get_file_path()

        terminal_cmd = f"manim {file_path} {scene} {flags}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")

    @classmethod
    def render_video_4k_without_cache(cls):
        flags = "-pqk --disable_caching"
        scene = cls.__name__
        file_path = cls.get_file_path()

        terminal_cmd = f"manim {file_path} {scene} {flags}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")

    @classmethod
    def show_last_frame(cls):
        file_path = cls.get_file_path()
        scene = cls.__name__
        terminal_cmd = f"manim -pqm -s {file_path} {scene}"
        log.info(f"running command: \n\n\t{terminal_cmd}\n")
        os.system(f"{terminal_cmd}")







