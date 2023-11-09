import algo, fern_key
import tkinter as tk
import simple_crypto as crypto
import os
from os import environ, path, mkdir
from tkinter import filedialog, messagebox, Menu, Toplevel
import cryptography

color = "black"
text_color = "white"

class GUI:
    def __init__(self):
        self.TITLE = 'Protect'
        APPDATA = environ['APPDATA']
        self.PROTECTOR = path.join(APPDATA, self.TITLE)
        self.img_loc = os.path.join(self.PROTECTOR, "index.ico")
        self.img_location_avilable = os.path.exists(self.img_loc)
        protect = f"{APPDATA}\\{self.TITLE}"
        self.last_loc = os.path.join(self.PROTECTOR, "last location.txt")
        self.color_font_init()
        if path.exists(self.PROTECTOR):
            pass
        else:
            mkdir(protect)
        self.img_loc_available()

        self.key_location = path.join(self.PROTECTOR, 'keyfile.txt')
        self.keyfile_ = crypto.get_key(self.key_location)
        self.userpass = path.join(self.PROTECTOR, 'userpass.txt')
        self.encrypted_msg = path.join(self.PROTECTOR, 'encrypted')
        self.START_LOCATION = path.join(os.environ['USERPROFILE'], "Documents")
        path.join(self.PROTECTOR, "")
        USERNAME = os.environ['USERNAME']
        exists_ = path.join(self.PROTECTOR, 'warn.txt')
        old_one = path.exists(exists_)
        if not os.path.exists(self.last_loc):
            with open(self.last_loc, 'w') as f:
                f.write(self.START_LOCATION)
        self.start_up()
        if old_one:
            pass
        else:
            with open(exists_, 'w') as f:
                f.write("used")
            messagebox.showinfo("Info", f"Hi {USERNAME}!!\nPlease Kindly Read The Help and About Before You Peform Encrypion")


        self.fern_enc()        

        self.root.mainloop()

    def color_font_init(self):
            self.font = "widelattin"
            
            self.text_color = text_color
            self.enc_label_frame_bg = color
            self.dec_label_frame_bg = color
            self.enc_dec_start_bg = color
            self.option_label_bg = color
            self.loc_entry_bg = color
            self.open_file_bg  = color
            self.home_bg  = color
            self.submit_bg  = color
            self.pass_frame_bg = color
            self.pass_change_label_bg = color
            self.pass_entry_bg = color
            self.help_win_color = color
            self.get_pass_bg = color
            self.about_color = color
            self.pass_color = color
            self.pass_label_bg = color
            self.pass_btn_bg  = color
            self.help_bg  = color
            self.back_btn_bg = color
            self.help_btn_bg  = color
            self.pass_frame_bg = color
            self.label_frame_bg = color

    def img_loc_available(self):
        if self.img_location_avilable:
            self.img_location  = self.img_loc
        else:
            with open("index.ico", 'rb') as f:
                index = f.read()
            with open(self.img_loc, 'wb') as f:
                f.write(index)
            self.img_location = self.img_loc

    def start_up(self):
        HEIGHT =  300
        WIDTH = 400
        self.root = tk.Tk()
        self.root.title(self.TITLE)
        self.root.iconbitmap(self.img_location)
        self.root.minsize(WIDTH, HEIGHT)
        self.root.maxsize(WIDTH, HEIGHT)
        self.root.geometry(self.root.wm_geometry())
        self.pass_getter()
        self.get_pass_and_check_pass()

    def fern_enc(self):
        #Check user pass and fern key available and check enc file 
        if not path.exists(self.encrypted_msg):
            if path.exists(self.key_location) and path.exists(self.userpass):
                with open(self.userpass, 'r') as f:
                    userpass = int(f.readline())
                fern_key.fern_value_writer(self.keyfile_, self.userpass, self.key_location)
                self.keyfile = fern_key.fern_key_decoder(self.key_location, userpass)
                with open(self.encrypted_msg, 'w') as msg:
                    msg.write("Created")
        else:
            with open(self.userpass, 'r') as f:
                userpass = int(f.readline())
            self.keyfile = fern_key.fern_key_decoder(self.key_location, userpass)

    def help_txt(self, msg):
        help_enc ="""
        Very Very Important>>>
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        When You Choose The Location Be Careful.Because That Location fully converted
        To Another Format and With Out Decrypt You Can't Use Any File Exists On The
        Specified Location
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        In cryptography, encryption is the process of encoding information.
        This process converts the original representation of the information,
        known as plaintext, into an alternative form known as ciphertext.
        Only authorized parties can decipher a ciphertext back to plaintext
        and access the original information.
        Encryption does not itself prevent interference but denies the intelligible 
        content to a would-be interceptor. For technical reasons, an encryption
        scheme usually uses a pseudo-random encryption key generated by an algorithm.
        It is possible to decrypt the message without possessing the key, but, 
        for a well-designed encryption scheme, considerable computational resources
        and skills are required. An authorized recipient can easily decrypt the message 
        with the key provided by the originator to recipients but not to unauthorized users.
        Historically, various forms of encryption have been used to aid in cryptography.
        Early encryption techniques were often utilized in military messaging.
        Since then, new techniques have emerged and become commonplace in all areas of modern
        computing. Modern encryption schemes utilize the concepts of public-key and 
        symmetric-key. Modern encryption techniques ensure security because modern
        computers are inefficient at cracking the encryption. 

        """

        help_dec = """

        Very Very Important>>>
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        When You Choose The Location Be Careful.Because That Location fully converted
        To Another Format and With Out Decrypt You Can't Use Any File Exists On The
        Specified Location
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        The conversion of encrypted data into its original form is called Decryption.
        It is generally a reverse process of encryption. It decodes the encrypted 
        information so that an authorized user can only decrypt the data because
        decryption requires a secret key or password.One of the reasons for implementing
        an encryption-decryption system is privacy. As information travels over
        the Internet, it is necessary to scrutinise the access from unauthorized 
        organisations or individuals. Due to this, the data is encrypted to reduce 
        data loss and theft. Few common items that are encrypted include text files, 
        images, e-mail messages, user data and directories. The recipient of decryption
        receives a prompt or window in which a password can be entered to access 
        the encrypted data. For decryption, the system extracts and converts the garbled
        data and transforms it into words and images that are easily understandable not 
        only by a reader but also by a system. Decryption can be done manually or automatically. 
        It may also be performed with a set of keys or passwords.

        """
        about_me = """
        My Name Is Insan. I studied at Araly Hindu College and Vaddu Hindu College.
        My Github Page => https://github.com/Cracker-Vp-Insan/
        Contact me @GMAIL => imsorrynine99@gmail.com
        My Facebook Id => https://www.facebook.com/crackervp.insan

        """

        if msg == 'enc':
            return help_enc
        elif msg == 'dec':
            return help_dec
        elif msg == 'about':
            return about_me

    def passwd_hider(self, entry_box, txt_variable):
        option = txt_variable.get()
        for box in entry_box:
            if option == 1:
                box.configure(show="")
            else:
                box.configure(show="*")

    def pass_getter(self):
        if path.exists(self.userpass):
            self.user_pass_available = True
            with open(self.userpass, 'r') as f:
                userpasswd = f.readlines()
            self.user_passwd = userpasswd[0]
            self.user_pass_len = userpasswd[1]    
        else:
            self.user_pass_available = False

    def get_pass_and_check_pass(self):
        self.root.configure(bg=self.pass_color)
        self.pass_frame = tk.Frame(self.root, bg=self.pass_color)
        self.pass_frame.pack(pady=80, ipady=100)
        if path.exists(self.userpass):
            self.label = tk.Label(self.pass_frame, text="Put Your Password", bg=self.pass_label_bg, font=self.font, fg = self.text_color)
            self.label.pack(pady=10)
        else:
            self.label = tk.Label(self.pass_frame, text="Set Your Master Password(Must Require!!) : ", bg=self.pass_label_bg, font=self.font, fg = self.text_color)
            self.label.pack(pady=10)

        self._pass_frame = tk.LabelFrame(self.pass_frame, borderwidth=10, bg=self.pass_frame_bg)
        self._pass_frame.pack(pady=5)
        self.pass_value = tk.StringVar()
        self.get_pass = tk.Entry(self._pass_frame, textvariable=self.pass_value, insertbackground=self.text_color, bg=self.get_pass_bg, fg=self.text_color, show="*")
        self.get_pass.pack()

        self.pass_check_btn_text_variable = tk.IntVar()

        check_btn = tk.Checkbutton(self.pass_frame, text="Show Password", onvalue=1, offvalue=0, fg="green", bg=self.get_pass_bg, command=lambda: self.passwd_hider([self.get_pass], self.pass_check_btn_text_variable), variable=self.pass_check_btn_text_variable)
        check_btn.pack()
        self.btn_pass = tk.Button(self.pass_frame, text="Submit", bg=self.pass_btn_bg, command=self.pass_command, font=self.font, fg = self.text_color)
        self.btn_pass.pack()

    def pass_command(self):
        user_passwd = self.pass_value.get()
        lenth = len(user_passwd)
        passwd = algo.write(user_passwd)       
        if user_passwd != '':
            if not self.user_pass_available:
                algo.write(user_passwd, self.userpass, write=True)
                self.fern_enc()
                self.button()
            else:
                if (int(passwd) == int(self.user_passwd)) and (int(lenth) == int(self.user_pass_len)):
                    self.fern_enc()
                    self.button()
                else:
                    self.pass_frame.destroy()
                    self.get_pass_and_check_pass()
                    self.label.configure(text="Wrong Password !!!")
        else:
            self.pass_frame.destroy()
            self.get_pass_and_check_pass()
            self.label.configure(text="Must Input The Password !!!")

    def help_menu(self, event=None):
        self.top_help = Toplevel(self.root)
        self.top_help.title('Help')
        self.top_help.minsize(800, 600)
        self.top_help.maxsize(800, 600)
        self.top_help.iconbitmap(self.img_location)
        self.help_menu_help()

    def help_menu_help(self):
        self.f = tk.LabelFrame(self.top_help, bg=self.help_win_color)
        self.f.pack(fill='both', ipady=500)

        self.f1 = tk.Frame(self.f, bg=self.help_win_color)
        self.f1.pack(pady=250)

        self.enc_btn_frame = tk.LabelFrame(self.f1, bg=self.help_win_color)
        self.enc_btn_frame.grid(row=3, column=4, padx=30)
        self.help_enc_btn = tk.Button(self.enc_btn_frame, text='Encryption Help', bg =self.help_btn_bg, command=self.help_enc, font=self.font, fg = self.text_color)
        self.help_enc_btn.pack()

        self.dec_btn_frame = tk.LabelFrame(self.f1, bg=self.help_win_color)
        self.dec_btn_frame.grid(row=3, column=40, padx=30)
        self.help_dec_btn = tk.Button(self.dec_btn_frame, text='Decryption Help', bg =self.help_btn_bg, command=self.help_enc, font=self.font, fg = self.text_color)
        self.help_dec_btn.pack()

    def back_btn(self):
        self.f.destroy()
        self.help_menu_help()

    def help_enc(self):
        self.f1.destroy()
        help_enc = self.help_txt('enc')
        label = tk.Label(self.f, text=help_enc, font=self.font, bg=self.help_win_color, fg=self.text_color)
        label.pack()
        back_btn = tk.Button(self.f, text="Back", command=self.back_btn, bg=self.back_btn_bg, fg = self.text_color)
        back_btn.pack()

    def help_dec(self):
        self.f1.destroy()
        help_dec = self.help_txt('dec')
        label = tk.Label(self.f, text=help_dec, fg=self.text_color)
        label.pack()
        back_btn = tk.Button(self.f, text="Back", command=self.back_btn, bg=self.back_btn_bg, fg = self.text_color)
        back_btn.pack()

    def about_menu(self, event=None):
        self.top_about = Toplevel(self.root)
        self.top_about.title('About')
        self.top_about.minsize(600, 300)
        self.top_about.maxsize(600, 300)
        self.top_about.iconbitmap(self.img_location)
        self.about_menu_help()

    def about_menu_help(self):
        self.top_about.configure(bg=self.about_color)
        about_me = self.help_txt('about')
        tk.Label(self.top_about, text=about_me, bg=self.about_color, font=self.font, fg = self.text_color).pack()

    def settings(self, event=None):
        old_passwd = self.old_passwd_variable.get()
        new_passwd = self.new_passwd_variable.get()
        conform_passwd = self.conform_passwd_variable.get()

        if (len(old_passwd) != 0) and (len(new_passwd)!=0) and (len(conform_passwd)!=0):
            with open(self.userpass, 'r') as f:
                pass_len = f.readlines()
            old_pass = pass_len[0]
            # old_pass_len = pass_len[1]
            passwd = algo.write(old_passwd)
            if int(passwd) == int(old_pass):
                fernkey = fern_key.fern_key_decoder(self.key_location ,passwd)
                if new_passwd == conform_passwd:
                    f_key = bytes(fernkey, 'ascii')
                    algo.write(new_passwd, self.userpass, write=True)
                    fern_key.fern_value_writer(f_key, self.userpass, self.key_location)
                    self.settings_win.destroy()
                    self.popup_complete("Password Changed!!")
                else:
                    self.settings_win.destroy()
                    self.warning("New Password Doesn't Match With\nConform Password")
            else:
                self.settings_win.destroy()
                self.warning("Your Old Password Doesn't Match.")

        else:
            self.settings_win.destroy()
            self.warning("Must Input Password")

    def settings_passwd(self, event=None):
        self.settings_win = Toplevel(self.root)
        self.settings_win.title("Settings")
        self.settings_win.iconbitmap(self.img_location)
        self.settings_win.minsize(400, 300)
        self.settings_win.maxsize(400, 300)
        self.settings_frame = tk.Frame(self.settings_win, bg=self.pass_frame_bg)
        self.settings_frame.pack(fill='both', expand=50)

        entry_width =25
        # Entry and Label and text variable
        self.old_passwd_variable = tk.StringVar()
        old_passwd_label = tk.Label(self.settings_frame, text="Enter Your Old Password", bg=self.pass_change_label_bg, font=self.font, fg = self.text_color)
        old_passwd_label.pack()
        self.old_passwd_entry = tk.Entry(self.settings_frame, insertbackground=self.text_color, textvariable=self.old_passwd_variable, width=entry_width, bg=self.pass_entry_bg, fg=self.text_color, show="*")
        self.old_passwd_entry.pack()

        self.new_passwd_variable = tk.StringVar()
        new_passwd_label = tk.Label(self.settings_frame, text="Enter Your New Password", bg=self.pass_change_label_bg, font=self.font, fg = self.text_color)
        new_passwd_label.pack()
        self.new_passwd_entry = tk.Entry(self.settings_frame, insertbackground=self.text_color, textvariable=self.new_passwd_variable, width=entry_width, bg=self.pass_entry_bg, fg=self.text_color, show="*")
        self.new_passwd_entry.pack()

        self.conform_passwd_variable = tk.StringVar()
        conform_passwd_label = tk.Label(self.settings_frame, text="Conform Your Password", bg=self.pass_change_label_bg, font=self.font, fg = self.text_color)
        conform_passwd_label.pack()
        self.conform_passwd_entry = tk.Entry(self.settings_frame, insertbackground=self.text_color, textvariable=self.conform_passwd_variable, width=entry_width, bg=self.pass_entry_bg, fg=self.text_color, show="*")
        self.conform_passwd_entry.pack()

        self.setting_variable = tk.IntVar()
        check_btn = tk.Checkbutton(self.settings_frame, text="Show Password", onvalue=1, offvalue=0, fg="green", bg=self.get_pass_bg, command=lambda: self.passwd_hider([self.old_passwd_entry, self.new_passwd_entry, self.conform_passwd_entry], self.setting_variable), variable=self.setting_variable)
        check_btn.pack()

        conform_btn = tk.Button(self.settings_frame, text="Submit", bg=self.pass_change_label_bg, font=self.font, command=self.settings, fg = self.text_color)
        conform_btn.pack()

    def last_loc_adder(self, event=None):
        before_loc = os.path.join(self.PROTECTOR, "before location.txt")
        try:
            value = self.dark_theme.get()
            entered_loc = self.value.get()
            if value == 0:
                with open(before_loc, 'r') as f:
                    beforeloc = f.read()
                self.value.set(beforeloc)
            else:
                with open(before_loc, 'w') as f:
                    f.write(entered_loc)
                self.last_loc = os.path.join(self.PROTECTOR, "last location.txt")
                with open(self.last_loc, 'r') as f:
                    last_loc = f.read()
                self.value.set(last_loc)
        except AttributeError:
            self.popup_error("You Can Only Use This Option to set \nPrevious location on location Menu")

    def quit(self, event=None):
        self.root.quit()

    def menu_bar(self):
        main_menu = Menu(self.root, background='black', foreground='white',
               activebackground='#004c99', activeforeground='white' )
        file_menu = Menu(main_menu, tearoff=0, background='black', foreground='white',
               activebackground='#004c99', activeforeground='white')
        file_menu.add_command(label='Help', command=self.help_menu, accelerator="Ctrl+H")
        file_menu.add_command(label='About', command=self.about_menu, accelerator="Ctrl+I")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
        main_menu .add_cascade(label='Info', menu=file_menu)


        self.dark_theme = tk.IntVar()
        settings_menu = Menu(main_menu, tearoff=0, background='black', foreground='white',
               activebackground='#004c99', activeforeground='white')
        settings_menu.add_command(label='Change Password', command=self.settings_passwd, accelerator="Ctrl+C")
        main_menu.add_cascade(label='Settings', menu=settings_menu)
        settings_menu.add_checkbutton(label="Last Location", onvalue=1, offvalue=0, variable=self.dark_theme, command=self.last_loc_adder, activebackground='#004c99', activeforeground='white', accelerator="Ctrl+L")

        self.root.bind_all("<Control-q>", self.quit)
        self.root.bind_all("<Control-h>", self.help_menu)
        self.root.bind_all("<Control-i>", self.about_menu)
        self.root.bind_all("<Control-c>", self.settings_passwd)
        self.root.bind_all("<Control-l>", self.last_loc_adder)

        self.root.config(menu=main_menu)

    def popup_complete(self, text):
        messagebox.showinfo("Complete!",text)

    def popup_error(self, msg):
        messagebox.showerror('Error', msg)

    def warning(self, text):
        messagebox.showwarning("Warning", text)

    def final_option(self, text, command):

        command_encrypt = crypto.encrypt
        command_decrypt = crypto.decrypt
        if command == 'encrypt':
            command = command_encrypt
        elif command == "decrypt":
            command = command_decrypt


        try:
            self.location_checker(text, command)
        except cryptography.fernet.binascii.Error:
            self.popup_error("Ha Ha!!!\nYou Cheated. Don't Change the value in userpass.")
        except cryptography.fernet.InvalidToken:
            self.start_up()
            self.popup_error("Can't Decrypt This File.\nBecause This File Didn't Encrypted.")
        except FileNotFoundError:
            self.popup_error("Invalid File Selected")

    def location_checker(self, text, command):
        locations = self.value.get()
        guess = locations.split('/')

        location = ""
        for loc in guess:
            location+= f"{loc}\\"
        passwd = guess[-1].split('.')
        len_pass = len(passwd)

        if location.startswith(self.PROTECTOR):
            self.warning(f"This Location Have Important Credentials.\n We Can't {text}.")
            self.entry.delete(0, 'end')

        else:
            self.entry.delete(0, 'end')
            self.__label__.configure(text="Processing Your Files....")
            if len_pass >= 2:
                with open(self.last_loc, 'w') as f:
                    f.write(locations)
                command(self.keyfile, locations)
                self.__label__.configure(text="Process Complete.!")
                self.popup_complete(f"Your Data Successfully {text}")
            elif len_pass==1 and location!="\\":
                with open(self.last_loc, 'w') as f:
                    f.write(location)
                i=0
                self.popup_complete("For Speed Up Your Process Application GUI now Disable.\nProcessing Your Files In Backend.")
                self.root.destroy()
                for root, _, files in os.walk(location):
                    for file in files:
                        location = os.path.join(root, file)
                        command(self.keyfile, location)
                        i+=1

                self.start_up()
                self.popup_complete(f"{i} Files are Sucessfully {text}ed.")
                self.__label__.configure(text="Process Complete.!")
            elif location == '\\':
                self.popup_error("Can't Leave Empty.\n Must Input Location")

    def encrypt(self):
        self.final_option(text="Encrypt", command="encrypt")

    def decrypt(self):
        self.final_option(text="Decrypt", command="decrypt")

    def open_location(self):
        root_filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("text files", "*.txt"),("mp3 files", "*.mp3"),("all files", "*.*")))
        self.value.set(root_filename)

    def option(self, command, text):
        self.frame1.destroy()   
        self.value = tk.StringVar()

        self.frame2 = tk.LabelFrame(self.root, bg=self.option_label_bg, borderwidth=15)
        self.frame2.pack(fill='both', expand=10)
        
        self.__label__ =tk.Label(self.frame2, text=f'Location Of File You Want To {text}', bg=self.option_label_bg, font=self.font, fg = self.text_color)
        self.__label__.grid(pady=10, row=5, column=2)
        
        self.entry = tk.Entry(self.frame2, bg=self.loc_entry_bg, width=30, textvariable = self.value, fg=self.text_color, insertbackground=self.text_color)
        self.entry.grid(row=10, column=2, padx=40, pady=10)

        self.value.set(self.START_LOCATION)

        open_file_btn = tk.Button(self.frame2, command=self.open_location, text='Search', bg=self.open_file_bg, fg = self.text_color)
        open_file_btn.grid(row=10, column=3, pady=10)
        
        self._frame = tk.LabelFrame(self.frame2, borderwidth=10, bg=self.label_frame_bg)
        self._frame.grid(row=20, pady=100, column=3)
        
        btn = tk.Button(self._frame, text='Submit', command=command, bg=self.submit_bg, fg = self.text_color)
        btn.grid()

        home_btn_pack = tk.LabelFrame(self.frame2, borderwidth=10, bg=self.home_bg)
        home_btn_pack.grid(row=20, pady=100, column=2)

        home_btn = tk.Button(home_btn_pack, text="Home", command=self.home, bg=self.home_bg, fg = self.text_color)
        home_btn.grid()

    def home(self):
        self.frame2.destroy()
        self.button()

    def	button(self):
        self.pass_frame.destroy()
        self.frame1 = tk.LabelFrame(self.root, bg=self.enc_dec_start_bg, borderwidth=15)
        self.frame1.pack(fill='both', expand=10)
        enc_button_pack = tk.LabelFrame(self.frame1, bg=self.enc_label_frame_bg,borderwidth=10)
        enc_button_pack.pack(pady=40)
        enc_button = tk.Button(enc_button_pack, bg=self.enc_label_frame_bg, text="Encrypt", padx=10, pady=10, command=lambda:self.option(self.encrypt, "Encrypt"), font=self.font, fg = self.text_color)
        self.menu_bar()
        enc_button.pack()
        dec_button_pack = tk.LabelFrame(self.frame1, bg=self.dec_label_frame_bg,borderwidth=10)
        dec_button_pack.pack(padx=120)
        dec_button = tk.Button(dec_button_pack, bg=self.dec_label_frame_bg, text='Decrypt', padx=10, pady=10, command=lambda:self.option(self.decrypt, "Decrypt"), font=self.font, fg = self.text_color)
        dec_button.pack()

