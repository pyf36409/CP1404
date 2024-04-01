from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesConvertApp(App):
    def build(self):
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert(self, value):
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def up(self, value):
        try:
            result = int(value) + 1
            self.root.ids.input_number.text = str(result)
        except ValueError:
            pass

    def down(self, value):
        try:
            result = int(value) - 1
            self.root.ids.input_number.text = str(result)
        except ValueError:
            pass


MilesConvertApp().run()
