from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        # write code in .kv file (the correct way)

        # Get user query from textInput
        query = self.manager.current_screen.ids.user_query.text
        # print(query)

        # Get the wikipedia page and image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # getting User-Agent
        headers = {'User-agent': 'Mozilla/5.0'}
        # this is a added trick because wikipedia will only answer to a browser, hence we pose as a browser

        # download the image
        req = requests.get(self.get_image_link(), headers=headers)
        # print(req)
        img_path = f'files/image.jpg'
        with open(img_path, 'wb') as file:
            file.write(req.content)
        return img_path

    def set_image(self):
        # Set the image in image widget
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
MainApp().run()
