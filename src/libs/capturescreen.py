import kivy
kivy.require('2.0.0')

from functools import partial
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from engine.main import process_image_with_rotation
from constants import Screen

class CaptureScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(lambda _: self.ids.camera.force_landscape())

    def on_leave(self):
        Clock.schedule_once(lambda _: self.ids.camera.restore_orientation())

    def picture_taken(self, _, filename):
        Clock.schedule_once(partial(process_image_with_rotation, filename))
        Clock.schedule_once(partial(self.manager.get_screen(Screen.Gallery.value).add_photo, filename))