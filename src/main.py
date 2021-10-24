import kivy
import os
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

class ImageButton(ButtonBehavior, Image):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class BlackBoardGreenBoardApp(App):
    kv_directory = 'modules'

    def build(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        files = os.listdir(app_folder)
        for file in files:
            if(file.endswith("jpg")):
                self.root.ids.gallery_content.add_widget(ImageButton(source=file, allow_stretch=True, keep_ratio=False))

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()