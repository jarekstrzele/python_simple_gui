from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.btn1 = Button(self, text="Pierwszy")
        self.btn1.grid()

        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text="Drugi")

        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3["text"] = "No i trzeci"

root =Tk()
root.title("Przyciski z klasą")
root.geometry("210x85")

app = App(root)
app.grid()

root.mainloop()
