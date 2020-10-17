from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

con = pymysql.connect(host="localhost", user="root", password="", port=3308, database="lmspython")
cur = con.cursor()
# mycursor.execute("select * from student")
# result = mycursor.fetchall()

root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.title("Library Management System")


# Adding background Image
b_g = Image.open("Image/bg.jpg")
b_g = b_g.resize((width, height), Image.ANTIALIAS)
img = ImageTk.PhotoImage(b_g)
label = Label(image=img)
label.pack()

f1 = Frame(root, bg="#FFBB00", relief=SUNKEN, bd=10) # bg=yellow
l1 = Label(f1, text="Welcome to Ritik Vishvakarma's \n Library Management System", bg='black', fg='white', font=('Courier', 15))
f1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
l1.place(relx=0, rely=0, relwidth=1, relheight=1)

# Buttons
btn1 = Button(root, text="Add Books Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.32, rely=0.3, relwidth=0.35, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.32, rely=0.4, relwidth=0.35, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.32, rely=0.5, relwidth=0.35, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.32, rely=0.6, relwidth=0.35, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.32, rely=0.7, relwidth=0.35, relheight=0.1)
root.mainloop()
