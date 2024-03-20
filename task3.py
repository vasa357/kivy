from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import Boxlayout
class MyApp(App):
    def build(self):
        txt = Label(text = 'This is Text!!!')
        btn = Button(text = 'This is Button!!!')
        layout = Boxlayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run()
