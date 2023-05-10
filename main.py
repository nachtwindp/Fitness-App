from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.clock import Clock
Window.size = (300, 500)


class SweatWell(MDApp):
    def build(self):
        self.icon = "logo.png"
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("loading_screen.kv"))
        sm.add_widget(Builder.load_file("start.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("main_menu.kv"))
        sm.add_widget(Builder.load_file("workout.kv"))
        sm.add_widget(Builder.load_file("training.kv"))
        return sm

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(*args):
        sm.current = "start"

    def validate_fields(self):
        name = self.root.ids.name_field.text
        date = self.root.ids.date_field.text
        weight = self.root.ids.weight_field.text
        height = self.root.ids.height_field.text

        if not name or not date or not weight or not height:
            # if any field is empty, show an error message and return False
            self.root.ids.error_label.text = "Please fill in all fields."
            return False

        # perform other validation here
        # ...

        return True


if __name__ == "__main__":
    SweatWell().run()
