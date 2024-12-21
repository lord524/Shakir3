from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from datetime import datetime

# ضبط حجم نافذة التطبيق لتناسب شاشة الهاتف
Window.size = (360, 640)  # يمكنك تعديل الأبعاد حسب الحاجة

class TimeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(font_size='48sp', size_hint=(1, 0.2))
        layout.add_widget(self.label)
        Clock.schedule_interval(self.update_time, 1)  # تحديث الوقت كل ثانية
        return layout

    def update_time(self, dt):
    
        current_date = datetime.now().strftime('%Y-%m-%d')
        self.label.text += f'\n{current_date}'  # إضافة التاريخ أسفل الوقت

if __name__ == '__main__':
    TimeApp().run()
