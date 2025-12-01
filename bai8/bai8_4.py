#họ và tên: lê tiến lực
#MSSV: 245752021610103

from tkinter import * 
window = Tk() 
window.title("Chào mừng đến LikeGeeks app") 
window.geometry('350x200') 
lbl = Label(window, text="Xin chào") 
lbl.grid(column=0, row=0) 
def clicked(): 
    lbl.configure(text="Bạn đã nhấn nút !!") 
btn = Button(window, text="Click Me", command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop()
