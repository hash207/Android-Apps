from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

def one_and_zero(string: str):
    for i in string:
        if i == '1' or i == '0':
            pass
        else:
            return False
    return True

class Home(MDScreen):
    def get_data(self):
        x = str(self.ids.input.text)
        try:
            if x[2:].isnumeric() and x[:2] == "0b":
                self.ids.ans.text = str(eval(x))
            else:
                self.ids.ans.text = str(bin(int(x)))[2:]
        except:
                self.ids.ans.text = "Invaled value"

class Asciilator(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file('design.kv')

if __name__ == "__main__":
    Asciilator().run()