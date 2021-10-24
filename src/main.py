import kivy
import os
from functools import partial

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.popup import Popup
from engine.main import process_image

photos = os.path.abspath((os.path.dirname(__file__)))

def enable_widget(self):
    self.ids.camera.opacity = 100
    self.ids.camera.disabled = False

def disable_widget(self):
    self.ids.camera.opacity = 0
    self.ids.camera.disabled = True

class ImageButton(ButtonBehavior, Image):
    pass

class CaptureScreen(Screen):
    def on_pre_enter(self):
        Clock.schedule_once(self.force_landscape)

    def force_landscape(self, _):
        self.ids.camera.force_landscape()

    def picture_taken(self, _, filename):
        self.ids.camera.restore_orientation()
        self.manager.current = 'gallery'
        Clock.schedule_once(partial(process_image, filename))

class GalleryScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.load_photos)

    def load_photos(self, _):
        self.ids.gallery_content.clear_widgets()
        files = os.listdir(photos)
        for file in files:
            try:
                if(file.endswith("jpg") ):
                    self.ids.gallery_content.add_widget(ImageButton(source=file, allow_stretch=True, keep_ratio=True))
            except Exception as e:
                popup = Popup(title='Error', content=Label(text=str(e)))
                popup.open()

class BlackBoardGreenBoardApp(App):
    kv_directory = 'modules'

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()