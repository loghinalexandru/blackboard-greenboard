import kivy
kivy.require('2.0.0')

import os
from kivymd.uix.screen import MDScreen
from kivymd.uix.imagelist import SmartTile
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from functools import partial
from constants import ROOT_DIR

class CustomSmartTile(SmartTile):
    def __init__(self, **kwargs):
        super(CustomSmartTile, self).__init__(**kwargs)
        self.height = '240dp'
        self.size_hint_y = None
        self.box_color = [0, 0, 0, 0]
        self.on_press = partial(self.maximize, self.source)

    def maximize(self, file):
        self.parent.parent.parent.manager.get_screen('imageview').file_name = file
        self.parent.parent.parent.manager.current = 'imageview'

class GalleryScreen(MDScreen):
    data = {
        'Take a picture': 'camera',
        'Add a file': 'file-multiple'
    }

    photo_widgets = {}

    def __init__(self, **kwargs):
        super(GalleryScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.load_photos)

    def load_photos(self, _):
        self.ids.gallery_content.clear_widgets()
        files = os.listdir(ROOT_DIR)
        for file in files:
            self.core_load(file)

    def delete_photo(self, filename):
        self.core_delete(filename)

    def add_photo(self, filename, _):
        self.core_load(filename)

    def custom_transition(self, _):
        if(_.icon == 'camera'):
            self.manager.current = 'capture'
        else:
            self.file_manager = MDFileManager(select_path=self.select_path)
            self.file_manager.show('/') 
        self.ids.dial.close_stack()

    def select_path(self, path):
        print(path)

    def core_load(self, file_path):
        if(file_path.endswith("jpg") ):
            self.photo_widgets[file_path] = CustomSmartTile(source=file_path)
            self.ids.gallery_content.add_widget(self.photo_widgets[file_path])

    def core_delete(self, file_path):
        if(file_path.endswith("jpg") ):
            self.ids.gallery_content.remove_widget(self.photo_widgets[file_path])
            os.remove(file_path)



          