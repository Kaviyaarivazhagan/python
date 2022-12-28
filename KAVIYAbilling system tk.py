from tkinter import *
import random
from datetime import datetime
import mysql.connector as mysql

root= Tk()
root.geometry("1200x650+100+20")
root.title("RESTAURANT MANAGEMENT SYSTEM")

f= Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400,width=300, relief= RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root, bd=5,height=400, width=300, relief=RAISED)

lbl_info= Label(f, font=('aria', 30, 'bold'),text="Fresh juice")
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M")

rand           = StringVar()
Apple          = StringVar()
Orange         = StringVar()
Watermelon     = StringVar()
Carrot         = StringVar()
Kiwi           = StringVar()
Pineapple      = StringVar()
Total          = StringVar()
Tax            = StringVar()
cost           = StringVar()
date           = StringVar()
service_charge = StringVar()

lbl_Apple = Label(f1, font=('aria', 20, 'bold'),text="Apple Rs.80")
lbl_Apple.grid(row=1,column=0)
txt_Apple = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Apple)
txt_Apple.grid(row=1,column=1)

lbl_Orange = Label(f1, font=('aria', 20, 'bold'),text="Orange Rs.50")
lbl_Orange.grid(row=2,column=0)
txt_Orange = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Orange)
txt_Orange.grid(row=2,column=1)

lbl_Watermelon = Label(f1, font=('aria', 20, 'bold'),text="Watermelon Rs.50")
lbl_Watermelon.grid(row=3,column=0)
txt_Watermelon= Entry(f1, font=('ariel', 20, 'bold'),textvariable=Watermelon)
txt_Watermelon.grid(row=3,column=1)

lbl_Carrot  = Label(f1, font=('aria', 20, 'bold'),text="Carrot  Rs.50")
lbl_Carrot .grid(row=4,column=0)
txt_Carrot = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Carrot)
txt_Carrot .grid(row=4,column=1)

lbl_Kiwi  = Label(f1, font=('aria', 20, 'bold'),text="Kiwi  Rs.50")
lbl_Kiwi  .grid(row=5,column=0)
txt_Kiwi  = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Kiwi )
txt_Kiwi .grid(row=5,column=1)

lbl_Pineapple  = Label(f1, font=('aria', 20, 'bold'),text="Pineapple  Rs.60")
lbl_Pineapple.grid(row=6,column=0)
txt_Pineapple= Entry(f1, font=('ariel', 20, 'bold'),textvariable=Pineapple  )
txt_Pineapple.grid(row=6,column=1)

def generate_bill():

    bill_no = str(random.randint(50, 300))
    rand.set(bill_no)
    date.set(localtime)
    try: qa = int(Apple.get())
    except: qa = 0
    try: qo = int(Orange.get())
    except: qo = 0
    try: qw= int(Watermelon.get())
    except: qw = 0
    try: qc = int(Carrot.get())
    except: qc = 0
    try: qk = int(Kiwi.get())
    except: qk = 0
    try: qp = int(Pineapple.get())
    except: qp = 0

    costofapple      = qa * 80 
    costoforange     = qo * 50
    costofwatermelon = qw * 50
    costofcarrot     = qc * 50
    costofkiwi       = qk * 50
    costofpineapple  = qp * 60

    f2.pack(side=RIGHT, fill="both", expand=1)
    f2.configure(background="light yellow")

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text="Bill no")
    lbl_bill.grid(row=1,column=0)
    
    lbl_date = Label(f2, font=('aria', 18, 'bold'), text="Date")
    lbl_date.grid(row=2,column=0)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text="Cost")
    lbl_cost.grid(row=3,column=0)
    
    lbl_service = Label(f2, font=('aria', 18, 'bold'), text="Service charge")
    lbl_service.grid(row=4,column=0)
  
    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text="Tax")
    lbl_tax.grid(row=5,column=0)

    lbl_total = Label(f2, font=('aria', 18, 'bold'), text="Total")
    lbl_total.grid(row=6,column=0)
    

    Totalcost= costofapple + costoforange + costofwatermelon + costofcarrot + costofkiwi + costofpineapple
    costofmeal =  "Rs.", str('%.2f' % Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = "Rs.", str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = "Rs.", str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = "Rs.", str('%.2f' % overall)

    service_charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

txt_bill = Entry(f2, font=('ariel', 18, 'bold'),textvariable=rand)
txt_bill.grid(row=1, column=1)

txt_date = Entry(f2, font=('ariel', 18, 'bold'),textvariable=date)
txt_date.grid(row=2, column=1)

txt_cost = Entry(f2, font=('ariel', 18, 'bold'),textvariable=cost)
txt_cost.grid(row=3, column=1)

txt_service = Entry(f2, font=('ariel', 18, 'bold'),textvariable=service_charge)
txt_service.grid(row=4, column=1)

txt_tax = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Tax)
txt_tax.grid(row=5, column=1)

txt_total = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Total)
txt_total.grid(row=6, column=1)

def extra_root():
    new_root = Toplevel(root)
    new_root.title("RESTAURENT")
    new_root.geometry("450x450")
    Label(new_root,text='MENU').pack()
    Label(new_root,text=txt_bill.get()).pack()
    Label(new_root,text=txt_date.get()).pack()
    Label(new_root,text=txt_cost.get()).pack()
    Label(new_root,text=txt_service.get()).pack()
    Label(new_root,text=txt_tax.get()).pack()
    Label(new_root,text=txt_total.get()).pack()

    new_root.mainloop()

btn_total = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="GET DETAILS",command=extra_root)
btn_total.grid(row=10,column=0)

def qexit():
    root.destroy()

def reset():
    Apple.set('') 
    Orange.set('')  
    Watermelon.set('') 
    Carrot.set('')      
    Kiwi.set('')  
    Pineapple.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="CALCULATE BILL",command=generate_bill)
btn_Total.grid(row=9,column=0)

btn_Reset = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="RESET",command=reset)
btn_Reset.grid(row=9,column=1)

btn_Exit = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="EXIT",command=qexit)
btn_Exit.grid(row=9,column=2)

def save_data():
    bill = txt_bill.get()
    date_time = txt_date.get()
    cost = txt_cost.get()
    service_charge = txt_service.get()
    tax = txt_tax.get()
    total_cost=txt_total.get()
    con = mysql.connect(host="localhost",user="root",password="",database="billing_sys")
    cursor = con.cursor()
    cursor.execute("insert into total_bill values('"+ bill +"','"+ date_time +"','"+ cost +"','"+ service_charge +"','"+ tax +"','"+ total_cost +"')")
    cursor.execute("commit")

    con.close()
   
btn_Savedetails = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="SAVE DETAILS",command=save_data)
btn_Savedetails.grid(row=10,column=2)

root.mainloop()







