import os,time
import datetime
import shutil
import datetime as dt
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Check files!")
window.geometry('450x200')


#creating a from browse 
def from_browse_button():
	global folder_path
	filename = filedialog.askdirectory()
	from_folder_path.set(filename)
	print(filename)

from_folder_path = StringVar()

#creating a to browse         
def to_browse_button():
	global folder_path
	filename = filedialog.askdirectory()
	to_folder_path.set(filename)
	print(filename)

to_folder_path = StringVar()


# function creates a now variable and an ago variable subtracting 24 hrs
# then created a variable for the created folder path based on user
# selection above. along with a destination folder. 

def file_move():
	now = dt.datetime.now()
	ago = now-dt.timedelta(hours=24)
	strftime = "%H:%M %m/%d/%Y"
	created = str(from_folder_path)
	dest = str(to_folder_path)

# pass in the created variable folder structure and should then
# go into a loop using the os.walk method but no matter how much
# i tweek it i keep only printing the two directories. 
	for root,dirs,files in os.walk(created):  
		for fname in files:
			path = os.path.join(dirs, fname)
			st = os.stat(path)    
			mtime = dt.datetime.fromtimestamp(st.st_mtime)
			if mtime < ago:
				print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
				shutil.move(path, dest)


btn_1 = Button(window, width=10, text="From...",font=("Arial", 15), bg="white", fg="black", command= from_browse_button)
btn_1.grid(column=0,row=5, pady = (65,5))
txt_1 = Entry (window, width=25, font=("Arial", 15), bg="white", fg="black", textvariable= from_folder_path)
txt_1.grid(column=1,row=5, pady = (65,5), padx =(25,0))

btn_2 = Button(window, width=10, text="To...",font=("Arial", 15), bg="white", fg="black", command= to_browse_button)
btn_2.grid(column=0,row=7, pady = (0,5))
txt_2 = Entry (window, width=25, font=("Arial", 15), bg="white", fg="black", textvariable= to_folder_path)
txt_2.grid(column=1,row=7, padx =(25,0))

btn_3 = Button(window, width=10, text="Move Files...", font=("Arial", 15), bg="white", fg="black", command=file_move)
btn_3.grid(column=0,row=9, pady = (0,25))


btn_4 = Button(window, width=10, text="Close Program", font=("Arial", 15), bg="white", fg="black")
btn_4.grid(column=1,row=9, pady = (0,25), padx = (140,0))



window.mainloop()
