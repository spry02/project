from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
#dialog info
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivy.config import Config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 500)
Config.set('graphics', 'height', 800)
Config.write()

KV='''
<MenuHeader>
    spacing: "12dp"
    padding: "4dp"
    adaptive_height: True

MDScreen:
    MDTopAppBar:
        title: "Z:              Na:"
        pos_hint: {'center_x': 0.5, 'center_y': 0.97}
    MDTextField:
        id: tf1
        pos_hint: {'center_x': 0.5, 'center_y': 0.77}
        size_hint: .8, None
        write_tab: False
        require: True
    MDRectangleFlatIconButton:
        id: call
        icon: 'heart'
        text: "Przeliczanie"
        pos_hint: {'center_x': 0.5,'center_y': 0.7}
        size_hint: .4, None
        on_release: app.buton()
        # on_release: app.menu.open()
    MDFlatButton:
        id: z
        text: "2"
        font_size: 25
        value: 2
        pos_hint: {'center_x': 0.15, "center_y": 0.968}
        on_release: app.menu.open()
    MDFlatButton:
        id: na
        text: "10"
        font_size: 25
        value: 10
        pos_hint: {'center_x': 0.35, "center_y": 0.968}
        on_release: app.menu2.open()
    MDLabel:
        id: footer
        text: '© All rights reserved @ plspry 2024'
        pos_hint: {'center_x': 0.65,'center_y': 0.03}
        size_hint: .8, .01
        theme_text_color: "Custom"
        text_color: (75, 75, 75, 1)
    MDLabel:
        id: wynik2
        text: ''
        size_hint: .9, .01
        pos_hint: {'center_x': 0.52,'center_y': 0.62}
    MDLabel:
        id: wynik3
        text: ''
        size_hint: .9, .01
        pos_hint: {'center_x': 0.52,'center_y': 0.54}
'''

class MenuHeader(MDBoxLayout):
    ''''''


class MyApp(MDApp):
    dialog = None
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        # menu
        menu_list = [
            {
                "viewclass": "OneLineListItem",
                "id": f"{i}",
                "text": f"{i}",
                "on_release": lambda x=i: self.system(x)
            } for i in range(2,17)
        ]
        menu2_list = [
            {
                "viewclass": "OneLineListItem",
                "id": f"{i}",
                "text": f"{i}",
                "on_release": lambda x=i: self.system2(x)
            } for i in range(2,17)
        ]
        self.menu = MDDropdownMenu(
            # header_cls = MenuHeader(),
            caller = self.kvs.ids.z,
            items = menu_list,
            max_height = 300,
            width_mult = 4
        )
        self.menu2 = MDDropdownMenu(
            # header_cls = MenuHeader(),
            caller = self.kvs.ids.na,
            items = menu2_list,
            max_height = 300,
            width_mult = 4
        )
        # alert
        if not self.dialog:
            self.dialog = MDDialog(
                text="Upewnij się, że podałeś poprawną liczbę dla danego systemu!",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=lambda _: self.dialog.dismiss()
                    )
                ],
                size_hint_x=0.9, 
                size_hint_y=0.4,
            )
    def build(self):
        self.title='Konwerter liczb by plspry'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        screen=Screen()
        screen.add_widget(self.kvs)
        return screen
    
    def buton(self):
        fst=self.kvs.ids
        l=0
        ls=['F','E','D','C','B','A']
        c=fst.tf1.text
        s=''
        try:
            l=int(fst.tf1.text, fst.z.value)
            if fst.na.value!=10:
                while l!=0:
                    if l%fst.na.value>9:
                        newNum=ls[15-l%fst.na.value]
                    else:
                        newNum=l%fst.na.value
                    l = l//fst.na.value
                    s+=f"{newNum}"
                self.binor(c, s[::-1])
            else:
                self.binor(c, l)
        except:
            self.dialog.open()
    
    def binor(self, src, dest):
        self.kvs.ids.wynik2.text=f'Liczba bazowa:({self.kvs.ids.z.value})\n {src}'
        self.kvs.ids.wynik3.text=f'Liczba finalna:({self.kvs.ids.na.value})\n {dest}'
        

    def system(self, i):
        self.menu.dismiss()
        self.kvs.ids.z.text=f"{i}"
        self.kvs.ids.z.value=i

    def system2(self, i):
        self.menu2.dismiss()
        self.kvs.ids.na.text=f"{i}"
        self.kvs.ids.na.value=i

    
ma=MyApp()
ma.run()
