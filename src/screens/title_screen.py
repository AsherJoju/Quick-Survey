from tkinter import Button, Frame, Label

from navigation_manager import NavigationManager


class TitleScreen(Frame):
    
    def __init__(self, navigator: NavigationManager):
        super().__init__(navigator.root)
        
        self.navigator = navigator
        self.root = navigator.root
        
        self.title_label = Label(self, text="Quick Survey", font=("Arial", 32))
        self.new_survey_button = Button(self, text="New", font=("Arial", 18), command=self.on_new_survey)
        
        self.title_label.place(relx=0.5, rely=0.1, anchor="n")
        self.new_survey_button.place(relx=0.5, rely=0.5, anchor="center")


    def on_new_survey(self):
        # self.navigator.push() TODO
        pass
