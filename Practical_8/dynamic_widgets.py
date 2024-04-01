from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_and_phone = {"Jessica Patel": "8642097531", "Benjamin Lee": "2156873094", "Samantha Rodriguez": "7490321865", "Emily Johnson": "5309642178", "Elena Cruz": "5734562349"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_and_phone:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            temp_button.background_color = (1, 0, 0, 1)
            self.root.ids.entries.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.text
        instance.background_color = (0, 0, 1, 1)
        self.status = f"{name}'s number is {self.name_and_phone[name]}"

    def clear(self):
        self.root.ids.entries.clear_widgets()


DynamicWidgetsApp().run()
