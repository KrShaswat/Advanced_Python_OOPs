import webbrowser
import time

# import pyperclip as pyperclip

from fileSharer import FileSharer
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
from kivy.lang import Builder

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        """starts the cam feed in kivy"""
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """stops the cam feed and removes texture"""
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera.texture = None

    def capture(self):
        """captures a pic and changes screen to ImageScreen"""
        # not 'datetime' lib but 'time'
        time_string = time.strftime('%d%m%Y-%H%M%S')
        self.filepath = f'output/{time_string}.png'
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        # since we need to access another class
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    link_message = "Create a Link first"
    def create_link(self):
        """take the pic and upload it on the web and share link in label"""
        filepath = App.get_running_app().root.ids.camera_screen.filepath
        file_link = FileSharer(file_path=filepath)
        self.url = file_link.share()
        self.ids.link.text = str(self.url)

    def copy(self):
        """Copy link to the clipboard"""
        try:
            # pyperclip.copy(self.url)
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open(self):
        """Open the link in the browser"""
        try:
            # pyperclip.copy(self.url)
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
