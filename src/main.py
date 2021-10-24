import kivy
import os
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.clock import Clock
from kivy.uix.popup import Popup

def get_permissions():
    if platform == "android":
        from android.permissions import request_permissions, Permission
        request_permissions([
            Permission.CAMERA,
            Permission.WRITE_EXTERNAL_STORAGE,
            Permission.READ_EXTERNAL_STORAGE
        ])

photos = os.path.abspath((os.path.dirname(__file__)))

class ImageButton(ButtonBehavior, Image):
    pass

class CaptureScreen(Screen):
    def __init__(self, **kwargs):
        super(CaptureScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start)

    def on_start(self, *args):
        self.ids.camera.force_landscape()

class GalleryScreen(Screen):
    def __init__(self, **kwargs):
        super(GalleryScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.on_start)

    def on_start(self, *args):
        for file in os.listdir(photos):
            try:
                if(file.endswith("jpg")):
                    self.ids.gallery_content.add_widget(ImageButton(source=file, allow_stretch=True, keep_ratio=True))
            except Exception as e:
                popup = Popup(title='Error', content=Label(text=str(e)))
                popup.open()

class BlackBoardGreenBoardApp(App):
    kv_directory = 'modules'
    def build(self):
        get_permissions()

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()