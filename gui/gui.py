from tkinter import *


class Gui(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master  # master widget
        self.init_window()

    def init_window(self):
        self.master.title("Hackathon Starter")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text=quit)
        quit_button.place(x=0, y=0)

root = Tk()
root.geometry("1200x800")

app = Gui(root)

root.mainloop()
