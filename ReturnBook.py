from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

con = pymysql.connect(host="localhost", user="root", password="", port=3308, database="lmspython")
print(con)
cur = con.cursor() 

# Enter Table Names here
issueTable = "books_issued"
bookTable = "books"
allBid = []

def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status
    bid = bookInfo1.get()
    extractBid = "select id from "+issueTable

    try:
        cur.execute(extractBid)
        con.commit()
        # result = mycursor.fecthall()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = f"select status from {bookTable} where id = '{bid}'"
            cur.execute(checkAvail)
            con.commit()
            # rs = mycursor.fecthall()
            for i in cur:
                check = i[0]
            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = f"delete from {issueTable} where id = '{bid}'"
    updateStatus = f"update {bookTable} set status = 'avail' where id = '{bid}'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")
    allBid.clear()
    root.destory()

def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, labelFrame, root, lb1 

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.minsize(width=width, height=height)
    root.geometry(f"{width}x{height}")
    root.title("Return Book")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.13)

    headingLable1 = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLable1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.4)

    # Book ID to Delete
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    submitBtn = Button(root, text="SUBMIT", bg='blue', fg='white', command=returnn)
    submitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="red", fg="white", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()