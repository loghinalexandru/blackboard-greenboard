import kivy
import os
from functools import partial

kivy.require('2.0.0')

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image
from kivymd.uix.imagelist import SmartTile
from kivy.clock import Clock
from engine.main import process_image

photos = os.path.abspath((os.path.dirname(__file__)))

class CustomSmartTile(SmartTile):
    def __init__(self, **kwargs):
        super(CustomSmartTile, self).__init__(**kwargs)
        self.ripple_scale = 0.85
        self.height='400dp'
        self.size_hint_y=None
        self.box_color = [0, 0, 0, 0]
        self.on_press = partial(self.maximize, self.source)

    def maximize(self, file):
        self.parent.parent.parent.manager.get_screen('imageview').file_name = file
        self.parent.parent.parent.manager.current = 'imageview'

class ImageViewScreen(MDScreen):
    def __init__(self,**kwargs):
        super(ImageViewScreen,self).__init__(**kwargs)
        Window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            self.manager.current = 'gallery'
            return True

class CaptureScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(self.force_landscape)

    def force_landscape(self, _):
        self.ids.camera.force_landscape()

    def picture_taken(self, _, filename):
        self.manager.current = 'gallery'
        self.ids.camera.restore_orientation()
        Clock.schedule_once(partial(process_image, filename))

class GalleryScreen(MDScreen):
    data = {
        'Take a picture': 'camera',
        'Add a file': 'file-multiple'
    }

    def custom_transition(self, _):
        if(_.icon == 'camera'):
            self.manager.current = 'capture'
        self.ids.dial.close_stack()

    def on_enter(self):
        Clock.schedule_once(self.load_photos)

    def load_photos(self, _):
        self.ids.gallery_content.clear_widgets()
        files = os.listdir(photos)
        for file in files:
            if(file.endswith("jpg") ):
                self.ids.gallery_content.add_widget(CustomSmartTile(source=file))

class BlackBoardGreenBoardApp(MDApp):
    kv_directory = 'modules'

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()