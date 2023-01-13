import random
import tkinter as tk
def roll():
    lbl_result['text']=str(random.randint(1,6))
    lbl_result['text']=str(random.randint(1,6))

win=tk.Tk()

win.columnconfigure(0,minsize=350)
win.columnconfigure([0,1],minsize=150)
win.columnconfigure(0,minsize=345)
win.columnconfigure([0,2])

btn1_roll=tk.Button(text='')
btn_roll=tk.Button(text='Бросить',command=roll)
lbl_result=tk.Label()
btn_roll.grid(row=0,column=0,sticky="nsew")
lbl_result.grid(row=1,column=0)
win.mainloop()
