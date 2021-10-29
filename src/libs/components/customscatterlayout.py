import kivy
kivy.require('2.0.0')

from kivymd.uix.behaviors import TouchBehavior
from kivy.graphics.transformation import Matrix
from kivy.uix.scatterlayout import ScatterLayout

class CustomScatterLayout(TouchBehavior, ScatterLayout):
    def on_double_tap(self, *args):
        trans = Matrix().scale(1, 1, 1)
        self.transform = trans
