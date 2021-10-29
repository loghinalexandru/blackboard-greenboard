import os
from enum import Enum

ROOT_DIR = os.path.abspath((os.path.dirname(__file__)))
class Screen(Enum):
    Gallery = 'gallery'
    Capture = 'capture'
    ImageView = 'imageview'