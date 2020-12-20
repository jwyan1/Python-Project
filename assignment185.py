import sqlite3
import os

#create a variable for the fileList 
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#create a connection to '185.db'
conn = sqlite3.connect('185.db')

#with connection create a cursor variable and execute the
#create table with an autoincrement int id and file_name
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
    conn.commit()
conn.close()

#re-establish the connection
conn = sqlite3.connect('185.db')

#using for loop go through each file and taking any that end with
# 'txt' put them into the data base and print it out. 
for file in fileList:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (file,))
            print(file)

conn.close()
                        


