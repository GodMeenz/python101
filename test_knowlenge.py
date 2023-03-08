from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI= Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#ชื่อโปรแกรม
GUI.geometry('500x400')#ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)
##########
def Button2():
    text ='ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1=Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=80)
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)#ชื่อปุ่ม
B2.pack(ipadx=20,ipady=20)

##########
def Button3():
    text ='Python101, Math'
    messagebox.showinfo('วิชาที่เรียน',text)

FB2=Frame(GUI) #คล้ายกระดาน
FB2.place(x=20,y=180)
B3=ttk.Button(FB1,text='วิชาที่เรียน',command=Button3)#ชื่อปุ่ม
B3.pack(ipadx=20,ipady=20)



GUI.mainloop()

#B1=ttk.Button(GUI,text='เงินมีอยู่กี่บาท')#ชื่อปุ่ม
#B1.pack(ipadx=20,ipady=20)#จะเป็นกลายเพิ่มขนาดตัวอักษร .ipad จะเริ่มที่ 0,0
#B1.pack(ipadx=20,ipady=20)#จะเป็นกลายเพิ่มขนาดตัวอักษร .
#B2.place(x=50,y=200) #เป็นการกำหนดตำแหน่ง .place จะเป็นการกำหนดตำแหน่ง

