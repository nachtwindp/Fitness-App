from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivymd.app import MDApp
from kivy.clock import Clock

Window.size = (300, 500)
list_food = []
list_calories = []
list_pushups = []


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
        sm.add_widget(Builder.load_file("timer.kv"))
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

    def update_error_text(self):
        self.root.get_screen("login").ids.error.text = "Please fill everything"

    def display_food(self, foods, calories):
        total_calories = 0
        list_food.append(foods)
        list_calories.append(calories)
        food_string = ", ".join(list_food)
        for i in range(len(list_calories)):
            total_calories += int(list_calories[i])

        self.root.get_screen("date").ids.date_food.text = f"Food:{food_string}\n"
        self.root.get_screen("date").ids.date_calories.text = f"Total calories for the day:{str(total_calories)}"

    def display_push_up(self, pushups):
        total_pushups = 0
        list_pushups.append(pushups)
        for i in range(len(list_pushups)):
            total_pushups += int(list_pushups[i])
        self.root.get_screen("date").ids.push_up.text = f"Total push ups:{total_pushups}"

    def start_timer(self, duration):
        self.root.get_screen("timer").ids.timer_label.text = str(duration)
        Clock.schedule_interval(lambda dt: self.update_timer(dt, duration), 1)

    def update_timer(self, dt, duration):
        current_time = int(self.root.get_screen("timer").ids.timer_label.text)
        if current_time > 0:
            current_time -= 1
            self.root.get_screen("timer").ids.timer_label.text = str(current_time)
        else:
            self.root.get_screen("timer").ids.timer_label.text = str(duration)
            Clock.unschedule(self.update_timer)


if __name__ == "__main__":
    SweatWell().run()
