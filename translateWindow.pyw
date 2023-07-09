# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import Tk
import signal
from translate import frtrans, frtrans2, frtrans3, voice, transer, count

root= tk.Tk()

h_s = tk.Scrollbar(root, orient='horizontal', bg = 'black')
h_s.pack(side='bottom', fill='x')

canvas1 = tk.Canvas(root, width = 400, height = 160, bg = 'dark grey')
canvas1.pack()

entry1 = tk.Entry(root, bg = 'black', fg = 'light green')
entry1.configure(highlightbackground = "black", font=("Times New Roman", 15))
canvas1.create_window(200, 10, window=entry1)

#translate button/enter
def translater(event):
  translates()

def hi(event):
  trans = transer()
  voice(trans, count())
  
def on (event): #sets main image to off
  canvas1.config(width=400, height=165)
  
def off(event):
  canvas1.config(width=400, height=50)

def on_hover(l, h2, i):
    input_text_area = tk.Text(root, pady = 0, width = 20, height = 20, bg='black', fg='light green')

    input_text_area.configure(highlightbackground = "black", font=("Times New Roman", 16))

    frame = canvas1.create_window(340, 16, window=input_text_area)
    canvas1.itemconfig(frame, width = 130, height = 30)
    input_text_area.delete("1.0", tk.END)
    x = frtrans3(h2[i]).splitlines()
    input_text_area.insert("1.0", " " + x[0] + " : " + x[1])
    input_text_area.config(state='disabled')

def go(event):
    entry1.delete(0, tk.END)
    a = Tk()
    clip = a.clipboard_get()
    entry1.insert(0, clip)
    a.destroy()
    translates()

entry1.bind('<Return>', translater)
entry1.bind('<Down>', hi)
root.bind('<Leave>', off)
root.bind('<Enter>', on)
root.bind('<Button-3>', go)

#word window
def translates():  
    x1 = entry1.get()
    h = frtrans(x1)
    h2 = frtrans2(x1).splitlines()

    canvas1.delete("all")
    canvas1.create_window(200, 14, window=entry1)
    textarea = tk.Text(root, padx = 5, bg = 'black', fg = 'light green')
    textarea.configure(highlightbackground = "black", font=("Times New Roman", 25))
    f = canvas1.create_window(205, 110, window=textarea)
    canvas1.itemconfig(f, width = 410, height = 160)

    textarea.insert("1.0", h2[1] + "\n" + h2[2] + "\n")
    textarea.insert(tk.END, h)
    textarea.config(state='disabled')

    l = h2[0]
    x = []
    for i in range(len(l) + 1):
        temp = "1." + str(i)
        x = x + [temp]

    for i in range(len(l)):
        textarea.tag_add(x[i+1], x[i], x[i+1])
        textarea.tag_bind(x[i+1], "<Enter>", lambda event, i=i: on_hover(x[i+1], h2[0], i))

    entry1.delete(0, tk.END)

button1 = tk.Button(text='translator', command=translates)
canvas1.create_window(200, 50, window=button1)
button2 = tk.Button(text='voice', command=hi)


root.attributes('-topmost',True)
root.attributes()
root.mainloop()

