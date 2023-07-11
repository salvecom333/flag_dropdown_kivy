from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class CenterOption(SpinnerOption):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(40)

        self.layout = BoxLayout(padding=5, spacing=10)
        self.add_widget(self.layout)

        self.flag_image = Image(source=f"flag_icons/{self.text.lower()}.ico", size_hint=(None, None),
                                size=(dp(40), dp(40)))
        self.layout.add_widget(self.flag_image)

        self.bind(size=self.update_layout)

    def update_layout(self, *args):
        self.flag_image.pos = self.pos

class FlagSpinner(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.pos_hint = {"center_x": 0.5}
        self.option_cls = "CenterOption"

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10)
        flag_spinner = FlagSpinner(pos_hint={"center_x": 0.5, "center_y": 0.5})
        flag_spinner.values = ["English", "Spanish"]
        layout.add_widget(flag_spinner)
        return layout

if __name__ == "__main__":
    MyApp().run()
