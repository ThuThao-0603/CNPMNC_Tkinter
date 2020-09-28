import tkinter as TK
from tkinter import messagebox
tiki = TK.Tk()
def BinhPhuong():
    #tmp = str(e1.get()) ;
    messagebox.showinfo('Ket qua la',( e1.get()))
TK.Label(tiki, text = "Nhap mot so nguyen").grid(row=0)
e1 = TK.Entry(tiki)
e1.grid(row=0, column = 2)
btn = TK.Button(tiki, text="Click Me", command = BinhPhuong).grid(row=1,column=2)
TK.mainloop()        
