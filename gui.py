from tkinter import *
from tkinter import ttk
import config

def gui_event():
    config.EMAIL = Input1.get()
    config.EMAIL_PASSWORD = Input2.get()
    config.APP_PASSWORD = Input3.get()

    return

    pass

root = Tk()
root.title("Enter the values")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

Input1 = StringVar()
Input2 = StringVar()
Input3 = StringVar()

I1_entry = ttk.Entry(mainframe, width=35, textvariable=Input1)
I2_entry = ttk.Entry(mainframe, width=35, textvariable=Input2)
I3_entry = ttk.Entry(mainframe, width=35, textvariable=Input3)

I1_entry.grid(column=2, row=3)
I2_entry.grid(column=2, row=4)
I3_entry.grid(column=2, row=5)

ttk.Button(mainframe, text="Enter", command=gui_event).grid(column=8, row=11, sticky=S)

ttk.Label(mainframe, text="Set up").grid(column=0, row=0)
ttk.Label(mainframe, text="Email address").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Email Password").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="App Password").grid(column=1, row=5, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

def OnButtonClick(self):
    self.labelVariable.set(self.entryVariable.get() + " (You clicked the button)")

I1_entry.focus()
root.bind('<Return>', gui_event)

root.mainloop()