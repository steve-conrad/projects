#Pyprmenu - a simple menu system for hyprland written in python

import subprocess
import customtkinter as ctk

class PyprMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry = ("900x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Main Menu
        self.main_menu_frame = ctk.CTkFrame(self)
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.main_menu_frame.grid_rowconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(2, weight=1)
        
        self.button_1 = ctk.CTkButton(
            self.main_menu_frame, 
            text="Shutdown",
            command=self.button_shutdown,
        )
        self.button_1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.button_2 = ctk.CTkButton(
            self.main_menu_frame,
            text="Restart",
            command=self.button_restart,
        )
        self.button_2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.button_3 = ctk.CTkButton(
            self.main_menu_frame,
            text="Lock",
            command=self.button_lock,
        )
        self.button_3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Define button actions
    def button_shutdown(self):
        print("Shutdown")

    def button_restart(self):
        print("Restart")

    def button_lock(self):
        print("Lock")

app = PyprMenu()
app.mainloop()
