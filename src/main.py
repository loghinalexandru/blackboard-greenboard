import kivy
import glob
import os
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class ImageButton(ButtonBehavior, Image):
    pass

class BlackBoardGreenBoardApp(App):
    kv_directory = 'modules'

    def build(self):
        app_folder = os.path.dirname(os.path.abspath(__file__))
        files = os.listdir(app_folder)
        for file in files:
            print(file)
            if(file.endswith("jpg")):
                self.root.ids.gallery_content.add_widget(ImageButton(source=file))

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()