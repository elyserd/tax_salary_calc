from kivi.app import App
from kivi.uix.label import Label
from kivi.uix.button import Button 
from kivi.uix.textinput import TextInput
from kivi.uix.boxlayout import BoxLayout
from kivi.uix.screenmanager import ScreenManager, Screen
from kivi.uix.scrollview import ScrollView 
from kivy.uix.textinput import TextInput

class ScrButton(Button):
    def __init__(self, screen, direction = 'right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal




class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text="Это мобильное приложение по расчёту зарплаты, чтобы продолжить выбери экран",size_hint=(.5, .5),pos_hint={'center_x': .5, 'center_y': .5}, family_name = 'Calibri'))


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        vl.add_widget(ScrButton(self, direction='right', goal ='first', text='Нажми сюда, чтобы рассчитать зарплату', family_name='Times New Roman'))
        vl.add_widget(ScrButton(self, direction='left', goal='second', text='Нажми сюда, чтобы рассчитать налог'))
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(255, 182, 193)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        lbl = Label(text = 'Нажмите на кнопку, чтобы перейти к рассчету зарплаты', family_name='Arial')
        vl.add_widget(ScrButton(self, direction='right', goal ='third', text='Нажми сюда, чтобы рассчитать повременную зарплату'))
        vl.add_widget(ScrButton(self, direction='left', goal='forth', text='Нажми сюда, чтобы рассчитать сдельную зарплату'))
        vl.add_widget(lbl)
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(224, 207, 159)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        lbl = Label(text = 'Нажмите на кнопку, чтобы перейти к расчету налога', family_name='Arial')
        vl.add_widget(ScrButton(self, direction='right', goal ='fifth', text='Нажми сюда, чтобы рассчитать налог самозанятости'))
        vl.add_widget(ScrButton(self, direction='left', goal='sixth', text='Нажми сюда, чтобы рассчитать ставку НДФЛ'))
        vl.add_widget(lbl)
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(188, 143, 143)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root



class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        self.part_time_input = TextInput(hint_text = 'Введите почасовую зарплату', multiline = False)
        self.hours_worked_input = TextInput(hint_text = 'Введите количество рабочих часов в неделю', multiline = False)
        self.result_label1 = Label(text = 'Результаты будут отображены здесь')
        self.calculate_button1 = Button(text='Рассчитать', on_press=self.calculate_part_time_salary, family_name='Arial)
        vl.add_widget(self.part_time_input)
        vl.add_widget(self.hours_worked_input)
        vl.add_widget(self.result_label1)
        vl.add_widget(self.calculate_button1)
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(119, 136, 153)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root


    def part_time(self):
        hourly_rate = float(self.part_time_input.text)
        hours_worked = float(self.hours_worked_input.text)
        return hourly_rate * hours_worked * 4

    def calculate_part_time_salary(self, instance):
        part_time_salary = self.part_time()
        result_text = (f"Почасовая зарплата: {part_time_salary:.2f}\n")
        self.result_label1.text = result_text

class ForthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        self.full_time_input = TextInput(hint_text = 'Введите почасовую зарплату', multiline = False)
        self.result_label2 = Label(text = 'Результаты будут отображены здесь')
        self.calculate_button2 = Button(text='Рассчитать', on_press=self.calculate_full_time_salary, family_name='Arial)
        vl.add_widget(self.full_time_input)
        vl.add_widget(self.result_label2)
        vl.add_widget(self.calculate_button2)
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(176, 196, 222)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def full_time(self):
        hourly_rate = float(self.full_time_input.text)
        return hourly_rate * 160

    def calculate_part_time_salary(self, instance):
        full_time_salary = self.full_time()
        result_text = (f"Сдельная зарплата: {full_time_salary:.2f}\n")
        self.result_label2.text = result_text

class FifthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertucal', padding = 8, spacing = 8)
        hl = BoxLayout()
        self.part_time_input_tax = TextInput(hint_text = 'Введите ежемесячную зарплату', multiline = False)
        self.result_label3 = Label(text = 'Результаты будут отображены здесь')
        self.calculate_button3 = Button(text='Рассчитать', on_press=self.calculate_part_time_tax, family_name='Arial)
        vl.add_widget(self.part_time_input_tax)
        vl.add_widget(self.result_label3)
        vl.add_widget(self.calculate_button3)
        hl.add_widget(vl)
        self.add_widget(hl)
    
    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(175, 238, 238)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def part_time_tax(self):
        p_t_tax = float(self.part_time_tax_input.text)
        return p_t_tax * 0.06
    def calculate_part_time_tax(self, instance):
        part_time_tax = self.part_time_tax()
        result_text = (f'Налог самознятости: {part_time_tax:.2f}')
        self.result_label3.text = result_text

class SixthSct(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        hl = BoxLayout()
        self.full_time_input_tax = TextInput(hint_text = 'Введите ежемесячнуб зарплату', multiline = False)
        self.result_label4 = Label(text = 'Результаты будут отображены здесь')
        self.calculate_button4 = Button(text='Рассчитать', on_press = self.calculate_full_time_tax, family_name = 'Arial')
        vl.add_widget(self.full_time_input_tax)
        vl.add_widget(self.result_label4)
        vl.add_widget(self.calculate_button4)
        hl.add_widget(vl)
        self.add_widget(hl)

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        with root.canvas.before:
            Color(216, 191, 216)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root

    def full_time_tax(self):
        f_t_tax = float(self.full_time_tax_input.text)
        return f_t_tax * 0.13
    def calculate_full_time_tax(self, instance):
        full_time_tax = self.full_time_tax()
        result_text = (f'Налог самознятости: {full_time_tax:.2f}')
        self.result_label4.text = result_text








        


        

