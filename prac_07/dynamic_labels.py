"""
Prac_07 for CP1404
Tianhui Shi
May 6th, 2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

        self._name = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Michael Jackson"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_Labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        for name in self._name:

            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)

DynamicWidgetsApp().run()
