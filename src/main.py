import kivy
import os
import time
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder

class ImageButton(ButtonBehavior, Image):
    pass

class CaptureScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))

class GalleryScreen(Screen):
    def build(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        files = os.listdir(app_folder)
        for file in files:
            if(file.endswith("jpg")):
                self.root.ids.gallery_content.add_widget(ImageButton(source=file, allow_stretch=True, keep_ratio=False))

class BlackBoardGreenBoardApp(App):
    kv_directory = 'modules'

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()