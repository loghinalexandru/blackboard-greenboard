import kivy
import os
from functools import partial

kivy.require('2.0.0')

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.graphics.transformation import Matrix
from kivymd.uix.imagelist import SmartTile
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from engine.main import process_image

photos = os.path.abspath((os.path.dirname(__file__)))

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(CustomScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(lambda _: Window.bind(on_keyboard=self.hook_keyboard))

    def get_previous_screen(self):
        if(self.current == 'capture'):
            return ('gallery', True)
        if(self.current == 'gallery'):
            return ('gallery', False)
        if(self.current == 'imageview'):
            return ('gallery', True)

    def hook_keyboard(self, _, key, *args):
        if key == 27:
            self.current, done = self.get_previous_screen()
            return done

class CustomSmartTile(SmartTile):
    def __init__(self, **kwargs):
        super(CustomSmartTile, self).__init__(**kwargs)
        self.ripple_scale = 0.85
        self.height = '240dp'
        self.size_hint_y = None
        self.box_color = [0, 0, 0, 0]
        self.on_press = partial(self.maximize, self.source)

    def maximize(self, file):
        self.parent.parent.parent.manager.get_screen('imageview').file_name = file
        self.parent.parent.parent.manager.current = 'imageview'

class ImageViewScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(self.reset_scatter)

    def delete_photo(self):
        os.remove(self.file_name)
        self.manager.current = 'gallery'

    def reset_scatter(self, _):
        trans = Matrix().scale(1, 1, 1)
        self.ids.image_container.transform = trans

class CaptureScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(lambda _: self.ids.camera.force_landscape())

    def on_leave(self):
        Clock.schedule_once(lambda _: self.ids.camera.restore_orientation())

    def picture_taken(self, _, filename):
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