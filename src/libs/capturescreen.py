import kivy
kivy.require('2.0.0')

from functools import partial
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from engine.main import process_image
from kivy.graphics.texture import Texture
from constants import Screen, get_filename
from kivy.uix.camera import Camera
import numpy as np
import cv2

class AndroidCamera(Camera):
    camera_resolution = (1920, 1080)

    def _camera_loaded(self, *largs):
        self.texture = Texture.create(size=np.flip(self.camera_resolution), colorfmt='rgb')
        self.texture_size = list(self.texture.size)

    def on_tex(self, *l):
        if self._camera._buffer is None:
            return None
        frame = self.frame_from_buf()
        self.frame_to_screen(frame)
        super(AndroidCamera, self).on_tex(*l)

    def frame_from_buf(self):
        w, h = self.resolution
        frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
        frame_bgr = cv2.cvtColor(frame, 93)
        return np.rot90(frame_bgr, 3)

    def frame_to_screen(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        flipped = np.flip(frame_rgb, 0)
        buf = flipped.tostring()
        self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

class CaptureScreen(MDScreen):
    def __init__(self, **kwargs):
        super(CaptureScreen, self).__init__(**kwargs)

    def on_picture_taken(self):
        filename = get_filename()
        self.ids.camera.texture.save(filename)
        Clock.schedule_once(partial(process_image, filename, filename))
        Clock.schedule_once(partial(self.manager.get_screen(Screen.Gallery.value).add_photo, filename))