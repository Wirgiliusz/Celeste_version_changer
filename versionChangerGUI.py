import shutil
import pathlib
import tkinter as tk
from tkinter import ttk


class Application:
    orginal_exe_path = pathlib.Path("./Celeste_Test/orgi/CelesteEXE")
    everest_exe_path = pathlib.Path("./Celeste_Test/oeve/CelesteEXE")
    destination_path = pathlib.Path("./Celeste_Test/CelesteEXE")
    actualVersion = "Unknown"

    def changeToOrginal(self):
        shutil.copy2(self.orginal_exe_path, self.destination_path)
        print("Game switched to Orginal version")

    def changeToEverest(self):
        shutil.copy2(self.everest_exe_path, self.destination_path)
        print("Game switched to Everest version")

    def __init__(self, root):
        root.geometry("400x100")
        root.title("Celeste version changer")

        ttk.Label(text="What game version do you want to play?").grid(row=0,column=0,columnspan=2,padx=10,pady=15)
        ttk.Button(command=self.changeToOrginal, text="Orginal Celeste", width=15).grid(row=1,column=0,padx=5,pady=5)
        ttk.Button(command=self.changeToEverest, text="Everest Celeste", width=15).grid(row=1,column=1,padx=5,pady=5)


# Main #
root = tk.Tk()
app = Application(root)
root.mainloop()