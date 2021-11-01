import kivy
import os
import datetime

kivy.require('2.0.0')

from kivymd.uix.screen import MDScreen
from functools import partial
from kivymd.uix.filemanager import MDFileManager
from kivy.clock import Clock
from constants import ROOT_DIR, Screen, PRIMARY_STORAGE_PATH
from engine.main import process_image
from libs.components.customsmarttile import CustomSmartTile

class GalleryScreen(MDScreen):
    def __init__(self, **kwargs):
        super(GalleryScreen, self).__init__(**kwargs)
        self.file_manager = MDFileManager(preview=True, select_path=self._select_path, ext=['.jpg','.png','.jpeg','.gif'])
        self.data = {'Take a picture': 'camera','Add a file': 'file-multiple'}
        self.photo_widgets = {}
        Clock.schedule_once(self.load_photos)

    def load_photos(self, _):
        self.ids.gallery_content.clear_widgets()
        files = os.listdir(ROOT_DIR)
        for file in files:
            self._core_load(file)

    def delete_photo(self, filename):
        self._core_delete(filename)

    def add_photo(self, filename, _):
        self._core_load(filename)

    def custom_transition(self, _):
        if(_.icon == 'camera'):
            self.manager.current = Screen.Capture.value
        else:
            self.file_manager.show(PRIMARY_STORAGE_PATH)
        self.ids.dial.close_stack()

    def _camera_callback(self, **kwargs):
        return False

    def on_success_shot(self, loaded_image_path):
        return True

    def _select_path(self, selection):
        Clock.schedule_once(partial(process_image, path, os.path.join(ROOT_DIR, self._get_filename())))
        Clock.schedule_once(partial(self.manager.get_screen(Screen.Gallery.value).add_photo, self._get_filename()))
        self.file_manager.close()

    def _core_load(self, file_path):
        if(file_path.endswith("jpg") ):
            self.photo_widgets[file_path] = CustomSmartTile(source=file_path)
            self.ids.gallery_content.add_widget(self.photo_widgets[file_path])

    def _core_delete(self, file_path):
        if(file_path.endswith("jpg") ):
            self.ids.gallery_content.remove_widget(self.photo_widgets[file_path])
            os.remove(file_path)

    def _get_filename(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H.%M.%S.jpg')