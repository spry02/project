from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
#dialog info
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'resizable', '0')

KV='''
<MenuHeader>
    spacing: "12dp"
    padding: "4dp"
    adaptive_height: True

    MDIconButton:
        icon: "gesture-tap-button"
        pos_hint: {"center_y": .5}

    MDLabel:
        text: "Actions"
        adaptive_size: True
        pos_hint: {"center_y": .5}

MDScreen:
    MDTopAppBar:
        title: "Kalkulator adresów IPv4"
        pos_hint: {'center_x': 0.5, 'center_y': 0.97}
    MDTextField:
        id: tf1
        max_text_length: 3
        pos_hint: {'center_x': 0.1, 'center_y': 0.817}
        size_hint: .07, None
        input_filter: 'int'
        write_tab: False
        require: True
    MDLabel:
        text: "."
        pos_hint: {'center_x': 0.643, 'center_y': 0.805}
    MDTextField:
        id: tf2
        max_text_length: 3
        pos_hint: {'center_x': 0.19, 'center_y': 0.817}
        size_hint: .07, None
        input_filter: 'int'
        write_tab: False
        require: True
    MDLabel:
        text: "."
        pos_hint: {'center_x': 0.732, 'center_y': 0.805}
    MDTextField:
        id: tf3
        max_text_length: 3
        pos_hint: {'center_x': 0.28, 'center_y': 0.817}
        size_hint: .07, None
        input_filter: 'int'
        write_tab: False
        require: True
    MDLabel:
        text: "."
        pos_hint: {'center_x': 0.822, 'center_y': 0.805}
    MDTextField:
        id: tf4
        max_text_length: 3
        pos_hint: {'center_x': 0.37, 'center_y': 0.817}
        size_hint: .07, None
        input_filter: 'int'
        write_tab: False
        require: True
    MDRectangleFlatIconButton:
        id: call
        icon: 'heart'
        text: "Przeliczanie"
        pos_hint: {'center_x': 0.2,'center_y': 0.72}
        on_release: app.buton()
        # on_release: app.menu.open()
    MDFlatButton:
        id: maska
        text: "/24"
        value: 24
        pos_hint: {'center_x': 0.5, "center_y": 0.8}
        on_release: app.menu.open()
    MDLabel:
        id: wynik
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.65}
    MDLabel:
        id: wynik2
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.62}
    MDLabel:
        id: wynik3
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.59}
    MDLabel:
        id: wynik4
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.56}
    MDLabel:
        id: wynik5
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.53}
    MDLabel:
        id: wynik6
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.50}
    MDLabel:
        id: wynik7
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.47}
    MDLabel:
        id: wynik8
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.44}
    MDLabel:
        id: wynik9
        text: ''
        pos_hint: {'center_x': 0.52,'center_y': 0.41}
'''

class MenuHeader(MDBoxLayout):
    ''''''

Window.size=(450,800)

class MyApp(MDApp):
    icon=''
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
                "text": f"/{i}",
                "on_release": lambda x=i: self.maska(x)
            } for i in range(1,32)
        ]
        self.menu = MDDropdownMenu(
            # header_cls = MenuHeader(),
            caller = self.kvs.ids.maska,
            items = menu_list,
            width_mult = 4
        )
        # alert
        if not self.dialog:
            self.dialog = MDDialog(
                text="Upewnij się, że podałeś poprawny adres!",
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
        self.title='Kalkulator IP by plspry'
        self.icon="network.256x2502.ico"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        screen=Screen()
        screen.add_widget(self.kvs)
        return screen
    def buton(self):
        fst=self.kvs.ids
        l=[]
        l1=[]
        if (fst.tf1.text and int(fst.tf1.text)>=0 and int(fst.tf1.text)<=255) and (fst.tf2.text and int(fst.tf2.text)>=0 and int(fst.tf2.text)<=255) and (fst.tf3.text and int(fst.tf3.text)>=0 and int(fst.tf3.text)<=255) and (fst.tf4.text and int(fst.tf4.text)>=0 and int(fst.tf4.text)<=255):
            l1.append(int(fst.tf1.text))
            l1.append(int(fst.tf2.text))
            l1.append(int(fst.tf3.text))
            l1.append(int(fst.tf4.text))
            po=(bin(int(fst.tf1.text)).split('b')[1])
            do=(bin(int(fst.tf2.text)).split('b')[1])
            to=(bin(int(fst.tf3.text)).split('b')[1])
            co=(bin(int(fst.tf4.text)).split('b')[1])
            l.append(po)
            l.append(do)
            l.append(to)
            l.append(co)
            c=0
            for i in l:
                while len(i)<8:
                    i="0"+i
                l[c]=i
                c+=1
            self.binor(l1, l, self.kvs.ids.maska.value)
        else:
            self.dialog.open()
    
    def binor(self, lista1, lista, maska):
        maskabin=""
        adresbin=""
        adressiecibin, adressieci='', []
        adresrozglobin, adresrozglo='', []
        adrestemp1, adrestemp2='', ''
        for i in range(maska):
            maskabin+="1"
        for i in range(32-maska):
            maskabin+='0'
        for i in lista:
            adresbin+=i
        # print(adresbin)
        # print(maskabin)

        for i in range(len(maskabin)):
            if maskabin[i]=='0':
                adressiecibin+='0'
                adresrozglobin+='1'
            else:
                adressiecibin+=adresbin[i]
                adresrozglobin+=adresbin[i]

        for i in range(len(adresrozglobin)+1):
            if i%8==0 and i>0:
                adressieci.append(int(adrestemp1, 2))
                adresrozglo.append(int(adrestemp2, 2))
                adrestemp1, adrestemp2='', ''
            if i<len(adresrozglobin):
                adrestemp1+=adressiecibin[i]
                adrestemp2+=adresrozglobin[i]

        # print(adresbin)
        # print(adressieci)
        # print(adresrozglo)
        # print(pow(2, maskabin.count('0'))-2)
        self.kvs.ids.wynik.text="Adres IP: "
        self.kvs.ids.wynik2.text="Adres IP (binarnie): "
        self.kvs.ids.wynik3.text="Maska (binarnie): "
        self.kvs.ids.wynik4.text="Adres sieci: "
        self.kvs.ids.wynik5.text="Pierwszy adres hosta: "
        self.kvs.ids.wynik7.text="Adres rozgłoszeniowy: "
        self.kvs.ids.wynik6.text="Ostatni adres hosta: "
        self.kvs.ids.wynik8.text="Ilość hostów: "
        self.kvs.ids.wynik9.text="Klasa: "

        for i in range(4):
            if i<3:
                self.kvs.ids.wynik.text+=str(lista1[i])+'.'
                self.kvs.ids.wynik2.text+=str(lista[i])+'.'
                self.kvs.ids.wynik4.text+=str(adressieci[i])+'.'
                self.kvs.ids.wynik5.text+=str(adressieci[i])+'.'
                self.kvs.ids.wynik7.text+=str(adresrozglo[i])+'.'
                self.kvs.ids.wynik6.text+=str(adresrozglo[i])+'.'
            else:
                self.kvs.ids.wynik.text+=str(lista1[i])
                self.kvs.ids.wynik2.text+=str(lista[i])
                self.kvs.ids.wynik4.text+=str(adressieci[i])
                self.kvs.ids.wynik5.text+=str(adressieci[i]+1)
                self.kvs.ids.wynik7.text+=str(adresrozglo[i])
                self.kvs.ids.wynik6.text+=str(adresrozglo[i]-1)
                self.kvs.ids.wynik8.text+=str(pow(2, maskabin.count('0'))-2)
                
            # self.kvs.ids.wynik4.text=
            # self.kvs.ids.wynik5.text=
            # self.kvs.ids.wynik6.text=
        for i in range(1, len(maskabin)+1):
            if i%8==0 and i<len(maskabin):
                self.kvs.ids.wynik3.text+=str(maskabin[i-1])+'.'
            else:
                self.kvs.ids.wynik3.text+=str(maskabin[i-1])

        if adressieci[0]<128:
            self.kvs.ids.wynik9.text+="A, poprawna maska /8"
            if adressieci[0]==10:
                self.kvs.ids.wynik9.text+=", pula publiczna"
            elif adressieci[0]==0:
                self.kvs.ids.wynik9.text+=", sieć \"nieznana\""
            elif adressieci[0]==127:
                self.kvs.ids.wynik9.text+=", adres loopback"
        elif adressieci[0]>=128 and adressieci[0]<192:
            self.kvs.ids.wynik9.text+="B, poprawna maska /16"
            if adressieci[0]==172 and adressieci[1]>=16 and adressieci[1]<32:
                self.kvs.ids.wynik9.text+=", pula publiczna"
        elif adressieci[0]>=192 and adressieci[0]<224:
            self.kvs.ids.wynik9.text+="C, poprawna maska /24"
            if adressieci[0]==192 and adressieci[1]==168:
                self.kvs.ids.wynik9.text+=", pula publiczna"
        elif adressieci[0]>=224 and adressieci[0]<240:
            self.kvs.ids.wynik9.text+="D"
        elif adressieci[0]>=240:
            self.kvs.ids.wynik9.text+="E"

    def maska(self, i):
        self.menu.dismiss()
        self.kvs.ids.maska.text=f"/{i}"
        self.kvs.ids.maska.value=i

    
ma=MyApp()
ma.run()