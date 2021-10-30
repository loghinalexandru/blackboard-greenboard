import os
import kivy
kivy.require('2.0.0')

from enum import Enum
from kivy.utils import platform

def __get_primary_storage():
    if(IS_ANDROID):
        from android.storage import primary_external_storage_path
        return primary_external_storage_path()
    else:
        return '/'

ROOT_DIR = os.path.abspath((os.path.dirname(__file__)))
IS_ANDROID = kivy.utils.platform == 'android'
PRIMARY_STORAGE_PATH = __get_primary_storage()
class Screen(Enum):
    Gallery = 'gallery'
    Capture = 'capture'
    ImageView = 'imageview'



