from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

con = pymysql.connect(host="localhost", user="root", password="", port=3308, database="lmspython")
cur = con.cursor() 

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"

def deleteBook():
    bid = bookInfo1.get()
    
    deleteSql = f"delete from {bookTable} where id = '{bid}';"
    deleteIssue = f"delete from {issueTable} where id = '{bid}';"

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Book Record Delete Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    bookInfo1.delete(0, END)
    root.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root 

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.minsize(width=width, height=height)
    root.geometry(f"{width}x{height}")
    root.title("Delete Book")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="purple")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.13)

    headingLable1 = Label(headingFrame1, text="Delete Books", bg='black', fg='white', font=('Courier', 15))
    headingLable1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    submitBtn = Button(root, text="SUBMIT", bg='blue', fg='white', command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="red", fg="white", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()