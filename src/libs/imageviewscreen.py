import kivy
kivy.require('2.0.0')

from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.graphics.transformation import Matrix
from constants import Screen, IS_ANDROID

class ImageViewScreen(MDScreen):
    def on_pre_enter(self):
        Clock.schedule_once(self.ids.image_container.on_double_tap)

    def on_delete(self):
        self.manager.get_screen(Screen.Gallery.value).delete_photo(self.file_name)
        self.manager.current = Screen.Gallery.value

    def on_back(self):
        self.manager.current = Screen.Gallery.value

    def on_share(self):
        if IS_ANDROID:
            from jnius import autoclass
            
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')
            intent = Intent()
            intent.setAction(Intent.ACTION_SEND)
            intent.putExtra(Intent.EXTRA_TEXT, String('{}'.format('test')))
            intent.setType('text/plain')
            chooser = Intent.createChooser(intent, String('test'))
            PythonActivity.mActivity.startActivity(chooser)

    def reset_scatter(self, _):
        trans = Matrix().scale(1, 1, 1)
        self.ids.image_container.transform = trans