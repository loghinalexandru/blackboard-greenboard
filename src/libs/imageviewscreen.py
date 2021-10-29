import kivy
kivy.require('2.0.0')

from functools import partial
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
from kivymd.uix.behaviors import TouchBehavior
from kivy.uix.scatterlayout import ScatterLayout

class CustomScatterLayout(TouchBehavior, ScatterLayout):
    def on_double_tap(self, *args):
        trans = Matrix().scale(1, 1, 1)
        self.transform = trans

class ImageViewScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(self.ids.image_container.on_double_tap)

    def on_delete(self):
        self.manager.get_screen('gallery').delete_photo(self.file_name)
        self.manager.current = 'gallery'

    def reset_scatter(self, _):
        trans = Matrix().scale(1, 1, 1)
        self.ids.image_container.transform = trans