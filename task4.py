from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import Boxlayout

class MyApp(App):
    def build(self):
        self.i =0
        self.txt = Label(text = "This is TETX")
        btn = Button(text = "This is BUTTON!!!")
        btn.on_press = self.change_text
        layout= Boxlayout()
        layout.add_widget(self.txt)
        layout.add_widget(btn)
        return layout
    
    def change_txt(self):
        self.txt.text = str(self.i)
        self.i += 1

MyApp().run()