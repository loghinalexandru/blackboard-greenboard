import kivy
kivy.require('2.0.0')

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from constants import Screen

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(CustomScreenManager, self).__init__(**kwargs)
        Clock.schedule_once(lambda _: Window.bind(on_keyboard=self.hook_keyboard))

    def get_previous_screen(self):
        if(self.current == Screen.Gallery.value):
            return ('gallery', False)
        return ('gallery', True)

    def hook_keyboard(self, _, key, *args):
        if key == 27:
            self.current, done = self.get_previous_screen()
            return done

class BlackBoardGreenBoardApp(MDApp):
    kv_directory = 'modules'

if __name__ == '__main__':
    BlackBoardGreenBoardApp().run()