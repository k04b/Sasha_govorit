# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text='Привет, Саша! Kivy работает! 🐻')

TestApp().run()