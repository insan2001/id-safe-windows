import helper
import os
import tkinter as tk
from tkinter import messagebox


file = os.path.join(os.environ['APPDATA'], "Protector_Errors.txt")


try:
    helper.GUI()
except tk._tkinter.TclError as t:
    messagebox.showerror('Error', f"{t} Please Download the index.ico from \nhttps://github.com/Cracker-Vp-Insan/protect_frnds_")
except Exception as e:
    messagebox.showerror('Error', e)
    with open(file, 'a+') as error:
        error.write(str(e))