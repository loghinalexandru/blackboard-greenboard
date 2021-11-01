import kivy
kivy.require('2.0.0')

from functools import partial
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from engine.main import process_image_with_rotation
from constants import Screen

class CaptureScreen(MDScreen):
    def __init__(self, **kwargs):
        super(CaptureScreen, self).__init__(**kwargs)
        self.camera_resolution = Window.size

    def on_picture_taken(self):
        return True
        # Clock.schedule_once(partial(process_image_with_rotation, filename))
        # Clock.schedule_once(partial(self.manager.get_screen(Screen.Gallery.value).add_photo, filename))