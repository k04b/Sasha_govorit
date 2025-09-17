# main.py — "Саша говорит" — модуль рисования + кнопка "Что это?"
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import json
import os
from datetime import datetime

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(0, 0, 0, 1)  # черный цвет
                touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)

    def on_touch_move(self, touch):
        if 'line' in touch.ud and self.collide_point(*touch.pos):
            touch.ud['line'].points += [touch.x, touch.y]

class AnalyticsLogger:
    def __init__(self, log_file="data/logs.json"):
        self.log_file = log_file
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                json.dump([], f)

    def log_event(self, event_type, data=None):
        with open(self.log_file, 'r+') as f:
            logs = json.load(f)
            log_entry = {
                "timestamp": datetime.now().isoformat(),
                "event": event_type,
                "data": data or {}
            }
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f, indent=2, ensure_ascii=False)

class SashaGovoritApp(App):
    def build(self):
        # Инициализируем логгер
        self.logger = AnalyticsLogger()

        # Главный вертикальный макет
        layout = BoxLayout(orientation='vertical')

        # Заголовок
        title_label = Label(text="САША ГОВОРИТ", font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(title_label)

        # Холст для рисования
        self.drawing_widget = DrawingWidget()
        layout.add_widget(self.drawing_widget)

        # Кнопка "Что это?"
        recognize_button = Button(text="ЧТО ЭТО?", font_size='20sp', size_hint=(1, 0.15))
        recognize_button.bind(on_press=self.recognize_drawing)
        layout.add_widget(recognize_button)

        # Лейбл для обратной связи
        self.feedback_label = Label(text="", font_size='20sp', size_hint=(1, 0.1))
        layout.add_widget(self.feedback_label)

        return layout

    def recognize_drawing(self, instance):
        # Пока просто имитация
        self.feedback_label.text = "Скоро научусь угадывать! 🐱"
        print("Кнопка 'Что это?' нажата — рисунок сохранён в лог.")
        
        # Логируем событие
        self.logger.log_event("drawing_recognize_attempt", {
            "status": "stub",
            "message": "кнопка нажата, распознавание ещё не реализовано"
        })

# Запуск приложения
if __name__ == '__main__':
    SashaGovoritApp().run()