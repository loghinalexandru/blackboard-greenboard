import kivy
import os

kivy.require('2.0.0')

from kivymd.uix.screen import MDScreen
from functools import partial
from kivymd.uix.filemanager import MDFileManager
from kivy.clock import Clock
from constants import ROOT_DIR, Screen, PRIMARY_STORAGE_PATH
from engine.main import process_image
from libs.components.customsmarttile import CustomSmartTile
from plyer import camera

class GalleryScreen(MDScreen):
    def __init__(self, **kwargs):
        super(GalleryScreen, self).__init__(**kwargs)
        self.file_manager = MDFileManager(select_path=self.select_path)
        self.data = {'Take a picture': 'camera','Add a file': 'file-multiple'}
        self.photo_widgets = {}
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
            camera.take_picture(filename='asd.jpg', on_complete=self.camera_callback)
        else:
            self.file_manager.show(PRIMARY_STORAGE_PATH)
        self.ids.dial.close_stack()

    def camera_callback(self, **kwargs):
        return False

    def select_path(self, path):
        Clock.schedule_once(partial(process_image, path, os.path.join(ROOT_DIR, os.path.split(path)[1])))
        Clock.schedule_once(partial(self.manager.get_screen(Screen.Gallery.value).add_photo, os.path.split(path)[1]))

    def core_load(self, file_path):
        if(file_path.endswith("jpg") ):
            self.photo_widgets[file_path] = CustomSmartTile(source=file_path)
            self.ids.gallery_content.add_widget(self.photo_widgets[file_path])

    def core_delete(self, file_path):
        if(file_path.endswith("jpg") ):
            self.ids.gallery_content.remove_widget(self.photo_widgets[file_path])
            os.remove(file_path)