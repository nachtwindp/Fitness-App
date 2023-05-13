from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.pickers import MDDatePicker
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
        sm.add_widget(Builder.load_file("date.kv"))
        sm.add_widget(Builder.load_file("food.kv"))
        sm.add_widget(Builder.load_file("stats.kv"))
        return sm

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(*args):
        sm.current = "start"

    def on_save(self, instance, value, date_range):
        self.root.get_screen('date').ids.date.text = str(value)

    def on_cancel(self, instance, value):
        self.root.get_screen('date').ids.date.text = "You clicked cancel"

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


if __name__ == "__main__":
    SweatWell().run()
