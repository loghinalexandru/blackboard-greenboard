import kivy
kivy.require('2.0.0')

from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
from constants import Screen

class ImageViewScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(self.ids.image_container.on_double_tap)

    def on_delete(self):
        self.manager.get_screen(Screen.Gallery.value).delete_photo(self.file_name)
        self.manager.current = Screen.Gallery.value

    def reset_scatter(self, _):
        trans = Matrix().scale(1, 1, 1)
        self.ids.image_container.transform = trans