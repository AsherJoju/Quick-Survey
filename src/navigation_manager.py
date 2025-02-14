from tkinter import Frame


class NavigationManager:
    
    def __init__(self, root):
        self.root = root
        self.frames: list[Frame] = []


    def push(self, frame: Frame):
        if self.frames:
            self.frames[-1].pack_forget()
        
        self.frames.append(frame)
        frame.pack(fill="both", expand=True)


    def pop(self):
        if self.frames:
            frame = self.frames.pop()
            frame.pack_forget()
            
            if self.frames:
                self.frames[-1].pack(fill="both", expand=True)
                
            return frame
        
        return None
