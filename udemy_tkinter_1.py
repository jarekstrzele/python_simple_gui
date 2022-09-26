# https://docs.python.org/3/library/tk.html

from tkinter import Tk, Label, Button, Entry

def miles_to_km():
    miles = float(input.get())
    km = miles *1.609
    lbl_result.config(text=f"{km}")


window = Tk()
window.title("fowfjweoifjwf")
window.minsize(width=500,height=300)
# padding
window.config(padx=20, pady=20)


# Entry
input = Entry(width=10)
input.grid(column=1,row=0)


# Labels
lbl_miles = Label(text="Miles", font=("Arial", 24, "bold"))
lbl_miles.grid(column=2,row=0)

my_lbl = Label(text="is equal to", font=("Arial", 24, "bold"))
my_lbl.grid(column=0,row=1) 

lbl_result = Label(text=" 0 ", font=("Arial", 24, "bold"))
lbl_result.grid(column=1,row=1) 

my_lbl3 = Label(text=" Km ", font=("Arial", 24, "bold"))
my_lbl3.grid(column=2,row=1) 


#button 1
btn = Button(text="Calculate", command=miles_to_km)
btn.config(padx=10, pady=10)
btn.grid(column=1, row=2)









window.mainloop()