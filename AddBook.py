from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def bookRegister():
    bid = bookInfo1.get()   #fetch data from input field by .get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = f"insert into {bookTable} values('{bid}','{title}','{author}','{status}')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo("Success", "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")
    root.destroy()

def addBook():

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Add Books")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.minsize(width=width, height=height)
    root.geometry(f"{width}x{height}")
    con = pymysql.connect(host="localhost", user="root", password="", port=3308, database="lmspython")
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40") # bg=orange
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.13)
    headingLable1 = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLable1.place(relx=0, rely=0, relwidth=1, relheight=1)

    lableFrame = Frame(root, bg='black')
    lableFrame.place(relx=0.15, rely=0.3, relheight=0.4, relwidth=0.7)

    #Book ID
    l2 = Label(lableFrame, text="Book ID : ", bg='black', fg='white')
    l2.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo1 = Entry(lableFrame)
    bookInfo1.place(relx=0.25, rely=0.2, relwidth=0.62, relheight=0.08)
    
    #Title
    l3 = Label(lableFrame, text="Title : ", bg='black', fg='white')
    l3.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(lableFrame)
    bookInfo2.place(relx=0.25, rely=0.35, relwidth=0.62, relheight=0.08)

    #Book Author
    l4 = Label(lableFrame, text="Author : ", bg='black', fg='white')
    l4.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(lableFrame)
    bookInfo3.place(relx=0.25, rely=0.50, relwidth=0.62, relheight=0.08)

    #Book Status
    l5 = Label(lableFrame, text="Status(Avail/issued) : ", bg='black', fg='white')
    l5.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(lableFrame)
    bookInfo4.place(relx=0.25, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='blue', font=(12), fg='white', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='blue', font=(12), fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()