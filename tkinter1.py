from tkinter import *
window = Tk()
window.title("gui app")
window.geometry('350x200')
lbl = Label(window, text="Hello")#label
lbl.grid(column=0, row=0)
 #buttons
btn = Button(window, text="button1")
btn.grid(column=1, row=0)
btn1 = Button(window, text="button2")
btn1.grid(column=1, row=1)
btn2 = Button(window, text="button3")
btn2.grid(column=1, row=2)
window.mainloop()