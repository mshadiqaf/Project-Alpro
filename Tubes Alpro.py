import customtkinter as ctk
import mysql.connector as mysql
import time as tm
import ast, re
from datetime import *
from customtkinter import *
from CTkTable import *
from CTkScrollableDropdown import *
from CTkXYFrame import *
from CTkMessagebox import *
from tkcalendar import *
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

        self.conn = mysql.connect(host='localhost', username='root', password='', db='hostay')
        self.cursor = self.conn.cursor()

        self.login_page = LoginPage(self)
        self.registration_page = RegistrationPage(self)
        self.show_mainmenu_page()

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

        # =====================================================================================================
        #                                         -----  IMAGES  -----
        # =====================================================================================================

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
        self.foodservice_image = ctk.CTkImage(Image.open('Aset Projek/Food and Drink Service.png'), size=(369,257.48))
        self.repairingservice_image = ctk.CTkImage(Image.open('Aset Projek/Repairing Service.png'), size=(369,257.48))
        self.cleaningservice_image = ctk.CTkImage(Image.open('Aset Projek/Cleaning Service.png'), size=(369,257.48))
        self.logout_image = ctk.CTkImage(Image.open('Aset Projek/Logout.png'), size=(20,20))
        self.appetizer_cireng_image = ctk.CTkImage(Image.open('Aset Projek/A_Cireng.png'), size=(175,159))
        self.appetizer_risoles_image = ctk.CTkImage(Image.open('Aset Projek/A_Risoles.png'), size=(175,159))
        self.appetizer_tahuisi_image = ctk.CTkImage(Image.open('Aset Projek/A_Tahu Isi.png'), size=(175,159))
        self.appetizer_tempemendoan_image = ctk.CTkImage(Image.open('Aset Projek/A_Tempe Mendoan.png'), size=(175,159))
        self.appetizer_kroketkentang_image = ctk.CTkImage(Image.open('Aset Projek/A_Kroket Kentang.png'), size=(175,159))
        self.maincourse_ayambetutu_image = ctk.CTkImage(Image.open('Aset Projek/M_Ayam Betutu.png'), size=(175,159))
        self.maincourse_ayamsambalmatah_image = ctk.CTkImage(Image.open('Aset Projek/M_Ayam Sambal Matah.png'), size=(175,159))
        self.maincourse_ayamtaliwang_image = ctk.CTkImage(Image.open('Aset Projek/M_Ayam Taliwang.png'), size=(175,159))
        self.maincourse_miegoreng_image = ctk.CTkImage(Image.open('Aset Projek/M_Mie Goreng.png'), size=(175,159))
        self.maincourse_nasigoreng_image = ctk.CTkImage(Image.open('Aset Projek/M_Nasi Goreng.png'), size=(175,159))
        self.maincourse_sateayam_image = ctk.CTkImage(Image.open('Aset Projek/M_Sate Ayam.png'), size=(175,159))
        self.maincourse_sopbuntut_image = ctk.CTkImage(Image.open('Aset Projek/M_Sop Buntut.png'), size=(175,159))
        self.dessert_escampur_image = ctk.CTkImage(Image.open('Aset Projek/D_Es Campur.png'), size=(175,159))
        self.dessert_esdawet_image = ctk.CTkImage(Image.open('Aset Projek/D_Es Dawet.png'), size=(175,159))
        self.dessert_espisangijo_image = ctk.CTkImage(Image.open('Aset Projek/D_Es Pisang Ijo.png'), size=(175,159))
        self.dessert_klepon_image = ctk.CTkImage(Image.open('Aset Projek/D_Klepon.png'), size=(175,159))
        self.dessert_pisangkeju_image = ctk.CTkImage(Image.open('Aset Projek/D_Pisang Keju.png'), size=(175,159))
        self.drinks_esjeruk_image = ctk.CTkImage(Image.open('Aset Projek/Dr_Es Jeruk.png'), size=(175,159))
        self.drinks_eskelapa_image = ctk.CTkImage(Image.open('Aset Projek/Dr_Es Kelapa.png'), size=(175,159))
        self.drinks_esteh_image = ctk.CTkImage(Image.open('Aset Projek/Dr_Es Teh.png'), size=(175,159))
        self.drinks_kopi_image = ctk.CTkImage(Image.open('Aset Projek/Dr_Kopi.png'), size=(175,159))
        self.drinks_susu_image = ctk.CTkImage(Image.open('Aset Projek/Dr_Susu.png'), size=(175,159))
        self.message_question = ctk.CTkImage(Image.open('Aset Projek/Question.png'), size=(305,264))

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((1, 2), weight=1)

        # =====================================================================================================
        #                                         -----  FRAMES  -----
        # =====================================================================================================

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
        self.main_frame_checkout = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_checkout_detail = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_checkout = ctk.CTkFrame(self.main_frame_checkout, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkout_detail = ctk.CTkFrame(self.main_frame_checkout_detail, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_checkout_billingdetail = ctk.CTkFrame(self.main_frame_checkout_detail, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_guestlist = ctk.CTkFrame(self.main_frame_checkout, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_guestlist = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_guestlist = ctk.CTkFrame(self.main_frame_guestlist, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_guesthistory = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_guesthistory = ctk.CTkFrame(self.main_frame_guesthistory, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_roomservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_roomservice_request = ctk.CTkFrame(self.main_frame_roomservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_roomservice_menu = ctk.CTkFrame(self.main_frame_roomservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_foodservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_foodservice_menu = ctk.CTkFrame(self.main_frame_foodservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_framebar_foodservice_order = ctk.CTkFrame(self.main_frame_foodservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_repairingservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_repairingservice = ctk.CTkFrame(self.main_frame_repairingservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_cleaningservice = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_framebar_cleaningservice = ctk.CTkFrame(self.main_frame_cleaningservice, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_frame_about = ctk.CTkFrame(self, fg_color="#0C0B10", bg_color='#0C0B10', corner_radius=15)
        self.main_frame_dashboard_roomstatus = ctk.CTkFrame(self.main_frame_dashboard, fg_color="#131318", bg_color='#0C0B10', border_color='#101014', border_width=5, corner_radius=20)
        self.main_scrollframe_dashboard_roomstatus = ctk.CTkScrollableFrame(self.main_frame_dashboard_roomstatus, width=1150, corner_radius=20, height=30, fg_color='#191922', bg_color='transparent', scrollbar_button_color='#9599C8', scrollbar_button_hover_color='#636685', scrollbar_fg_color='#242531', border_color='#171720', border_width=5)
        
        # ========================================== FRAMES POSITIONING ==========================================

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
        self.main_framebar_checkout.grid(row=1, column=0, padx=(10,35), pady=(5,100), sticky='news')
        self.main_frame_checkout_detail.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_framebar_checkout_detail.grid(row=0, column=0, padx=(10,0), pady=(70,30), sticky='news')
        self.main_framebar_checkout_billingdetail.grid(row=0, column=1, padx=(20,30), pady=(70,30), sticky='news')
        self.main_framebar_checkout_billingdetail.grid_columnconfigure(0, weight=1)
        self.main_frame_checkout_detail.grid_columnconfigure(1, weight=1)
        self.main_frame_checkout_detail.grid_rowconfigure(0, weight=1)
        self.main_frame_checkout.grid_rowconfigure(1, weight=1)
        self.main_frame_checkout.grid_columnconfigure(0, weight=1)
        self.main_frame_guestlist.grid(row=1, column=1, padx=30, sticky='news')
        self.main_frame_guestlist.grid_rowconfigure(1, weight=1)
        self.main_frame_guestlist.grid_columnconfigure(0, weight=1)
        self.main_frame_guesthistory.grid_rowconfigure(1, weight=1)
        self.main_frame_guesthistory.grid_columnconfigure(0, weight=1)
        self.main_frame_guesthistory.grid(row=1, column=1, rowspan=3, ipady=300, padx=0, pady=0, sticky='news')
        self.main_framebar_guestlist.grid(row=1, column=0, padx=(10,35), pady=(5,25), sticky='news')
        self.main_framebar_guesthistory.grid(row=1, column=0, padx=(10,35), pady=(5,25), sticky='news')
        self.main_frame_roomservice.grid(row=1, column=1, rowspan=3, padx=0, pady=0, sticky='news')        
        self.main_frame_roomservice.grid_columnconfigure(0, weight=1)
        self.main_framebar_roomservice_request.grid(row=1, column=0, padx=(10,35), pady=(0,0), sticky='news')
        self.main_framebar_roomservice_request.grid_columnconfigure(0, weight=1)
        self.main_framebar_roomservice_request.grid_columnconfigure(1, weight=1)
        self.main_framebar_roomservice_menu.grid(row=0, column=0, padx=(10,35), pady=(70,25), sticky='news')
        self.main_frame_foodservice.grid(row=1, column=1, rowspan=3, padx=0, pady=0, sticky='news')
        self.main_frame_foodservice.grid_rowconfigure(1, weight=1)         
        self.main_framebar_foodservice_menu.grid(row=1, column=0, padx=(10,25), pady=(0,22.5), sticky='news')        
        self.main_framebar_foodservice_order.grid(row=1, column=1, padx=(0,0), pady=(0,22.5), sticky='nws')  
        self.main_framebar_foodservice_order.grid_rowconfigure(2, weight=1)      
        self.main_frame_repairingservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_repairingservice.grid_columnconfigure(0, weight=1)
        self.main_framebar_repairingservice.grid(row=1, column=0, padx=(10,35), pady=(0,0), sticky='news')
        self.main_framebar_repairingservice.grid_columnconfigure(0, weight=1)
        self.main_frame_cleaningservice.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')        
        self.main_frame_cleaningservice.grid_columnconfigure(0, weight=1)
        self.main_framebar_cleaningservice.grid(row=1, column=0, padx=(10,35), pady=(0,0), sticky='news')
        self.main_framebar_cleaningservice.grid_columnconfigure(0, weight=1)
        self.main_frame_about.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        self.main_frame_dashboard_roomstatus.grid(row=2, column=0, rowspan=1, columnspan=4, padx=(9,37), pady=5, ipady=10, sticky='news')
        self.main_scrollframe_dashboard_roomstatus.grid(row=1, column=0, columnspan=10, padx=(17.5,10), ipady=15, sticky='news')

        self.headbar_frame.grid_columnconfigure(1, weight=1)
        self.main_frame_dashboard.grid_columnconfigure(3, weight=1)
        self.main_frame_checkin.grid_columnconfigure(3, weight=1)        

        # =====================================================================================================
        #                                         -----  WIDGETS  -----
        # =====================================================================================================

        # ========================================== SIDEBAR WIDGETS ==========================================

        self.sidebar_label_mainnav = ctk.CTkButton(self.sidebar_frame, corner_radius=25, width=180, height=45, text="Main Nav", font=ctk.CTkFont('Mona-Sans Bold', 20), fg_color='#19191F', bg_color='transparent', text_color="#D2D2DD", hover_color='#191922', border_color='#1B1B22', border_width=4)
        self.sidebar_button_dashboard = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Dashboard", font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", image=self.dashboard_image, command=self.dashboard_menu)
        self.sidebar_button_checkinout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=30, height=45, text="Check In/Out      ", font=ctk.CTkFont('Mona-Sans SemiBold', 14), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", image=self.rightarrow_image, compound='left', command=self.expand_button)
        self.sidebar_button_checkin = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check In", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkin_image, command=self.checkin_menu)
        self.sidebar_button_checkout = ctk.CTkButton(self.sidebar_frame, corner_radius=20, width=140, height=40, text="Check Out", font=ctk.CTkFont('Mona-Sans SemiBold', 12), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="w", compound='left', image=self.checkout_image, command=self.checkout_menu)
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

        # ========================================== HEADBAR WIDGETS ==========================================

        self.headbar_logo_label = ctk.CTkLabel(self.headbar_frame, text="", image=self.logo_image)
        self.headbar_button_profile = ctk.CTkButton(self.headbar_frame, corner_radius=30, width=50, height=45, image=self.user_image, text="Profile", font=ctk.CTkFont('Mona-Sans', 20), fg_color="transparent", text_color=("#FFFFFF"), hover_color='#4646DD', cursor='hand2', anchor="center", command=self.profile_menu)
        self.headbar_logo_label.grid(row=0, column=0, padx=30, pady=0, ipadx=25)
        self.headbar_button_profile.grid(row=0, column=6, padx=12, pady=10)
        self.headbar_clock_label = ctk.CTkButton(self.headbar_frame, font=ctk.CTkFont('Mona-Sans', 20), fg_color='#19191F', bg_color='transparent', text_color="#D2D2DD", hover_color='#191922', border_color='#1B1B22', border_width=4, corner_radius=20)
        self.headbar_clock_label.grid(row=0, column=5, padx=(0,10), pady=10)
        self.current_time()

        # ========================================= DASHBOARD WIDGETS ==========================================

        self.main_dashboard_heading_label = ctk.CTkLabel(self.main_frame_dashboard, text="Dashboard", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_dashboard_desc_label =  ctk.CTkLabel(self.main_frame_dashboard, text="Welcome to Hotel Management System  |  by Kelompok 4", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_dashboard_heading_label.grid(row=0, column=0, pady=5, sticky='news')
        self.main_dashboard_desc_label.place(x=580, y=43, anchor='center')

        self.main_dashboard_vacantrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_occupiedrooms_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_vacantdirty_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
        self.main_dashboard_requiringservice_frame = ctk.CTkFrame(self.main_frame_dashboard, fg_color='transparent', width=300, height=200)
    
        self.main_dashboard_vacantrooms_label = ctk.CTkLabel(self.main_dashboard_vacantrooms_frame, text='\n\n                   30', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacantready_image)
        self.main_dashboard_occupiedrooms_label = ctk.CTkLabel(self.main_dashboard_occupiedrooms_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.occupiedrooms_image)
        self.main_dashboard_vacantdirty_label = ctk.CTkLabel(self.main_dashboard_vacantdirty_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.vacantdirty_image)
        self.main_dashboard_requiringservice_label = ctk.CTkLabel(self.main_dashboard_requiringservice_frame, text='\n\n                   0', font=ctk.CTkFont('Mona-Sans Bold', 50), text_color='#FFFFFF', image=self.requiringservice_image)
        
        self.main_dashboard_vacantrooms_frame.grid(row=1, column=0, pady=0, sticky='news')
        self.main_dashboard_occupiedrooms_frame.grid(row=1, column=1, pady=0, sticky='news')
        self.main_dashboard_vacantdirty_frame.grid(row=1, column=2, pady=0, sticky='news')
        self.main_dashboard_requiringservice_frame.grid(row=1, column=3, pady=0, sticky='news')
        
        self.main_dashboard_vacantrooms_label.grid(row=0, column=0)
        self.main_dashboard_occupiedrooms_label.grid(row=0, column=0)
        self.main_dashboard_vacantdirty_label.grid(row=0, column=0)
        self.main_dashboard_requiringservice_label.grid(row=0, column=0)  
        
        # ===================================== DASHBOARD - ROOM STATUS WIDGETS ==========================================

        self.main_dashboard_roomstatus_frame = ctk.CTkButton(self.main_frame_dashboard_roomstatus, corner_radius=25, width=180, height=45, text="Room Status", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_dashboard_roomstatus_frame.grid(row=0, column=0, columnspan=10, padx=(20,12), pady=(15,20), sticky='news')

        # =========================================== FRAMES ROOM 01 - 30 ================================================

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
        
        # ======================================== FRAMES ROOM INDICATOR 01 - 30 ===================================================

        #3C58F7
        #9031D3
        #B52483

        self.room01_frame_indicator = ctk.CTkFrame(self.room01_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20)
        self.room02_frame_indicator = ctk.CTkFrame(self.room02_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) 
        self.room03_frame_indicator = ctk.CTkFrame(self.room03_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) 
        self.room04_frame_indicator = ctk.CTkFrame(self.room04_frame, width=70, height=10, fg_color='#0FBFB0', corner_radius=20) 
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
        
        # =========================================== FRAMES ROOM STATUS 01 - 30 ================================================

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
      
        # =========================================== FRAMES ROOM LABEL 01 - 30 ================================================

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
                
        self.update_room_status()

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
        
        self.cursor.execute("SELECT MAX(id) FROM guest")
        max_guest_id = self.cursor.fetchone()[0]
        if max_guest_id is not None:
            self.guestid = max_guest_id + 1
        else:
            self.guestid = 1

       # CHECK OUT WIDGET

        self.main_checkout_heading_label = ctk.CTkLabel(self.main_frame_checkout, text="Check Out", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkout_heading_label.grid(row=0, column=0, rowspan=1, pady=(5,0), padx=(20,100), sticky='news')
        self.main_checkout_desc_label =  ctk.CTkLabel(self.main_frame_checkout, text='Select a room that can be checked out', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkout_desc_label.place(x=480, y=45, anchor='center')

        self.main_checkout_title_frame = ctk.CTkButton(self.main_framebar_checkout, corner_radius=25, height=45, text="Occupied Rooms", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_checkout_title_frame.grid(row=0, column=0, columnspan=10, padx=(20,20), pady=(15,10), sticky='news')

        self.room01_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='01', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(1))
        self.room02_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='02', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(2))
        self.room03_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='03', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(3))
        self.room04_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='04', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(4))
        self.room05_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='05', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(5))
        self.room06_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='06', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(6))
        self.room07_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='07', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(7))
        self.room08_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='08', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(8))
        self.room09_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='09', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(9))
        self.room10_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='10', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFDC99', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(10))
        self.room11_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='11', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(11))
        self.room12_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='12', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(12))
        self.room13_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='13', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(13))
        self.room14_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='14', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(14))
        self.room15_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='15', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(15))
        self.room16_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='16', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(16))
        self.room17_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='17', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(17))
        self.room18_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='18', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(18))
        self.room19_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='19', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(19))
        self.room20_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='20', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#CE5700', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(20))
        self.room21_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='21', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(21))
        self.room22_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='22', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(22))
        self.room23_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='23', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(23))
        self.room24_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='24', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(24))
        self.room25_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='25', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(25))
        self.room26_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='26', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#BBCDCA', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(26))
        self.room27_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='27', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFB800', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(27))
        self.room28_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='28', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFB800', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(28))
        self.room29_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='29', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFB800', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(29))
        self.room30_checkout_button = ctk.CTkButton(self.main_framebar_checkout, width=98, height=125, fg_color='#242531', corner_radius=20, text='30', font=ctk.CTkFont('Mona-Sans ExtraBold', 45), text_color='#FFB800', hover_color='#4646DD', border_color='#1E1F29', border_width=5, command=lambda: self.checkout_detail(30))
        
        self.room01_checkout_button.grid(row=1, column=0, padx=(25,10), pady=(10,10), sticky='news')
        self.room02_checkout_button.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky='news')
        self.room03_checkout_button.grid(row=1, column=2, padx=(10,10), pady=(10,10), sticky='news')
        self.room04_checkout_button.grid(row=1, column=3, padx=(10,10), pady=(10,10), sticky='news')
        self.room05_checkout_button.grid(row=1, column=4, padx=(10,10), pady=(10,10), sticky='news')
        self.room06_checkout_button.grid(row=1, column=5, padx=(10,10), pady=(10,10), sticky='news')
        self.room07_checkout_button.grid(row=1, column=6, padx=(10,10), pady=(10,10), sticky='news')
        self.room08_checkout_button.grid(row=1, column=7, padx=(10,10), pady=(10,10), sticky='news')
        self.room09_checkout_button.grid(row=1, column=8, padx=(10,10), pady=(10,10), sticky='news')
        self.room10_checkout_button.grid(row=1, column=9, padx=(10,25), pady=(10,10), sticky='news')
        self.room11_checkout_button.grid(row=2, column=0, padx=(25,10), pady=(10,10), sticky='news')
        self.room12_checkout_button.grid(row=2, column=1, padx=(10,10), pady=(10,10), sticky='news')
        self.room13_checkout_button.grid(row=2, column=2, padx=(10,10), pady=(10,10), sticky='news')
        self.room14_checkout_button.grid(row=2, column=3, padx=(10,10), pady=(10,10), sticky='news')
        self.room15_checkout_button.grid(row=2, column=4, padx=(10,10), pady=(10,10), sticky='news')
        self.room16_checkout_button.grid(row=2, column=5, padx=(10,10), pady=(10,10), sticky='news')
        self.room17_checkout_button.grid(row=2, column=6, padx=(10,10), pady=(10,10), sticky='news')
        self.room18_checkout_button.grid(row=2, column=7, padx=(10,10), pady=(10,10), sticky='news')
        self.room19_checkout_button.grid(row=2, column=8, padx=(10,10), pady=(10,10), sticky='news')
        self.room20_checkout_button.grid(row=2, column=9, padx=(10,25), pady=(10,10), sticky='news')
        self.room21_checkout_button.grid(row=3, column=0, padx=(25,10), pady=(10,10), sticky='news')
        self.room22_checkout_button.grid(row=3, column=1, padx=(10,10), pady=(10,10), sticky='news')
        self.room23_checkout_button.grid(row=3, column=2, padx=(10,10), pady=(10,10), sticky='news')
        self.room24_checkout_button.grid(row=3, column=3, padx=(10,10), pady=(10,10), sticky='news')
        self.room25_checkout_button.grid(row=3, column=4, padx=(10,10), pady=(10,10), sticky='news')
        self.room26_checkout_button.grid(row=3, column=5, padx=(10,10), pady=(10,10), sticky='news')
        self.room27_checkout_button.grid(row=3, column=6, padx=(10,10), pady=(10,10), sticky='news')
        self.room28_checkout_button.grid(row=3, column=7, padx=(10,10), pady=(10,10), sticky='news')
        self.room29_checkout_button.grid(row=3, column=8, padx=(10,10), pady=(10,10), sticky='news')
        self.room30_checkout_button.grid(row=3, column=9, padx=(10,25), pady=(10,10), sticky='news')
        
        for data in self.room_status:
            self.room_id, self.status = data
            self.room_button = {
                    1: self.room01_button,
                    2: self.room02_button,
                    3: self.room03_button,
                    4: self.room04_button,
                    5: self.room05_button,
                    6: self.room06_button,
                    7: self.room07_button,
                    8: self.room08_button,
                    9: self.room09_button,
                    10: self.room10_button,
                    11: self.room11_button,
                    12: self.room12_button,
                    13: self.room13_button,
                    14: self.room14_button,
                    15: self.room15_button,
                    16: self.room16_button,
                    17: self.room17_button,
                    18: self.room18_button,
                    19: self.room19_button,
                    20: self.room20_button,
                    21: self.room21_button,
                    22: self.room22_button,
                    23: self.room23_button,
                    24: self.room24_button,
                    25: self.room25_button,
                    26: self.room26_button,
                    27: self.room27_button,
                    28: self.room28_button,
                    29: self.room29_button,
                    30: self.room30_button,
                }
            
            self.room_checkout_button = {
                    1: self.room01_checkout_button,
                    2: self.room02_checkout_button,
                    3: self.room03_checkout_button,
                    4: self.room04_checkout_button,
                    5: self.room05_checkout_button,
                    6: self.room06_checkout_button,
                    7: self.room07_checkout_button,
                    8: self.room08_checkout_button,
                    9: self.room09_checkout_button,
                    10: self.room10_checkout_button,
                    11: self.room11_checkout_button,
                    12: self.room12_checkout_button,
                    13: self.room13_checkout_button,
                    14: self.room14_checkout_button,
                    15: self.room15_checkout_button,
                    16: self.room16_checkout_button,
                    17: self.room17_checkout_button,
                    18: self.room18_checkout_button,
                    19: self.room19_checkout_button,
                    20: self.room20_checkout_button,
                    21: self.room21_checkout_button,
                    22: self.room22_checkout_button,
                    23: self.room23_checkout_button,
                    24: self.room24_checkout_button,
                    25: self.room25_checkout_button,
                    26: self.room26_checkout_button,
                    27: self.room27_checkout_button,
                    28: self.room28_checkout_button,
                    29: self.room29_checkout_button,
                    30: self.room30_checkout_button,
                }
            
            if self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Occupied':
                self.room_button[self.room_id].configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans Bold', 25))
                
                if 1 <= int(self.room_id) <= 10:
                    text_color = '#FFDC99'
                elif 11 <= int(self.room_id) <= 20:
                    text_color = '#CE5700'
                elif 21 <= int(self.room_id) <= 25:
                    text_color = '#BBCDCA'
                elif 26 <= int(self.room_id) <= 30:
                    text_color = '#FFB800'

                formatted_room_id = str(self.room_id).zfill(2)

                self.room_checkout_button[self.room_id].configure(state='normal', text=formatted_room_id, text_color=text_color, font=ctk.CTkFont('Mona-Sans ExtraBold', 45))

            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Dirty':
                self.room_button[self.room_id].configure(state='disabled', text='Dirty', font=ctk.CTkFont('Mona-Sans Bold', 25))
                self.room_checkout_button[self.room_id].configure(state='disabled', text='Dirty', text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Bold', 15))

            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Service':
                formatted_room_id = str(self.room_id).zfill(2)
                self.room_button[self.room_id].configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans Bold', 25))
                self.room_checkout_button[self.room_id].configure(state='normal', text=formatted_room_id, font=ctk.CTkFont('Mona-Sans ExtraBold', 45))

            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button:
                self.room_button[self.room_id].configure(state='normal')
                self.room_checkout_button[self.room_id].configure(state='disabled', text='Ready', text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Bold', 15))

       # GUEST LIST WIDGET

        self.main_guestlist_heading_label = ctk.CTkLabel(self.main_frame_guestlist, text="Guest List", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guestlist_heading_label.grid(row=0, column=0, rowspan=1, pady=(5,0), padx=(20,100), sticky='news')
        self.main_guestlist_desc_label =  ctk.CTkLabel(self.main_frame_guestlist, text='List of guests currently staying', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guestlist_desc_label.place(x=430, y=45, anchor='center')

        self.cursor.execute("SELECT id, status FROM kamar")
        room_statuses = self.cursor.fetchall()

        self.cursor.execute("SELECT room_num, first_name, last_name, check_in_date, check_out_date, guest_note FROM guest")
        self.guest_datas = self.cursor.fetchall()

        self.guest_list = [
            ["Room Number", "Room Type", "Guest Name", "Check In Date", 'Check Out Date',"Status",'Guest Note'],
            ['01', 'Single','','','','Ready',''],  
            ['02', 'Single','','','','Ready',''],
            ['03', 'Single','','','','Ready',''],
            ['04', 'Single','','','','Ready',''],
            ['05', 'Single','','','','Ready',''],
            ['06', 'Single','','','','Ready',''],
            ['07', 'Single','','','','Ready',''],
            ['08', 'Single','','','','Ready',''],        
            ['09', 'Single','','','','Ready',''],        
            ['10', 'Single','','','','Ready',''],        
            ['11', 'Double','','','','Ready',''],        
            ['12', 'Double','','','','Ready',''],        
            ['13', 'Double','','','','Ready',''],        
            ['14', 'Double','','','','Ready',''],        
            ['15', 'Double','','','','Ready',''],        
            ['16', 'Double','','','','Ready',''],        
            ['17', 'Double','','','','Ready',''],        
            ['18', 'Double','','','','Ready',''],        
            ['19', 'Double','','','','Ready',''],        
            ['20', 'Double','','','','Ready',''],        
            ['21', 'Suite','','','','Ready',''],        
            ['22', 'Suite','','','','Ready',''],        
            ['23', 'Suite','','','','Ready',''],        
            ['24', 'Suite','','','','Ready',''],        
            ['25', 'Suite','','','','Ready',''],        
            ['26', 'Suite','','','','Ready',''],        
            ['27', 'President Suite','','','','Ready',''],        
            ['28', 'President Suite','','','','Ready',''],        
            ['29', 'President Suite','','','','Ready',''],        
            ['30', 'President Suite','','','','Ready',''],        
        ]
    
        self.main_guestlist_scrollableframe = CTkXYFrame(self.main_framebar_guestlist, scrollbar_fg_color='transparent', fg_color="#131318", scrollbar_button_color='#4646DD', scrollbar_button_hover_color='#3434A6')
        self.main_guestlist_scrollableframe.pack(fill="both", expand=True, padx=20, pady=20)
        self.main_guestlist_table = CTkTable(self.main_guestlist_scrollableframe, font=ctk.CTkFont('Mona-Sans Medium', 13), values=self.guest_list, header_color='#4646DD', colors=['#131318', '#15151B'], border_color='#101016', corner_radius=0, border_width=2, color_phase='horizontal', wraplength=550)
        self.main_guestlist_table.pack(expand=True)
        self.main_guestlist_table.edit_column(0, width=110)
        self.main_guestlist_table.edit_column(1, width=150)
        self.main_guestlist_table.edit_column(2, width=400)
        self.main_guestlist_table.edit_column(3, width=110)
        self.main_guestlist_table.edit_column(4, width=120)
        self.main_guestlist_table.edit_column(5, width=130)
        self.main_guestlist_table.edit_column(6, width=550)
        

        for guest_data in self.guest_datas:
            room_num = guest_data[0]
            guest_full_name = f"{guest_data[1]} {guest_data[2]}"
            check_in_date = guest_data[3]
            check_out_date = guest_data[4]
            guest_note = guest_data[5]

            self.main_guestlist_table.insert(room_num, 2, guest_full_name)
            self.main_guestlist_table.insert(room_num, 3, check_in_date)
            self.main_guestlist_table.insert(room_num, 4, check_out_date)
            self.main_guestlist_table.insert(room_num, 6, guest_note)
            
        for room_status in room_statuses:
            room_number = room_status[0]
            self.statuses = room_status[1]

            self.main_guestlist_table.insert(room_number, 5, self.statuses)

            if self.statuses == 'Dirty':
                self.main_guestlist_table.delete(room_number, 2)    
                self.main_guestlist_table.delete(room_number, 3)    
                self.main_guestlist_table.delete(room_number, 4)    
                self.main_guestlist_table.delete(room_number, 6)  
        
          

        self.main_guesthistory_heading_label = ctk.CTkLabel(self.main_frame_guesthistory, text="Guest History", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guesthistory_heading_label.grid(row=0, column=0, rowspan=1, pady=(5,0), padx=(20,100), sticky='news')
        self.main_guesthistory_desc_label =  ctk.CTkLabel(self.main_frame_guesthistory, text="List of guest's history", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_guesthistory_desc_label.place(x=475, y=45, anchor='center')
          
        self.cursor.execute("SELECT * FROM guest")
        rows = self.cursor.fetchall()

        self.guest_history = [['Guest ID', 'Room Number', 'Guest Name', 'Age', 'Gender', 'NIN',
                        'Mobile Phone Number', 'Email', 'Address', 'Check In Date', 'Check Out Date']]
        
        for row in rows:
            guest_name = f"{row[2]} {row[3]}"
            self.guest_history.append([
                row[0],  
                row[1],  
                guest_name,
                row[4], 
                row[5],  
                row[6],  
                row[7],  
                row[8],  
                row[9],  
                row[10],  
                row[11]
        ])
    
        self.main_guesthistory_scrollableframe = CTkXYFrame(self.main_framebar_guesthistory, scrollbar_fg_color='transparent', fg_color="#131318", scrollbar_button_color='#4646DD', scrollbar_button_hover_color='#3434A6')
        self.main_guesthistory_scrollableframe.pack(fill="both", expand=True, padx=20, pady=20)
        self.main_guesthistory_table = CTkTable(self.main_guesthistory_scrollableframe, font=ctk.CTkFont('Mona-Sans Medium', 13), values=self.guest_history, header_color='#4646DD', colors=['#131318', '#15151B'], border_color='#101016', corner_radius=0, border_width=2, color_phase='horizontal', wraplength=350)
        self.main_guesthistory_table.pack(expand=True)
        self.main_guesthistory_table.edit_column(0, width=80)
        self.main_guesthistory_table.edit_column(1, width=120)
        self.main_guesthistory_table.edit_column(2, width=280)
        self.main_guesthistory_table.edit_column(3, width=60)
        self.main_guesthistory_table.edit_column(4, width=100)
        self.main_guesthistory_table.edit_column(5, width=200)
        self.main_guesthistory_table.edit_column(6, width=200)
        self.main_guesthistory_table.edit_column(7, width=250)
        self.main_guesthistory_table.edit_column(8, width=350)
        self.main_guesthistory_table.edit_column(9, width=150)
        self.main_guesthistory_table.edit_column(10, width=150)

       # ROOM SERVICES WIDGET

        self.main_roomservice_heading_label = ctk.CTkLabel(self.main_frame_roomservice, text="Room Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_roomservice_heading_label.place(x=20, y=5)
        self.main_roomservice_desc_label =  ctk.CTkLabel(self.main_frame_roomservice, text='Choose the type of service', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_roomservice_desc_label.place(x=527.5, y=45, anchor='center')

        self.main_roomservice_menu_request_frame = ctk.CTkButton(self.main_framebar_roomservice_request, corner_radius=25, height=45, text="Guest's Request ", anchor='center', font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_roomservice_menu_request_frame.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(15,10), sticky='news')
        
        self.main_roomservice_menu_title_frame = ctk.CTkButton(self.main_framebar_roomservice_menu, corner_radius=25, height=45, text="Service Menu", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_roomservice_menu_title_frame.grid(row=0, column=0, columnspan=3, padx=(20,20), pady=(15,10), sticky='news')

        self.main_roomservice_roomoption_label = ctk.CTkLabel(self.main_framebar_roomservice_request, text="Room Number", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.main_roomservice_roomoption_label.place(relx=0.35, rely=0.4, anchor='center')

        self.main_roomservice_servicetype_label = ctk.CTkLabel(self.main_framebar_roomservice_request, text="Type of Service", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.main_roomservice_servicetype_label.place(relx=0.65, rely=0.4, anchor='center')
        self.main_roomservice_servicetype = ctk.CTkOptionMenu(self.main_framebar_roomservice_request, values=['Food and Drink Service','Repairing Service','Cleaning Service'], width=250, height=30, font=ctk.CTkFont('Mona-Sans Bold', 15), corner_radius=30, anchor='center', dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6')
        self.main_roomservice_servicetype.place(relx=0.65, rely=0.55, anchor='center')

        self.main_roomservice_roomoption = ctk.CTkOptionMenu(self.main_framebar_roomservice_request, values=[''], width=100, height=25, font=ctk.CTkFont('Mona-Sans Bold', 20), corner_radius=30, anchor='center', dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6')
        self.main_roomservice_roomoption.place(relx=0.35, rely=0.55, anchor='center')
        self.roomlist = [f"{room[0]:02d}" for room in self.room_status if room[1] == 'Occupied']
        CTkScrollableDropdown(self.main_roomservice_roomoption, width=100, double_click=False, resize=False, y=-250, values=self.roomlist, fg_color='#242531', frame_border_color='#1E1F29', frame_border_width=3, alpha=1, frame_corner_radius=25, button_color='#4646DD', hover_color='#3434A6', scrollbar_button_color='#4646DD', scrollbar_button_hover_color='#3434A6')
        
        self.main_roomservice_request_button = ctk.CTkButton(self.main_framebar_roomservice_request, command=lambda: self.servicerequest(self.main_roomservice_roomoption.get(), self.main_roomservice_servicetype.get()),text='Request Service', font=ctk.CTkFont('Mona-Sans Bold', 18), text_color='#FFFFFF', fg_color='#4646DD', hover_color='#3434A6', corner_radius=30, width=200, height=35, bg_color='transparent', cursor='hand2')
        self.main_roomservice_request_button.grid(row=1, column=0, columnspan=2, pady=(90,20), padx=(20,15),sticky='ns')

        self.main_roomservice_foodservice_button = ctk.CTkButton(self.main_framebar_roomservice_menu, corner_radius=50, image=self.foodservice_image, text="", fg_color='#131318', hover_color='#4646DD', cursor='hand2', anchor="center", command=self.foodservice_menu)
        self.main_roomservice_repairingservice_button = ctk.CTkButton(self.main_framebar_roomservice_menu, corner_radius=50, image=self.repairingservice_image, text="", fg_color='#131318', hover_color='#4646DD', cursor='hand2', anchor="center", command=self.repairingservice_menu)
        self.main_roomservice_cleaningservice_button = ctk.CTkButton(self.main_framebar_roomservice_menu, corner_radius=50, image=self.cleaningservice_image, text="", fg_color='#131318', hover_color='#4646DD', cursor='hand2', anchor="center", command=self.cleaningservice_menu)

        self.main_roomservice_foodservice_button.grid(row=1, column=0, padx=(10,0), pady=(5,10), sticky='news')
        self.main_roomservice_repairingservice_button.grid(row=1, column=1, padx=(0,0), pady=(5,10), sticky='news')
        self.main_roomservice_cleaningservice_button.grid(row=1, column=2, padx=(0,10), pady=(5,10), sticky='news')

        # FOOD AND DRINKS SERVICES WIDGET

        self.main_foodservice_heading_label = ctk.CTkLabel(self.main_frame_foodservice, text="Food & Drink Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_foodservice_heading_label.grid(row=0, column=0, pady=(5,5), padx=(80,0), sticky='news')
        self.main_foodservice_desc_label =  ctk.CTkLabel(self.main_frame_foodservice, text='Choose from the available food and beverages', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_foodservice_desc_label.place(x=855, y=45, anchor='center')
        self.main_foodservice_back = ctk.CTkButton(self.main_frame_foodservice, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.roomservice_menu)
        self.main_foodservice_back.place(x=25, y=33, anchor='center')

        self.main_foodservice_menu_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, fg_color='#191922', border_color='#171720', border_width=5, corner_radius=20)
        self.main_foodservice_appetizer_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Appetizer', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.appetizer_menu)
        self.main_foodservice_maincourse_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Main Course', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.maincourse_menu)
        self.main_foodservice_dessert_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Dessert', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.dessert_menu)
        self.main_foodservice_drinks_button = ctk.CTkButton(self.main_foodservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Drinks', font=ctk.CTkFont('Mona-Sans Bold', 18), command=self.drinks_menu)
        self.main_foodservice_appetizer_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, corner_radius=20, fg_color='#191922', bg_color='transparent' , border_color='#171720', border_width=5)
        self.main_foodservice_maincourse_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, corner_radius=20, fg_color='#191922', bg_color='transparent' , border_color='#171720', border_width=5)
        self.main_foodservice_dessert_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, corner_radius=20, fg_color='#191922', bg_color='transparent' , border_color='#171720', border_width=5)
        self.main_foodservice_drinks_frame = ctk.CTkFrame(self.main_framebar_foodservice_menu, corner_radius=20, fg_color='#191922', bg_color='transparent' , border_color='#171720', border_width=5)

        self.main_foodservice_appetizer_cireng = self.create_button(self.main_foodservice_appetizer_frame, 'Cireng', self.appetizer_cireng_image, 0, 0, 17.5, 0, 20, 0)
        self.main_foodservice_appetizer_risoles = self.create_button(self.main_foodservice_appetizer_frame, 'Risoles', self.appetizer_risoles_image, 0, 1, 0, 0, 20, 0)
        self.main_foodservice_appetizer_tahuisi = self.create_button(self.main_foodservice_appetizer_frame, 'Tahu Isi', self.appetizer_tahuisi_image, 0, 2, 0, 0, 20, 0)
        self.main_foodservice_appetizer_tempemendoan = self.create_button(self.main_foodservice_appetizer_frame, 'Tempe Mendoan', self.appetizer_tempemendoan_image, 0, 3, 0, 0, 20, 0)
        self.main_foodservice_appetizer_kroketkentang = self.create_button(self.main_foodservice_appetizer_frame, 'Kroket Kentang', self.appetizer_kroketkentang_image, 1, 0, 17.5, 0, 10, 0)

        self.main_foodservice_maincourse_ayambetutu = self.create_button(self.main_foodservice_maincourse_frame, 'Ayam Betutu', self.maincourse_ayambetutu_image, 0, 0, 17.5, 0, 20 ,0)
        self.main_foodservice_maincourse_ayamsambalmatah = self.create_button(self.main_foodservice_maincourse_frame, 'Ayam Sambal Matah', self.maincourse_ayamsambalmatah_image, 0, 1, 0, 0, 20, 0)
        self.main_foodservice_maincourse_ayamtaliwang = self.create_button(self.main_foodservice_maincourse_frame, 'Ayam Taliwang', self.maincourse_ayamtaliwang_image, 0, 2, 0, 0, 20, 0)
        self.main_foodservice_maincourse_miegoreng = self.create_button(self.main_foodservice_maincourse_frame, 'Mie Goreng', self.maincourse_miegoreng_image, 0, 3, 0, 0, 20, 0)
        self.main_foodservice_maincourse_nasigoreng = self.create_button(self.main_foodservice_maincourse_frame, 'Nasi Goreng', self.maincourse_nasigoreng_image, 1, 0, 17.5, 0, 10, 0)
        self.main_foodservice_maincourse_sateayam = self.create_button(self.main_foodservice_maincourse_frame, 'Sate Ayam', self.maincourse_sateayam_image, 1, 1, 0, 0, 10, 0)
        self.main_foodservice_maincourse_sopbuntut = self.create_button(self.main_foodservice_maincourse_frame, 'Sop Buntut', self.maincourse_sopbuntut_image, 1, 2, 0, 0, 10, 0)

        self.main_foodservice_dessert_escampur = self.create_button(self.main_foodservice_dessert_frame, 'Es Campur', self.dessert_escampur_image, 0, 0, 17.5, 0, 20, 0)
        self.main_foodservice_dessert_esdawet = self.create_button(self.main_foodservice_dessert_frame, 'Es Dawet', self.dessert_esdawet_image, 0, 1, 0, 0, 20, 0)
        self.main_foodservice_dessert_espisangijo = self.create_button(self.main_foodservice_dessert_frame, 'Es Pisang Ijo', self.dessert_espisangijo_image, 0, 2, 0, 0, 20, 0)
        self.main_foodservice_dessert_klepon = self.create_button(self.main_foodservice_dessert_frame, 'Klepon', self.dessert_klepon_image, 0, 3, 0, 0, 20, 0)
        self.main_foodservice_dessert_pisangkeju = self.create_button(self.main_foodservice_dessert_frame, 'Pisang Keju', self.dessert_pisangkeju_image, 1, 0, 17.5, 0, 10, 0)

        self.main_foodservice_drinks_esjeruk = self.create_button(self.main_foodservice_drinks_frame, 'Es Jeruk', self.drinks_esjeruk_image, 0, 0, 17.5, 0, 20, 0)
        self.main_foodservice_drinks_eskelapa = self.create_button(self.main_foodservice_drinks_frame, 'Es Kelapa', self.drinks_eskelapa_image, 0, 1, 0, 0, 20, 0)
        self.main_foodservice_drinks_esteh = self.create_button(self.main_foodservice_drinks_frame, 'Es Teh', self.drinks_esteh_image, 0, 2, 0, 0, 20, 0)
        self.main_foodservice_drinks_kopi = self.create_button(self.main_foodservice_drinks_frame, 'Kopi', self.drinks_kopi_image, 0, 3, 0, 0, 20, 0)
        self.main_foodservice_drinks_susu = self.create_button(self.main_foodservice_drinks_frame, 'Susu', self.drinks_susu_image, 1, 0, 17.5, 0, 10, 0)    
        
        self.main_foodservice_order_title = ctk.CTkButton(self.main_framebar_foodservice_order, corner_radius=25, width=317.5, height=50, text="Order List", text_color="#D9D9FF",font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', border_color='#171720', border_width=5)
        self.main_foodservice_order_roomlist_label = ctk.CTkLabel(self.main_framebar_foodservice_order, text="ROOM NUMBER  :", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_foodservice_order_roomlist = ctk.CTkOptionMenu(self.main_framebar_foodservice_order, values=[''], width=100, height=25, font=ctk.CTkFont('Mona-Sans Bold', 20), corner_radius=30, anchor='center', dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6')
        foodserviceroom = []
        CTkScrollableDropdown(self.main_foodservice_order_roomlist, width=100, values=foodserviceroom)
        self.main_foodservice_order_button = ctk.CTkButton(self.main_framebar_foodservice_order, text='Proceed', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=200, height=50, bg_color='transparent', cursor='hand2')
        self.main_foodservice_order_frame = ctk.CTkFrame(self.main_framebar_foodservice_order, fg_color='#191922', border_color='#171720', border_width=5, corner_radius=20)
        self.main_foodservice_order_scrollableframe = ctk.CTkScrollableFrame(self.main_foodservice_order_frame, scrollbar_button_color='#4646DD', scrollbar_button_hover_color='#3434A6', scrollbar_fg_color='transparent', fg_color='#191922') 
        self.main_foodservice_order_scrollableframe.pack(fill="both", expand=True, padx=(15,15), pady=20)

        self.main_foodservice_orderlist_product_label = ctk.CTkLabel(self.main_foodservice_order_scrollableframe, text="Product", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_foodservice_orderlist_quantity_label = ctk.CTkLabel(self.main_foodservice_order_scrollableframe, text="Quantity", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.main_foodservice_orderlist_product_label.grid(row=0, column=0, padx=(0,90), sticky='nws')
        self.main_foodservice_orderlist_quantity_label.grid(row=0, column=1, padx=(0,0), sticky='news')

        self.orders = []

        self.main_foodservice_menu_frame.grid(row=0, column=0, padx=(15,15), pady=(15,15), sticky='new')
        self.main_foodservice_appetizer_button.grid(row=0, column=0, padx=(10,5), pady=(10,10), sticky='news')
        self.main_foodservice_maincourse_button.grid(row=0, column=1, padx=(5,5), pady=(10,10), sticky='news')
        self.main_foodservice_dessert_button.grid(row=0, column=2, padx=(5,5), pady=(10,10), sticky='news')
        self.main_foodservice_drinks_button.grid(row=0, column=3, padx=(5,10), pady=(10,10), sticky='news')
        self.main_foodservice_appetizer_frame.grid(row=1, column=0, padx=(20,20), pady=(0,20), ipady=75, sticky='news')
        self.main_foodservice_maincourse_frame.grid(row=1, column=0, padx=(20,20), pady=(0,20), ipady=75, sticky='news')
        self.main_foodservice_dessert_frame.grid(row=1, column=0, padx=(20,20), pady=(0,20), ipady=75, sticky='news')
        self.main_foodservice_drinks_frame.grid(row=1, column=0, padx=(20,20), pady=(0,20), ipady=75, sticky='news')

        self.main_foodservice_order_title.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(15,15), sticky='new')
        self.main_foodservice_order_roomlist_label.grid(row=1, column=0, pady=(10,10), padx=(30,0))
        self.main_foodservice_order_roomlist.grid(row=1, column=1, pady=(10,10), padx=(0,30))
        self.main_foodservice_order_frame.grid(row=2, column=0, columnspan=2, padx=(15,15), pady=(15,20), sticky='news')
        self.main_foodservice_order_button.grid(row=3, column=0, columnspan=2, pady=(0,20), padx=(77.25,77.25), sticky='news')


        # REPAIRING SERVICE WIDGET

        self.main_repairingservice_heading_label = ctk.CTkLabel(self.main_frame_repairingservice, text="Repairing Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_repairingservice_heading_label.grid(row=0, column=0, pady=(5,5), padx=(80,0), sticky='news')
        self.main_repairingservice_desc_label =  ctk.CTkLabel(self.main_frame_repairingservice, text='Choose the type of repairing', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_repairingservice_desc_label.place(x=690, y=45, anchor='center')
        self.main_repairingservice_back = ctk.CTkButton(self.main_frame_repairingservice, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.roomservice_menu)
        self.main_repairingservice_back.place(x=25, y=33, anchor='center')

        self.main_repairingservice_button = ctk.CTkButton(self.main_framebar_repairingservice, corner_radius=25, width=180, height=45, text="Repairing Service Menu", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_repairingservice_button.grid(row=0, column=0, columnspan=1, padx=(20,20), pady=(15,15), sticky='news')


        self.main_roomservice_repairingtype_label = ctk.CTkLabel(self.main_framebar_repairingservice, text="Repairing type select", font=ctk.CTkFont('Mona-Sans Bold', 40), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_repairingservice_menu_frame = ctk.CTkFrame(self.main_framebar_repairingservice, fg_color='#191922', border_color='#171720', border_width=5, corner_radius=20)
        self.main_repairingservice_electricityrepair_button = ctk.CTkButton(self.main_repairingservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Electricity Repairing', font=ctk.CTkFont('Mona-Sans Bold', 18), command=lambda: self.select_repairingservice_menu('electricity'))
        self.main_repairingservice_furniturerepair_button = ctk.CTkButton(self.main_repairingservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Furniture Repairing', font=ctk.CTkFont('Mona-Sans Bold', 18), command=lambda: self.select_repairingservice_menu('furniture'))
        self.main_repairingservice_roomlist_label = ctk.CTkLabel(self.main_framebar_repairingservice, text="ROOM NUMBER  :", font=ctk.CTkFont('Mona-Sans Bold', 25), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_repairingservice_roomlist = ctk.CTkOptionMenu(self.main_framebar_repairingservice, values=[''], width=100, height=25, font=ctk.CTkFont('Mona-Sans Bold', 20), corner_radius=30, anchor='center', dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6')
        repairingserviceroom = []
        CTkScrollableDropdown(self.main_repairingservice_roomlist, width=100, values=repairingserviceroom)
        self.main_repairingservice_proceed_button = ctk.CTkButton(self.main_framebar_repairingservice, text='Proceed', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=150, height=35, bg_color='transparent', cursor='hand2')

        self.main_roomservice_repairingtype_label.grid(row=1, column=0, sticky='news', padx=(40,0), pady=(15,0))
        self.main_repairingservice_menu_frame.grid(row=2, column=0, padx=(25,0), pady=(10,0), sticky='nws')
        self.main_repairingservice_electricityrepair_button.grid(row=0, column=0, padx=(10,5), pady=(10,10), sticky='news')
        self.main_repairingservice_furniturerepair_button.grid(row=0, column=1, padx=(5,5), pady=(10,10), sticky='news')
        self.main_repairingservice_roomlist_label.grid(row=3, column=0, padx=(40,0), pady=(40,0), sticky='news')
        self.main_repairingservice_roomlist.grid(row=3, column=0, padx=(280,0), pady=(40,0), sticky='w')  
        self.main_repairingservice_proceed_button.grid(row=4, column=0, padx=(0,0), pady=(80,30), sticky='ns')

        # CLEANING SERVICE WIDGET

        self.main_cleaningservice_heading_label = ctk.CTkLabel(self.main_frame_cleaningservice, text="Cleaning Services", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_cleaningservice_heading_label.grid(row=0, column=0, pady=(5,5), padx=(80,0), sticky='news')
        self.main_cleaningservice_desc_label =  ctk.CTkLabel(self.main_frame_cleaningservice, text='Choose the cleaning purpose', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_cleaningservice_desc_label.place(x=667.5, y=45, anchor='center')
        self.main_cleaningservice_back = ctk.CTkButton(self.main_frame_cleaningservice, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.roomservice_menu)
        self.main_cleaningservice_back.place(x=25, y=33, anchor='center')

        self.main_cleaningservice_button = ctk.CTkButton(self.main_framebar_cleaningservice, corner_radius=25, width=180, height=45, text="Cleaning Service Menu", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_cleaningservice_button.grid(row=0, column=0, columnspan=1, padx=(20,20), pady=(15,15), sticky='news')


        self.main_roomservice_cleaningtype_label = ctk.CTkLabel(self.main_framebar_cleaningservice, text="Cleaning type select", font=ctk.CTkFont('Mona-Sans Bold', 40), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_cleaningservice_menu_frame = ctk.CTkFrame(self.main_framebar_cleaningservice, fg_color='#191922', border_color='#171720', border_width=5, corner_radius=20)
        self.main_cleaningservice_vacantdirty_button = ctk.CTkButton(self.main_cleaningservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Vacant Dirty', font=ctk.CTkFont('Mona-Sans Bold', 18), command=lambda: self.select_cleaningservice_menu('vacantdirty'))
        self.main_cleaningservice_cleaningrequest_button = ctk.CTkButton(self.main_cleaningservice_menu_frame, width=190, height=40, corner_radius=20, fg_color='#242432', bg_color='transparent', border_color='#1E1E2A', border_width=4, hover_color='#4646DD', text_color='#D9D9FF', text='Cleaning Request', font=ctk.CTkFont('Mona-Sans Bold', 18), command=lambda: self.select_cleaningservice_menu('cleaningrequest'))
        self.main_cleaningservice_roomlist_label = ctk.CTkLabel(self.main_framebar_cleaningservice, text="ROOM NUMBER  :", font=ctk.CTkFont('Mona-Sans Bold', 25), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_cleaningservice_roomlist = ctk.CTkOptionMenu(self.main_framebar_cleaningservice, values=[''], width=100, height=25, font=ctk.CTkFont('Mona-Sans Bold', 20), corner_radius=30, anchor='center', dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6')
        cleaningserviceroom = []
        CTkScrollableDropdown(self.main_cleaningservice_roomlist, width=100, values=cleaningserviceroom)
        self.main_cleaningservice_proceed_button = ctk.CTkButton(self.main_framebar_cleaningservice, text='Proceed', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=150, height=35, bg_color='transparent', cursor='hand2')

        self.main_roomservice_cleaningtype_label.grid(row=1, column=0, sticky='news', padx=(40,0), pady=(15,0))
        self.main_cleaningservice_menu_frame.grid(row=2, column=0, padx=(25,0), pady=(10,0), sticky='nws')
        self.main_cleaningservice_vacantdirty_button.grid(row=0, column=0, padx=(10,5), pady=(10,10), sticky='news')
        self.main_cleaningservice_cleaningrequest_button.grid(row=0, column=1, padx=(5,5), pady=(10,10), sticky='news')
        self.main_cleaningservice_roomlist_label.grid(row=3, column=0, padx=(40,0), pady=(40,0), sticky='news')
        self.main_cleaningservice_roomlist.grid(row=3, column=0, padx=(280,0), pady=(40,0), sticky='w')
        self.main_cleaningservice_proceed_button.grid(row=4, column=0, padx=(0,0), pady=(80,30), sticky='ns')


        # ABOUT WIDGET

        self.main_about_heading_label = ctk.CTkLabel(self.main_frame_about, text="About", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_about_heading_label.grid(row=0, column=0, pady=(5,20), padx=20, sticky='news')
        self.main_about_desc_label =  ctk.CTkLabel(self.main_frame_about, text='Some information about us and the application', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_about_desc_label.place(x=410, y=45, anchor='center')

        self.main_about_logo = ctk.CTkLabel(self.main_frame_about, text='', image=self.logoshadow_image)
        self.main_about_logo.place(x=600, y=140, anchor='center')

        self.main_about_desc = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Medium', 15), text='"Hostay" merupakan sebuah program yang dirancang untuk membantu dan mempermudah\nresepsionis dalam melakukan pelayanan yang diberikan kepada tamu.\n\nDengan otomatisasi tugas-tugas seperti pemesanan, Check-in dan Check-out, dan manajemen inventaris.\n Sehingga hotel dapat mengelola operasinya dengan lebih efisien.')
        self.main_about_desc.place(x=600, y=260, anchor='center')

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

        self.main_about_incha.place(x=300, y=400, anchor='center')
        self.main_about_shadiq.place(x=600, y=400, anchor='center')
        self.main_about_syahrul.place(x=900, y=400, anchor='center')
        self.main_about_khanza.place(x=430, y=470, anchor='center')
        self.main_about_ajeng.place(x=770, y=470, anchor='center')
        self.main_about_bagas.place(x=600, y=540, anchor='center')

        self.main_about_incha_nim.place(x=300, y=415, anchor='center')
        self.main_about_shadiq_nim.place(x=600, y=415, anchor='center')
        self.main_about_syahrul_nim.place(x=900, y=415, anchor='center')
        self.main_about_khanza_nim.place(x=430, y=485, anchor='center')
        self.main_about_ajeng_nim.place(x=770, y=485, anchor='center')
        self.main_about_bagas_nim.place(x=600, y=555, anchor='center')


        self.main_about_copyright = ctk.CTkLabel(self.main_frame_about, font=ctk.CTkFont('Mona-Sans Bold', 14), text='Copyright © 2023 Hostay', text_color='#FFFFFF')
        self.main_about_copyright.place(x=600, y=635, anchor='center')
        self.main_about_credit = ctk.CTkLabel(self.main_frame_about, height=10, font=ctk.CTkFont('Mona-Sans', 12), text='by Kelompok 4', text_color='#4646DD', fg_color='transparent', bg_color='transparent')
        self.main_about_credit.place(x=600, y=655, anchor='center')

        self.select_frame('dashboard')
        self.select_foodservice_menu('appetizer')
        self.select_repairingservice_menu('electricity')
        self.select_cleaningservice_menu('vacantdirty')

    def select_frame(self, name):
        self.sidebar_button_dashboard.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'dashboard' else 'transparent')
        self.sidebar_button_checkinout.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkinout' else 'transparent')
        self.sidebar_button_checkin.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkin' or name == 'singleroom' or name == 'identityroomsingle' or name == 'doubleroom' or name == 'identityroomdouble' or name == 'suiteroom' or name == 'identityroomsuite' or name == 'presidentsuiteroom' or name == 'identityroompresidentsuite' else 'transparent')
        self.sidebar_button_checkout.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'checkout' or name == 'checkoutdetail' else 'transparent')
        self.sidebar_button_guestlist.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'guestlist' else 'transparent')
        self.sidebar_button_guesthistory.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'guesthistory' else 'transparent')
        self.sidebar_button_roomservice.configure(self.sidebar_frame, fg_color=('#3434A6') if name == 'roomservice' or name == 'foodservice' or name == 'repairingservice' or name == 'cleaningservice' else 'transparent')
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
        if name == "checkout":
            self.main_frame_checkout.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkout.grid_forget()
        if name == "checkoutdetail":
            self.main_frame_checkout_detail.grid(row=1, column=1, rowspan=3, ipady=320, padx=0, pady=0, sticky='news')
        else:
            self.main_frame_checkout_detail.grid_forget()
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

    def checkout_menu(self):
        self.select_frame('checkout')

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
            self.main_foodservice_appetizer_frame.grid(row=1, column=0, padx=(20,20), pady=(0,15), ipady=75, sticky='news')
        else:
            self.main_foodservice_appetizer_frame.grid_forget()   
        if name == "maincourse":
            self.main_foodservice_maincourse_frame.grid(row=1, column=0, padx=(20,20), pady=(0,15), ipady=75, sticky='news')
        else:
            self.main_foodservice_maincourse_frame.grid_forget()
        if name == "dessert":
            self.main_foodservice_dessert_frame.grid(row=1, column=0, padx=(20,20), pady=(0,15), ipady=75, sticky='news')
        else:
            self.main_foodservice_dessert_frame.grid_forget()
        if name == "drinks":
            self.main_foodservice_drinks_frame.grid(row=1, column=0, padx=(20,20), pady=(0,15), ipady=75, sticky='news')
        else:
            self.main_foodservice_drinks_frame.grid_forget()

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

    def select_repairingservice_menu(self, name):
        self.main_repairingservice_electricityrepair_button.configure(self.main_repairingservice_menu_frame, fg_color=('#3434A6') if name == 'electricity' else '#242432')
        self.main_repairingservice_furniturerepair_button.configure(self.main_repairingservice_menu_frame, fg_color=('#3434A6') if name == 'furniture' else '#242432')

    def select_cleaningservice_menu(self,name):
        self.main_cleaningservice_vacantdirty_button.configure(self.main_cleaningservice_menu_frame, fg_color=('#3434A6') if name == 'vacantdirty' else '#242432')
        self.main_cleaningservice_cleaningrequest_button.configure(self.main_cleaningservice_menu_frame, fg_color=('#3434A6') if name == 'cleaningrequest' else '#242432')

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
        self.identityform_roomtype_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_guestid_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text=f'Guest ID  :  {self.guestid}', font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='e')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformsingle, command=lambda room=roomnumber: self.checkin(room, 'single'), text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
        
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_rupiah_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Rp", font=ctk.CTkFont('Mona-Sans Medium', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsingle, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle ,width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's address here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=300, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsingle, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)

        self.identityform_roomtype_label.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_guestid_label.grid(row=1, column=2, sticky='news', padx=(0,40), pady=(5,0))
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
        self.identityform_rupiah_label.place(x=855, y=315)
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
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='nw', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='ne', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))
        
    def identityform_doubleroom(self, roomnumber):
        self.select_frame('identityroomdouble')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformdouble, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformdouble, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformdouble, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.doubleroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_guestid_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text=f'Guest ID  :  {self.guestid}', font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='e')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformdouble, command=lambda room=roomnumber: self.checkin(room, 'double'), text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
   
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_rupiah_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Rp", font=ctk.CTkFont('Mona-Sans Medium', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformdouble, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's address here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=300, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformdouble, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_label.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_guestid_label.grid(row=1, column=2, sticky='news', padx=(0,40), pady=(5,0))
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
        self.identityform_rupiah_label.place(x=855, y=315)
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
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='nw', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='ne', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))

    def identityform_suiteroom(self, roomnumber):
        self.select_frame('identityroomsuite')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformsuite, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformsuite, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformsuite, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.suiteroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_guestid_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text=f'Guest ID  :  {self.guestid}', font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='e')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformsuite, command=lambda room=roomnumber: self.checkin(room, 'suite'), text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
       
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_rupiah_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Rp", font=ctk.CTkFont('Mona-Sans Medium', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformsuite, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's address here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=300, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_label.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_guestid_label.grid(row=1, column=2, sticky='news', padx=(0,40), pady=(5,0))
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
        self.identityform_rupiah_label.place(x=855, y=315)
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
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='nw', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='ne', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))
        
    def identityform_presidentsuiteroom(self, roomnumber):
        self.select_frame('identityroompresidentsuite')
        self.main_checkin_label = ctk.CTkLabel(self.main_frame_checkin_identityformpresidentsuite, text="Check In", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='s')
        self.main_checkin_label.grid(row=0, column=0, pady=(5,5), padx=(0,70), ipadx=40, sticky='news')        
        self.main_checkin_fillform_label = ctk.CTkLabel(self.main_frame_checkin_identityformpresidentsuite, text='Fill the form below', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkin_fillform_label.place(x=392.5, y=45, anchor='center')
        self.main_checkin_back =  ctk.CTkButton(self.main_frame_checkin_identityformpresidentsuite, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.presidentsuiteroom_menu)
        self.main_checkin_back.place(x=25, y=33, anchor='center')
        self.identityform_roomtype_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text=f"ROOM NUMBER :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent')
        self.identityform_guestid_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text=f'Guest ID  :  {self.guestid}', font=ctk.CTkFont('Mona-Sans Bold', 30), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='e')
        self.identityform_checkin_button = ctk.CTkButton(self.main_framebar_checkin_identityformpresidentsuite, command=lambda room=roomnumber: self.checkin(room, 'president'), text='Check In', font=ctk.CTkFont('Mona-Sans Bold', 25), text_color='#FFFFFF',  fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=220, height=50, bg_color='transparent', cursor='hand2')
       
        self.identityform_firstname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="First Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_lastname_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Last Name", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_gender_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Gender", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_age_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Age", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nin_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Nationality ID Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_nohandphone_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Mobile Phone Number", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_email_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Email", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_address_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Address", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkindate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Check In Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_checkoutdate_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Check Out Date", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_rupiah_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Rp", font=ctk.CTkFont('Mona-Sans Medium', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.identityform_deposit_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Deposit", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.identityform_guestnote_label = ctk.CTkLabel(self.main_framebar_checkin_identityformpresidentsuite, text="Guest Note", font=ctk.CTkFont('Mona-Sans', 20), text_color=("#F0F0FF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.identityform_firstname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's first name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_lastname_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's last name here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30) 
        self.identityform_gender_entry = ctk.CTkOptionMenu(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, font=ctk.CTkFont('Mona-Sans Bold Italic', 15), dropdown_font=ctk.CTkFont('Mona-Sans', 15), fg_color='#292982', dropdown_fg_color='#1A1A23', dropdown_text_color='#F0F0FF', text_color='#FFFFFF', button_color='#4646DD', button_hover_color='#3434A6', dropdown_hover_color='#3434A6', values=['Male', 'Female'], corner_radius=30, anchor='center', dynamic_resizing=True)
        self.identityform_age_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's age here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nin_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's ID number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_nohandphone_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's mobile phone number here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_email_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's email here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_address_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's address here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkindate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-in date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_checkoutdate_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text='Enter check-out date (yyyy-mm-dd)', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_deposit_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=300, height=40, text_color='#FFFFFF', placeholder_text='Enter deposit ammount here', font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        self.identityform_guestnote_entry = ctk.CTkEntry(self.main_framebar_checkin_identityformpresidentsuite, width=341.5, height=40, text_color='#FFFFFF', placeholder_text="Enter guest's requests here", font=ctk.CTkFont('Mona-Sans Regular', 15), fg_color='#242531', border_width=0, corner_radius=30)
        
        self.identityform_roomtype_label.grid(row=1, column=0, sticky='news', padx=(35,0), pady=(25,20))
        self.identityform_guestid_label.grid(row=1, column=2, sticky='news', padx=(0,40), pady=(5,0))
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
        self.identityform_rupiah_label.place(x=855, y=315)
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
        self.identityform_checkindate_entry.grid(row=3, column=2, sticky='nw', padx=(65,35), pady=(3,15))
        self.identityform_checkoutdate_entry.grid(row=5, column=2, sticky='new', padx=(65,35), pady=(3,15))
        self.identityform_deposit_entry.grid(row=7, column=2, sticky='ne', padx=(65,35), pady=(3,15))
        self.identityform_guestnote_entry.grid(row=9, column=2, rowspan=2, sticky='new', padx=(65,35), pady=(3,15))

    def checkout_detail(self, roomnumber):
        self.select_frame('checkoutdetail')
        self.main_checkout_label = ctk.CTkLabel(self.main_frame_checkout_detail, text="Check Out", font=ctk.CTkFont('Mona-Sans Bold', 50), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkout_label.place(x=76.5, y=5)
        self.main_checkout_fillform_label = ctk.CTkLabel(self.main_frame_checkout_detail, text='Checking out and paying the bills', font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#B6B6C6"), fg_color='transparent', bg_color='transparent', anchor='sw')
        self.main_checkout_fillform_label.place(x=510, y=45, anchor='center')
        self.main_checkout_back = ctk.CTkButton(self.main_frame_checkout_detail, width=20, height=20, fg_color='transparent', bg_color='transparent', text='', hover_color='#0C0B10', cursor='hand2', image=self.back_image, command=self.checkout_menu)
        self.main_checkout_back.place(x=25, y=33, anchor='center')
        self.main_checkout_button = ctk.CTkButton(self.main_framebar_checkout_billingdetail, command=lambda room=roomnumber: self.checkout(room), text='Check Out', font=ctk.CTkFont('Mona-Sans Bold', 20), text_color='#FFFFFF', fg_color='#4646DD', hover_color='#3434A6', corner_radius=25, width=180, height=40, bg_color='transparent', cursor='hand2')
        self.main_checkout_button.place(relx=0.85, rely=0.92, anchor='center')
        self.main_checkout_roomnumber_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text=f"ROOM NUMBER  :   {roomnumber}", font=ctk.CTkFont('Mona-Sans Bold', 25), text_color="#B6B6C6", fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_guestid_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text=f'Guest ID  :  {self.guestid}', font=ctk.CTkFont('Mona-Sans SemiBold', 25), text_color="#9696A4", fg_color='transparent', bg_color='transparent', anchor='w')
    
        if hasattr(self, 'main_checkout_billingdetail_roomtype'):
            self.main_checkout_billingdetail_roomtype.grid_forget()
            self.main_checkout_billingdetail_quantity.grid_forget()
            self.main_checkout_billingdetail_total.grid_forget()
            self.main_checkout_billingdetail_items.grid_forget()
            self.main_checkout_billingdetail_itemprice.grid_forget()
            self.main_checkout_billingdetail_itemquantity.grid_forget()
            self.main_checkout_billingdetail_itemtotal.grid_forget()
            self.main_checkout_billingdetail_subtotal.grid_forget()
            self.main_checkout_billingdetail_ppn.grid_forget()
            self.main_checkout_billingdetail_deposit.grid_forget()
            self.main_checkout_billingdetail_grandtotal.grid_forget()

        self.main_checkout_checkindetail_button = ctk.CTkButton(self.main_framebar_checkout_detail, corner_radius=25, width=180, height=45, text="Check In Detail", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_checkout_checkindetail_button.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(15,15), sticky='news')
        self.main_checkout_date_frame = ctk.CTkFrame(self.main_framebar_checkout_detail, corner_radius=25, width=180, height=100, fg_color='#191922', bg_color='transparent', border_color='#171720', border_width=3)
        self.main_checkout_date_frame.grid(row=9, column=0, sticky='news', padx=(20,20), pady=(30,0))
        self.main_checkout_date_frame.grid_columnconfigure(0, weight=1)

        self.main_checkout_checkindetail_name_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Bold', 22), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_checkindetail_age_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#C3C3D3"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_checkindetail_gender_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#BBBBCC"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_checkindetail_nin_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#AEAEBD"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_checkindetail_phonenum_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#A3A3B1"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_checkindetail_email_label = ctk.CTkLabel(self.main_framebar_checkout_detail, text="", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#9797A5"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.main_checkout_checkindetail_checkindate_label = ctk.CTkLabel(self.main_checkout_date_frame, text="Check In Date", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.main_checkout_checkindetail_checkindate_button = ctk.CTkButton(self.main_checkout_date_frame, text="", font=ctk.CTkFont('Mona-Sans Bold Wide Italic', 20), text_color=("#ACAEC3"), fg_color='#242432', border_color='#1E1E2A', hover_color='#242432', border_width=3, anchor="center", corner_radius=30)
        self.main_checkout_checkindetail_checkoutdate_label = ctk.CTkLabel(self.main_checkout_date_frame, text="Check Out Date", font=ctk.CTkFont('Mona-Sans SemiBold', 20), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='center')
        self.main_checkout_checkindetail_checkoutdate_button = ctk.CTkButton(self.main_checkout_date_frame, text="", font=ctk.CTkFont('Mona-Sans Bold Wide Italic', 20), text_color=("#9C9EB3"), fg_color='#242432', border_color='#1E1E2A', hover_color='#242432', border_width=3, anchor="center", corner_radius=30)
        
        self.main_checkout_roomnumber_label.grid(row=1, column=0, sticky='news', padx=(35,35), pady=(10,0))
        self.main_checkout_guestid_label.grid(row=2, column=0, sticky='news', padx=(35,35), pady=(0,20))
        self.main_checkout_checkindetail_name_label.grid(row=3, column=0, sticky='news', padx=(35,50), pady=(20,0))
        self.main_checkout_checkindetail_age_label.grid(row=4, column=0, sticky='news', padx=(35,50), pady=(0,0))
        self.main_checkout_checkindetail_gender_label.grid(row=5, column=0, sticky='news', padx=(35,50), pady=(0,0))
        self.main_checkout_checkindetail_nin_label.grid(row=6, column=0, sticky='news', padx=(35,50), pady=(0,0))
        self.main_checkout_checkindetail_phonenum_label.grid(row=7, column=0, sticky='news', padx=(35,50), pady=(0,0))
        self.main_checkout_checkindetail_email_label.grid(row=8, column=0, sticky='news', padx=(35,50), pady=(0,0))
        
        self.main_checkout_checkindetail_checkindate_label.grid(row=0, column=0, sticky='news', padx=(15,15), pady=(10,0))
        self.main_checkout_checkindetail_checkindate_button.grid(row=1, column=0, sticky='news', padx=(15,15), pady=(0,0))
        self.main_checkout_checkindetail_checkoutdate_label.grid(row=2, column=0, sticky='news', padx=(15,15), pady=(15,0))
        self.main_checkout_checkindetail_checkoutdate_button.grid(row=3, column=0, sticky='news', padx=(15,15), pady=(0,15))

        self.cursor.execute(f"SELECT first_name, last_name, age, gender, nin, phone_number, email, check_in_date, check_out_date, deposit FROM guest WHERE room_num = {roomnumber}")
        guest_data = self.cursor.fetchone()

        if guest_data:
            first_name, last_name, age, gender, nin, phone_number, email, check_in_date, check_out_date, deposit = guest_data
            full_name = f"{first_name} {last_name}"

            self.main_checkout_checkindetail_name_label.configure(text=full_name)
            self.main_checkout_checkindetail_age_label.configure(text=f"Age\t:    {age}")
            self.main_checkout_checkindetail_gender_label.configure(text=f"Gender\t:    {gender}")
            self.main_checkout_checkindetail_nin_label.configure(text=f"NIN\t:    {nin}")
            self.main_checkout_checkindetail_phonenum_label.configure(text=f"Phone\t:    {phone_number}")
            self.main_checkout_checkindetail_email_label.configure(text=f"Email\t:    {email}")
            self.main_checkout_checkindetail_checkindate_button.configure(text=check_in_date)
            self.main_checkout_checkindetail_checkoutdate_button.configure(text=check_out_date)
        
        self.main_checkout_billingdetail_frame = ctk.CTkButton(self.main_framebar_checkout_billingdetail, corner_radius=25, width=200, height=45, text="Billing Detail", font=ctk.CTkFont('Mona-Sans Bold', 30), fg_color='#191922', bg_color='transparent', hover_color='#191922', text_color="#FFFFFF", border_color='#171720', border_width=3)
        self.main_checkout_billingdetail_frame.grid(row=0, column=0, columnspan=4, padx=(20,20), pady=(15,20), sticky='news')

        self.main_checkout_billingdetail_costdetail_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Cost Details", font=ctk.CTkFont('Mona-Sans Bold', 35), text_color=("#FFFFFF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_costdetail_label.grid(row=1, column=0, columnspan=2, sticky='news', padx=(35,0), pady=(0,0))
        
        self.main_checkout_billingdetail_roomtype_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Room Type", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_orderlist_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Order List", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_price_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Price", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_quantity_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Quantity", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_total_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Total", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        
        self.main_checkout_billingdetail_roomtype_label.grid(row=2, column=0, sticky='nws', padx=(35,0), pady=(10,0))
        self.main_checkout_billingdetail_orderlist_label.grid(row=4, column=0, sticky='nws', padx=(35,0), pady=(20,0))
        self.main_checkout_billingdetail_price_label.grid(row=2, column=1, sticky='nws', padx=(0,0), pady=(20,0))
        self.main_checkout_billingdetail_quantity_label.grid(row=2, column=2, sticky='nws', padx=(50,60), pady=(20,0))
        self.main_checkout_billingdetail_total_label.grid(row=2, column=3, sticky='nws', padx=(0,60), pady=(20,0))


        if 1 <= roomnumber <= 10:
            room_type_color = '#FFDC99'
            room_type_text = 'Single Room'
            price_per_night = 300000
        elif 11 <= roomnumber <= 20:
            room_type_color = '#CE5700'  
            room_type_text = 'Double Room'
            price_per_night = 450000
        elif 21 <= roomnumber <= 26:
            room_type_color = '#BBCDCA'  
            room_type_text = 'Suite Room'
            price_per_night = 550000
        elif 27 <= roomnumber <= 30:
            room_type_color = '#FFB800' 
            room_type_text = 'President Suite Room'
            price_per_night = 850000

        check_in_date_str = str(check_in_date)
        check_out_date_str = str(check_out_date)

        check_in_date = datetime.strptime(check_in_date_str, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out_date_str, "%Y-%m-%d")
        quantity = (check_out_date - check_in_date).days
        total_price = quantity * price_per_night

        total_food_cost = 0
        ppn_percentage = 0.1
        subtotal = total_price + total_food_cost
        ppn_amount = total_price * ppn_percentage
        grand_total = total_price + ppn_amount - deposit
        
        self.main_checkout_billingdetail_roomtype = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=room_type_text, font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color=room_type_color, fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_price = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"Rp {price_per_night:,.0f}", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_quantity = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"{quantity} Night", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_total = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"Rp {total_price:,.0f}", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        
        self.main_checkout_billingdetail_items = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text='-', font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color='#B3B4BF', fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_itemprice = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text='-', font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color='#B3B4BF', fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_itemquantity = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text='-', font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color='#B3B4BF', fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_itemtotal = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text='-', font=ctk.CTkFont('Mona-Sans SemiBold', 14), text_color='#B3B4BF', fg_color='transparent', bg_color='transparent', anchor='w')

        self.main_checkout_billingdetail_roomtype.grid(row=3, column=0, sticky='nws', padx=(35,0), pady=(0,0))
        self.main_checkout_billingdetail_price.grid(row=3, column=1, sticky='nws', padx=(0,0), pady=(0,0))
        self.main_checkout_billingdetail_quantity.grid(row=3, column=2, sticky='nws', padx=(50,60), pady=(0,0))
        self.main_checkout_billingdetail_total.grid(row=3, column=3, sticky='nws', padx=(0,60), pady=(0,0))

        self.main_checkout_billingdetail_items.grid(row=5, column=0, sticky='nws', padx=(35,0), pady=(10,0))
        self.main_checkout_billingdetail_itemprice.grid(row=5, column=1, sticky='nws', padx=(0,0), pady=(10,0))
        self.main_checkout_billingdetail_itemquantity.grid(row=5, column=2, sticky='nws', padx=(50,60), pady=(10,0))
        self.main_checkout_billingdetail_itemtotal.grid(row=5, column=3, sticky='nws', padx=(0,60), pady=(10,0))

        self.main_checkout_billingdetail_subtotal_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Sub-Total", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_ppn_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="PPn 10%", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_deposit_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Deposit", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_grandtotal_label = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text="Grand Total", font=ctk.CTkFont('Mona-Sans Bold', 20), text_color=("#D6D7E2"), fg_color='transparent', bg_color='transparent', anchor='w')
        
        self.main_checkout_billingdetail_subtotal = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f'Rp {subtotal:,.0f}', font=ctk.CTkFont('Mona-Sans SemiBold', 17), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_ppn = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"Rp {ppn_amount:,.0f}", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_deposit = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"Rp {deposit:,.0f}", font=ctk.CTkFont('Mona-Sans Medium', 14), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')
        self.main_checkout_billingdetail_grandtotal = ctk.CTkLabel(self.main_framebar_checkout_billingdetail, text=f"Rp {grand_total:,.0f}", font=ctk.CTkFont('Mona-Sans SemiBold', 17), text_color=("#B3B4BF"), fg_color='transparent', bg_color='transparent', anchor='w')

        self.main_checkout_billingdetail_subtotal_label.grid(row=6, column=1, sticky='nws', padx=(0,0), pady=(30,0))
        self.main_checkout_billingdetail_ppn_label.grid(row=7, column=1, sticky='nws', padx=(0,0), pady=(5,0))
        self.main_checkout_billingdetail_deposit_label.grid(row=8, column=1, sticky='nws', padx=(0,0), pady=(0,0))
        self.main_checkout_billingdetail_grandtotal_label.grid(row=9, column=1, sticky='nws', padx=(0,0), pady=(5,0))

        self.main_checkout_billingdetail_subtotal.grid(row=6, column=3, sticky='nws', padx=(0,60), pady=(30,0))
        self.main_checkout_billingdetail_ppn.grid(row=7, column=3, sticky='nws', padx=(0,60), pady=(5,0))
        self.main_checkout_billingdetail_deposit.grid(row=8, column=3, sticky='nws', padx=(0,60), pady=(0,0))
        self.main_checkout_billingdetail_grandtotal.grid(row=9, column=3, sticky='nws', padx=(0,60), pady=(5,0))

    def update_room_button(self):
        
        for data in self.room_status:
            self.room_id, self.status = data
            if self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Occupied':
                self.room_button[self.room_id].configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans Bold', 25))
                self.roomlist = [f"{room[0]:02d}" for room in self.room_status if room[1] == 'Occupied']
                CTkScrollableDropdown(self.main_roomservice_roomoption, width=100, double_click=False, resize=False, y=-250, values=self.roomlist)

                
                if 1 <= int(self.room_id) <= 10:
                    text_color = '#FFDC99'
                elif 11 <= int(self.room_id) <= 20:
                    text_color = '#CE5700'
                elif 21 <= int(self.room_id) <= 25:
                    text_color = '#BBCDCA'
                elif 26 <= int(self.room_id) <= 30:
                    text_color = '#FFB800'

                formatted_room_id = str(self.room_id).zfill(2)

                self.room_checkout_button[self.room_id].configure(state='normal', text=formatted_room_id, text_color=text_color, font=ctk.CTkFont('Mona-Sans ExtraBold', 45))

            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Dirty':
                self.room_button[self.room_id].configure(state='disabled', text='Dirty', font=ctk.CTkFont('Mona-Sans Bold', 25))
                self.room_checkout_button[self.room_id].configure(state='disabled', text='Dirty', text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Bold', 15))

            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button and self.status == 'Service':
                formatted_room_id = str(self.room_id).zfill(2)
                self.room_button[self.room_id].configure(state='disabled', text='Unavailable', font=ctk.CTkFont('Mona-Sans Bold', 25))
                self.room_checkout_button[self.room_id].configure(state='normal', text=formatted_room_id, font=ctk.CTkFont('Mona-Sans ExtraBold', 45))
                
            elif self.room_id in self.room_button and self.room_id in self.room_checkout_button:
                self.room_button[self.room_id].configure(state='normal')
                self.room_checkout_button[self.room_id].configure(state='disabled', text='Ready', text_color='#FFFFFF', font=ctk.CTkFont('Mona-Sans Bold', 15))

        print('Berhasil Update')

    def update_room_status(self):
        try:
            self.cursor.execute("SELECT id, status FROM kamar")
            self.room_status = self.cursor.fetchall()

            self.ready_rooms = 0
            self.occupied_rooms = 0
            self.dirty_rooms = 0
            self.service_rooms = 0

            self.room_labels = {
                1: self.room01_frame_status,
                2: self.room02_frame_status,
                3: self.room03_frame_status,
                4: self.room04_frame_status,
                5: self.room05_frame_status,
                6: self.room06_frame_status,
                7: self.room07_frame_status,
                8: self.room08_frame_status,
                9: self.room09_frame_status,
                10: self.room10_frame_status,
                11: self.room11_frame_status,
                12: self.room12_frame_status,
                13: self.room13_frame_status,
                14: self.room14_frame_status,
                15: self.room15_frame_status,
                16: self.room16_frame_status,
                17: self.room17_frame_status,
                18: self.room18_frame_status,
                19: self.room19_frame_status,
                20: self.room20_frame_status,
                21: self.room21_frame_status,
                22: self.room22_frame_status,
                23: self.room23_frame_status,
                24: self.room24_frame_status,
                25: self.room25_frame_status,
                26: self.room26_frame_status,
                27: self.room27_frame_status,
                28: self.room28_frame_status,
                29: self.room29_frame_status,
                30: self.room30_frame_status,
            }

            self.room_indicator = {
                1: self.room01_frame_indicator,
                2: self.room02_frame_indicator,
                3: self.room03_frame_indicator,
                4: self.room04_frame_indicator,
                5: self.room05_frame_indicator,
                6: self.room06_frame_indicator,
                7: self.room07_frame_indicator,
                8: self.room08_frame_indicator,
                9: self.room09_frame_indicator,
                10: self.room10_frame_indicator,
                11: self.room11_frame_indicator,
                12: self.room12_frame_indicator,
                13: self.room13_frame_indicator,
                14: self.room14_frame_indicator,
                15: self.room15_frame_indicator,
                16: self.room16_frame_indicator,
                17: self.room17_frame_indicator,
                18: self.room18_frame_indicator,
                19: self.room19_frame_indicator,
                20: self.room20_frame_indicator,
                21: self.room21_frame_indicator,
                22: self.room22_frame_indicator,
                23: self.room23_frame_indicator,
                24: self.room24_frame_indicator,
                25: self.room25_frame_indicator,
                26: self.room26_frame_indicator,
                27: self.room27_frame_indicator,
                28: self.room28_frame_indicator,
                29: self.room29_frame_indicator,
                30: self.room30_frame_indicator,
            }

            self.color_status = {
                'Ready': '#0FBFB0',
                'Occupied': '#3C58F7',
                'Dirty': '#9031D3',
                'Service': '#B52483',
            }
            
            for data in self.room_status:
                self.room_id, self.status = data

                if self.room_id in self.room_labels:
                    self.room_labels[self.room_id].configure(text=self.status)

                if self.room_id in self.room_indicator and self.status in self.color_status:
                    color = self.color_status[self.status]
                    self.room_indicator[self.room_id].configure(fg_color=color)

                if self.status == 'Ready':
                    self.ready_rooms += 1
                elif self.status == 'Occupied':
                    self.occupied_rooms += 1
                elif self.status == 'Dirty':
                    self.dirty_rooms += 1
                elif self.status == 'Service':
                    self.service_rooms += 1
                    self.occupied_rooms += 1

            
            self.main_dashboard_vacantrooms_label.configure(text=f"\n\n                   {self.ready_rooms}")
            self.main_dashboard_occupiedrooms_label.configure(text=f"\n\n                   {self.occupied_rooms}")
            self.main_dashboard_vacantdirty_label.configure(text=f"\n\n                   {self.dirty_rooms}")
            self.main_dashboard_requiringservice_label.configure(text=f"\n\n                   {self.service_rooms}")

        except Exception as e:
            print(f"Error: {e}")

    def checkin(self, roomnumber, roomtype):
        if self.identityform_firstname_entry.get() == '' or self.identityform_age_entry.get() == '' or self.identityform_gender_entry.get() == '' or self.identityform_nin_entry.get() == '' or self.identityform_nohandphone_entry.get() == '' or self.identityform_email_entry.get() == '' or self.identityform_address_entry.get() == '' or self.identityform_checkindate_entry.get() == '' or self.identityform_checkoutdate_entry.get() == '' or self.identityform_deposit_entry.get() == '':
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), message="Fill all the forms first.", icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=350, height=200)
        elif not all(char.isalpha() or char == '-' or char.isspace() for char in self.identityform_firstname_entry.get()):
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="First name must be alphabetic and cannot contain numbers.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif not all(char.isalpha() or char == '-' or char.isspace() for char in self.identityform_lastname_entry.get()):
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Last name must be alphabetic and cannot contain numbers.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif not self.identityform_age_entry.get().isdigit() or len(self.identityform_age_entry.get()) > 2 or len(self.identityform_age_entry.get()) < 1:
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Age must be 1-2 digits and cannot be in a letter form", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225) 
        elif not self.identityform_nin_entry.get().isdigit() or len(self.identityform_nin_entry.get()) != 16:
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Nationality ID Number must be 16 digit and cannot be in a letter form.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)  
        elif not self.identityform_nohandphone_entry.get().isdigit() or not (10 <= len(self.identityform_nohandphone_entry.get()) <= 13):
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Phone number must be between 10 and 13 digit and cannot be in a letter form.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif '@' not in self.identityform_email_entry.get():
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Invalid email form, example : example@example.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif not self.dateformatvalidation(self.identityform_checkindate_entry.get()):
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Enter valid check-in date format (yyyy-mm-dd).", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif not self.dateformatvalidation(self.identityform_checkoutdate_entry.get()):
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Enter valid check-out date format (yyyy-mm-dd).", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
        elif not self.identityform_deposit_entry.get().isdigit():
            self.messageboxwarning = CTkMessagebox(self, title="Warning!", message="Enter deposit with number.", font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#FF473B', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Warning.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)  
        else:
            try:
                self.messageboxconfirm = CTkMessagebox(self, title="Check In Confirmation", font=ctk.CTkFont('Mona-Sans Medium', 14), justify='center',corner_radius=20, text_color='#FFFFFF', title_color='#B6B6C6', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), message="Are you sure want to Check in?", icon='Aset Projek/Question.png', cancel_button='None', icon_size=(80,80), button_height=40, button_width=180, option_focus=1, option_1="Yes", option_2='Cancel', width=450, height=250) 
                if self.messageboxconfirm.get() == "Yes":
                    self.messagebox = CTkMessagebox(self, title="Success", message="Check In Successful!",font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#3AE942', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Checked.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)
                    self.cursor.execute("insert into guest values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.guestid,
                                                                                                roomnumber,
                                                                                                self.identityform_firstname_entry.get(),
                                                                                                self.identityform_lastname_entry.get(),
                                                                                                self.identityform_age_entry.get(),
                                                                                                self.identityform_gender_entry.get(),
                                                                                                self.identityform_nin_entry.get(),
                                                                                                self.identityform_nohandphone_entry.get(),
                                                                                                self.identityform_email_entry.get(),
                                                                                                self.identityform_address_entry.get(),
                                                                                                self.identityform_checkindate_entry.get(),
                                                                                                self.identityform_checkoutdate_entry.get(),
                                                                                                self.identityform_deposit_entry.get(),
                                                                                                self.identityform_guestnote_entry.get(),
                                                                                            ))
                    
                    self.cursor.execute(f"UPDATE kamar SET status='Occupied' WHERE id=%s", (roomnumber,)) 
                    self.guestid +=1
                    
                    self.room_indicator[self.room_id].after(1000, self.update_room_status)
                    self.room_labels[self.room_id].after(1000, self.update_room_status)
                    self.room_button[self.room_id].after(1000, self.update_room_button)
                    
                    self.update_guest_history_table()
                    self.update_guest_list_table()

                    self.conn.commit()    
                    print('Berhasil Input Database')

                    if self.messagebox.get() == "Ok":
                        if roomtype == "single":   
                            self.select_frame('singleroom')
                        elif roomtype == "double":
                            self.select_frame('doubleroom')
                        elif roomtype == "suite":
                            self.select_frame('suiteroom')
                        elif roomtype == "president":
                            self.select_frame('presidentsuiteroom')
                if self.messageboxconfirm.get() == "Cancel":
                    pass
            
            except Exception as es:
                print(f'Gagal: {es}')
    
    def update_guest_history_table(self):
        self.cursor.execute("SELECT * FROM guest ORDER BY id DESC LIMIT 1; ")
        rows = self.cursor.fetchall()

        self.guest_history = []

        for row in rows:
            guest_name = f"{row[2]} {row[3]}"  
        
            self.guest_history.append([
                row[0],  
                row[1],  
                guest_name,
                row[4],  
                row[5], 
                row[6],  
                row[7],  
                row[8], 
                row[9],  
                row[10],  
                row[11]   
            ])

        print(self.guest_history)
        self.main_guesthistory_table.add_row(*self.guest_history)

    def update_guest_list_table(self):

        self.cursor.execute("SELECT id, status FROM kamar")
        room_statuses = self.cursor.fetchall()
        print(room_statuses)

        self.cursor.execute("SELECT room_num, first_name, last_name, check_in_date, check_out_date, guest_note FROM guest")
        self.guest_datas = self.cursor.fetchall()

        for guest_data in self.guest_datas:
            room_num = guest_data[0]
            guest_full_name = f"{guest_data[1]} {guest_data[2]}"
            check_in_date = guest_data[3]
            check_out_date = guest_data[4]
            guest_note = guest_data[5]

            self.main_guestlist_table.insert(room_num, 2, guest_full_name)
            self.main_guestlist_table.insert(room_num, 3, check_in_date)
            self.main_guestlist_table.insert(room_num, 4, check_out_date)
            self.main_guestlist_table.insert(room_num, 6, guest_note)
            
        for room_status in room_statuses:
            room_number = room_status[0]
            self.statuses = room_status[1]

            self.main_guestlist_table.insert(room_number, 5, self.statuses)

            if self.statuses == 'Dirty':
                self.main_guestlist_table.delete(room_number, 2)    
                self.main_guestlist_table.delete(room_number, 3)    
                self.main_guestlist_table.delete(room_number, 4)    
                self.main_guestlist_table.delete(room_number, 6)  


    def dateformatvalidation(self, date_string):
        try:
            self.datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    def checkout(self, roomnumber):
        try:
            self.messageboxconfirm = CTkMessagebox(self, title="Check Out Confirmation", font=ctk.CTkFont('Mona-Sans Medium', 14), justify='center',corner_radius=20, text_color='#FFFFFF', title_color='#B6B6C6', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), message="Are you sure want to Check Out?", icon='Aset Projek/Question.png', cancel_button='None', icon_size=(80,80), button_height=40, button_width=180, option_focus=1, option_1="Yes", option_2='Cancel', width=450, height=250) 
            if self.messageboxconfirm.get() == "Yes":
                self.messagebox = CTkMessagebox(self, title="Success", message="Check Out Successful!",font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#3AE942', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Checked.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)    
                
                self.cursor.execute(f"UPDATE kamar SET status='Dirty' WHERE id=%s", (roomnumber,))
                
                self.room_indicator[self.room_id].after(1000, self.update_room_status)
                self.room_labels[self.room_id].after(1000, self.update_room_status)
                self.room_button[self.room_id].after(1000, self.update_room_button)
    
                self.cursor.execute("SELECT id, status FROM kamar")
                room_statuses = self.cursor.fetchall()
                print(room_statuses)

                self.cursor.execute("SELECT room_num, first_name, last_name, check_in_date, check_out_date, guest_note FROM guest")
                self.guest_datas = self.cursor.fetchall()
                for guest_data in self.guest_datas:
                    room_num = guest_data[0]
                    guest_full_name = f"{guest_data[1]} {guest_data[2]}"
                    check_in_date = guest_data[3]
                    check_out_date = guest_data[4]
                    guest_note = guest_data[5]

                    self.main_guestlist_table.insert(room_num, 2, guest_full_name)
                    self.main_guestlist_table.insert(room_num, 3, check_in_date)
                    self.main_guestlist_table.insert(room_num, 4, check_out_date)
                    self.main_guestlist_table.insert(room_num, 6, guest_note)
                    
                for room_status in room_statuses:
                    room_number = room_status[0]
                    self.statuses = room_status[1]

                    self.main_guestlist_table.insert(room_number, 5, self.statuses)

                    if self.statuses == 'Dirty':
                        self.main_guestlist_table.delete(room_number, 2)    
                        self.main_guestlist_table.delete(room_number, 3)    
                        self.main_guestlist_table.delete(room_number, 4)    
                        self.main_guestlist_table.delete(room_number, 6)

                self.conn.commit()    
                print('Berhasil Checkout')
                
                if self.messagebox.get() == "Ok":   
                    self.select_frame('checkout')
                    
            if self.messageboxconfirm.get() == "Cancel":
                pass

        except Exception as es:
                print(f'Gagal: {es}')

    def servicerequest(self, roomnumber, servicetype):
        try:
            self.messageboxconfirm = CTkMessagebox(self, title="Service Request Confirmation", font=ctk.CTkFont('Mona-Sans Medium', 14), justify='center',corner_radius=20, text_color='#FFFFFF', title_color='#B6B6C6', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), message="Are you sure want to request a Service?", icon='Aset Projek/Question.png', cancel_button='None', icon_size=(80,80), button_height=40, button_width=180, option_focus=1, option_1="Yes", option_2='Cancel', width=450, height=250) 
            if self.messageboxconfirm.get() == "Yes":
                self.messagebox = CTkMessagebox(self, title="Success", message="Requesting service Successful!",font=ctk.CTkFont('Mona-Sans Medium', 14), corner_radius=20, text_color='#FFFFFF', title_color='#3AE942', sound=True, border_color='#15151F', border_width=4, fg_color='#181823', bg_color='#181823', button_hover_color='#4646DD', button_color=('#181823','#181823'), button_text_color=('#FFFFFF','#FFFFFF'), icon='Aset Projek/Checked.png', cancel_button='None', icon_size=(70,70), option_focus=1, option_1="Ok", width=400, height=225)    
                
                self.cursor.execute(f"UPDATE kamar SET status='Service' WHERE id=%s", (roomnumber,))

                self.service_rooms += 1
                self.main_dashboard_requiringservice_label.configure(text=f"\n\n                   {self.service_rooms}")
                
                self.room_indicator[self.room_id].after(1000, self.update_room_status)
                self.room_labels[self.room_id].after(1000, self.update_room_status)
                self.room_button[self.room_id].after(1000, self.update_room_button)
                
                self.update_guest_list_table()

                self.conn.commit()    
                print('Berhasil Requesting Service')
                
                if self.messagebox.get() == "Ok":   
                    pass
                    
            if self.messageboxconfirm.get() == "Cancel":
                pass

        except Exception as es:
                print(f'Gagal: {es}')
    
    def add_to_order(self, item_name, quantity):
        existing_item = next((item for item in self.orders if item['item_name'] == item_name), None)
        if existing_item is None:
            self.orders.append({'item_name': item_name, 'quantity': quantity})
        else:
            existing_item['quantity'] += quantity
        self.update_order_scrollable_frame()

    def create_button(self, frame, item_name, image, row, column, valuex1, valuex2, valuey1, valuey2):
        button = ctk.CTkButton(frame, command=lambda name=item_name: self.item_name(name, button), cursor='hand2', hover_color='#4646DD', fg_color='transparent', image=image, text='')
        button.grid(row=row, column=column, padx=(valuex1,valuex2), pady=(valuey1,valuey2))

        return button     

    def item_name(self, name, button):
        self.add_to_order(f'{name}', 1)
        button.configure(state='disabled')
        
    def update_order_scrollable_frame(self):
        self.main_foodservice_order_scrollableframe.grid_forget()       
        order_list = {
            "Cireng": 14000,
            "Risoles": 20000,
            "Tahu Isi": 18000,
            "Tempe Mendoan": 14000,
            "Kroket Kentang": 20000,
            "Ayam Betutu": 51000,
            "Ayam Sambal Matah": 37000,
            "Ayam Taliwang": 45000,
            "Mie Goreng": 25000,
            "Nasi Goreng": 27000,
            "Sate Ayam": 55000,
            "Sop Buntut": 66000,
            "Es Campur": 17000,
            "Es Dawet": 18000,
            "Es Pisang Ijo": 20000,
            "Klepon": 17000,
            "Pisang Keju": 20000,
            "Es Jeruk": 15000,
            "Es Kelapa": 23000,
            "Es Teh": 13000,
            "Kopi": 20000,
            "Susu": 19000,
        }

        for i, order in enumerate(self.orders):
            item_name = order['item_name']
            quantity = order['quantity']
            price_per_item = order_list.get(item_name, 0)
            total_price = quantity * price_per_item

            item_label_text = f"{item_name}"
            quantity_label_text = str(quantity)
            price_label_text = f"Rp {total_price:,.0f}"
            start_row = 1
            
            if hasattr(self, f"item_label_{i}"):
                self.item_label.configure(text='')
                self.quantity_label.configure(text='')
            else:
                self.item_label = ctk.CTkLabel(self.main_foodservice_order_scrollableframe, text=item_label_text, font=ctk.CTkFont('Mona-Sans Medium', 14), text_color='#B3B4BF', fg_color='#191922', bg_color='transparent', anchor='w')
                self.item_label.grid(row=start_row + i, column=0, sticky='nws', pady=(0,0), padx=(0,0))

                self.quantity_label = ctk.CTkLabel(self.main_foodservice_order_scrollableframe, text=quantity_label_text, font=ctk.CTkFont('Mona-Sans Medium', 14), text_color='#B3B4BF', fg_color='#191922', bg_color='transparent', anchor='w')
                self.quantity_label.grid(row=start_row + i, column=1, sticky='news', padx=(40,0))

                self.add_button = ctk.CTkButton(self.main_foodservice_order_scrollableframe, text='+', width=25, fg_color='#4646DD', hover_color='#3434A6', font=ctk.CTkFont('Mona-Sans Medium', 14), anchor='center', command=lambda i=i: self.update_quantity(i, 'add'))
                self.add_button.grid(row=start_row + i, column=1, sticky='nws', pady=(2,0), padx=(0,0))

                self.subtract_button = ctk.CTkButton(self.main_foodservice_order_scrollableframe, text='-', width=25, fg_color='#4646DD', hover_color='#3434A6', font=ctk.CTkFont('Mona-Sans Medium', 14), anchor='center', command=lambda i=i: self.update_quantity(i, 'subtract'))
                self.subtract_button.grid(row=start_row + i, column=1, sticky='ns', pady=(2,0), padx=(60,0))

    def update_quantity(self, index, action):
        if action == 'add':
            self.orders[index]['quantity'] += 1
            self.item_label.configure(text='')
            self.quantity_label.configure(text='')
        elif action == 'subtract' and self.orders[index]['quantity'] > 0:
            self.orders[index]['quantity'] -= 1
            self.item_label.configure(text='')
            self.quantity_label.configure(text='')
        
        self.update_order_scrollable_frame()

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
        self.main_frame_checkout.grid_forget()
        self.main_frame_checkin_singleroom.grid_forget()
        self.main_frame_checkin_doubleroom.grid_forget()
        self.main_frame_checkin_suiteroom.grid_forget()
        self.main_frame_checkin_presidentsuiteroom.grid_forget()
        self.main_frame_checkin_identityformsingle.grid_forget()
        self.main_frame_checkin_identityformdouble.grid_forget()
        self.main_frame_checkin_identityformsuite.grid_forget()
        self.main_frame_checkin_identityformpresidentsuite.grid_forget() 
        self.main_frame_guestlist.grid_forget()
        self.main_frame_guesthistory.grid_forget()
        self.main_frame_roomservice.grid_forget()
        self.main_frame_foodservice.grid_forget()
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
        self.skip = False

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