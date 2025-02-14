from tkinter import Button, Label, Frame
import tkinter.font as tkFont

class TitleScreen(Frame):
    
    def __init__(self, root, on_new_survey):
        super().__init__(root)
        
        self.root = root
        self.on_new_survey = on_new_survey
        
        self.title_label = Label(self, text="Quick Survey", font=("Arial", 32))
        self.new_survey_button = Button(self, text="New", font=("Arial", 18), command=self.on_new_survey)
        
        self.title_label.place(relx=0.5, rely=0.1, anchor="n")
        self.new_survey_button.place(relx=0.5, rely=0.5, anchor="center")
