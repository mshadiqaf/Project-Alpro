import customtkinter as ctk
import mysql.connector as mysql
import time as tm
import ast, re
from customtkinter import *
from CTkTable import *
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('dark-blue')
        self.title('Hostay')
        self.geometry('800x600')
        self.iconbitmap('Aset Projek/favicon (4).ico')
        self.img_mainmenu_background = ctk.CTkImage(Image.open('Aset Projek/Solid BG.png'), size=(1600, 900))
        self.img_login = ctk.CTkImage(Image.open('Aset Projek/Box Shadow Login.png'), size=(1600, 900))
        self.img_registration = ctk.CTkImage(Image.open('Aset Projek/Box Shadow Regis.png'), size=(1600, 900))
        self.background = ctk.CTkLabel(self, text='', image=self.img_login)
        self.background.place(relx=0.5, rely=0.5, anchor='center')

        self.login_page = LoginPage(self)
        self.registration_page = RegistrationPage(self)
        self.show_login_page()

        self.login_page.regis_label_button.configure(command=self.show_registration_page)
        self.registration_page.login_label_button.configure(command=self.show_login_page)
    
    def current_time(self):
        self.currenttime = tm.strftime('%H : %M : %S')
        self.headbar_clock_label.configure(text=self.currenttime)
        self.headbar_clock_label.after(1000, self.current_time)

    def show_login_page(self):
        self.login_page.place(relx=0.5, rely=0.5, anchor='center')
        self.registration_page.place_forget()
        self.background.configure(image=self.img_login)
        
    def show_registration_page(self):
        self.registration_page.place(relx=0.5, rely=0.5, anchor='center')
        self.login_page.place_forget()
        self.background.configure(image=self.img_registration)

    def show_mainmenu_page(self):
        self.login_page.place_forget()
        self.background.place(relx=0.5, rely=0.5, anchor='center')
        self.background.configure(self, text='', image=self.img_mainmenu_background)

        self.logo_image = ctk.CTkImage(Image.open('Aset Projek/Hostay White.png'), size=(110, 55))
        self.logoshadow_image = ctk.CTkImage(Image.open('Aset Projek/Hostay Dark.png'), size=(250, 125))
        self.dashboard_image = ctk.CTkImage(Image.open('Aset Projek/Dashboard.png'), size=(20, 20))
        self.checkin_image = ctk.CTkImage(Image.open('Aset Projek/Check In.png'), size=(20, 20))
        self.checkout_image = ctk.CTkImage(Image.open('Aset Projek/Check Out.png'), size=(20, 20))
        self.guestlist_image = ctk.CTkImage(Image.open('Aset Projek/Guest List.png'), size=(20, 20))
        self.guesthistory_image = ctk.CTkImage(Image.open('Aset Projek/Guest History.png'), size=(20, 20))
        self.roomservice_image = ctk.CTkImage(Image.open('Aset Projek/Room Service.png'), size=(20, 20))
        self.about_image =  ctk.CTkImage(Image.open('Aset Projek/About.png'), size=(20, 20))
        self.user_image = ctk.CTkImage(Image.open('Aset Projek/User.png'), size=(25, 25))
        self.user2_image = ctk.CTkImage(Image.open('Aset Projek/User2.png'), size=(30, 30))
        self.vacantready_image = ctk.CTkImage(Image.open('Aset Projek/Vacant Ready.png'), size=(310, 207))
        self.occupiedrooms_image = ctk.CTkImage(Image.open('Aset Projek/Occupied Rooms.png'), size=(310, 207))
        self.vacantdirty_image = ctk.CTkImage(Image.open('Aset Projek/Vacant Dirty.png'), size=(310, 207))
        self.requiringservice_image = ctk.CTkImage(Image.open('Aset Projek/Requiring Service.png'), size=(310, 207))
        self.rightarrow_image = ctk.CTkImage(Image.open('Aset Projek/Right Arrow.png'), size=(10, 10))
        self.downarrow_image = ctk.CTkImage(Image.open('Aset Projek/Down Arrow.png'), size=(10, 10))
        self.singleroom_image = ctk.CTkImage(Image.open('Aset Projek/Single Room.png'), size=(305, 264))
        self.doubleroom_image = ctk.CTkImage(Image.open('Aset Projek/Double Room.png'), size=(305, 264))
        self.suiteroom_image = ctk.CTkImage(Image.open('Aset Projek/Suite Room.png'), size=(305, 264))
        self.presidentsuiteroom_image = ctk.CTkImage(Image.open('Aset Projek/President Suite Room.png'), size=(305, 264))
        self.back_image = ctk.CTkImage(Image.open('Aset Projek/Back.png'), size=(40, 40))
        self.foodservice_image = ctk.CTkImage(Image.open('Aset Projek/Food and Drink Service.png'), size=(405,351))
        self.repairingservice_image = ctk.CTkImage(Image.open('Aset Projek/Repairing Service.png'), size=(405,351))
        self.cleaningservice_image = ctk.CTkImage(Image.open('Aset Projek/Cleaning Service.png'), size=(405,351))
        self.logout_image = ctk.CTkImage(Image.open('Aset Projek/Logout.png'), size=(20,20))

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        # FRAMES

        self.sidebar_frame = ctk.CTkFrame(self, fg_color='#1F1F27', bg_color='#0C0B10', border_color='#1B1B22', corner_radius=40, border_width=5)
        self.headbar_frame = ctk.CTkFrame(self, fg_color='#242531', bg_color='#0C0B10', corner_radius=30, border_color='#1F1F27', border_width=5)
        self.main_frame_dashboard = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_singleroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_doubleroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_suiteroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_presidentsuiteroom = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_identityformsingle = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_identityformdouble = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_identityformsuite = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkin_identityformpresidentsuite = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_checkin_identityformsingle = ctk.CTkFrame(self.main_frame_checkin_identityformsingle, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_identityformdouble = ctk.CTkFrame(self.main_frame_checkin_identityformdouble, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_identityformsuite = ctk.CTkFrame(self.main_frame_checkin_identityformsuite, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_identityformpresidentsuite = ctk.CTkFrame(self.main_frame_checkin_identityformpresidentsuite, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_singleroom = ctk.CTkFrame(self.main_frame_checkin_singleroom, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_doubleroom = ctk.CTkFrame(self.main_frame_checkin_doubleroom, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_suiteroom = ctk.CTkFrame(self.main_frame_checkin_suiteroom, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkin_presidentsuiteroom = ctk.CTkFrame(self.main_frame_checkin_presidentsuiteroom, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_guestlist = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_guestlist = ctk.CTkFrame(self.main_frame_guestlist, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_guesthistory = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_guesthistory = ctk.CTkFrame(self.main_frame_guesthistory, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_roomservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_foodservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_foodservice_menu = ctk.CTkFrame(self.main_frame_foodservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_foodservice_order = ctk.CTkFrame(self.main_frame_foodservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_repairingservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_cleaningservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_about = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_dashboard_roomstatus = ctk.CTkFrame(self.main_frame_dashboard, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_scrollframe_dashboard_roomstatus = ctk.CTkScrollableFrame(self.main_frame_dashboard_roomstatus, width=1150, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        
        self.sidebar_frame.grid(row=1, column=0, rowspan=3, padx=(30,20), pady=(10,25), sticky='nsew')
        self.headbar_frame.grid(row=0, column=0, columnspan=4, padx=30, pady=20, sticky='news')
        self.main_frame_dashboard.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_singleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_doubleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_suiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_presidentsuiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_identityformsingle.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_identityformdouble.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_identityformsuite.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_checkin_identityformpresidentsuite.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_framebar_checkin_identityformsingle.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_identityformdouble.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_identityformsuite.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_identityformpresidentsuite.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_singleroom.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_doubleroom.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_suiteroom.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_framebar_checkin_presidentsuiteroom.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=10, pady=(0,0), sticky='news')
        self.main_frame_guestlist.grid(row=1, column=1, rowspan=3, ipady=300, padx=0, pady=0, sticky='news')
        self.main_frame_guesthistory.grid(row=1, column=1, rowspan=3, ipady=300, padx=0, pady=0, sticky='news')
        self.main_framebar_guestlist.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=0, pady=(5,0), sticky='news')
        self.main_framebar_guesthistory.grid(row=1, column=0, columnspan=10, padx=(10,10), ipady=0, pady=(5,0), sticky='news')
        self.main_frame_roomservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_frame_foodservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_framebar_foodservice_menu.grid(row=1, column=0, padx=(10,10), pady=(0,0), sticky='news')        
        self.main_framebar_foodservice_order.grid(row=1, column=1, padx=(20,10), pady=(0,0), sticky='news')        
        self.main_frame_repairingservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_frame_cleaningservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_frame_about.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_dashboard_roomstatus.grid(row=2, column=0, rowspan=1, columnspan=4, padx=(9,37), pady=5, ipady=10, sticky='news')
        self.main_scrollframe_dashboard_roomstatus.grid(row=1, column=0, columnspan=10, padx=(17.5,10), ipady=15, sticky='news')

        self.headbar_frame.grid_columnconfigure(1, weight=1)
        self.main_frame_dashboard.grid_columnconfigure(3, weight=1)
        self.main_frame_checkin.grid_columnconfigure(3, weight=1)        

        # WIDGETS

        # SIDEBAR WIDGETS
        self.sidebar_label_mainnav = ctk.CTkButton(self.sidebar_frame, corner_radius=25, width=180, height=45, text="Main Nav", font=ctk.CTkFont('Mona-Sans Bold', 20), fg_color='#19191F', bg_color='transparent', text_color="#D2D2DD", hover_color='#191922', border_color='#1B1B22', border_width=4)
        self.sidebar_button_dashboard = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Dashboard", font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.dashboard_image, command=self.dashboard_menu)
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.rightarrow_image, compound='left', command=self.expand_button)
        self.sidebar_button_checkin = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check In", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkin_image, command=self.checkin_menu)
        self.sidebar_button_checkout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check Out", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkout_image)
        self.sidebar_button_guestlist = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Guest List", font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.guestlist_image, command=self.guestlist_menu)
        self.sidebar_button_guesthistory = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Guest History", font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.guesthistory_image, command=self.guesthistory_menu)
        self.sidebar_button_roomservice = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Room Services", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.roomservice_image, command=self.roomservice_menu)
        self.sidebar_button_about = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="About", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.about_image, command=self.about_menu)

        self.sidebar_label_mainnav.grid(row=0, column=0, ipadx=0, pady=15, ipady=0)
        self.sidebar_button_dashboard.grid(row=1, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_guestlist.grid(row=3, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_guesthistory.grid(row=4, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_roomservice.grid(row=5, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=6, column=0, padx=20, pady=5, sticky='news')

        # HEADBAR WIDGETS

        self.headbar_logo_label = ctk.CTkLabel(self.headbar_frame, text="", image=self.logo_image)
        self.headbar_button_profile = ctk.CTkButton(self.headbar_frame, corner_radius=30, width=50, height=45, image=self.user_image, text="Profile", font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", command=self.profile_menu)
        self.headbar_logo_label.grid(row=0, column=0, padx=30, pady=0, ipadx=25)
        self.headbar_button_profile.grid(row=0, column=6, padx=12, pady=10)
        self.headbar_clock_label = ctk.CTkButton(self.headbar_frame, font=ctk.CTkFont('Mona-Sans', 20), fg_color='#19191F', bg_color='transparent', text_color="#D2D2DD", hover_color='#191922', border_color='#1B1B22', border_width=4, corner_radius=20)
        self.headbar_clock_label.grid(row=0, column=5, padx=(0,10), pady=10)
        self.current_time()

        # DASHBOARD WIDGET

        self.main_dashboard_heading_label = ctk.CTkLabel(self.main_frame_dashboard, text="Dashboard", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_dashboard_desc_label =  ctk.CTkLabel(self.main_frame_dashboard, text="Welcome to Hotel Management System  |  by Kelompok 4", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_dashboard_heading_label.grid(row=0, column=0, pady=5, sticky='news')
        self.main_dashboard_desc_label.place(x=580, y=43, anchor='center')

        self.main_dashboard_vacantrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_occupiedrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_vacatedrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_requiringservice_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
       
        self.main_dashboard_vacantrooms_label = ctk.CTkLabel(self.main_dashboard_vacantrooms_frame, text='\n\n                   30', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacantready_image)
        self.main_dashboard_occupiedrooms_label = ctk.CTkLabel(self.main_dashboard_occupiedrooms_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.occupiedrooms_image)
        self.main_dashboard_vacatedrooms_label = ctk.CTkLabel(self.main_dashboard_vacatedrooms_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacantdirty_image)
        self.main_dashboard_requiringservice_label = ctk.CTkLabel(self.main_dashboard_requiringservice_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.requiringservice_image)
        
        self.main_dashboard_vacantrooms_frame.grid(row=1, column=0, pady=0, sticky='news')
        self.main_dashboard_occupiedrooms_frame.grid(row=1, column=1, pady=0, sticky='news')
        self.main_dashboard_vacatedrooms_frame.grid(row=1, column=2, pady=0, sticky='news')
        self.main_dashboard_requiringservice_frame.grid(row=1, column=3, pady=0, sticky='news')
        
        self.main_dashboard_vacantrooms_label.grid(row=0, column=0)
        self.main_dashboard_occupiedrooms_label.grid(row=0, column=0)
        self.main_dashboard_vacatedrooms_label.grid(row=0, column=0)
        self.main_dashboard_requiringservice_label.grid(row=0, column=0)  
        
        # DASHBOARD ROOM STATUS WIDGET

        self.main_dashboard_roomstatus_frame = ctk.CTkButton(self.main_frame_dashboard_roomstatus, corner_radius=25, width=180, height=45, text="Room Status", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_dashboard_roomstatus_frame.grid(row=0, column=0, columnspan=10, padx=(20,12), pady=(15,20), sticky='news')

        # 1-10
        self.room01_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room02_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room03_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room04_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room05_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room06_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room07_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room08_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room09_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room10_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room11_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room12_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room13_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room14_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room15_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room16_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room17_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room18_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room19_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room20_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room21_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room22_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room23_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room24_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room25_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room26_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room27_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room28_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room29_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        self.room30_frame = ctk.CTkFrame(self.main_scrollframe_dashboard_roomstatus, width=94, height=125, fg_color='#242531', border_color='#1E1F29', border_width=3, corner_radius=20)
        
        self.room01_frame_indicator = ctk.CTkFrame(self.room01_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room02_frame_indicator = ctk.CTkFrame(self.room02_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) #3C58F7
        self.room03_frame_indicator = ctk.CTkFrame(self.room03_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) #9031D3
        self.room04_frame_indicator = ctk.CTkFrame(self.room04_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) #B52483
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
        
        self.room01_frame_status = ctk.CTkLabel(self.room01_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room02_frame_status = ctk.CTkLabel(self.room02_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room03_frame_status = ctk.CTkLabel(self.room03_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room04_frame_status = ctk.CTkLabel(self.room04_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room05_frame_status = ctk.CTkLabel(self.room05_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room06_frame_status = ctk.CTkLabel(self.room06_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room07_frame_status = ctk.CTkLabel(self.room07_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room08_frame_status = ctk.CTkLabel(self.room08_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room09_frame_status = ctk.CTkLabel(self.room09_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room10_frame_status = ctk.CTkLabel(self.room10_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room11_frame_status = ctk.CTkLabel(self.room11_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room12_frame_status = ctk.CTkLabel(self.room12_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room13_frame_status = ctk.CTkLabel(self.room13_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room14_frame_status = ctk.CTkLabel(self.room14_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room15_frame_status = ctk.CTkLabel(self.room15_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room16_frame_status = ctk.CTkLabel(self.room16_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room17_frame_status = ctk.CTkLabel(self.room17_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room18_frame_status = ctk.CTkLabel(self.room18_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room19_frame_status = ctk.CTkLabel(self.room19_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room20_frame_status = ctk.CTkLabel(self.room20_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room21_frame_status = ctk.CTkLabel(self.room21_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room22_frame_status = ctk.CTkLabel(self.room22_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room23_frame_status = ctk.CTkLabel(self.room23_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room24_frame_status = ctk.CTkLabel(self.room24_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room25_frame_status = ctk.CTkLabel(self.room25_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room26_frame_status = ctk.CTkLabel(self.room26_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room27_frame_status = ctk.CTkLabel(self.room27_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room28_frame_status = ctk.CTkLabel(self.room28_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room29_frame_status = ctk.CTkLabel(self.room29_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
        self.room30_frame_status = ctk.CTkLabel(self.room30_frame, text='Ready', font=ctk.CTkFont('Mona-Sans semiBold', 14), text_color='#B6B6C6')
      
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
       
        self.room01_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room02_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room03_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room04_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room05_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room06_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room07_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room08_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room09_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room10_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room11_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room12_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')    
        self.room13_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room14_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room15_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room16_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room17_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')        
        self.room18_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room19_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room20_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room21_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room22_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room23_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room24_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room25_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room26_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room27_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room28_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room29_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
        self.room30_frame_indicator.place(relx=0.5, rely=0.85, anchor='center')
       
        self.room01_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room02_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room03_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room04_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room05_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room06_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room07_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room08_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room09_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room10_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room11_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room12_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room13_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room14_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room15_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room16_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room17_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room18_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room19_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room20_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room21_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room22_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room23_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room24_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room25_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room26_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room27_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room28_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room29_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        self.room30_frame_status.place(relx=0.5, rely=0.15, anchor='center')
        
        self.room01_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room02_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room03_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room04_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room05_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room06_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room07_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room08_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room09_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room10_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room11_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room12_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room13_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room14_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room15_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room16_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room17_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room18_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room19_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room20_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room21_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room22_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room23_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room24_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room25_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room26_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room27_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room28_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room29_frame_label.place(relx=0.5, rely=0.5, anchor='center')
        self.room30_frame_label.place(relx=0.5, rely=0.5, anchor='center')
     

       # CHECK IN WIDGET

        self.main_checkin_heading_label = ctk.CTkLabel(self.main_frame_checkin, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_heading_label.grid(row=0, column=0, pady=(5,5), padx=(20,60), sticky='news')
        self.main_checkin_desc_label =  ctk.CTkLabel(self.main_frame_checkin, text="Choose the room type", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_desc_label.place(x=355, y=43, anchor='center')

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
      
        self.main_checkin_singleroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#FFDC99', border_width=2, anchor="center", command=self.singleroom_menu)
        self.main_checkin_doubleroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#CE5700', border_width=2, anchor="center", command=self.doubleroom_menu)
        self.main_checkin_suiteroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#BBCDCA', border_width=2, anchor="center", command=self.suiteroom_menu)
        self.main_checkin_presidentsuiteroom_button = ctk.CTkButton(self.main_frame_checkin, corner_radius=30, width=50, height=45, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#FFB800', border_width=2, anchor="center", command=self.presidentsuiteroom_menu)

        self.main_checkin_singleroom_frame.grid(row=1, column=0, pady=0, sticky='news')
        self.main_checkin_doubleroom_frame.grid(row=1, column=1, pady=0, sticky='news')
        self.main_checkin_suiteroom_frame.grid(row=1, column=2, pady=0, sticky='news')
        self.main_checkin_presidentsuiteroom_frame.grid(row=1, column=3, pady=0, sticky='news')
        
        self.main_checkin_singleroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_doubleroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_suiteroom_label.grid(row=0, column=0, padx=3)
        self.main_checkin_presidentsuiteroom_label.grid(row=0, padx=3)

        self.main_checkin_singleroom_available_label.place(x=155, y=350, anchor='center')
        self.main_checkin_doubleroom_available_label.place(x=465, y=350, anchor='center')
        self.main_checkin_suiteroom_available_label.place(x=775, y=350, anchor='center')
        self.main_checkin_presidentsuiteroom_available_label.place(x=1085, y=350, anchor='center')

        self.main_checkin_singleroom_button.grid(row=2, column=0, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_doubleroom_button.grid(row=2, column=1, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_suiteroom_button.grid(row=2, column=2, padx=(40,40), pady=30, sticky='news')
        self.main_checkin_presidentsuiteroom_button.grid(row=2, column=3, padx=(40,65), pady=30, sticky='news')

        # CHECK IN SINGLE ROOM WIDGET

        self.main_checkin_heading_label = ctk.CTkLabel(self.main_frame_checkin_singleroom, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_heading_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_singleroom_desc_label =  ctk.CTkLabel(self.main_frame_checkin_singleroom, text='Pick an available room', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_singleroom_desc_label.place(x=415, y=45, anchor='center')
        self.main_checkin_back = ctk.CTkButton(self.main_frame_checkin_singleroom, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.checkin_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')

        self.main_checkin_singleroom_frame = ctk.CTkButton(self.main_framebar_checkin_singleroom, corner_radius=25, width=180, height=45, text="Available Single Room",  text_color="#FFDC99", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=3)
        self.main_checkin_singleroom_frame.grid(row=0, column=0, columnspan=10, padx=(20,20), pady=(15,5), sticky='news')

        self.room01_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='01', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(1))
        self.room02_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='02', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(2))
        self.room03_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='03', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(3))
        self.room04_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='04', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(4))
        self.room05_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='05', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(5))
        self.room06_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='06', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(6))
        self.room07_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='07', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(7))
        self.room08_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='08', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(8))
        self.room09_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='09', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(9))
        self.room10_button = ctk.CTkButton(self.main_framebar_checkin_singleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='10', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_singleroom(10))

        self.room01_button.grid(row=1, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room02_button.grid(row=1, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room03_button.grid(row=1, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room04_button.grid(row=1, column=3, padx=(0,15), pady=(15,0), sticky='news')
        self.room05_button.grid(row=1, column=4, padx=(0,20), pady=(15,0), sticky='news')
        self.room06_button.grid(row=2, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room07_button.grid(row=2, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room08_button.grid(row=2, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room09_button.grid(row=2, column=3, padx=(0,15), pady=(15,0), sticky='news')
        self.room10_button.grid(row=2, column=4, padx=(0,20), pady=(15,0), sticky='news')

        # CHECK IN DOUBLE ROOM WIDGET

        self.main_checkin_heading_label = ctk.CTkLabel(self.main_frame_checkin_doubleroom, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_heading_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_doubleroom_desc_label =  ctk.CTkLabel(self.main_frame_checkin_doubleroom, text='Pick an available room', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_doubleroom_desc_label.place(x=415, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_doubleroom, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.checkin_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')

        self.main_checkin_doubleroom_frame = ctk.CTkButton(self.main_framebar_checkin_doubleroom, corner_radius=25, width=180, height=45, text="Available Double Room", text_color="#CE5700", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=3)
        self.main_checkin_doubleroom_frame.grid(row=0, column=0, columnspan=10, padx=(20,20), pady=(15,5), sticky='news')

        self.room11_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='11', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(11))
        self.room12_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='12', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(12))
        self.room13_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='13', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(13))
        self.room14_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='14', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(14))
        self.room15_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='15', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(15))
        self.room16_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='16', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(16))
        self.room17_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='17', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(17))
        self.room18_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='18', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(18))
        self.room19_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='19', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(19))
        self.room20_button = ctk.CTkButton(self.main_framebar_checkin_doubleroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='20', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_doubleroom(20))

        self.room11_button.grid(row=1, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room12_button.grid(row=1, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room13_button.grid(row=1, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room14_button.grid(row=1, column=3, padx=(0,15), pady=(15,0), sticky='news')
        self.room15_button.grid(row=1, column=4, padx=(0,20), pady=(15,0), sticky='news')
        self.room16_button.grid(row=2, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room17_button.grid(row=2, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room18_button.grid(row=2, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room19_button.grid(row=2, column=3, padx=(0,15), pady=(15,0), sticky='news')
        self.room20_button.grid(row=2, column=4, padx=(0,20), pady=(15,0), sticky='news')

        self.room11_button.configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans ExtraBold', 25), text_color='#FFFFFF')

        # CHECK IN SUITE ROOM WIDGET

        self.main_checkin_heading_label = ctk.CTkLabel(self.main_frame_checkin_suiteroom, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_heading_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_suiteroom_desc_label =  ctk.CTkLabel(self.main_frame_checkin_suiteroom, text='Pick an available room', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_suiteroom_desc_label.place(x=415, y=45, anchor='center')
        self.main_checkin_back2 =  ctk.CTkButton(self.main_frame_checkin_suiteroom, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.checkin_menu)
        self.main_checkin_back2.place(x=25, y=33, anchor='center')

        self.main_checkin_suiteroom_frame = ctk.CTkButton(self.main_framebar_checkin_suiteroom, corner_radius=25, width=180, height=45, text="Available Suite Room", text_color="#BBCDCA",font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=3)
        self.main_checkin_suiteroom_frame.grid(row=0, column=0, columnspan=10, padx=(20,20), pady=(15,5), sticky='news')

        self.room21_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='21', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(21))
        self.room22_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='22', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(22))
        self.room23_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='23', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(23))
        self.room24_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='24', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(24))
        self.room25_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='25', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(25))
        self.room26_button = ctk.CTkButton(self.main_framebar_checkin_suiteroom, width=225, height=155, fg_color='#242531', corner_radius=25, text='26', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_suiteroom(26))
       
        self.room21_button.grid(row=1, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room22_button.grid(row=1, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room23_button.grid(row=1, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room24_button.grid(row=1, column=3, padx=(0,15), pady=(15,0), sticky='news')
        self.room25_button.grid(row=1, column=4, padx=(0,20), pady=(15,0), sticky='news')
        self.room26_button.grid(row=2, column=0, padx=(20,15), pady=(15,0), sticky='news')
        
        self.room21_button.configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans ExtraBold', 25), text_color='#FFFFFF')
       
         # CHECK IN PRESIDENT SUITE ROOM WIDGET

        self.main_checkin_heading_label = ctk.CTkLabel(self.main_frame_checkin_presidentsuiteroom, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_heading_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_presidentsuiteroom_desc_label =  ctk.CTkLabel(self.main_frame_checkin_presidentsuiteroom, text='Pick an available room', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_presidentsuiteroom_desc_label.place(x=415, y=45, anchor='center')
        self.main_checkin_back = ctk.CTkButton(self.main_frame_checkin_presidentsuiteroom, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.checkin_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')

        self.main_checkin_presidentroom_frame = ctk.CTkButton(self.main_framebar_checkin_presidentsuiteroom, corner_radius=25, width=180, height=45, text="Available President Suite Room", text_color="#FFB800",font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=3)
        self.main_checkin_presidentroom_frame.grid(row=0, column=0, columnspan=10, padx=(20,20), pady=(15,5), sticky='news')

        self.room27_button = ctk.CTkButton(self.main_framebar_checkin_presidentsuiteroom, width=285, height=173, fg_color='#242531', corner_radius=25, text='27', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_presidentsuiteroom(27))
        self.room28_button = ctk.CTkButton(self.main_framebar_checkin_presidentsuiteroom, width=285, height=173, fg_color='#242531', corner_radius=25, text='28', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_presidentsuiteroom(28))
        self.room29_button = ctk.CTkButton(self.main_framebar_checkin_presidentsuiteroom, width=285, height=173, fg_color='#242531', corner_radius=25, text='29', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_presidentsuiteroom(29))
        self.room30_button = ctk.CTkButton(self.main_framebar_checkin_presidentsuiteroom, width=285, height=173, fg_color='#242531', corner_radius=25, text='30', font=ctk.CTkFont('Mona-Sans ExtraBold', 60), text_color='#FFFFFF', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.identityform_presidentsuiteroom(30))
        
        self.room27_button.grid(row=1, column=0, padx=(20,15), pady=(15,0), sticky='news')
        self.room28_button.grid(row=1, column=1, padx=(0,15), pady=(15,0), sticky='news')
        self.room29_button.grid(row=1, column=2, padx=(0,15), pady=(15,0), sticky='news')
        self.room30_button.grid(row=1, column=3, padx=(0,20), pady=(15,0), sticky='news')
        
        self.room27_button.configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans ExtraBold', 25), text_color='#FFFFFF')


       # CHECK OUT WIDGET

         
       # GUEST LIST WIDGET

        self.main_guestlist_heading_label = ctk.CTkLabel(self.main_frame_guestlist, text="Guest List", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guestlist_heading_label.grid(row=0, column=0, rowspan=1, pady=(5,0), padx=(20,100), sticky='news')
        self.main_guestlist_desc_label =  ctk.CTkLabel(self.main_frame_guestlist, text='List of guests currently staying', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guestlist_desc_label.place(x=430, y=45, anchor='center')

        self.guest_list = [
            ["Room Number", "Room Type", "Guest Name", "Check In Date", 'Check Out Date',"Status"],
            ['01', 'Single','','','','Ready'],
            ['02', 'Single','','','','Ready'],
            ['03', 'Single','','','','Ready'],
            ['04', 'Single','','','','Ready'],
            ['05', 'Single','','','','Ready'],
            ['06', 'Single','','','','Ready'],
            ['07', 'Single','','','','Ready'],
            ['08', 'Single','','','','Ready'],        
            ['09', 'Single','','','','Ready'],        
            ['10', 'Single','','','','Ready'],        
            ['11', 'Double','','','','Ready'],        
            ['12', 'Double','','','','Ready'],        
            ['13', 'Double','','','','Ready'],        
            ['14', 'Double','','','','Ready'],        
            ['15', 'Double','','','','Ready'],        
            ['16', 'Double','','','','Ready'],        
            ['17', 'Double','','','','Ready'],        
            ['18', 'Double','','','','Ready'],        
            ['19', 'Double','','','','Ready'],        
            ['20', 'Double','','','','Ready'],        
            ['21', 'Suite','','','','Ready'],        
            ['22', 'Suite','','','','Ready'],        
            ['23', 'Suite','','','','Ready'],        
            ['24', 'Suite','','','','Ready'],        
            ['25', 'Suite','','','','Ready'],        
            ['26', 'Suite','','','','Ready'],        
            ['27', 'President Suite','','','','Ready'],        
            ['28', 'President Suite','','','','Ready'],        
            ['29', 'President Suite','','','','Ready'],        
            ['30', 'President Suite','','','','Ready'],        
        ]

        self.main_guestlist_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_guestlist, width=1200, height=550, fg_color='transparent')
        self.main_guestlist_scrollableframe.grid(row=1, column=0, pady=(15,15), padx=(10,0), columnspan=12, sticky='news')
        self.main_guestlist_table = CTkTable(self.main_guestlist_scrollableframe, font=ctk.CTkFont('Mona-Sans Bold', 14), values=self.guest_list, header_color='#4646DD', colors=['#131318', '#15151B'], border_color='#101016', corner_radius=0, border_width=2, color_phase='horizontal', wraplength=200)
        self.main_guestlist_table.pack(expand=True)
        self.main_guestlist_table.edit_column(0, width=130)
        self.main_guestlist_table.edit_column(1, width=150)
        self.main_guestlist_table.edit_column(2, width=400)
        self.main_guestlist_table.edit_column(3, width=150)
        self.main_guestlist_table.edit_column(4, width=150)
        self.main_guestlist_table.edit_column(5, width=200)

        # GUEST HISTORY WIDGET

        self.main_guesthistory_heading_label = ctk.CTkLabel(self.main_frame_guesthistory, text="Guest History", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guesthistory_heading_label.grid(row=0, column=0, rowspan=1, pady=(5,0), padx=(20,100), sticky='news')
        self.main_guesthistory_desc_label =  ctk.CTkLabel(self.main_frame_guesthistory, text="List of guest's history", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guesthistory_desc_label.place(x=475, y=45, anchor='center')

        self.guest_history = [
            ['Check In Date', 'Check Out Date', 'Guest Name', 'NIN', 'Mobile Phone Number','Email','Adress','Room Number'],
            ['31/07/05','02/08/05','Muhammad Shadiq Al-Fatiy','6471053011690007','082138140621','mshadiqaf@gmail.com','Perum. Papan Lestari, Jl. Sepinggan Asri Utara II RT 45, No.11', '01'],
            ['','','','','',''],
            ['','','','','',''],
            ['','','','','',''],
            ['','','','','',''],
            ['','','','','',''],
            ['','','','','',''],
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
            ['','','','','',''],        
        ]

        self.main_guesthistory_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_guesthistory, width=1200, height=550, fg_color='transparent')
        self.main_guesthistory_scrollableframe.grid(row=1, column=0, pady=(15,15), padx=(10,0), columnspan=12, sticky='news')
        self.main_guesthistory_table = CTkTable(self.main_guesthistory_scrollableframe, font=ctk.CTkFont('Mona-Sans Bold', 12), values=self.guest_history, header_color='#4646DD', colors=['#131318', '#15151B'], border_color='#101016', corner_radius=0, border_width=2, color_phase='horizontal', wraplength=200)
        self.main_guesthistory_table.pack(expand=True)
        self.main_guesthistory_table.edit_column(0, width=100)
        self.main_guesthistory_table.edit_column(1, width=110)
        self.main_guesthistory_table.edit_column(2, width=200)
        self.main_guesthistory_table.edit_column(3, width=130)
        self.main_guesthistory_table.edit_column(4, width=150)
        self.main_guesthistory_table.edit_column(5, width=170)
        self.main_guesthistory_table.edit_column(6, width=200)
        self.main_guesthistory_table.edit_column(7, width=120)
        
       # ROOM SERVICES WIDGET

        self.main_roomservice_heading_label = ctk.CTkLabel(self.main_frame_roomservice, text="Room Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_roomservice_heading_label.grid(row=0, column=0, pady=(5,5), padx=20, sticky='news')
        self.main_roomservice_desc_label =  ctk.CTkLabel(self.main_frame_roomservice, text='Choose the type of service', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_roomservice_desc_label.place(x=527.5, y=45, anchor='center')

        self.main_roomservice_foodservice_frame = ctk.CTkFrame(self.main_frame_roomservice, fg_color='transparent', width=300, height=200)
        self.main_roomservice_repairingservice_frame = ctk.CTkFrame(self.main_frame_roomservice, fg_color='transparent', width=300, height=200)
        self.main_roomservice_cleaningservice_frame = ctk.CTkFrame(self.main_frame_roomservice, fg_color='transparent', width=300, height=200)
        
        self.main_roomservice_foodservice_label = ctk.CTkLabel(self.main_roomservice_foodservice_frame, text="", image=self.foodservice_image)
        self.main_roomservice_repairingservice_label = ctk.CTkLabel(self.main_roomservice_repairingservice_frame, text="", image=self.repairingservice_image)
        self.main_roomservice_cleaningservice_label = ctk.CTkLabel(self.main_roomservice_cleaningservice_frame, text="", image=self.cleaningservice_image)

        self.main_roomservice_foodservice_button = ctk.CTkButton(self.main_frame_roomservice, corner_radius=30, width=50, height=60, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#121319', border_width=3, anchor="center", command=self.foodservice_menu)
        self.main_roomservice_repairingservice_button = ctk.CTkButton(self.main_frame_roomservice, corner_radius=30, width=50, height=60, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#121319', border_width=3, anchor="center", command=self.repairingservice_menu)
        self.main_roomservice_cleaningservice_button = ctk.CTkButton(self.main_frame_roomservice, corner_radius=30, width=50, height=60, text="Select", font=ctk.CTkFont('Mona-Sans', 20), fg_color='#191A22', text_color="#FFFFFF", hover_color='#4646DD', cursor='hand2', border_color='#121319', border_width=3, anchor="center", command=self.cleaningservice_menu)

        self.main_roomservice_foodservice_frame.grid(row=1, column=0, padx=0, sticky='news')
        self.main_roomservice_repairingservice_frame.grid(row=1, column=1, padx=0, sticky='news')
        self.main_roomservice_cleaningservice_frame.grid(row=1, column=2, padx=0, sticky='news')

        self.main_roomservice_foodservice_label.grid(row=0, column=0, padx=(0,5))
        self.main_roomservice_repairingservice_label.grid(row=0, column=0, padx=5)
        self.main_roomservice_cleaningservice_label.grid(row=0, column=0, padx=5)

        self.main_roomservice_foodservice_button.grid(row=2, column=0, padx=(40,40), pady=5, sticky='news')
        self.main_roomservice_repairingservice_button.grid(row=2, column=1, padx=(40,40), pady=5, sticky='news')
        self.main_roomservice_cleaningservice_button.grid(row=2, column=2, padx=(40,40), pady=5, sticky='news')

        # FOOD AND SERVICES WIDGET

        self.main_foodservice_heading_label = ctk.CTkLabel(self.main_frame_foodservice, text="Food & Drink Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_foodservice_heading_label.grid(row=0, column=0, pady=(5,5), padx=(80,0), sticky='news')
        self.main_foodservice_desc_label =  ctk.CTkLabel(self.main_frame_foodservice, text='Choose from the available food and beverages', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_foodservice_desc_label.place(x=855, y=45, anchor='center')
        self.main_foodservice_back = ctk.CTkButton(self.main_frame_foodservice, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.roomservice_menu)
        self.main_foodservice_back.place(x=25, y=33, anchor='center')

        self.main_foodservice_menu_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, fg_color='#191922', border_color='#171720', border_width=5, corner_radius=20)
        self.main_foodservice_appetizer_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_foodservice_menu, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        self.main_foodservice_maincourse_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_foodservice_menu, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        self.main_foodservice_dessert_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_foodservice_menu, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        self.main_foodservice_drinks_scrollableframe = ctk.CTkScrollableFrame(self.main_framebar_foodservice_menu, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        self.main_foodservice_appetizer_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Appetizer', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.appetizer_menu)
        self.main_foodservice_maincourse_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Main Course', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.maincourse_menu)
        self.main_foodservice_dessert_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Dessert', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.dessert_menu)
        self.main_foodservice_drinks_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Drinks', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.drinks_menu)

        self.main_foodservice_order_frame = ctk.CTkButton(self.main_framebar_foodservice_order, corner_radius=25, width=315, height=45, text="Order", text_color="#D9D9FF",font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=5)

        self.main_foodservice_menu_frame.grid(row=0, column=0, padx=(15,15), pady=(15,15), sticky='new')
        self.main_foodservice_appetizer_scrollableframe.grid(row=1, column=0, padx=(20,20), sticky='news')
        self.main_foodservice_appetizer_button.grid(row=0, column=0, padx=(10,5), pady=(10,10), sticky='news')
        self.main_foodservice_maincourse_button.grid(row=0, column=1, padx=(5,5), pady=(10,10), sticky='news')
        self.main_foodservice_dessert_button.grid(row=0, column=2, padx=(5,5), pady=(10,10), sticky='news')
        self.main_foodservice_drinks_button.grid(row=0, column=3, padx=(5,10), pady=(10,10), sticky='news')

        self.main_foodservice_order_frame.grid(row=0, column=0, columnspan=2, padx=(15,20), pady=(20,15), sticky='new')


        # ABOUT WIDGET

        self.main_about_heading_label = ctk.CTkLabel(self.main_frame_about, text="About", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_about_heading_label.grid(row=0, column=0, pady=(5,20), padx=20, sticky='news')

        self.main_about_logo = ctk.CTkLabel(self.main_frame_about, text='', image=self.logoshadow_image)
        self.main_about_logo.place(x=600, y=120, anchor='center')

        self.main_about_desc = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Medium', 15), text='"Hostay" merupakan sebuah program yang dirancang untuk membantu dan mempermudah\nresepsionis dalam melakukan pelayanan yang diberikan kepada tamu.\n\nDengan otomatisasi tugas-tugas seperti pemesanan, Check-in dan Check-out, dan manajemen inventaris.\n Sehingga hotel dapat mengelola operasinya dengan lebih efisien.')
        self.main_about_desc.place(x=600, y=240, anchor='center')

        self.main_about_incha = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Incha Raghil', text_color='#FFFFFF')
        self.main_about_shadiq = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Muhammad Shadiq Al-Fatiy', text_color='#FFFFFF')
        self.main_about_syahrul = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Syahrul Hidayat', text_color='#FFFFFF')
        self.main_about_bagas = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Muhammad Bagas Setiawan', text_color='#FFFFFF')
        self.main_about_khanza = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Khanza Nabila Tsabita', text_color='#FFFFFF')
        self.main_about_ajeng = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold Wide', 12), text='Ajeng Masayu Anjani Putri', text_color='#FFFFFF')

        self.main_about_incha_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Wide', 12), text='10231043', text_color='#D2D2DD')
        self.main_about_shadiq_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Wide', 12), text='11231065', text_color='#D2D2DD')
        self.main_about_syahrul_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Wide', 12), text='20231077', text_color='#D2D2DD')
        self.main_about_bagas_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Medium Wide', 12), text='10231061', text_color='#D2D2DD')
        self.main_about_khanza_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Medium Wide', 12), text='10231049', text_color='#D2D2DD')
        self.main_about_ajeng_nim = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans Medium Wide', 12), text='16231003', text_color='#D2D2DD')

        self.main_about_incha.place(x=300, y=380, anchor='center')
        self.main_about_shadiq.place(x=600, y=380, anchor='center')
        self.main_about_syahrul.place(x=900, y=380, anchor='center')
        self.main_about_khanza.place(x=430, y=450, anchor='center')
        self.main_about_ajeng.place(x=770, y=450, anchor='center')
        self.main_about_bagas.place(x=600, y=520, anchor='center')

        self.main_about_incha_nim.place(x=300, y=395, anchor='center')
        self.main_about_shadiq_nim.place(x=600, y=395, anchor='center')
        self.main_about_syahrul_nim.place(x=900, y=395, anchor='center')
        self.main_about_khanza_nim.place(x=430, y=465, anchor='center')
        self.main_about_ajeng_nim.place(x=770, y=465, anchor='center')
        self.main_about_bagas_nim.place(x=600, y=535, anchor='center')


        self.main_about_copyright = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold', 14), text='Copyright © 2023 Hostay', text_color='#FFFFFF')
        self.main_about_copyright.place(x=600, y=635, anchor='center')
        self.main_about_credit = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans', 12), text='by Kelompok 4', text_color='#4646DD', fg_color='transparent', bg_color='transparent')
        self.main_about_credit.place(x=600, y=655, anchor='center')





        self.select_frame('dashboard')
        self.select_foodservice_menu('appetizer')
    
    def select_frame(self, name):
        self.sidebar_button_dashboard.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'dashboard' else 'transparent')
        self.sidebar_button_checkinout.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkinout' else 'transparent')
        self.sidebar_button_checkin.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkin' or name == 'singleroom' or name == 'identityroomsingle' else 'transparent')
        self.sidebar_button_guestlist.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'guestlist' else 'transparent')
        self.sidebar_button_guesthistory.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'guesthistory' else 'transparent')
        self.sidebar_button_roomservice.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'roomservice' else 'transparent')
        self.sidebar_button_about.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'about' else 'transparent')
        self.headbar_button_profile.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'profile' else 'transparent')

        if name == "dashboard":
            self.main_frame_dashboard.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_dashboard.grid_forget()
        if name == "checkin":
            self.main_frame_checkin.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin.grid_forget()
        if name == "singleroom":
            self.main_frame_checkin_singleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_singleroom.grid_forget()
        if name == "doubleroom":
            self.main_frame_checkin_doubleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_doubleroom.grid_forget()
        if name == "suiteroom":
            self.main_frame_checkin_suiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_suiteroom.grid_forget()
        if name == "presidentsuiteroom":
            self.main_frame_checkin_presidentsuiteroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_presidentsuiteroom.grid_forget()
        if name == "identityroomsingle":
            self.main_frame_checkin_identityformsingle.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')    
        else:
            self.main_frame_checkin_identityformsingle.grid_forget()
        if name == "identityroomdouble":
            self.main_frame_checkin_identityformdouble.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')    
        else:
            self.main_frame_checkin_identityformdouble.grid_forget()
        if name == "identityroomsuite":
            self.main_frame_checkin_identityformsuite.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')    
        else:
            self.main_frame_checkin_identityformsuite.grid_forget()
        if name == "identityroompresidentsuite":
            self.main_frame_checkin_identityformpresidentsuite.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')    
        else:
            self.main_frame_checkin_identityformpresidentsuite.grid_forget()       
        if name == "guestlist":
            self.main_frame_guestlist.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_guestlist.grid_forget()
        if name == "guesthistory":
            self.main_frame_guesthistory.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_guesthistory.grid_forget()
        if name == "roomservice":
            self.main_frame_roomservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_roomservice.grid_forget()
        if name == "foodservice":
            self.main_frame_foodservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_foodservice.grid_forget()
        if name == "repairingservice":
            self.main_frame_repairingservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_repairingservice.grid_forget()
        if name == "cleaningservice":
            self.main_frame_cleaningservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_cleaningservice.grid_forget()
        if name == "about":
            self.main_frame_about.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_about.grid_forget()
        
    def dashboard_menu(self):
        self.select_frame('dashboard')

    def checkin_menu(self):
        self.select_frame('checkin')    

    def singleroom_menu(self):
        self.select_frame('singleroom')

    def doubleroom_menu(self):
        self.select_frame('doubleroom')

    def suiteroom_menu(self):
        self.select_frame('suiteroom')

    def presidentsuiteroom_menu(self):
        self.select_frame('presidentsuiteroom')        

    def roomservice_menu(self):
        self.select_frame('roomservice')

    def foodservice_menu(self):
        self.select_frame('foodservice')

    def select_foodservice_menu(self, name):
        self.main_foodservice_appetizer_button.configure(self.main_foodservice_menu_frame, fg_color=('#3434A6') if name == 'appetizer' else '#242432')
        self.main_foodservice_maincourse_button.configure(self.main_foodservice_menu_frame, fg_color=('#3434A6') if name == 'maincourse' else '#242432')
        self.main_foodservice_dessert_button.configure(self.main_foodservice_menu_frame, fg_color=('#3434A6') if name == 'dessert' else '#242432')
        self.main_foodservice_drinks_button.configure(self.main_foodservice_menu_frame, fg_color=('#3434A6') if name == 'drinks' else '#242432')
        
        if name == "appetizer":
            self.main_foodservice_appetizer_scrollableframe.grid(row=1, column=0, padx=(20,20), sticky='news')
        else:
            self.main_foodservice_appetizer_scrollableframe.grid_forget()   
        if name == "maincourse":
            self.main_frame_checkin.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin.grid_forget()
        if name == "dessert":
            self.main_frame_checkin_singleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_singleroom.grid_forget()
        if name == "drinks":
            self.main_frame_checkin_doubleroom.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkin_doubleroom.grid_forget()

    def appetizer_menu(self):
        self.select_foodservice_menu('appetizer')

    def maincourse_menu(self):
        self.select_foodservice_menu('maincourse')
        
    def dessert_menu(self):
        self.select_foodservice_menu('dessert')

    def drinks_menu(self):
        self.select_foodservice_menu('drinks')            

    def repairingservice_menu(self):
        self.select_frame('repairingservice')

    def cleaningservice_menu(self):
        self.select_frame('cleaningservice')

    def guestlist_menu(self):
        self.select_frame('guestlist')

    def guesthistory_menu(self):
        self.select_frame('guesthistory')

    def about_menu(self):
        self.select_frame('about')

    def identityform_singleroom(self, roomnumber):
        self.select_frame('identityroomsingle')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformsingle, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformsingle, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformsingle, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.singleroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_button = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformsingle, text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
        
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guesttotal_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Guest Total", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_guesttotal_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['2', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkTextbox(self.main_framebar_checkin_identityformsingle, width=341.5, height=80, text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=15, activate_scrollbars=True, wrap='word')
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_button.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_checkin_button.grid(row=9, column=2, sticky='ne', padx=(0,30), pady=(120,10))
        self.identityform_firstname_label.grid(row=2, column=0, sticky='news', padx=(55,0), pady=(20,0))
        self.identityform_lastname_label.grid(row=4, column=0, sticky='news', padx=(55,0))
        self.identityform_age_label.grid(row=6, column=0, sticky='news', padx=(55,0))
        self.identityform_gender_label.grid(row=8, column=0, sticky='news', padx=(55,0))
        self.identityform_nin_label.grid(row=2, column=1, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_nohandphone_label.grid(row=4, column=1, sticky='news', padx=(85,0))
        self.identityform_email_label.grid(row=6, column=1, sticky='news', padx=(85,0))
        self.identityform_address_label.grid(row=8, column=1, sticky='news', padx=(85,0))
        self.identityform_checkindate_label.grid(row=2, column=2, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_checkoutdate_label.grid(row=4, column=2, sticky='news', padx=(85,20))
        self.identityform_deposit_label.grid(row=6, column=2, sticky='news', padx=(85,20))
        self.identityform_guestnote_label.grid(row=8, column=2, sticky='news', padx=(85,20))

        self.identityform_firstname_entry.grid(row=3, column=0, sticky='new', padx=(35,0), pady=(3,15))
        self.identityform_lastname_entry.grid(row=5, column=0, sticky='new', padx=(35,0), pady=(3,15)) 
        self.identityform_age_entry.grid(row=7, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_gender_entry.grid(row=9, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_nin_entry.grid(row=3, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_nohandphone_entry.grid(row=5, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_email_entry.grid(row=7, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_address_entry.grid(row=9, column=1, sticky='new', padx=(65,0), pady=(3,15))
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))
        
        
    def identityform_doubleroom(self, roomnumber):
        self.select_frame('identityroomdouble')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformdouble, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformdouble, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformdouble, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.doubleroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_button = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformdouble, text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
        
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guesttotal_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Guest Total", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_guesttotal_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['2', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkTextbox(self.main_framebar_checkin_identityformdouble, width=341.5, height=80, text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=15, activate_scrollbars=True, wrap='word')
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_button.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_checkin_button.grid(row=9, column=2, sticky='ne', padx=(0,30), pady=(120,10))
        self.identityform_firstname_label.grid(row=2, column=0, sticky='news', padx=(55,0), pady=(20,0))
        self.identityform_lastname_label.grid(row=4, column=0, sticky='news', padx=(55,0))
        self.identityform_age_label.grid(row=6, column=0, sticky='news', padx=(55,0))
        self.identityform_gender_label.grid(row=8, column=0, sticky='news', padx=(55,0))
        self.identityform_nin_label.grid(row=2, column=1, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_nohandphone_label.grid(row=4, column=1, sticky='news', padx=(85,0))
        self.identityform_email_label.grid(row=6, column=1, sticky='news', padx=(85,0))
        self.identityform_address_label.grid(row=8, column=1, sticky='news', padx=(85,0))
        self.identityform_checkindate_label.grid(row=2, column=2, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_checkoutdate_label.grid(row=4, column=2, sticky='news', padx=(85,20))
        self.identityform_deposit_label.grid(row=6, column=2, sticky='news', padx=(85,20))
        self.identityform_guestnote_label.grid(row=8, column=2, sticky='news', padx=(85,20))

        self.identityform_firstname_entry.grid(row=3, column=0, sticky='new', padx=(35,0), pady=(3,15))
        self.identityform_lastname_entry.grid(row=5, column=0, sticky='new', padx=(35,0), pady=(3,15)) 
        self.identityform_age_entry.grid(row=7, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_gender_entry.grid(row=9, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_nin_entry.grid(row=3, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_nohandphone_entry.grid(row=5, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_email_entry.grid(row=7, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_address_entry.grid(row=9, column=1, sticky='new', padx=(65,0), pady=(3,15))
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))

    def identityform_suiteroom(self, roomnumber):
        self.select_frame('identityroomsuite')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformsuite, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformsuite, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformsuite, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.suiteroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_button = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformsuite, text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
        
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guesttotal_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Guest Total", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_guesttotal_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['2', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkTextbox(self.main_framebar_checkin_identityformsuite, width=341.5, height=80, text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=15, activate_scrollbars=True, wrap='word')
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_button.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_checkin_button.grid(row=9, column=2, sticky='ne', padx=(0,30), pady=(120,10))
        self.identityform_firstname_label.grid(row=2, column=0, sticky='news', padx=(55,0), pady=(20,0))
        self.identityform_lastname_label.grid(row=4, column=0, sticky='news', padx=(55,0))
        self.identityform_age_label.grid(row=6, column=0, sticky='news', padx=(55,0))
        self.identityform_gender_label.grid(row=8, column=0, sticky='news', padx=(55,0))
        self.identityform_nin_label.grid(row=2, column=1, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_nohandphone_label.grid(row=4, column=1, sticky='news', padx=(85,0))
        self.identityform_email_label.grid(row=6, column=1, sticky='news', padx=(85,0))
        self.identityform_address_label.grid(row=8, column=1, sticky='news', padx=(85,0))
        self.identityform_checkindate_label.grid(row=2, column=2, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_checkoutdate_label.grid(row=4, column=2, sticky='news', padx=(85,20))
        self.identityform_deposit_label.grid(row=6, column=2, sticky='news', padx=(85,20))
        self.identityform_guestnote_label.grid(row=8, column=2, sticky='news', padx=(85,20))

        self.identityform_firstname_entry.grid(row=3, column=0, sticky='new', padx=(35,0), pady=(3,15))
        self.identityform_lastname_entry.grid(row=5, column=0, sticky='new', padx=(35,0), pady=(3,15)) 
        self.identityform_age_entry.grid(row=7, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_gender_entry.grid(row=9, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_nin_entry.grid(row=3, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_nohandphone_entry.grid(row=5, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_email_entry.grid(row=7, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_address_entry.grid(row=9, column=1, sticky='new', padx=(65,0), pady=(3,15))
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))
        
    def identityform_presidentsuiteroom(self, roomnumber):
        self.select_frame('identityroompresidentsuite')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformpresidentsuite, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformpresidentsuite, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformpresidentsuite, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.presidentsuiteroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_button = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformpresidentsuite, text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
        
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guesttotal_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Guest Total", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_guesttotal_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['2', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkTextbox(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=80, text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=15, activate_scrollbars=True, wrap='word')
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_button.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_checkin_button.grid(row=9, column=2, sticky='ne', padx=(0,30), pady=(120,10))
        self.identityform_firstname_label.grid(row=2, column=0, sticky='news', padx=(55,0), pady=(20,0))
        self.identityform_lastname_label.grid(row=4, column=0, sticky='news', padx=(55,0))
        self.identityform_age_label.grid(row=6, column=0, sticky='news', padx=(55,0))
        self.identityform_gender_label.grid(row=8, column=0, sticky='news', padx=(55,0))
        self.identityform_nin_label.grid(row=2, column=1, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_nohandphone_label.grid(row=4, column=1, sticky='news', padx=(85,0))
        self.identityform_email_label.grid(row=6, column=1, sticky='news', padx=(85,0))
        self.identityform_address_label.grid(row=8, column=1, sticky='news', padx=(85,0))
        self.identityform_checkindate_label.grid(row=2, column=2, sticky='news', padx=(85,20), pady=(20,0))
        self.identityform_checkoutdate_label.grid(row=4, column=2, sticky='news', padx=(85,20))
        self.identityform_deposit_label.grid(row=6, column=2, sticky='news', padx=(85,20))
        self.identityform_guestnote_label.grid(row=8, column=2, sticky='news', padx=(85,20))

        self.identityform_firstname_entry.grid(row=3, column=0, sticky='new', padx=(35,0), pady=(3,15))
        self.identityform_lastname_entry.grid(row=5, column=0, sticky='new', padx=(35,0), pady=(3,15)) 
        self.identityform_age_entry.grid(row=7, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_gender_entry.grid(row=9, column=0, sticky='new', padx=(35,0), pady=(3,17.5))
        self.identityform_nin_entry.grid(row=3, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_nohandphone_entry.grid(row=5, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_email_entry.grid(row=7, column=1, sticky='new', padx=(65,0), pady=(3,17.5))
        self.identityform_address_entry.grid(row=9, column=1, sticky='new', padx=(65,0), pady=(3,15))
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))
        
    def profile_menu(self):
        self.profile_frame = ctk.CTkFrame(self, width=180, height=140, fg_color='#242531', bg_color='#1E1F29', border_width=7, border_color='#1E1F29', corner_radius=20)
        self.profile_frame.grid(row=1,column=1, padx=(100,50), sticky='ne')
        self.headbar_button_profile = ctk.CTkButton(self.headbar_frame, corner_radius=30, width=50, height=45, image=self.user_image, text="Profile", font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", command=self.close_profile_frame)
        self.headbar_button_profile.grid(row=0, column=6, padx=12, pady=10)
        self.profile_logout_button = ctk.CTkButton(self.profile_frame, width=120, height=35, text='Logout', fg_color='#BF2BB5', image=self.logout_image, hover_color='#92218A', font=ctk.CTkFont('Mona-Sans SemiBold', 20), cursor='hand2', corner_radius=20, command=self.logout)
        self.profile_logout_button.place(relx=0.5, rely=0.75, anchor='center')
        self.profile_label_user = ctk.CTkButton(self.profile_frame, image=self.user2_image, text=usernameGlobal, font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", hover_color='#242531', text_color=("#FFFFFF"))
        self.profile_label_user.place(relx=0.5, rely=0.35, anchor='center')
        
    def close_profile_frame(self):
        self.profile_frame.grid_forget()
        self.headbar_button_profile = ctk.CTkButton(self.headbar_frame, corner_radius=30, width=50, height=45, image=self.user_image, text="Profile", font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", command=self.profile_menu)
        self.headbar_button_profile.grid(row=0, column=6, padx=12, pady=10)
    
    def logout(self):
        self.sidebar_frame.grid_forget()
        self.headbar_frame.grid_forget()
        self.main_frame_dashboard.grid_forget()
        self.main_frame_checkin.grid_forget()
        self.main_frame_checkin_singleroom.grid_forget()
        self.main_frame_checkin_doubleroom.grid_forget()
        self.main_frame_checkin_suiteroom.grid_forget()
        self.main_frame_checkin_presidentsuiteroom.grid_forget()
        self.main_framebar_checkin_singleroom.grid_forget()
        self.main_framebar_checkin_doubleroom.grid_forget()
        self.main_framebar_checkin_suiteroom.grid_forget()
        self.main_framebar_checkin_presidentsuiteroom.grid_forget()
        self.main_frame_guestlist.grid_forget()
        self.main_frame_roomservice.grid_forget()
        self.main_frame_about.grid_forget()
        self.main_frame_dashboard_roomstatus.grid_forget()
        self.main_scrollframe_dashboard_roomstatus.grid_forget()
        self.profile_frame.grid_forget()

        self.login_page = LoginPage(self)
        self.registration_page = RegistrationPage(self)
        self.show_login_page()

        self.login_page.regis_label_button.configure(command=self.show_registration_page)
        self.registration_page.login_label_button.configure(command=self.show_login_page)

    def expand_button(self):
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.downarrow_image, compound='left', command=self.close_button)
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_checkin.grid(row=3, column=0, padx=20, pady=0, sticky='ns')
        self.sidebar_button_checkout.grid(row=4, column=0, padx=20, pady=3, sticky='ns')
        self.sidebar_button_guestlist.grid(row=5, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_guesthistory.grid(row=6, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_roomservice.grid(row=7, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=8, column=0, padx=20, pady=5, sticky='ew')

    def close_button(self):
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.rightarrow_image, compound='left', command=self.expand_button)
        self.sidebar_button_checkin.grid_forget()
        self.sidebar_button_checkout.grid_forget()
        self.sidebar_button_checkinout.grid(row=2, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_guestlist.grid(row=3, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_guesthistory.grid(row=4, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_roomservice.grid(row=5, column=0, padx=20, pady=5, sticky='news')
        self.sidebar_button_about.grid(row=6, column=0, padx=20, pady=5, sticky='ew')

class LoginPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master, bg_color='#FFFFFF', fg_color='#FFFFFF', border_width=20, border_color='#FFFFFF', corner_radius=30, width=250, height=300)
        self.place(relx=0.5, rely=0.5, anchor='center')

        self.hide_eye = ctk.CTkImage(Image.open('Aset Projek/hide.png'), size=(17, 17))
        self.show_eye = ctk.CTkImage(Image.open('Aset Projek/show.png'), size=(17, 17))
        self.img_logo = ctk.CTkImage(Image.open('Aset Projek/Hostay Logo.png'), size=(140, 70))
    
        self.hostay_logo = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.hostay_logo.place(relx=0.5, rely=0.14, anchor='center')

        self.username_label = ctk.CTkLabel(self, text='Username', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.username_label.place(relx=0.24, rely=0.360, anchor='center')
        self.username_label_emoji = ctk.CTkLabel(self, text='👤', text_color='#000000')
        self.username_label_emoji.place(relx=0.41, rely=0.354, anchor='center')
        self.username_input = ctk.CTkEntry(self, width=200, placeholder_text='Masukkan Username', border_width=0)
        self.username_input.place(relx=0.5, rely=0.435, anchor='center')

        self.password_label = ctk.CTkLabel(self, text='Password', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.password_label.place(relx=0.24, rely=0.543, anchor='center')
        self.password_label_emoji = ctk.CTkLabel(self, text="🔐", text_color='#000000')
        self.password_label_emoji.place(relx=0.404, rely=0.535, anchor='center')
        self.password_input = ctk.CTkEntry(self, width=200, placeholder_text='Masukkan Password', show='*', border_width=0)
        self.password_input.place(relx=0.5, rely=0.617, anchor='center')

        
        self.show_password = ctk.CTkButton(self, width=20, height=20, fg_color='transparent', hover_color='#FFFFFF', text='', cursor='hand2', image=self.show_eye, command=self.ShowPassword)
        self.show_password.place(relx=0.966, rely=0.615, anchor='center')

        self.login_button = ctk.CTkButton(self, width=223, height=30, text='L O G I N', text_color='#FFFFFF', fg_color='#1f538d', hover_color='#0E4480', cursor='hand2', font=('Mona-Sans ExtraBold Wide', 13), border_width=2.5, border_color='#0E4480', corner_radius=25, command=self.Login)
        self.login_button.place(relx=0.5, rely=0.84, anchor='center')

        self.regis_label = ctk.CTkLabel(self, text='Anda belum memiki akun?', text_color='#000000', font=('Mona-Sans', 10.5))
        self.regis_label.place(relx=0.313, rely=0.96, anchor='center')
        
        self.regis_label_button = ctk.CTkButton(self, width=14, height=1, text='Registrasi disini', text_color='#004aad', border_width=0, fg_color='#FFFFFF', hover_color='#FFFFFF', cursor='hand2', font=('Mona-Sans', 11.5))
        self.regis_label_button.place(relx=0.782, rely=0.96, anchor='center')

        self.warning_label = CTkLabel(self, text="", font=CTkFont('Mona-Sans', 13), text_color='green')
        self.warning_label.place(relx=0.5, rely=0.72, anchor='center')

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

        self.file = open('Aset Projek/DataAkun.txt', 'r')
        d = self.file.read()
        r = ast.literal_eval(d)
        self.file.close()

        print(r.keys())
        print(r.values())

        if self.username in r.keys() and self.password == r[self.username]:
            global usernameGlobal

            usernameGlobal = self.username

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
        self.place(relx=0.5, rely=0.5, anchor='center')

        self.img_logo = ctk.CTkImage(Image.open('Aset Projek/Hostay Logo.png'), size=(140, 70))

        self.hostay_logo = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.hostay_logo.place(relx=0.5, rely=0.11, anchor='center')

        self.username_label = ctk.CTkLabel(self, text='Username', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.username_label.place(relx=0.26, rely=0.307, anchor='center')
        self.username_label_emoji = ctk.CTkLabel(self, text='👤', text_color='#000000')
        self.username_label_emoji.place(relx=0.443, rely=0.302, anchor='center')
        self.username_input = ctk.CTkEntry(self, width=180, placeholder_text='Masukkan Username', border_width=0)
        self.username_input.place(relx=0.5, rely=0.371, anchor='center')

        self.password_label = ctk.CTkLabel(self, text='Password', text_color='#000000', font=ctk.CTkFont('Mona-Sans', 13))
        self.password_label.place(relx=0.257, rely=0.463, anchor='center')
        self.password_label_emoji = ctk.CTkLabel(self, text="🔐", text_color='#000000')
        self.password_label_emoji.place(relx=0.433, rely=0.457, anchor='center')
        self.password_input = ctk.CTkEntry(self, width=180, placeholder_text='Masukkan Password', show='*', border_width=0)
        self.password_input.place(relx=0.5, rely=0.526, anchor='center')

        self.confirmpassword_label = ctk.CTkLabel(self, text="Konfirmasi Password", text_color="#000000", font=ctk.CTkFont('Mona-Sans', 13))
        self.confirmpassword_label.place(relx=0.412, rely=0.615, anchor='center')
        self.confirmpassword_emoji = ctk.CTkLabel(self, text="🛡️", text_color="#000000")
        self.confirmpassword_emoji.place(relx=0.78, rely=0.607, anchor='center')
        self.confirmpassword_input = ctk.CTkEntry(self, width=180, placeholder_text="Konfirmasi Password", show="*", border_width=0)
        self.confirmpassword_input.place(relx=0.5, rely=0.681, anchor='center')

        self.signup_button = ctk.CTkButton(self, width=200, height=30, text='S I G N  U P', text_color='#FFFFFF', fg_color='#1f538d', hover_color='#0E4480', cursor='hand2', font=('Mona-Sans ExtraBold Wide', 13), border_width=2.5, border_color='#0E4480', corner_radius=25, command=self.Registration)
        self.signup_button.place(relx=0.5, rely=0.88, anchor='center')

        self.login_label = ctk.CTkLabel(self, text='Anda telah memiki akun?', text_color='#000000', font=('Mona-Sans', 10.5))
        self.login_label.place(relx=0.355, rely=0.975, anchor='center')
        
        self.login_label_button = ctk.CTkButton(self, width=14, height=1, text='Login disini', text_color='#004aad', border_width=0, fg_color='#FFFFFF', hover_color='#FFFFFF', cursor='hand2', font=('Mona-Sans', 11.5))
        self.login_label_button.place(relx=0.79, rely=0.975, anchor='center')

        self.warning_label = CTkLabel(self, text="", font=CTkFont('Mona-Sans', 11), text_color="red")
        self.warning_label.place(relx=0.5, rely=0.77, anchor='center')

    def Registration(self):
        username = self.username_input.get()
        password = self.password_input.get()
        confirmpassword = self.confirmpassword_input.get()

        password_regex = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        with open("Aset Projek/DataAkun.txt", "r") as file:
            existing_users = ast.literal_eval(file.read())

        if username in existing_users:
            self.warning_label.configure(text="Username telah ada, Pilih username lain.", font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor='center')
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not username:
            self.warning_label.configure(text="Masukkan username terlebih dahulu.", font=CTkFont('Mona-Sans', 12))
            self.warning_label.place(relx=0.5, rely=0.77, anchor='center')
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not password:
            self.warning_label.configure(text="Harap masukkan password\nterlebih dahulu.", font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor='center')
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not confirmpassword:
            self.warning_label.configure(text='Harap masukkan konfirmasi password\nterlebih dahulu.', font=CTkFont('Mona-Sans', 11))
            self.warning_label.place(relx=0.5, rely=0.77, anchor='center')
            self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))
        elif not re.match(password_regex, password):
            self.warning_label.configure(text="Password harus memiliki minimal 8 karakter dan\nsetidaknya terdapat satu huruf dan satu angka.", font=CTkFont('Mona-Sans', 9))
            self.warning_label.after(2500, lambda: self.warning_label.configure(text=""))    
        else:
            if password == confirmpassword:
                try:
                    file = open("Aset Projek/DataAkun.txt", "r+")
                    d = file.read()
                    r = ast.literal_eval(d)

                    dict2 = {username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file = open("Aset Projek/DataAkun.txt", "w")
                    w = file.write(str(r))

                    self.warning_label.configure(text="Akun berhasil dibuat! Tunggu Sebentar...", font=CTkFont('Mona-Sans', 11), text_color="green")
                    self.warning_label.place(relx=0.5, rely=0.77, anchor='center')
                    self.warning_label.after(1500, self.master.show_login_page)

                except:
                    file = open('Aset Projek/DataAkun.txt', 'w')
                    pp = str({"Username": "password"})
                    file.write(pp)
                    file.close()
            else:
                self.warning_label.configure(text="Gagal, kedua password harus sama.", font=CTkFont('Mona-Sans', 11))
                self.warning_label.after(1500, lambda: self.warning_label.configure(text=""))

if __name__ == '__main__':
    app = App()
    app.mainloop()
