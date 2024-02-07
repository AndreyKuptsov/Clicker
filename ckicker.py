from tkinter import *
from tkinter import ttk
 
clicks1 = 0
clicks = 0
def click_button():
    global clicks
    clicks += 1
    
    btn["text"] = f"Yes {clicks}"  
    
def click_button1():    
    global clicks1
    clicks1 += 1
    
    bt1['text'] = f'No {clicks1}' 
 
root = Tk()
root.title("Are you ready?")
root.geometry("250x150")
 
btn = ttk.Button(text="Yes", command=click_button)
bt1 = ttk.Button(text = 'No', command=click_button1)

btn.pack(expand=True)
bt1.pack(expand=True)

root.mainloop()
