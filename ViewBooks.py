from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql

con = pymysql.connect(host="localhost", user="root", password="", port=3308, database="lmspython")
cur = con.cursor() 

# Enter Table Names here
bookTable = "books"

def View():
    root = Tk()
    root.title("View Books")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.minsize(width=width, height=height)
    root.geometry(f"{width}x{height}")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.13)
    headingLable1 = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLable1.place(relx=0, rely=0, relwidth=1, relheight=1)

    lableFrame = Frame(root, bg='black')
    lableFrame.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.54)
    y=0.25

    Label(lableFrame, text="%-30s%-50s%-40s%-30s"%('ID','Title','Author','Status'), bg='black', fg='white').place(relx=0.07,rely=0.1)
    Label(lableFrame, text="---------------------------------------------------------------------------------------------", bg='black',fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from "+bookTable
    
    try:
        cur.execute(getBooks)
        con.commit()
        # result = mycursor.fetchall()
        for i in cur:
            Label(lableFrame, text="%-30s%-40s%-40s%-30s"%(i[0], i[1], i[2], i[3]), bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.05
    except:
        messagebox.showinfo("Failed to fetch files from database")
    quitBtn = Button(root, text="Quit", bg="red", fg="white", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()