import shutil
import pathlib
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class Application:
    # Getting OS independent game.exe paths
    orginal_exe_path = pathlib.Path("./Celeste_Test/orgi/CelesteEXE")
    everest_exe_path = pathlib.Path("./Celeste_Test/oeve/CelesteEXE")
    destination_path = pathlib.Path("./Celeste_Test/CelesteEXE")
    # Getting OS independent icon images paths
    orginal_icon_path = pathlib.Path("./Icons/celeste_icon.jpg")
    everest_icon_path = pathlib.Path("./Icons/everest_icon.jpg")
    load_image_orginal = None
    load_image_everest = None
    icon = None
    icon_Label = None
    actualVersion = "Unknown" # Stores what version is choosen

    def changeToOrginal(self):
        shutil.copy2(self.orginal_exe_path, self.destination_path) # Copies orginal game.exe to main gamefolder
        self.actualVersion = "Orginal"
        self.updateIcons()

    def changeToEverest(self):
        shutil.copy2(self.everest_exe_path, self.destination_path) # Copies modded game.exe to main gamefolder
        self.actualVersion = "Everest"
        self.updateIcons()

    def updateIcons(self):
        if(self.actualVersion == "Orginal"):
            self.icon = ImageTk.PhotoImage(self.load_image_orginal)
            self.icon_Label.config(image=self.icon)
        elif(self.actualVersion == "Everest"):
            self.icon = ImageTk.PhotoImage(self.load_image_everest)
            self.icon_Label.config(image=self.icon)

    def __init__(self, root):
        root.geometry("365x90")
        root.title("Celeste version changer")
        self.load_image_orginal = Image.open(self.orginal_icon_path)
        self.load_image_everest = Image.open(self.everest_icon_path)

        ttk.Label(text="What game version do you want to play?").grid(row=0,column=0,columnspan=2,padx=10,pady=15)
        self.icon_Label = ttk.Label(image=self.icon)
        self.icon_Label.grid(row=0,column=2,rowspan=2,padx=5)
        ttk.Button(command=self.changeToOrginal, text="Orginal Celeste", width=15).grid(row=1,column=0,padx=5,pady=5)
        ttk.Button(command=self.changeToEverest, text="Everest Celeste", width=15).grid(row=1,column=1,padx=5,pady=5)


# Main #
root = tk.Tk()
app = Application(root)
root.mainloop()