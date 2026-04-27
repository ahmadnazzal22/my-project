from tkinter import *


def miles_to_km():
    miles=float(miles_entry.get())
    km=miles*1.609
    km_result.config(text=f"{km}")

window=Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20,pady=20)

miles_entry=Entry(width=7)
miles_entry.grid(column=1,row=0)

km_result=Label(text="0")
km_result.grid(column=1,row=1)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

calculate=Button(text="Calculate",command=miles_to_km)
calculate.grid(column=1,row=2)

window.mainloop()