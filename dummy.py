# light_blue = (108, 188, 218)
# dark_pink = (151, 22, 142)
# light_pink = (239, 19, 224)
# dark_blue = (26, 9, 137)
# light_blue = (27, 229, 229)
# green_blue = (27, 229, 128)
# light_green = (14, 249, 37)
# light_dark_green = (118, 219, 17)
# light_pink = (238, 102, 151)
# dark_pink = (226, 13, 91)
# red = (232, 12, 12)
# yellow = (215, 243, 74)
# gray = (129, 129, 126)
# orange = (249, 120, 7)
# purple = (168, 7, 249)

"""
default = {
    'enc_label_frame_bg' : "red",
    'dec_label_frame_bg' : "red",
    'enc_dec_start_bg' : "pink",
    'option_label_bg' : "lightblue",
    'loc_entry_bg' : "red",
    'open_file_bg' : "gray",
    'home_bg' : "orange",
    'submit_bg' : "blue",
    'pass_frame_bg' : "lightblue",
    'pass_change_label_bg' : "lightblue",
    'pass_entry_bg' : "lightgreen",
    "help_win_color" : "purple",
    "about_color" : "gray",
    "pass_color" : "red",
    "pass_label_bg" : "orange",
    "pass_btn_bg"  : "lightgreen",
    "help_bg"  : "purple",
    "back_btn_bg" : "blue",
    "help_btn_bg"  : "orange",
    "pass_frame_bg" : "purple",
    "label_frame_bg" : "purple",
    "font" : 'candara',
    "font1" : 'WideLatin',
    "pass_font"  : "WideLatin",
    "help_font"  : "WideLatin",
    "about_font"  : "WideLatin",
    "passwd_font"  : "WideLatin",
    "loc_font"  : "WideLatin",
    "enc_dec_font"  : "WideLatin",
    "text_color" : "white"
}

black_theme = {
    'enc_label_frame_bg' : "red",
    'dec_label_frame_bg' : "red",
    'enc_dec_start_bg' : "pink",
    'option_label_bg' : "lightblue",
    'loc_entry_bg' : "red",
    'open_file_bg' : "gray",
    'home_bg' : "orange",
    'submit_bg' : "blue",
    'pass_frame_bg' : "lightblue",
    'pass_change_label_bg' : "lightblue",
    'pass_entry_bg' : "lightgreen",
    "help_win_color" : "purple",
    "about_color" : "gray",
    "pass_color" : "red",
    "pass_label_bg" : "orange",
    "pass_btn_bg"  : "lightgreen",
    "help_bg"  : "purple",
    "back_btn_bg" : "blue",
    "help_btn_bg"  : "orange",
    "pass_frame_bg" : "purple",
    "label_frame_bg" : "purple",
    "font" : 'candara',
    "font1" : 'WideLatin',
    "pass_font"  : "WideLatin",
    "help_font"  : "WideLatin",
    "about_font"  : "WideLatin",
    "passwd_font"  : "WideLatin",
    "loc_font"  : "WideLatin",
    "enc_dec_font"  : "WideLatin",
    "text_color" : "white"
}

        color_path = os.path.join(self.PROTECTOR, "color.txt")

        is os.path.exists(color_path):
            with open(color_path, 'r') as f:
                color = f.read()
            if color == "default":
                font = default['font']
                font1 = default['font1']
                pass_font  = default["pass_font"]
                help_font  = default["help_font"]
                about_font  = default["about_font"]
                passwd_font  = default["passwd_font"]
                loc_font  = default["loc_font"]
                enc_dec_font  = default["enc_dec_font"]

                text_color = default["text_color"]

                enc_label_frame_bg = default['enc_label_frame_bg']
                dec_label_frame_bg = default['dec_label_frame_bg']
                enc_dec_start_bg = default['enc_dec_start_bg']
                option_label_bg = default['option_label_bg']
                loc_entry_bg = default['loc_entry_bg']
                open_file_bg  = default['open_file_bg']
                home_bg  = default['home_bg']
                submit_bg  = default['submit_bg']
                pass_frame_bg = default['pass_frame_bg']
                pass_change_label_bg = default['pass_change_label_bg']
                pass_entry_bg = default['pass_entry_bg']

                help_win_color = default['help_win_color']
                about_color = default['about_color']
                pass_color = default['pass_color']
                pass_label_bg = default['pass_label_bg']
                pass_btn_bg  = default['pass_btn_bg']
                help_bg  = default['help_bg']
                back_btn_bg = default['back_btn_bg']
                help_btn_bg  = default['help_btn_bg']
                pass_frame_bg = default['pass_frame_bg']
                label_frame_bg = default['label_frame_bg']                

            else:


"""




from tkinter import *

def donothing():
   x = 0
   
        # try:
        #     locations = self.value.get()
        #     guess = locations.split('/')

        #     location = ""
        #     for loc in guess:
        #         location+= f"{loc}\\"
        #     passwd = guess[-1].split('.')
        #     len_pass = len(passwd)

        #     if location.startswith(self.PROTECTOR):
        #         self.warning(f"This Location Have Important Credentials.\n We Can't {text}.")
        #         self.entry.delete(0, 'end')

        #     else:
        #         self.entry.delete(0, 'end')
        #         if len_pass < 2:
        #             for root, _, files in os.walk(location):
        #                 for file in files:
        #                     location = os.path.join(root, file)
        #                     command(self.keyfile, location)
        #                     value=True
        #                 if value:
        #                     self.popup_complete(f"Your Data Successfully {text}")
        #                 else:
        #                     pass
        #         else:
        #             command(self.keyfile, locations)

                    

# root = Tk()

# menubar = Menu(root)
# filemenu = Menu(menubar, tearoff=10)
# filemenu.add_command(label="New", command=donothing)
# filemenu.add_command(label="Open", command=donothing)
# filemenu.add_command(label="Save", command=donothing)
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=filemenu)

# helpmenu = Menu(menubar, tearoff=0)
# helpmenu.add_command(label="Help Index", command=donothing)
# helpmenu.add_command(label="About...", command=donothing)
# menubar.add_cascade(label="Help", menu=helpmenu)

# root.config(menu=menubar)
# root.mainloop()



# from tkinter import *

# root = Tk()
# root.title("Steam Trader")
# root.minsize(500, 800)
# root.maxsize(500, 0)

# menubar = Menu(root, background='#000099', foreground='white',
#                activebackground='#004c99', activeforeground='white')
# filemenu = Menu(menubar, tearoff=0, background='#000099',
# foreground='white',
#                 activebackground='#004c99', activeforeground='white')
# filemenu.add_command(label="Open", command=None)
# filemenu.add_command(label="Save", command=None)
# menubar.add_cascade(label="File", menu=filemenu)

# root.config(bg='#2A2C2B', menu=menubar)
# root.mainloop()

from tkinter import *


root = Tk()
root.title("Steam Trader")
root.minsize(500, 800)
root.maxsize(500, 0)

en = Entry(root, show="*")
en.pack()

btn = Button(root, text="fsd", command=lambda: en.configure(show=""))
btn.pack()
Checkbutton(root, text="input", command=None).pack()
# menubar = Menu(root, background='#000099', foreground='white',
#                activebackground='#004c99', activeforeground='white')
# filemenu = Menu(menubar, tearoff=0, background='#000099',
# foreground='white',
#                 activebackground='#004c99', activeforeground='white')
# filemenu.add_command(label="Open", command=root.quit)
# filemenu.add_command(label="Save", command=None)
# menubar.add_cascade(label="File", menu=filemenu)

# root.config(bg='#2A2C2B', menu=menubar)
root.mainloop()
