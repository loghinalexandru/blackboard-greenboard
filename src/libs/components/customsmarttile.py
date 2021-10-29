import kivy
from functools import partial
kivy.require('2.0.0')
from kivymd.uix.imagelist import SmartTile
from constants import Screen

class CustomSmartTile(SmartTile):
    def __init__(self, **kwargs):
        super(CustomSmartTile, self).__init__(**kwargs)
        self.height = '240dp'
        self.size_hint_y = None
        self.box_color = [0, 0, 0, 0]
        self.on_press = partial(self.maximize, self.source)

    def maximize(self, file):
        self.parent.parent.parent.manager.get_screen(Screen.ImageView.value).file_name = file
        self.parent.parent.parent.manager.current = Screen.ImageView.value