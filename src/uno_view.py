from tkinter import *

class Main (Tk):
    def __init__ (self):
        Tk.__init__(self)
        #self.wm_iconbitmap("") #for icons
        self.title("KWATRO!")
        self.geometry("600x600+300+0")
        self.resizable(0, 0)


main = Main ()
main.mainloop()