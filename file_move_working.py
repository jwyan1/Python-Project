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
	global from_folder_path
	filename = filedialog.askdirectory()
	from_folder_path.set(filename)
from_folder_path = StringVar()


def to_browse_button():
	global to_folder_path
	filename = filedialog.askdirectory()
	to_folder_path.set(filename)
to_folder_path = StringVar()

def file_move():
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    strftime = "%H:%M %m/%d/%Y"
    created = from_folder_path.get()
    dest = to_folder_path.get()
    files = os.listdir(created)
    for filename in files:
        path = os.path.join(created, filename)
        print (path)
        st = os.stat(path)
        print (st)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        print (mtime)
        if mtime < ago:
            print (path)
            shutil.move(path, dest)


"""
	for file in files: 
		path = os.path.join(created)
		new_path = shutil.move(f"{created}/{file}", dest)
		print(new_path)

-----

	now = dt.datetime.now()
	ago = now-dt.timedelta(hours=24)
	strftime = "%H:%M %m/%d/%Y"
	created = from_folder_path.get()
	dest = to_folder_path.get()

	for root,dirs,files in os.walk(created):  
		for fname in files:
			path = os.path.join(root, fname)
			st = os.stat(path)    
			mtime = dt.datetime.fromtimestamp(st.st_mtime)
			if mtime > ago:
				print("True:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
				shutil.move(path, dest)
"""

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
