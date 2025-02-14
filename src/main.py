from tkinter import Tk

from navigation_manager import NavigationManager
from screens.title_screen import TitleScreen


root = Tk()
root.title("Quick Survey")
root.geometry("500x500")

navigator = NavigationManager(root)

def on_new_survey():
    pass

navigator.push(TitleScreen(root, on_new_survey))

root.mainloop()
