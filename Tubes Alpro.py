import tkinter as tk
import customtkinter as ctk
import mysql.connector as mysql
import ast, re
from customtkinter import *
from PIL import Image


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('dark-blue')
        self.title('Hostay')
        self.geometry('800x600')
        self.iconbitmap('Aset/favicon (4).ico')
        self.img_login = ctk.CTkImage(Image.open('Aset/Box Shadow Login.png'), size=(1600, 900))
        self.img_registration = ctk.CTkImage(Image.open('Aset/Box Shadow Regis.png'), size=(1600, 900))
        self.background = ctk.CTkLabel(self, text='', image=self.img_login)
        self.background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.login_page = LoginPage(self)
        self.registration_page = RegistrationPage(self)
        self.show_login_page()

        self.login_page.regis_label_button.configure(command=self.show_registration_page)
        self.registration_page.login_label_button.configure(command=self.show_login_page)

    def show_login_page(self):
        self.login_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.registration_page.place_forget()
        self.background.configure(image=self.img_login)
        
    def show_registration_page(self):
        self.registration_page.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.login_page.place_forget()
        self.background.configure(image=self.img_registration)

    def show_mainmenu_page(self):
        self.login_page.place_forget()
        self.img_mainmenu_background = ctk.CTkImage(Image.open('Aset/Solid BG.png'), size=(1600, 900))
        self.background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.background.configure(self, text='', image=self.img_mainmenu_background)

        self.img_logo = ctk.CTkImage(Image.open('Aset/Hostay White.png'), size=(120, 60))
        self.dashboard_image = ctk.CTkImage(Image.open('Aset/Dashboard.png'), size=(20, 20))
        self.checkin_image = ctk.CTkImage(Image.open('Aset/Check In.png'), size=(20, 20))
        self.checkout_image = ctk.CTkImage(Image.open('Aset/Check Out.png'), size=(20, 20))
        self.roomservice_image = ctk.CTkImage(Image.open('Aset/Room Service.png'), size=(20, 20))
        self.about_image =  ctk.CTkImage(Image.open('Aset/About.png'), size=(20, 20))
        self.user_image = ctk.CTkImage(Image.open('Aset/person_icon.png'), size=(25, 25))
        self.vacantrooms_image = ctk.CTkImage(Image.open('Aset/Vacant Rooms.png'), size=(310, 207))
        self.occupiedrooms_image = ctk.CTkImage(Image.open('Aset/Occupied Rooms.png'), size=(310, 207))
        self.vacatedrooms_image = ctk.CTkImage(Image.open('Aset/Vacated Rooms.png'), size=(310, 207))
        self.requiringservice_image = ctk.CTkImage(Image.open('Aset/Requiring Service.png'), size=(310, 207))
        self.rightarrow_image = ctk.CTkImage(Image.open('Aset/Right Arrow.png'), size=(10, 10))
        self.downarrow_image = ctk.CTkImage(Image.open('Aset/Down Arrow.png'), size=(10, 10))
        self.singleroom_image = ctk.CTkImage(Image.open('Aset/Single Room.png'), size=(305, 264))
        self.doubleroom_image = ctk.CTkImage(Image.open('Aset/Double Room.png'), size=(305, 264))
        self.suiteroom_image = ctk.CTkImage(Image.open('Aset/Suite Room.png'), size=(305, 264))
        self.presidentsuiteroom_image = ctk.CTkImage(Image.open('Aset/President Suite Room.png'), size=(305, 264))
        
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        # FRAMES

        self.sidebar_frame = ctk.CTkFrame(self, fg_color='#1F1F27', bg_color='#0C0B10', border_color='#1B1B22', border_width=3, corner_radius=40)
        self.headbar_frame = ctk.CTkFrame(self, fg_color='#242531', bg_color='#0C0B10', corner_radius=30, border_color='#1F1F27', border_width=3)
        self.main_frame_dashboard = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_roomservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_about = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_dashboard_roomstatus = ctk.CTkFrame(self.main_frame_dashboard, fg_color="#17171E", bg_color='#0C0B10', border_color='#15151B', border_width=5, corner_radius=20)
        self.main_scrollframe_dashboard_roomstatus = ctk.CTkScrollableFrame(self.main_frame_dashboard_roomstatus, width=1150, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531')

        self.sidebar_frame.grid(row=1, column=0, rowspan=3, padx=(30,20), pady=(10,25), sticky='nsew')
        self.headbar_frame.grid(row=0, column=0, columnspan=4, padx=30, pady=20, sticky='news')
        self.main_frame_dashboard.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_roomservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_frame_about.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_dashboard_roomstatus.grid(row=2, column=0, rowspan=1, columnspan=4, padx=(9,37), pady=5, ipady=10, sticky='news')
        self.main_scrollframe_dashboard_roomstatus.grid(row=1, column=0, columnspan=10, padx=(17.5,10), ipady=20, sticky='news')
        
        self.headbar_frame.grid_columnconfigure(1, weight=1)
        self.main_frame_dashboard.grid_columnconfigure(3, weight=1)
        self.main_frame_checkin.grid_columnconfigure(3, weight=1)        

        # WIDGETS

        # SIDEBAR WIDGETS
        self.sidebar_label_mainnav = ctk.CTkButton(self.sidebar_frame, corner_radius=25, width=180, height=45, text="Main Nav", font=ctk.CTkFont('Mona-Sans Bold', 20), fg_color='#191922', bg_color='transparent', text_color="#D2D2DD", hover_color='#191922')
        self.sidebar_button_dashboard = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Dashboard", font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.dashboard_image, command=self.dashboard_menu)
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.rightarrow_image, compound='left', command=self.expand_button)
        self.sidebar_button_roomservice = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Room Services", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.roomservice_image, command=self.roomservice_menu)
        self.sidebar_button_about = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="About", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.about_image, command=self.about_menu)
       
        self.sidebar_label_mainnav.grid(row=0, column=0, ipadx=0, pady=15, ipady=0)
        self.sidebar_button_dashboard.grid(row=1, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_roomservice.grid(row=3, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=4, column=0, padx=20, pady=5, sticky='news')

        # HEADBAR WIDGETS

        self.headbar_label_logo = ctk.CTkLabel(self.headbar_frame, text="", image=self.img_logo)
        self.headbar_button_profile = ctk.CTkButton(self.headbar_frame, corner_radius=30, width=50, height=45, image=self.user_image, text="Profile", font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#C700FF', cursor='hand2', anchor="center")
        self.headbar_label_logo.grid(row=0, column=0, padx=30, pady=0, ipadx=25, ipady=0)
        self.headbar_button_profile.grid(row=0, column=6, padx=12, pady=10)

        # DASHBOARD WIDGET

        self.main_dashboard_label = ctk.CTkLabel(self.main_frame_dashboard, text="Dashboard", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_welcome_label =  ctk.CTkLabel(self.main_frame_dashboard, text="Welcome to Hotel Management System  |  by Kelompok 4", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_dashboard_label.grid(row=0, column=0, pady=5, sticky='news')
        self.main_welcome_label.place(x=580, y=43, anchor=tk.CENTER)

        self.main_dashboard_vacantrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_occupiedrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_vacatedrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_requiringservice_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
       
        self.main_dashboard_vacantrooms_label = ctk.CTkLabel(self.main_dashboard_vacantrooms_frame, text='\n\n                   27', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacantrooms_image)
        self.main_dashboard_occupiedrooms_label = ctk.CTkLabel(self.main_dashboard_occupiedrooms_frame, text='\n\n                   1', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.occupiedrooms_image)
        self.main_dashboard_vacatedrooms_label = ctk.CTkLabel(self.main_dashboard_vacatedrooms_frame, text='\n\n                   1', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacatedrooms_image)
        self.main_dashboard_requiringservice_label = ctk.CTkLabel(self.main_dashboard_requiringservice_frame, text='\n\n                   1', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.requiringservice_image)
        
        self.main_dashboard_vacantrooms_frame.grid(row=1, column=0, pady=0, sticky='news')
        self.main_dashboard_occupiedrooms_frame.grid(row=1, column=1, pady=0, sticky='news')
        self.main_dashboard_vacatedrooms_frame.grid(row=1, column=2, pady=0, sticky='news')
        self.main_dashboard_requiringservice_frame.grid(row=1, column=3, pady=0, sticky='news')
        
        self.main_dashboard_vacantrooms_label.grid(row=0, column=0)
        self.main_dashboard_occupiedrooms_label.grid(row=0, column=0)
        self.main_dashboard_vacatedrooms_label.grid(row=0, column=0)
        self.main_dashboard_requiringservice_label.grid(row=0, column=0)  
        
        # DASHBOARD ROOM STATUS WIDGET

        self.main_dashboard_roomstatus_frame = ctk.CTkButton(self.main_frame_dashboard_roomstatus, corner_radius=25, width=180, height=45, text="Room Status", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF")
        self.main_dashboard_roomstatus_frame.grid(row=0, column=0, columnspan=10, padx=(20,12), pady=(15,20), sticky='news')

        # 1-10
        self.room01_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room02_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room03_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room04_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room05_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room06_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room07_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room08_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room09_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room10_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room11_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room12_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room13_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room14_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room15_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room16_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room17_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room18_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room19_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room20_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room21_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room22_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room23_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room24_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room25_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room26_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room27_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room28_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room29_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        self.room30_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', corner_radius=20)
        
        self.room01_frame_indicator = ctk.CTkFrame(self.room01_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room02_frame_indicator = ctk.CTkFrame(self.room02_frame, width=70, height=10, fg_color='#3C58F7', corner_radius=20)
        self.room03_frame_indicator = ctk.CTkFrame(self.room03_frame, width=70, height=10, fg_color='#9031D3', corner_radius=20)
        self.room04_frame_indicator = ctk.CTkFrame(self.room04_frame, width=70, height=10, fg_color='#B52483', corner_radius=20)
        self.room05_frame_indicator = ctk.CTkFrame(self.room05_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room06_frame_indicator = ctk.CTkFrame(self.room06_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room07_frame_indicator = ctk.CTkFrame(self.room07_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room08_frame_indicator = ctk.CTkFrame(self.room08_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room09_frame_indicator = ctk.CTkFrame(self.room09_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room10_frame_indicator = ctk.CTkFrame(self.room10_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room11_frame_indicator = ctk.CTkFrame(self.room11_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room12_frame_indicator = ctk.CTkFrame(self.room12_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room13_frame_indicator = ctk.CTkFrame(self.room13_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room14_frame_indicator = ctk.CTkFrame(self.room14_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room15_frame_indicator = ctk.CTkFrame(self.room15_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room16_frame_indicator = ctk.CTkFrame(self.room16_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room17_frame_indicator = ctk.CTkFrame(self.room17_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room18_frame_indicator = ctk.CTkFrame(self.room18_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room19_frame_indicator = ctk.CTkFrame(self.room19_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room20_frame_indicator = ctk.CTkFrame(self.room20_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room21_frame_indicator = ctk.CTkFrame(self.room21_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room22_frame_indicator = ctk.CTkFrame(self.room22_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room23_frame_indicator = ctk.CTkFrame(self.room23_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room24_frame_indicator = ctk.CTkFrame(self.room24_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room25_frame_indicator = ctk.CTkFrame(self.room25_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room26_frame_indicator = ctk.CTkFrame(self.room26_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room27_frame_indicator = ctk.CTkFrame(self.room27_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room28_frame_indicator = ctk.CTkFrame(self.room28_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room29_frame_indicator = ctk.CTkFrame(self.room29_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room30_frame_indicator = ctk.CTkFrame(self.room30_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        
        self.room01_frame_status = ctk.CTkLabel(self.room01_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room02_frame_status = ctk.CTkLabel(self.room02_frame, text='Occupied', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room03_frame_status = ctk.CTkLabel(self.room03_frame, text='Vacated', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room04_frame_status = ctk.CTkLabel(self.room04_frame, text='Requiring', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room05_frame_status = ctk.CTkLabel(self.room05_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room06_frame_status = ctk.CTkLabel(self.room06_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room07_frame_status = ctk.CTkLabel(self.room07_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room08_frame_status = ctk.CTkLabel(self.room08_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room09_frame_status = ctk.CTkLabel(self.room09_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room10_frame_status = ctk.CTkLabel(self.room10_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room11_frame_status = ctk.CTkLabel(self.room11_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room12_frame_status = ctk.CTkLabel(self.room12_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room13_frame_status = ctk.CTkLabel(self.room13_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room14_frame_status = ctk.CTkLabel(self.room14_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room15_frame_status = ctk.CTkLabel(self.room15_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room16_frame_status = ctk.CTkLabel(self.room16_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room17_frame_status = ctk.CTkLabel(self.room17_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room18_frame_status = ctk.CTkLabel(self.room18_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room19_frame_status = ctk.CTkLabel(self.room19_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room20_frame_status = ctk.CTkLabel(self.room20_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room21_frame_status = ctk.CTkLabel(self.room21_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room22_frame_status = ctk.CTkLabel(self.room22_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room23_frame_status = ctk.CTkLabel(self.room23_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room24_frame_status = ctk.CTkLabel(self.room24_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room25_frame_status = ctk.CTkLabel(self.room25_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room26_frame_status = ctk.CTkLabel(self.room26_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room27_frame_status = ctk.CTkLabel(self.room27_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room28_frame_status = ctk.CTkLabel(self.room28_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room29_frame_status = ctk.CTkLabel(self.room29_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room30_frame_status = ctk.CTkLabel(self.room30_frame, text='Available', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
      
        self.room01_frame_label = ctk.CTkLabel(self.room01_frame, text='01', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room02_frame_label = ctk.CTkLabel(self.room02_frame, text='02', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room03_frame_label = ctk.CTkLabel(self.room03_frame, text='03', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room04_frame_label = ctk.CTkLabel(self.room04_frame, text='04', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room05_frame_label = ctk.CTkLabel(self.room05_frame, text='05', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room06_frame_label = ctk.CTkLabel(self.room06_frame, text='06', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room07_frame_label = ctk.CTkLabel(self.room07_frame, text='07', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room08_frame_label = ctk.CTkLabel(self.room08_frame, text='08', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room09_frame_label = ctk.CTkLabel(self.room09_frame, text='09', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room10_frame_label = ctk.CTkLabel(self.room10_frame, text='10', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFDC99')
        self.room11_frame_label = ctk.CTkLabel(self.room11_frame, text='11', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room12_frame_label = ctk.CTkLabel(self.room12_frame, text='12', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room13_frame_label = ctk.CTkLabel(self.room13_frame, text='13', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room14_frame_label = ctk.CTkLabel(self.room14_frame, text='14', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room15_frame_label = ctk.CTkLabel(self.room15_frame, text='15', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room16_frame_label = ctk.CTkLabel(self.room16_frame, text='16', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room17_frame_label = ctk.CTkLabel(self.room17_frame, text='17', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room18_frame_label = ctk.CTkLabel(self.room18_frame, text='18', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room19_frame_label = ctk.CTkLabel(self.room19_frame, text='19', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room20_frame_label = ctk.CTkLabel(self.room20_frame, text='20', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#CE5700')
        self.room21_frame_label = ctk.CTkLabel(self.room21_frame, text='21', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room22_frame_label = ctk.CTkLabel(self.room22_frame, text='22', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room23_frame_label = ctk.CTkLabel(self.room23_frame, text='23', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room24_frame_label = ctk.CTkLabel(self.room24_frame, text='24', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room25_frame_label = ctk.CTkLabel(self.room25_frame, text='25', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room26_frame_label = ctk.CTkLabel(self.room26_frame, text='26', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#BBCDCA')
        self.room27_frame_label = ctk.CTkLabel(self.room27_frame, text='27', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFB800')
        self.room28_frame_label = ctk.CTkLabel(self.room28_frame, text='28', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFB800')
        self.room29_frame_label = ctk.CTkLabel(self.room29_frame, text='29', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFB800')
        self.room30_frame_label = ctk.CTkLabel(self.room30_frame, text='30', font=ctk.CTkFont('Mona-Sans ExtraBold', 40), text_color='#FFB800')
       
        self.room01_frame.grid(row=1, column=0, padx=(0,20), pady=10, sticky='news')
        self.room02_frame.grid(row=1, column=1, padx=(0,20), pady=10, sticky='news')
        self.room03_frame.grid(row=1, column=2, padx=(0,20), pady=10, sticky='news')
        self.room04_frame.grid(row=1, column=3, padx=(0,20), pady=10, sticky='news')
        self.room05_frame.grid(row=1, column=4, padx=(0,20), pady=10, sticky='news')
        self.room06_frame.grid(row=1, column=5, padx=(0,20), pady=10, sticky='news')
        self.room07_frame.grid(row=1, column=6, padx=(0,20), pady=10, sticky='news')
        self.room08_frame.grid(row=1, column=7, padx=(0,20), pady=10, sticky='news')
        self.room09_frame.grid(row=1, column=8, padx=(0,20), pady=10, sticky='news')
        self.room10_frame.grid(row=1, column=9, padx=(0,20), pady=10, sticky='news')
        self.room11_frame.grid(row=2, column=0, padx=(0,20), pady=10, sticky='news')
        self.room12_frame.grid(row=2, column=1, padx=(0,20), pady=10, sticky='news')
        self.room13_frame.grid(row=2, column=2, padx=(0,20), pady=10, sticky='news')
        self.room14_frame.grid(row=2, column=3, padx=(0,20), pady=10, sticky='news')
        self.room15_frame.grid(row=2, column=4, padx=(0,20), pady=10, sticky='news')
        self.room16_frame.grid(row=2, column=5, padx=(0,20), pady=10, sticky='news')
        self.room17_frame.grid(row=2, column=6, padx=(0,20), pady=10, sticky='news')
        self.room18_frame.grid(row=2, column=7, padx=(0,20), pady=10, sticky='news')
        self.room19_frame.grid(row=2, column=8, padx=(0,20), pady=10, sticky='news')
        self.room20_frame.grid(row=2, column=9, padx=(0,20), pady=10, sticky='news')
        self.room21_frame.grid(row=3, column=2, padx=(0,20), pady=10, sticky='news') 
        self.room22_frame.grid(row=3, column=3, padx=(0,20), pady=10, sticky='news')
        self.room23_frame.grid(row=3, column=4, padx=(0,20), pady=10, sticky='news')
        self.room24_frame.grid(row=3, column=5, padx=(0,20), pady=10, sticky='news')
        self.room25_frame.grid(row=3, column=6, padx=(0,20), pady=10, sticky='news')
        self.room26_frame.grid(row=3, column=7, padx=(0,20), pady=10, sticky='news')
        self.room27_frame.grid(row=4, column=3, padx=(0,20), pady=10, sticky='news')
        self.room28_frame.grid(row=4, column=4, padx=(0,20), pady=10, sticky='news')
        self.room29_frame.grid(row=4, column=5, padx=(0,20), pady=10, sticky='news')
        self.room30_frame.grid(row=4, column=6, padx=(0,20), pady=10, sticky='news')
       
        self.room01_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room02_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room03_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room04_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room05_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room06_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room07_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room08_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room09_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room10_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room11_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room12_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)    
        self.room13_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room14_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room15_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room16_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room17_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)        
        self.room18_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room19_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room20_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room21_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room22_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room23_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room24_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room25_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room26_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room27_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room28_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room29_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        self.room30_frame_indicator.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
       
        self.room01_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room02_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room03_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room04_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room05_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room06_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room07_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room08_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room09_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room10_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room11_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room12_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room13_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room14_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room15_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room16_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room17_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room18_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room19_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room20_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room21_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room22_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room23_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room24_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room25_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room26_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room27_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room28_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room29_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.room30_frame_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
        
        self.room01_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room02_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room03_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room04_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room05_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room06_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room07_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room08_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room09_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room10_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room11_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room12_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room13_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room14_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room15_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room16_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room17_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room18_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room19_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room20_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room21_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room22_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room23_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room24_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room25_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room26_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room27_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room28_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room29_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.room30_frame_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
     

       # CHECK IN WIDGET

        self.main_checkin_choosetype_label =  ctk.CTkLabel(self.main_frame_checkin, text="Choose room type", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_choosetype_label.place(x=340, y=43, anchor=tk.CENTER)
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(20,60), sticky='news')

        self.main_checkin_singleroom_frame = ctk.CTkFrame(self.main_frame_checkin, fg_color='transparent', width=300, height=200)
        self.main_checkin_doubleroom_frame = ctk.CTkFrame(self.main_frame_checkin, fg_color='transparent', width=300, height=200)
        self.main_checkin_suiteroom_frame = ctk.CTkFrame(self.main_frame_checkin, fg_color='transparent', width=300, height=200)
        self.main_checkin_presidentsuiteroom_frame = ctk.CTkFrame(self.main_frame_checkin, fg_color='transparent', width=300, height=200)
        
        self.main_checkin_singleroom_label = ctk.CTkLabel(self.main_checkin_singleroom_frame, text="", image=self.singleroom_image)
        self.main_checkin_doubleroom_label = ctk.CTkLabel(self.main_checkin_doubleroom_frame, text="", image=self.doubleroom_image)
        self.main_checkin_suiteroom_label = ctk.CTkLabel(self.main_checkin_suiteroom_frame, text="", image=self.suiteroom_image)
        self.main_checkin_presidentsuiteroom_label = ctk.CTkLabel(self.main_checkin_presidentsuiteroom_frame, text="", image=self.presidentsuiteroom_image)
        
        self.main_checkin_singleroom_available_label = ctk.CTkLabel(self.main_frame_checkin, text="Room Available : 10", font=ctk.CTkFont('Mona-Sans', 12), text_color="#B6B6C6")
        self.main_checkin_doubleroom_available_label = ctk.CTkLabel(self.main_frame_checkin, text="Room Available : 10", font=ctk.CTkFont('Mona-Sans', 12), text_color="#B6B6C6")
        self.main_checkin_suiteroom_available_label = ctk.CTkLabel(self.main_frame_checkin, text="Room Available : 6", font=ctk.CTkFont('Mona-Sans', 12), text_color="#B6B6C6")
        self.main_checkin_presidentsuiteroom_available_label = ctk.CTkLabel(self.main_frame_checkin, text="Room Available : 4", font=ctk.CTkFont('Mona-Sans', 12), text_color="#B6B6C6")
      
        self.main_checkin_singleroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Choose", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#FFDC99', border_width=2, anchor="center", command=self.singleroom_menu)
        self.main_checkin_doubleroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Choose", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#CE5700', border_width=2, anchor="center", command=self.doubleroom_menu)
        self.main_checkin_suiteroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Choose", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#BBCDCA', border_width=2, anchor="center", command=self.suiteroom_menu)
        self.main_checkin_presidentsuiteroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Choose", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#FFB800', border_width=2, anchor="center", command=self.presidentsuiteroom_menu)

        self.main_checkin_singleroom_frame.grid(row=1, column=0, pady=0, sticky='news')
        self.main_checkin_doubleroom_frame.grid(row=1, column=1, pady=0, sticky='news')
        self.main_checkin_suiteroom_frame.grid(row=1, column=2, pady=0, sticky='news')
        self.main_checkin_presidentsuiteroom_frame.grid(row=1, column=3, pady=0, sticky='news')
        
        self.main_checkin_singleroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_doubleroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_suiteroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_presidentsuiteroom_label.grid(row=0, padx=3)

        self.main_checkin_singleroom_available_label.place(x=155, y=350, anchor=tk.CENTER)
        self.main_checkin_doubleroom_available_label.place(x=465, y=350, anchor=tk.CENTER)
        self.main_checkin_suiteroom_available_label.place(x=775, y=350, anchor=tk.CENTER)
        self.main_checkin_presidentsuiteroom_available_label.place(x=1085, y=350, anchor=tk.CENTER)

        self.main_checkin_singleroom_button.grid(row=2, column=0, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_doubleroom_button.grid(row=2, column=1, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_suiteroom_button.grid(row=2, column=2, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_presidentsuiteroom_button.grid(row=2, column=3, padx=(40,65), pady=30, sticky='news')

       # ROOM SERVICES WIDGET

        self.main_roomservice_label = ctk.CTkLabel(self.main_frame_roomservice, text="Room Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_roomservice_label.grid(row=0, column=0, pady=(5,10), padx=20, sticky='news')

        # ABOUT WIDGET

        self.main_about_label = ctk.CTkLabel(self.main_frame_about, text="About", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_about_label.grid(row=0, column=0, pady=(5,20), padx=20, sticky='news')


        self.select_frame_sidebar("dashboard")
    
    def select_frame_sidebar(self, name):
        # set button color for selected button
        self.sidebar_button_dashboard.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'dashboard' else 'transparent')
        self.sidebar_button_checkinout.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkinout' else 'transparent')
        self.sidebar_button_roomservice.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'roomservice' else 'transparent')
        self.sidebar_button_about.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'about' else 'transparent')
        self.headbar_button_profile.configure(self.sidebar_frame, fg_color=('#8500AB') if name == 'profile' else 'transparent')

        if name == "dashboard":
            self.main_frame_dashboard.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_dashboard.grid_forget()
        if name == "about":
            self.main_frame_about.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_about.grid_forget()
        if name == "roomservice":
            self.main_frame_roomservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_roomservice.grid_forget()
        if name == "checkin":
            self.main_frame_checkin.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin.grid_forget()

    def dashboard_menu(self):
        self.select_frame_sidebar('dashboard')

    def checkin_menu(self):
        self.select_frame_sidebar('checkin')    

    def roomservice_menu(self):
        self.select_frame_sidebar('roomservice')

    def about_menu(self):
        self.select_frame_sidebar('about')

    def singleroom_menu(self):
        self.main_frame_checkin.grid_forget()
        self.checkin_frame_singleroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.checkin_frame_singleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')

    def doubleroom_menu(self):
        self.main_frame_checkin.grid_forget()
        self.checkin_frame_doubleroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.checkin_frame_doubleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')

    def suiteroom_menu(self):
        self.main_frame_checkin.grid_forget()
        self.checkin_frame_suiteroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.checkin_frame_suiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')

    def presidentsuiteroom_menu(self):
        self.main_frame_checkin.grid_forget()
        self.checkin_frame_presidentsuiteroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.checkin_frame_presidentsuiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')


    
    def expand_button(self):
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.downarrow_image, compound='left', command=self.close_button)
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_checkin = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check In", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkin_image, command=self.checkin_menu)
        self.sidebar_button_checkin.grid(row=3, column=0, padx=20, pady=0, sticky='ns')
        self.sidebar_button_checkout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check Out", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkout_image)
        self.sidebar_button_checkout.grid(row=4, column=0, padx=20, pady=3, sticky='ns')
        self.sidebar_button_roomservice.grid(row=5, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=6, column=0, padx=20, pady=5, sticky='ew')

    def close_button(self):
        self.sidebar_button_checkin.grid_forget()
        self.sidebar_button_checkout.grid_forget()
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.rightarrow_image, compound='left', command=self.expand_button)
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_roomservice.grid(row=3, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=4, column=0, padx=20, pady=5, sticky='ew')

    # def select_frame_checkin(self, name):
    
    #     if name == 'singleroom':
    #         self.checkin_frame_singleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
    #     else:
    #         self.checkin_frame_singleroom.grid_forget()
    #     if name == 'doubleroom':
    #         self.checkin_frame_doubleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
    #     else:
    #         self.checkin_frame_doubleroom.grid_forget()
    #     if name == 'suiteroom':
    #         self.checkin_frame_suiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
    #     else:
    #         self.checkin_frame_suiteroom.grid_forget()
    #     if name == 'presidentsuiteroom':
    #         self.checkin_frame_presidentsuiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
    #     else:
    #         self.checkin_frame_presidentsuiteroom.grid_forget()

    

    # def doubleroom_menu(self):
    #     self.select_frame_checkin('doubleroom')    

    # def suiteroom_menu(self):
    #     self.select_frame_checkin('suiteroom')

    # def presidentsuite_menu(self):
    #     self.select_frame_checkin('presidentroom')
    
    def change_appearance_mode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode) 

class LoginPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color='#FFFFFF', fg_color='#FFFFFF', border_width=20, border_color='#FFFFFF', corner_radius=30, width=250, height=300)
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        self.img_logo = ctk.CTkImage(Image.open('Aset/Hostay Logo.png'), size=(140, 70))
        self.hostay_logo = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.hostay_logo.place(relx=0.5, rely=0.14, anchor=tk.CENTER)

        self.username_label = ctk.CTkLabel(self, text='Username', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.username_label.place(relx=0.24, rely=0.360, anchor=tk.CENTER)
        self.username_label_emoji = ctk.CTkLabel(self, text='👤', text_color='#000000')
        self.username_label_emoji.place(relx=0.41, rely=0.354, anchor=tk.CENTER)
        self.username_input = ctk.CTkEntry(self, width=200, placeholder_text='Masukkan Username')
        self.username_input.place(relx=0.5, rely=0.435, anchor=tk.CENTER)

        self.password_label = ctk.CTkLabel(self, text='Password', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.password_label.place(relx=0.24, rely=0.543, anchor=tk.CENTER)
        self.password_label_emoji = ctk.CTkLabel(self, text="🔐", text_color='#000000')
        self.password_label_emoji.place(relx=0.404, rely=0.535, anchor=tk.CENTER)
        self.password_input = ctk.CTkEntry(self, width=200, placeholder_text='Masukkan Password', show='*')
        self.password_input.place(relx=0.5, rely=0.617, anchor=tk.CENTER)

        self.hide_eye = ctk.CTkImage(Image.open('Aset/hide.png'), size=(17, 17))
        self.show_eye = ctk.CTkImage(Image.open('Aset/show.png'), size=(17, 17))
        self.show_password = ctk.CTkButton(self, width=20, height=20, fg_color='transparent', hover_color='#FFFFFF', text='', cursor='hand2', image=self.show_eye, command=self.ShowPassword)
        self.show_password.place(relx=0.966, rely=0.615, anchor=tk.CENTER)

        self.login_button = ctk.CTkButton(self, width=223, height=30, text='L O G I N', text_color='#FFFFFF', fg_color='#1f538d', hover_color='#0E4480', cursor='hand2', font=('Mona-Sans ExtraBold Wide', 13), border_width=0, border_color='#0E4480', corner_radius=25, command=self.Login)
        self.login_button.place(relx=0.5, rely=0.84, anchor=tk.CENTER)

        self.regis_label = ctk.CTkLabel(self, text='Anda belum memiki akun?', text_color='#000000', font=('Mona-Sans', 10.5))
        self.regis_label.place(relx=0.313, rely=0.96, anchor=tk.CENTER)
        
        self.regis_label_button = ctk.CTkButton(self, width=14, height=1, text='Registrasi disini', text_color='#004aad', border_width=0, fg_color='#FFFFFF', hover_color='#FFFFFF', cursor='hand2', font=('Mona-Sans', 11.5))
        self.regis_label_button.place(relx=0.782, rely=0.96, anchor=tk.CENTER)

        self.warning_label = CTkLabel(self, text="", font=CTkFont('Mona-Sans', 13), text_color='green')
        self.warning_label.place(relx=0.5, rely=0.72, anchor=tk.CENTER)

        self.password_visible = False
        self.skip = True

        if self.skip:
            self.Login()

    def Login(self):
        if self.skip:
            self.username = "admin"
            self.password = "admin123"

        else: 
            self.username = self.username_input.get()
            self.password = self.password_input.get()

        self.file = open('Aset/DataAkun.txt', 'r')
        d = self.file.read()
        r = ast.literal_eval(d)
        self.file.close()

        print(r.keys())
        print(r.values())

        if self.username in r.keys() and self.password == r[self.username]:
            self.warning_label.configure(text='Berhasil Login! Tunggu Sebentar...', text_color='green')
            self.warning_label.after(2000, self.master.show_mainmenu_page)
        else:
            self.warning_label.configure(text='Username atau Password salah.', text_color='red')
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))

    def ShowPassword(self):
        self.password_visible = not self.password_visible
        if self.password_visible:
            self.password_input.configure(show="")
            self.show_password.configure(image=self.hide_eye)
        else:
            self.password_input.configure(show="*")
            self.show_password.configure(image=self.show_eye)

class RegistrationPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color='#FFFFFF', fg_color='#FFFFFF', border_width=20, border_color='#FFFFFF', corner_radius=30, width=230, height=345)
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.img_logo = ctk.CTkImage(Image.open('Aset/Hostay Logo.png'), size=(140, 70))
        self.hostay_logo = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.hostay_logo.place(relx=0.5, rely=0.11, anchor=tk.CENTER)

        self.username_label = ctk.CTkLabel(self, text='Username', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.username_label.place(relx=0.26, rely=0.307, anchor=tk.CENTER)
        self.username_label_emoji = ctk.CTkLabel(self, text='👤', text_color='#000000')
        self.username_label_emoji.place(relx=0.443, rely=0.302, anchor=tk.CENTER)
        self.username_input = ctk.CTkEntry(self, width=180, placeholder_text='Masukkan Username')
        self.username_input.place(relx=0.5, rely=0.371, anchor=tk.CENTER)

        self.password_label = ctk.CTkLabel(self, text='Password', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.password_label.place(relx=0.257, rely=0.463, anchor=tk.CENTER)
        self.password_label_emoji = ctk.CTkLabel(self, text="🔐", text_color='#000000')
        self.password_label_emoji.place(relx=0.433, rely=0.457, anchor=tk.CENTER)
        self.password_input = ctk.CTkEntry(self, width=180, placeholder_text='Masukkan Password', show='*')
        self.password_input.place(relx=0.5, rely=0.526, anchor=tk.CENTER)

        self.confirmpassword_label = ctk.CTkLabel(self, text="Konfirmasi Password", text_color="#000000", font=ctk.CTkFont('Mona-Sans', 13))
        self.confirmpassword_label.place(relx=0.412, rely=0.615, anchor=tk.CENTER)
        self.confirmpassword_emoji = ctk.CTkLabel(self, text="🛡️", text_color="#000000")
        self.confirmpassword_emoji.place(relx=0.78, rely=0.607, anchor=tk.CENTER)
        self.confirmpassword_input = ctk.CTkEntry(self, width=180, placeholder_text="Konfirmasi Password", show="*")
        self.confirmpassword_input.place(relx=0.5, rely=0.681, anchor=tk.CENTER)

        self.signup_button = ctk.CTkButton(self, width=200, height=30, text='S I G N  U P', text_color='#FFFFFF', fg_color='#1f538d', hover_color='#0E4480', cursor='hand2', font=('Mona-Sans ExtraBold Wide', 13), border_width=2.5, border_color='#0E4480', corner_radius=25, command=self.Registration)
        self.signup_button.place(relx=0.5, rely=0.88, anchor=tk.CENTER)

        self.login_label = ctk.CTkLabel(self, text='Anda telah memiki akun?', text_color='#000000', font=('Mona-Sans', 10.5))
        self.login_label.place(relx=0.355, rely=0.975, anchor=tk.CENTER)
        
        self.login_label_button = ctk.CTkButton(self, width=14, height=1, text='Login disini', text_color='#004aad', border_width=0, fg_color='#FFFFFF', hover_color='#FFFFFF', cursor='hand2', font=('Mona-Sans', 11.5))
        self.login_label_button.place(relx=0.79, rely=0.975, anchor=tk.CENTER)

        self.warning_label = CTkLabel(self, text="", font=CTkFont('Mona-Sans', 11), text_color="red")
        self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

    def Registration(self):
        username = self.username_input.get()
        password = self.password_input.get()
        confirmpassword = self.confirmpassword_input.get()

        password_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        with open("Aset/DataAkun.txt", "r") as file:
            existing_users = ast.literal_eval(file.read())

        if username in existing_users:
            self.warning_label.configure(text="Username telah ada, Pilih username lain.", font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not username:
            self.warning_label.configure(text="Masukkan username terlebih dahulu.", font=CTkFont('Mona-Sans', 12))
            self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not password:
            self.warning_label.configure(text="Harap masukkan password\nterlebih dahulu.", font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not confirmpassword:
            self.warning_label.configure(text='Harap masukkan konfirmasi password\nterlebih dahulu.', font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not re.match(password_regex, password):
            self.warning_label.configure(text="Password harus memiliki minimal 8 karakter dan\nsetidaknya terdapat satu huruf dan satu angka.", font=CTkFont('Mona-Sans', 9))
            self.warning_label.after(2500, lambda: self.warning_label.configure(text=""))    
        else:
            if password == confirmpassword:
                try:
                    file = open("Aset/DataAkun.txt", "r+")
                    d = file.read()
                    r = ast.literal_eval(d)

                    dict2 = {username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file = open("Aset/DataAkun.txt", "w")
                    w = file.write(str(r))

                    self.warning_label.configure(text="Akun berhasil dibuat! Tunggu Sebentar...", font=CTkFont('Mona-Sans', 11), text_color="green")
                    self.warning_label.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
                    self.warning_label.after(1500, self.master.show_login_page)

                except:
                    file = open('Aset/DataAkun.txt', 'w')
                    pp = str({"Username": "password"})
                    file.write(pp)
                    file.close()
            else:
                self.warning_label.configure(text="Gagal, kedua password harus sama.", font=CTkFont('Mona-Sans', 11))
                self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))

if __name__ == '__main__':
    app = App()
    app.mainloop()

    