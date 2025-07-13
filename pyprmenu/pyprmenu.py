#!/usr/bin/env python3
#Pyprmenu - a simple menu system for hyprland written in python
import subprocess
import customtkinter as ctk

class PyprMenu(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pyprmenu")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Main Menu
        self.main_menu_frame = ctk.CTkFrame(self)
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.main_menu_frame.grid_rowconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(0, weight=1)
        self.main_menu_frame.grid_columnconfigure(1, weight=1)
        self.main_menu_frame.grid_columnconfigure(2, weight=1)
        
        self.shutdown = ctk.CTkButton(
            self.main_menu_frame,
            text=" ",
            command=self.button_shutdown,
            fg_color="#1f1f28",
            hover_color="#2d2d40",
            text_color="#bdf6ec",
            font=("JetBrainsMono Nerd Font", 36, "bold"),
            corner_radius=12,
        )
        self.shutdown.grid(row=1, column=0, padx=14, pady=14, sticky="nsew") 

        self.restart = ctk.CTkButton(
            self.main_menu_frame,
            text=" ",
            command=self.button_restart,
            fg_color="#1f1f28",
            hover_color="#2d2d40",
            text_color="#bdf6ec",
            font=("JetBrainsMono Nerd Font", 36, "bold"),
            corner_radius=12,
        )
        self.restart.grid(row=1, column=1, padx=14, pady=14, sticky="nsew")

        self.lock = ctk.CTkButton(
            self.main_menu_frame,
            text=" ",
            command=self.button_lock,
            fg_color="#1f1f28",
            hover_color="#2d2d40",
            text_color="#bdf6ec",
            font=("JetBrainsMono Nerd Font", 36, "bold"),
            corner_radius=12,
        )
        self.lock.grid(row=1, column=2, padx=14, pady=14, sticky="nsew")

# Define button actions
    def button_shutdown(self):
        subprocess.run(["systemctl", "poweroff"])

    def button_restart(self):
        subprocess.run(["systemctl", "reboot"])

    def button_lock(self):
        subprocess.run(["hyprlock"])

app = PyprMenu()
app.mainloop()
