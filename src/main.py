import kivy
import cv2
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
from engine.main import get_note

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
    def on_pre_enter(self):
        Clock.schedule_once(self.force_landscape)

    def force_landscape(self, _):
        self.ids.camera.force_landscape()

    def picture_taken(self):
        self.process_image()
        self.remove_widget(self.ids.camera)
        self.ids.camera.restore_orientation()
        self.manager.current = 'gallery'

    def process_image(self):
        files = os.listdir(photos)
        for file in files:
            if(file.endswith("jpg") ):
                if("processed" not in file):
                    buffer = get_note(file)
                    file_name = file[:-3] + "_processed.jpg"
                    cv2.imwrite(file_name, buffer)

class GalleryScreen(Screen):
    def on_pre_enter(self):
        Clock.schedule_once(self.load_photos)

    def load_photos(self, _):
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
    def build(self):
        get_permissions()

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()