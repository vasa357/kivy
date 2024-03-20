from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import Boxlayout
from kivy.uix.screenmaneger import Screen, ScreenManeger

class FirstScreen(Screen):
    def __init__(self, name= ""):
        super().__init__(name = name)
        btn = Button(text = "First button!")
        btn.on_press = self.next 
        self.add_widget(btn)
    
    def next(self):
        self.manager.transition.direction = "up"
        self.manager.current = "second"

class SecondScreen(Screen):
    def __init__(self, name= ""):
        super().__init__(name = name)
        btn = Button(text = "Second button!")
        btn.on_press = self.next 
        self.add_widget(btn)
    
    def next(self) :
        self.manager.transition.direction = "left" 
        self.manager.current = "first"

class MyApp(App):
    def build(self):
        sm = ScreenManeger()
        sm.add_widget(FirstScreen())
        sm.add_widget(SecondScreen())
        return sm

MyApp().run()