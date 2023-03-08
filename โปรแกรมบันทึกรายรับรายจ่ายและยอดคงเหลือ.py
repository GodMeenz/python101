from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI=Tk()
GUI.title('โปรแกรมบันทึกรายรับรายจ่ายและยอดคงเหลือ')
GUI.geometry('400x400')

L1 = Label(GUI,text=' โปรแกรมบันทึกรายรับรายจ่ายและยอดคงเหลือ ',font=('Angsana New',20),fg='Blue')
L1.place(x=30,y=20)

def Button1():
    text = 'รายรับ 7000 บาท '
    messagebox.showinfo('รายรับ',text)

FB1=Frame(GUI)
FB1.place(x=70,y=80)
B1=ttk.Button(FB1,text='รายรับเท่าไหร่',command=Button1)
B1.pack(ipadx=20,ipady=20)

def Button2():
    text = 'รายจ่าย 3500 บาท '
    messagebox.showinfo('รายจ่าย',text)

FB2=Frame(GUI)
FB2.place(x=200,y=80)
B2=ttk.Button(FB2,text='รายจ่ายเท่าไหร่',command=Button2)
B2.pack(ipadx=20,ipady=20)



def Button3():
    text = 'เงินออม 500 บาท '
    messagebox.showinfo('เงินออม',text)

FB3=Frame(GUI)
FB3.place(x=70,y=170)
B3=ttk.Button(FB3,text='เงินออมมีเท่าไหร่',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'เงินซื้อหุ้น 500 บาท '
    messagebox.showinfo('หุ้น',text)

FB4=Frame(GUI)
FB4.place(x=200,y=170)
B4=ttk.Button(FB4,text='เงินซ์้อหุ้นเท่าไหร่',command=Button4)
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'คงเหลือ 2500 บาท '
    messagebox.showinfo('คงเหลือ',text)

FB5=Frame(GUI)
FB5.place(x=150,y=260)
B5=ttk.Button(FB5,text='คงเหลือเท่าไหร่',command=Button5)
B5.pack(ipadx=20,ipady=20)

GUI.mainloop
