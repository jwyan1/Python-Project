import tkinter as tk 
from tkinter import *
from tkinter import filedialog
import webbrowser

window = Tk()
window.title("Create a webpage!")
window.geometry('450x200')


def webpage_button():
	f = open('user.html', 'w')
	message = """<html> <body>""" + entry_txt.get() + """</body> </html>""".format(entry_txt)
	f.write(message)	
	f.close()
	filename = 'file:///Users/jw/Desktop/techAcad/' + 'user.html'
	webbrowser.open_new_tab(filename)




btn_1 = Button(window, width=10, text="Generate...",font=("Arial", 15), bg="white", fg="black", command=webpage_button)
btn_1.grid(column=0,row=5, pady = (65,5))
entry_txt = tk.StringVar()
txt_1 = Entry (window, width=25, font=("Arial", 15), bg="white", fg="black", textvariable=entry_txt)
txt_1.grid(column=1,row=5, pady = (65,5), padx =(25,0))









window.mainloop()
