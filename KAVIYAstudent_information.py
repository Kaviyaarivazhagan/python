from tkinter.ttk import*
from tkinter import *
import mysql.connector as mysql

root = Tk()
root.geometry("450x450")
root.title("Student Data Window")

Label(root, text='STUDENT DATA').pack()
Label(root, text='student name').pack()
e1 = Entry(root,width=30)
e1.pack()
Label(root, text='student age').pack()
e2 = Entry(root,width=30)
e2.pack()
Label(root, text='student city').pack()
e3 = Entry(root,width=30)
e3.pack()
Label(root, text='student degree').pack()
c1 = Combobox(root)
c1['value'] = ('BE','BTECH','ME','MTECH','BSc','MSc','MBA')
c1.current(0)
c1.pack()
Label(root, text='student gender').pack()
c2 = Combobox(root)
c2['value'] = ('Male','Female','Transgender')
c2.current(0)
c2.pack()


def extra_root():
    new_root = Toplevel(root)
    new_root.title("Student Information Window")
    new_root.geometry("450x450")
    Label(new_root,text='STUDENT INFORMATION').pack()
    Label(new_root, text=e1.get()).pack()
    Label(new_root, text=e2.get()).pack()
    Label(new_root, text=e3.get()).pack()
    Label(new_root, text=c1.get()).pack()
    Label(new_root, text=c2.get()).pack()

    new_root.mainloop()

Button(root,text='Get Details', command=extra_root).pack()

def save_data():
    name = e1.get()
    age = e2.get()
    city = e3.get()
    degree = c1.get()
    gender = c2.get()

    con = mysql.connect(host="localhost",user="root",password="",database="pranitha")
    cursor = con.cursor()
    cursor.execute("insert into student_data values('"+ name +"','"+ age +"','"+ city +"','"+ degree +"','"+ gender +"')")
    cursor.execute("commit")

    con.close()
   
Button(root,text='Save Details', command=save_data).pack()
root.mainloop()


