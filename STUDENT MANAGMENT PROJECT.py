
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as c
entries=[]
listb=[]
lista=[]
listpt1=[]
listpt2=[]
listhy=[]
listae=[]
listpe=[]
total=[]
percent=[]
def createtable1():
    try:
        con1=c.connect(host='localhost',user='root',passwd=a[1])
        cur=con1.cursor()
        cur.execute('create database result')
        con1.commit()
        con1.close()
    except:
        pass
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    try:
        query1='create table studentdetail(rollno varchar(10),studentname varchar(50),\
             fathername varchar(50),mothername varchar(50),dob varchar(20),\
             subject varchar(20))'
        cursor.execute(query1)
        

    except:
        pass
    try:
        query='create table schooldetail(schoolname varchar(50),\
               schooladdress varchar(50),cbseno varchar(10),\
               schoolno varchar(10),schoolwebsite varchar(50),\
               academicsession varchar(10))'
        cursor.execute(query)
    except:
        pass
    try:
        query2='create table pt1(rollno varchar(10) primary key,studentname varchar(50) not null,\
               english varchar(10) default " ",cs varchar(10) default " ",physics varchar(10) default " ",\
                chemistry varchar(10) default " ",maths varchar(10) default " ",biology varchar(10) default " ",\
                hindi varchar(10) default " ")'
        cursor.execute(query2)
    except:
        pass
    try:
        query3='create table pt2(rollno varchar(10) primary key,studentname varchar(50) not null,\
               english varchar(10) default " ",cs varchar(10) default " ",physics varchar(10) default " ",\
                chemistry varchar(10) default " ",maths varchar(10) default " ",biology varchar(10) default " ",\
                hindi varchar(10) default " ")'
        cursor.execute(query3)
    except:
        pass
    try:
        query4='create table halfyearly(rollno varchar(10) primary key,studentname varchar(50) not null,\
               english varchar(10) default " ",cs varchar(10) default " ",physics varchar(10) default " ",\
                chemistry varchar(10) default " ",maths varchar(10) default " ",biology varchar(10) default " ",\
                hindi varchar(10) default " ")'
        cursor.execute(query4)
    except:
        pass
    try:
        query5='create table annualexam(rollno varchar(10) primary key,studentname varchar(50) not null,\
               english varchar(10) default " ",cs varchar(10) default " ",physics varchar(10) default " ",\
                chemistry varchar(10) default " ",maths varchar(10) default " ",biology varchar(10) default " ",\
                hindi varchar(10) default " ")'
        cursor.execute(query5)
    except:
        pass
    try:
        con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
        cursor=con.cursor()
        query6='create table practical(rollno varchar(10) primary key,studentname varchar(50) not null,\
               cs varchar(10) default " ",physics varchar(10) default " ",\
                chemistry varchar(10) default " ",biology varchar(10) default " ")'
                
        cursor.execute(query6)
    except:
        pass
    
    con.commit()
def insert1():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query="insert into schooldetail values('{}','{}','{}','{}','{}','{}')"\
           .format(entries[0],entries[1],entries[2],entries[3],\
                   entries[4],entries[5])
    cursor.execute(query)
    con.commit()

def check1():
     con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
     cursor=con.cursor()
     query='select * from schooldetail'
     cursor.execute(query)
     _=cursor.fetchall()
     if cursor.rowcount!=0:
         messagebox.showwarning('Warning','data already exist')
     else:
         messagebox.showinfo('SUCESSFULL','SUCCESSFULLY DATA INSERTED')
         insert1()

def warn2():
    for i in range(6):
        if len(entries[i])==0:
               messagebox.showwarning('WARNING','ENTER REQUIRED DETAIL')
               break
    else:
        check1()
               
def dele():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query='delete from schooldetail'
    cursor.execute(query)
    con.commit()
    messagebox.showinfo('successfully','Data Deleted successfully')

def warnview():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query='select * from schooldetail'
    cursor.execute(query)
    _=cursor.fetchall()
    if cursor.rowcount==0:
         messagebox.showwarning('Warning','Please Submit the data')
    else:
         view1()

def warnview1():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query='select * from schooldetail'
    cursor.execute(query)
    _=cursor.fetchall()
    if cursor.rowcount==0:
         messagebox.showwarning('Warning','NO DATA FOUND')
    else:
         view1()
         
def interface2_1():
    def insider2():
        global entries
        entries.clear()
        entries.extend([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()])
        warn2()
    win21=tk.Tk()
    win21.geometry('71300x41500')
    win21.title('RESULT')
    tk.Label(win21,text='CLASS 11th').pack()
    tk.Label(win21,text='SCHOOL ENTRY').pack()
    tk.Label(win21,text='SCHOOL NAME',bg='lightpink')\
                                .place(x=10,y=60)
    tk.Label(win21,text='SCHOOL ADDRESS',bg='lightpink')\
                                .place(x=10,y=100)
    tk.Label(win21,text='CBSE AFFILIATION NO.',bg='lightpink')\
                                .place(x=10,y=140)

    tk.Label(win21,text='SCHOOL NO.',bg='lightpink')\
                                .place(x=10,y=180)
    tk.Label(win21,text='SCHOOL WEBSITE',bg='lightpink')\
                                .place(x=10,y=220)

    tk.Label(win21,text='ACADEMIC SESSION',bg='lightpink')\
                                .place(x=10,y=260)
    
    e1=tk.Entry(win21,bg='yellow')
    e2=tk.Entry(win21,bg='yellow')
    e3=tk.Entry(win21,bg='yellow')
    e4=tk.Entry(win21,bg='yellow')
    e5=tk.Entry(win21,bg='yellow')
    e6=tk.Entry(win21,bg='yellow')
    e1.place(x=110,y=60)
    e2.place(x=120,y=100)
    e3.place(x=140,y=140)
    e4.place(x=90,y=180)
    e5.place(x=120,y=220)
    e6.place(x=130,y=260)
    entries.append(e1.get())
    
    tk.Button(win21,text='SUBMIT',bg='lightblue',command=insider2).place(x=180,y=300)
    tk.Button(win21,text='View',bg='lightblue',command=warnview).place(x=90,y=300)
    
entries_p1=[]
entries_u1=[]

def update1():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query1='delete from schooldetail'
    query2="insert into schooldetail values('{}','{}','{}','{}','{}','{}')"\
           .format(entries_u1[0],entries_u1[1],entries_u1[2],entries_u1[3],\
                   entries_u1[4],entries_u1[5])
    cursor.execute(query1)
    cursor.execute(query2)
    con.commit()
    #print(entries_u1)

def warn3():
    if len(entries_u1)==0 or len(entries_p1)==0:
        messagebox.showwarning('WARNING','FILL REQUIRED DETAIL')
    else:
        for i in range(6):
            if len(entries_u1[i])==0 or len(entries_p1[i])==0:
                messagebox.showwarning('WARNING','FILL REQUIRED DETAIL')
                break
        else:
            update1()
        #print(entries_u1)
        #print(entries_p1)
            messagebox.showinfo('SUCCESsfULL','SUCCESSFULLY UPDATED')

def view1():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select * from schooldetail')   
    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')
    tree['column']\
    =('schoolname','schooladdress','cbseno','schoolno','schoolwebsite','academicsession')

    tree.column('schoolname',minwidth=50,width=200,anchor=tk.CENTER)
    tree.column('schooladdress',minwidth=50,width=120,anchor=tk.CENTER)
    tree.column('cbseno',minwidth=50,width=100,anchor=tk.CENTER)
    tree.column('schoolno',minwidth=50,anchor=tk.CENTER)
    tree.column('schoolwebsite',minwidth=100,width=150,anchor=tk.CENTER)
    tree.column('academicsession',minwidth=100,width=150,anchor=tk.CENTER)
    #tree.column('schooladdress',width=200,anchor=tk.CENTER)

    tree.heading('schoolname',text='SCHOOL_NAME',anchor=tk.CENTER)
    tree.heading('schooladdress',text='SCHOOL_ADDRESS',anchor=tk.CENTER)
    tree.heading('cbseno',text='CBSE_NO',anchor=tk.CENTER)
    tree.heading('schoolno',text='SCHOOL_No',anchor=tk.CENTER)
    tree.heading('schoolwebsite',text='SCHOOL_WEBSITE',anchor=tk.CENTER)
    tree.heading('academicsession',text='ACCADEMIC_SESSION',anchor=tk.CENTER)
    #tree.heading('schooladdress',text='SCHOOL-ADDRESS',anchor=tk.CENTER)
    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i+=1
    tree.pack()    
        
def interface2_2():
    def insider3():
        global entries_p1
        global entries_u1
        entries_u1.clear()
        entries_p1.clear()
        entries_p1.extend([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()])
        entries_u1.extend([e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get()])             
        warn3()
    def insider4():
        global entries_p1
        global entries_u1
        entries_u1.clear()
        entries_p1.clear()
        entries_p1.extend([e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()])
        entries_u1.extend([e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get()])  
        if len(entries_u1)==0 or len(entries_p1)==0:
                messagebox.showwarning('WARNING','FILL REQUIRED DETAIL')

        else:
            for i in range(6):
                if len(entries_u1[i])==0 or len(entries_p1[i])==0:
                    messagebox.showwarning('WARNING','FILL REQUIRED DETAIL')
                    break
            else:
                con=c.connect(host=\
                              'localhost',user='root',passwd=a[1],database='result')
                cursor=con.cursor()
                query1='delete from schooldetail'
                query2="insert into schooldetail values('{}','{}','{}','{}','{}','{}')"\
                    .format(entries_u1[0],entries_u1[1],entries_u1[2],entries_u1[3],\
                       entries_u1[4],entries_u1[5])
                cursor.execute(query1)
                cursor.execute(query2)
                con.commit()
                view1()
                        
    win22=tk.Tk()
    win22.title('RESULT')
    win22.geometry('300x700')
    tk.Label(win22,text='CLASS XI').pack()
    tk.Label(win22,text='SCHOOL ENTRY').pack()
    tk.Label(win22,text='SCHOOL NAME',bg='lightpink')\
                                .place(x=10,y=60)
    tk.Label(win22,text='(Present)',fg='black')\
                                .place(x=20,y=80)

    tk.Label(win22,text='SCHOOL NAME',bg='lightpink')\
                                .place(x=10,y=100)
    tk.Label(win22,text='(Updated)',fg='black')\
                                .place(x=20,y=120)
    tk.Label(win22,text='SCHOOL ADDRESS.',bg='lightpink')\
                                .place(x=10,y=150)
    tk.Label(win22,text='(present)',fg='black')\
                                .place(x=30,y=170)
    tk.Label(win22,text='SCHOOL ADDRESS.',bg='lightpink')\
                                .place(x=10,y=190)
    tk.Label(win22,text='(Updated)',fg='black')\
                                .place(x=30,y=210)

    tk.Label(win22,text='CBSE AFFILIATION NO.',bg='lightpink')\
                                .place(x=10,y=240)
    tk.Label(win22,text='(Present)',fg='black')\
                                .place(x=20,y=260)
    tk.Label(win22,text='CBSE AFFILIATION NO',bg='lightpink')\
                                .place(x=10,y=280)
    tk.Label(win22,text='(Updated',fg='black')\
                                .place(x=20,y=300)
    tk.Label(win22,text='SCHOOL NO',bg='lightpink')\
                                .place(x=10,y=330)
    tk.Label(win22,text='(present)',fg='black')\
                                .place(x=20,y=350)
    tk.Label(win22,text='SCHOOL NO',bg='lightpink')\
                                .place(x=10,y=370)
    tk.Label(win22,text='(Updated)',fg='black')\
                                .place(x=20,y=390)

    tk.Label(win22,text='SCHOOL WEBSITE',bg='lightpink')\
                                .place(x=10,y=420)
    tk.Label(win22,text='(Present)',fg='black')\
                                .place(x=20,y=440)
    tk.Label(win22,text='SCHOOL WEBSITE',bg='lightpink')\
                                .place(x=10,y=460)
    tk.Label(win22,text='(Updated)',fg='black')\
                                .place(x=20,y=480)
    tk.Label(win22,text='ACCADEMIC SESSION',bg='lightpink')\
                                                            .place(x=10,y=510)
    tk.Label(win22,text='(present)',fg='black')\
                                               .place(x=20,y=530)
    tk.Label(win22,text='ACCADEMIc SESSIOn',bg='lightpink')\
                                               .place(x=10,y=550)
    tk.Label(win22,text='(Updated)',fg='black')\
                                               .place(x=20,y=570)
        
    e1=tk.Entry(win22,bg='yellow')
    e11=tk.Entry(win22,bg='yellow')
    e2=tk.Entry(win22,bg='yellow')
    e12=tk.Entry(win22,bg='yellow')
    e3=tk.Entry(win22,bg='yellow')
    e13=tk.Entry(win22,bg='yellow')
    e4=tk.Entry(win22,bg='yellow')
    e14=tk.Entry(win22,bg='yellow')
    e5=tk.Entry(win22,bg='yellow')
    e15=tk.Entry(win22,bg='yellow')
    e6=tk.Entry(win22,bg='yellow')
    e16=tk.Entry(win22,bg='yellow')
    

    e1.place(x=105,y=60)
    e11.place(x=105,y=100)
    e2.place(x=125,y=150)
    e12.place(x=125,y=190)
    e3.place(x=140,y=240)
    e13.place(x=140,y=280)
    e4.place(x=90,y=330)
    e14.place(x=90,y=370)
    e5.place(x=120,y=420)
    e15.place(x=120,y=460)
    e6.place(x=135,y=510)
    e16.place(x=135,y=550)
    
    tk.Button(win22,text='SUBMIT',bg='lightblue',command=insider3)\
    .place(x=190,y=590)
    tk.Button(win22,text='view',bg='lightblue',command=insider4)\
    .place(x=140,y=590)
    

def interface2(): 
    win2=tk.Tk()
    win2.title('RESULT')
    win2.geometry('300x300')
    tk.Label(win2,text="CLASS XI").pack()
    tk.Label(win2,text="SCHOOL ENTERY").pack()
    
    tk.Button(win2,text='INSERT ENTRY',bg='lightpink',command=interface2_1)\
                               .place(x=110,y=60)
    tk.Button(win2,text='UPDATE ENTRY',bg='lightpink',command=interface2_2
              )\
                               .place(x=107,y=97)
    tk.Button(win2,text='DELETE ENTRY',bg='lightpink',command=dele)\
                               .place(x=110,y=137)
    tk.Button(win2,text='VIEW DETAIl',bg='lightpink',command=warnview1)\
                               .place(x=115,y=177)

entries_p2=[]
def warn4():
    for i in range(7):
        if len(entries_p2[1])==0:
            messagebox.showwarning('WARNING','Fill Required Detail')
            break
    else:
        messagebox.showinfo('SUCCESSFULL','ENTRY SUBMITTED')

def periodic1():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor() 
    cursor.execute('select s.rollno,s.studentname,\
    p.english,p.cs,p.physics,p.chemistry,p.biology,p.maths,p.hindi from pt1 p,studentdetail s \
    where p.rollno=s.rollno')

    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)

    tk.Label(r,text='CLASS XI',fg='red').pack()
    tk.Label(r,text='PERIODIC TEST-I  MARKS ENTRY ',fg='red').pack()
    tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')

    tree['column']\
     =('rollno','studentname','english','cs','physics','chemistry','biology','maths','hindi')

    tree.column('rollno',minwidth=50,width=50,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=150,anchor=tk.CENTER)
    tree.column('english',minwidth=50,width=80,anchor=tk.CENTER)
    tree.column('cs',minwidth=50,width=120,anchor=tk.CENTER)
    tree.column('physics',minwidth=100,width=80,anchor=tk.CENTER)
    tree.column('chemistry',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('biology',width=100,anchor=tk.CENTER)
    tree.column('maths',width=100,anchor=tk.CENTER)
    tree.column('hindi',width=100,anchor=tk.CENTER)

    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student Name',anchor=tk.CENTER)
    tree.heading('english',text='English(40)',anchor=tk.CENTER)
    tree.heading('cs',text='Comupter science(40)',anchor=tk.CENTER)
    tree.heading('physics',text='Physics(40)',anchor=tk.CENTER)
    tree.heading('chemistry',text='Chemistry(40)',anchor=tk.CENTER)
    tree.heading('biology',text='Biology(40)',anchor=tk.CENTER)
    tree.heading('maths',text='Maths(40)',anchor=tk.CENTER)
    tree.heading('hindi',text='Hindi(40)',anchor=tk.CENTER)
    #tree.pack()
    #rollno=tk.StringVar()
    #cs=tk.StringVar()
    eng=tk.StringVar()
    cs=tk.StringVar()
    phy=tk.StringVar()
    chem=tk.StringVar()
    bio=tk.StringVar()
    maths=tk.StringVar()
    hindi=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')

    def insert_data():
            global lista
            curitem=tree.focus()
            values=tree.item(curitem,'values')
            if len(values)==0:
                    messagebox.showwarning('Warning','Select Student to Update marks')
            else:   
                    if values[7]=='---' and values[8]=='---':
                        f=tk.Frame(r,width=400,height=320,background='grey')
                        f.place(x=100,y=280)
                        l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                        l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                        l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                        l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                        l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                        a1=tk.Entry(f,textvariable=eng,width=25)
                        a2=tk.Entry(f,textvariable=cs,width=25)
                        a3=tk.Entry(f,textvariable=phy,width=25)
                        a4=tk.Entry(f,textvariable=chem,width=25)
                        a5=tk.Entry(f,textvariable=bio,width=25)
                        l1.place(x=50,y=50)
                        l2.place(x=30,y=90)
                        l3.place(x=50,y=130)
                        l4.place(x=50,y=170)
                        l5.place(x=50,y=210)
                        a1.place(x=170,y=50)
                        a2.place(x=170,y=90)
                        a3.place(x=170,y=130)
                        a4.place(x=170,y=170)
                        a5.place(x=170,y=210)
                        a1.insert(0,values[2])
                        a2.insert(0,values[3])
                        a3.insert(0,values[4])
                        a4.insert(0,values[5])
                        a5.insert(0,values[6])
                        def update_data1():
                            nonlocal a1,a2,a3,a4,a5,curitem,values
                            eng=a1.get()
                            cs=a2.get()
                            phy=a3.get()
                            chem=a4.get()
                            bio=a5.get()
                            lista.clear()
                            lista.extend([eng,cs,phy,chem,bio])
                            for i in lista:
                                    if len(i)==0:
                                            messagebox.showwarning('Warning','Fill the required detial')
                                            break
                                    try:
                                            error=int(i)
                                            
                                    except:
                                            messagebox.showwarning('Warning','Invalid Entry')
                                            break
                                    if int(i)>40:
                                            messagebox.showwarning('Warning','marks Out of /40')
                                            break
                                    
                            
                            else:
                                    tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                    #print((values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                    cursor=con.cursor()
                                    q1="update pt1 set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                        biology='{}' where rollno='{}'".format(eng,cs,phy,chem,bio,values[0])
                                    q2="update pt1_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                    q3="update pt1_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/4))
                                    q4="update pt1_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                    q5="update pt1_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                    q6="update pt1_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/4))
                                    cursor.execute(q1)
                                    cursor.execute(q2)
                                    cursor.execute(q3)
                                    cursor.execute(q4)
                                    cursor.execute(q5)
                                    cursor.execute(q6)
                                    
                                    con.commit()
                                
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                        def cancel1():
                                a1.delete(0,tk.END)
                                a2.delete(0,tk.END)
                                a3.delete(0,tk.END)
                                a4.delete(0,tk.END)
                                a5.delete(0,tk.END)
                                f.destroy()
                               
                        savebutton1=tk.Button(f,text='submit',fg='green',command=update_data1)
                        savebutton1.place(x=100,y=270)
                        cancelbutton1=tk.Button(f,text='cancel',fg='green',command=cancel1)
                        cancelbutton1.place(x=200,y=270)
                    elif values[3]=='---' and values[7]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=bio,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[6])
                            def update_data2():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    bio=a5.get()
                                    lista.clear()
                                    lista.extend([eng,phy,hindi,chem,bio])
                                    for j in lista:
                                            if len(j)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    
                                                    error=int(j)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(j)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break

                                            
                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,bio,values[7],hindi)) 
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q2="update pt1 set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                        biology='{}' where rollno='{}'".format(eng,hindi,phy,chem,bio,values[0])
                                            q11="update pt1_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q12="update pt1_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(hindi)/4))
                                            q13="update pt1_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q14="update pt1_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q15="update pt1_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/4))
                    
                                            cursor.execute(q2)
                                            cursor.execute(q11)
                                            cursor.execute(q12)
                                            cursor.execute(q13)
                                            cursor.execute(q14)
                                            cursor.execute(q15)
                                            #cursor.execute(q16)
                                            
                                            con.commit()
                                            #print(eng)
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                                                    
                            def cance2():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton2=tk.Button(f,text='submit',fg='green',command=update_data2)
                            savebutton2.place(x=100,y=270)
                            cancelbutton2=tk.Button(f,text='cancel',fg='green',command=cance2)
                            cancelbutton2.place(x=200,y=270)
                    elif values[6]=='---' and values[3]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data3():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,hindi,phy,chem,maths])
                                    for k in lista:
                                            if len(k)==0:
                                                    
                                                    
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(k)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(k)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break


                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,values[6],maths,hindi))
                                           
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q3="update pt1 set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                maths='{}' where rollno='{}'".format(eng,hindi,phy,chem,maths,values[0])
                                            q21="update pt1_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q22="update pt1_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(hindi)/4))
                                            q23="update pt1_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q24="update pt1_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q25="update pt1_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(maths)/4))
                
                                            cursor.execute(q3)
                                            cursor.execute(q21)
                                            cursor.execute(q22)
                                            cursor.execute(q23)
                                            cursor.execute(q24)
                                            cursor.execute(q25)
                                            con.commit()
                                            #print(eng)
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                            def cance3():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton3=tk.Button(f,text='submit',fg='green',command=update_data3)
                            savebutton3.place(x=100,y=270)
                            cancelbutton3=tk.Button(f,text='cancel',fg='green',command=cance3)
                            cancelbutton3.place(x=200,y=270)
                    elif values[6]=='---' and values[8]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=cs,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=30,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data4():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    cs=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,cs,phy,chem,maths])
                                    for v in lista:
                                            if len(v)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(v)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(v)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break

                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,values[6],maths,values[8]))
                                           
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q4="update pt1 set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                maths='{}' where rollno='{}'".format(eng,cs,phy,chem,maths,values[0])
                                            q31="update pt1_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q32="update pt1_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/4))
                                            q33="update pt1_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q34="update pt1_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q35="update pt1_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(maths)/4))
                

                                            cursor.execute(q4)
                                            cursor.execute(q31)
                                            cursor.execute(q32)
                                            cursor.execute(q33)
                                            cursor.execute(q34)
                                            cursor.execute(q35)
                                            
                                            
                                            con.commit()
                                            #print(type(str((int(eng)/4))))
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                            def cance4():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton4=tk.Button(f,text='submit',fg='green',command=update_data4)
                            savebutton4.place(x=100,y=270)
                            cancelbutton4=tk.Button(f,text='cancel',fg='green',command=cance4)
                            cancelbutton4.place(x=200,y=270)


                                                                        
                        
    insertbutton=tk.Button(r,text='Update marks',command=insert_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=350,y=300)




    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],\
                                         ro[5],ro[6],ro[7],ro[8]))

        i+=1
    tree.place(x=50,y=40)

def periodic2():
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select s.rollno,s.studentname,\
    p.english,p.cs,p.physics,p.chemistry,p.biology,p.maths,p.hindi from pt2 p,studentdetail s \
    where p.rollno=s.rollno')


    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)

    tk.Label(r,text='CLASS XI',fg='red').pack()
    tk.Label(r,text='PERIODIC TEST-II  MARKS ENTRY ',fg='red').pack()
    tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')

    tree['column']\
    =('rollno','studentname','english','cs','physics','chemistry','biology','maths','hindi')

    tree.column('rollno',minwidth=50,width=50,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=150,anchor=tk.CENTER)
    tree.column('english',minwidth=50,width=80,anchor=tk.CENTER)
    tree.column('cs',minwidth=50,width=120,anchor=tk.CENTER)
    tree.column('physics',minwidth=100,width=80,anchor=tk.CENTER)
    tree.column('chemistry',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('biology',width=100,anchor=tk.CENTER)
    tree.column('maths',width=100,anchor=tk.CENTER)
    tree.column('hindi',width=100,anchor=tk.CENTER)

    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student Name',anchor=tk.CENTER)
    tree.heading('english',text='English(40)',anchor=tk.CENTER)
    tree.heading('cs',text='Comupter science(40)',anchor=tk.CENTER)
    tree.heading('physics',text='Physics(40)',anchor=tk.CENTER)
    tree.heading('chemistry',text='Chemistry(40)',anchor=tk.CENTER)
    tree.heading('biology',text='Biology(40)',anchor=tk.CENTER)
    tree.heading('maths',text='Maths(40)',anchor=tk.CENTER)
    tree.heading('hindi',text='Hindi(40)',anchor=tk.CENTER)

    #tree.pack()
    #rollno=tk.StringVar()
    #cs=tk.StringVar()
    eng=tk.StringVar()
    cs=tk.StringVar()
    phy=tk.StringVar()
    chem=tk.StringVar()
    bio=tk.StringVar()
    maths=tk.StringVar()
    hindi=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')


    def insert_data():
            global lista
            curitem=tree.focus()
            values=tree.item(curitem,'values')
            if len(values)==0:
                    messagebox.showwarning('Warning','Select Student to Update marks')
            else:   
                    if values[7]=='---' and values[8]=='---':
                        f=tk.Frame(r,width=400,height=320,background='grey')
                        f.place(x=100,y=280)
                        l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                        l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                        l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                        l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                        l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                        a1=tk.Entry(f,textvariable=eng,width=25)
                        a2=tk.Entry(f,textvariable=cs,width=25)
                        a3=tk.Entry(f,textvariable=phy,width=25)
                        a4=tk.Entry(f,textvariable=chem,width=25)
                        a5=tk.Entry(f,textvariable=bio,width=25)
                        l1.place(x=50,y=50)
                        l2.place(x=30,y=90)
                        l3.place(x=50,y=130)
                        l4.place(x=50,y=170)
                        l5.place(x=50,y=210)
                        a1.place(x=170,y=50)
                        a2.place(x=170,y=90)
                        a3.place(x=170,y=130)
                        a4.place(x=170,y=170)
                        a5.place(x=170,y=210)
                        a1.insert(0,values[2])
                        a2.insert(0,values[3])
                        a3.insert(0,values[4])
                        a4.insert(0,values[5])
                        a5.insert(0,values[6])
                        def update_data1():
                            nonlocal a1,a2,a3,a4,a5,curitem,values
                            eng=a1.get()
                            cs=a2.get()
                            phy=a3.get()
                            chem=a4.get()
                            bio=a5.get()
                            lista.clear()
                            lista.extend([eng,cs,phy,chem,bio])
                            for i in lista:
                                    if len(i)==0:
                                            messagebox.showwarning('Warning','Fill the required detial')
                                            break
                                    try:
                                            error=int(i)
                                            
                                    except:
                                            messagebox.showwarning('Warning','Invalid Entry')
                                            break
                                    if int(i)>40:
                                            messagebox.showwarning('Warning','marks Out of /40')
                                            break
                                    
                            
                            else:
                                    tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                    #print((values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                    cursor=con.cursor()
                                    q1="update pt2 set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                        biology='{}' where rollno='{}'".format(eng,cs,phy,chem,bio,values[0])
                                    q2="update pt2_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                    q3="update pt2_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/4))
                                    q4="update pt2_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                    q5="update pt2_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                    q6="update pt2_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/4))

                                    cursor.execute(q1)
                                    cursor.execute(q2)
                                    cursor.execute(q3)
                                    cursor.execute(q4)
                                    cursor.execute(q5)
                                    cursor.execute(q6)
                                    
                                    con.commit()
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                        def cancel1():
                                a1.delete(0,tk.END)
                                a2.delete(0,tk.END)
                                a3.delete(0,tk.END)
                                a4.delete(0,tk.END)
                                a5.delete(0,tk.END)
                                f.destroy()
                               
                        savebutton1=tk.Button(f,text='submit',fg='green',command=update_data1)
                        savebutton1.place(x=100,y=270)
                        cancelbutton1=tk.Button(f,text='cancel',fg='green',command=cancel1)
                        cancelbutton1.place(x=200,y=270)
                    elif values[3]=='---' and values[7]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=bio,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[6])
                            def update_data2():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    bio=a5.get()
                                    lista.clear()
                                    lista.extend([eng,phy,hindi,chem,bio])
                                    for j in lista:
                                            if len(j)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    
                                                    error=int(j)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(j)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break

                                            
                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,bio,values[7],hindi)) 
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q2="update pt2 set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                        biology='{}' where rollno='{}'".format(eng,hindi,phy,chem,bio,values[0])
                                            q11="update pt2_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q12="update pt2_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(hindi)/4))
                                            q13="update pt2_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q14="update pt2_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q15="update pt2_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/4))
                    

                                            cursor.execute(q2)
                                            cursor.execute(q11)
                                            cursor.execute(q12)
                                            cursor.execute(q13)
                                            cursor.execute(q14)
                                            cursor.execute(q15)
                                            
                                            con.commit()
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                                                    
                            def cance2():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton2=tk.Button(f,text='submit',fg='green',command=update_data2)
                            savebutton2.place(x=100,y=270)
                            cancelbutton2=tk.Button(f,text='cancel',fg='green',command=cance2)
                            cancelbutton2.place(x=200,y=270)
                    elif values[6]=='---' and values[3]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data3():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,hindi,phy,chem,maths])
                                    for k in lista:
                                            if len(k)==0:
                                                    
                                                    
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(k)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(k)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break


                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,values[6],maths,hindi))
                                           
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q3="update pt2 set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                maths='{}' where rollno='{}'".format(eng,hindi,phy,chem,maths,values[0])
                                            q21="update pt2_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q22="update pt2_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(hindi)/4))
                                            q23="update pt2_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q24="update pt2_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q25="update pt2_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(maths)/4))
                
                                            cursor.execute(q3)
                                            cursor.execute(q21)
                                            cursor.execute(q22)
                                            cursor.execute(q23)
                                            cursor.execute(q24)
                                            cursor.execute(q25)
                                            
                                            con.commit()
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                            def cance3():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton3=tk.Button(f,text='submit',fg='green',command=update_data3)
                            savebutton3.place(x=100,y=270)
                            cancelbutton3=tk.Button(f,text='cancel',fg='green',command=cance3)
                            cancelbutton3.place(x=200,y=270)
                    elif values[6]=='---' and values[8]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=cs,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=30,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data4():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    cs=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,cs,phy,chem,maths])
                                    for v in lista:
                                            if len(v)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(v)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            if int(v)>40:
                                                    messagebox.showwarning('Warning','marks Out of /40')
                                                    break

                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,values[6],maths,values[8]))
                                           
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q4="update pt2 set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                maths='{}' where rollno='{}'".format(eng,cs,phy,chem,maths,values[0])
                                            q31="update pt2_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(eng)/4))
                                            q32="update pt2_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/4))
                                            q33="update pt2_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/4))
                                            q34="update pt2_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/4))
                                            q35="update pt2_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(maths)/4))
                
                                            cursor.execute(q4)
                                            cursor.execute(q31)
                                            cursor.execute(q32)
                                            cursor.execute(q33)
                                            cursor.execute(q34)
                                            cursor.execute(q35)
                                            con.commit() 
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                            def cance4():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton4=tk.Button(f,text='submit',fg='green',command=update_data4)
                            savebutton4.place(x=100,y=270)
                            cancelbutton4=tk.Button(f,text='cancel',fg='green',command=cance4)
                            cancelbutton4.place(x=200,y=270)                                            
                        
    insertbutton=tk.Button(r,text='Update marks',command=insert_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=350,y=300)

    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],\
                                         ro[5],ro[6],ro[7],ro[8]))

        i+=1
    tree.place(x=50,y=40)


def halfyearly():

    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select s.rollno,s.studentname,\
    p.english,p.cs,p.physics,p.chemistry,p.biology,p.maths,p.hindi from halfyearly p,studentdetail s \
    where p.rollno=s.rollno')


    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)

    tk.Label(r,text='CLASS XI',fg='red').pack()
    tk.Label(r,text='HALF YEARLY MARKS ENTRY ',fg='red').pack()
    tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')

    tree['column']\
    =('rollno','studentname','english','cs','physics','chemistry','biology','maths','hindi')

    tree.column('rollno',minwidth=50,width=50,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=150,anchor=tk.CENTER)
    tree.column('english',minwidth=50,width=80,anchor=tk.CENTER)
    tree.column('cs',minwidth=50,width=140,anchor=tk.CENTER)
    tree.column('physics',minwidth=100,width=80,anchor=tk.CENTER)
    tree.column('chemistry',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('biology',width=100,anchor=tk.CENTER)
    tree.column('maths',width=100,anchor=tk.CENTER)
    tree.column('hindi',width=100,anchor=tk.CENTER)

    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student Name',anchor=tk.CENTER)
    tree.heading('english',text='English(80)',anchor=tk.CENTER)
    tree.heading('cs',text='Comupter science(70)',anchor=tk.CENTER)
    tree.heading('physics',text='Physics(70)',anchor=tk.CENTER)
    tree.heading('chemistry',text='Chemistry(70)',anchor=tk.CENTER)
    tree.heading('biology',text='Biology(70)',anchor=tk.CENTER)
    tree.heading('maths',text='Maths(80)',anchor=tk.CENTER)
    tree.heading('hindi',text='Hindi(80)',anchor=tk.CENTER)

    #tree.pack()
    #rollno=tk.StringVar()
    #cs=tk.StringVar()
    eng=tk.StringVar()
    cs=tk.StringVar()
    phy=tk.StringVar()
    chem=tk.StringVar()
    bio=tk.StringVar()
    maths=tk.StringVar()
    hindi=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')

    def insert_data():
            global lista
            curitem=tree.focus()
            values=tree.item(curitem,'values')
            if len(values)==0:
                    messagebox.showwarning('Warning','Select Student to Update marks')
            else:   
                    if values[7]=='---' and values[8]=='---':
                        f=tk.Frame(r,width=400,height=320,background='grey')
                        f.place(x=100,y=280)
                        l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                        l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                        l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                        l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                        l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                        a1=tk.Entry(f,textvariable=eng,width=25)
                        a2=tk.Entry(f,textvariable=cs,width=25)
                        a3=tk.Entry(f,textvariable=phy,width=25)
                        a4=tk.Entry(f,textvariable=chem,width=25)
                        a5=tk.Entry(f,textvariable=bio,width=25)
                        l1.place(x=50,y=50)
                        l2.place(x=30,y=90)
                        l3.place(x=50,y=130)
                        l4.place(x=50,y=170)
                        l5.place(x=50,y=210)
                        a1.place(x=170,y=50)
                        a2.place(x=170,y=90)
                        a3.place(x=170,y=130)
                        a4.place(x=170,y=170)
                        a5.place(x=170,y=210)
                        a1.insert(0,values[2])
                        a2.insert(0,values[3])
                        a3.insert(0,values[4])
                        a4.insert(0,values[5])
                        a5.insert(0,values[6])
                        def update_data1():
                            nonlocal a1,a2,a3,a4,a5,curitem,values
                            eng=a1.get()
                            cs=a2.get()
                            phy=a3.get()
                            chem=a4.get()
                            bio=a5.get()
                            lista.clear()
                            lista.extend([eng,cs,phy,chem,bio])
                            for i in lista:
                                    if len(i)==0:
                                            messagebox.showwarning('Warning','Fill the required detial')
                                            break
                                    try:
                                            error=int(i)
                                            
                                    except:
                                            messagebox.showwarning('Warning','Invalid Marks')
                                            break
                                    
                                    
                            
                            else:
                                    if int(eng)>80:
                                            messagebox.showwarning('warning','Invalid Marks')
                                    elif int(cs)>70 or int(phy)>70 or int(chem)>70 or int(bio)>70:
                                            messagebox.showwarning('warning','invalid Marks')
                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                            #print((values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q1="update halfyearly set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                biology='{}' where rollno='{}'".format(eng,cs,phy,chem,bio,values[0])
                                            q2="update hy_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/2.66)))
                                            q3="update hy_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(int(cs)/2.33)))
                                            q4="update hy_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2.33)))
                                            q5="update hy_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2.33)))
                                            q6="update hy_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(int(bio)/2.33)))

                                            cursor.execute(q1)
                                            cursor.execute(q2)
                                            cursor.execute(q3)
                                            cursor.execute(q4)
                                            cursor.execute(q5)
                                            cursor.execute(q6)
                                            
                                            con.commit()
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                        def cancel1():
                                a1.delete(0,tk.END)
                                a2.delete(0,tk.END)
                                a3.delete(0,tk.END)
                                a4.delete(0,tk.END)
                                a5.delete(0,tk.END)
                                f.destroy()
                               
                        savebutton1=tk.Button(f,text='submit',fg='green',command=update_data1)
                        savebutton1.place(x=100,y=270)
                        cancelbutton1=tk.Button(f,text='cancel',fg='green',command=cancel1)
                        cancelbutton1.place(x=200,y=270)
                    elif values[3]=='---' and values[7]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=bio,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[6])
                            def update_data2():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    bio=a5.get()
                                    lista.clear()
                                    lista.extend([eng,phy,hindi,chem,bio])
                                    for j in lista:
                                            if len(j)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    
                                                    error=int(j)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                    
                                                                                           
                                    else:
                                            if int(eng)>80 or int(hindi)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(chem)>70 or int(bio)>70:
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,bio,values[7],hindi)) 
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q2="update halfyearly set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                                biology='{}' where rollno='{}'".format(eng,hindi,phy,chem,bio,values[0])
                                                    q11="update hy_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/2.66)))
                                                    q12="update hy_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(int(hindi)/2.66)))
                                                    q13="update hy_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2.33)))
                                                    q14="update hy_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2.33)))
                                                    q15="update hy_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(int(bio)/2.33)))
                            

                                                    cursor.execute(q2)
                                                    cursor.execute(q11)
                                                    cursor.execute(q12)
                                                    cursor.execute(q13)
                                                    cursor.execute(q14)
                                                    cursor.execute(q15)
                                                
                                                    con.commit()
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                                                    
                            def cance2():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton2=tk.Button(f,text='submit',fg='green',command=update_data2)
                            savebutton2.place(x=100,y=270)
                            cancelbutton2=tk.Button(f,text='cancel',fg='green',command=cance2)
                            cancelbutton2.place(x=200,y=270)
                    elif values[6]=='---' and values[3]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data3():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,hindi,phy,chem,maths])
                                    for k in lista:
                                            if len(k)==0:
                                                    
                                                    
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(k)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            


                                    else:
                                            if int(eng)>80 or int(hindi)>80 or int(maths)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(chem)>70 :
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,values[6],maths,hindi))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q3="update halfyearly set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                        maths='{}' where rollno='{}'".format(eng,hindi,phy,chem,maths,values[0])
                                                    q21="update hy_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/2.66)))
                                                    q22="update hy_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(int(hindi)/2.66)))
                                                    q23="update hy_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2.33)))
                                                    q24="update hy_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2.33)))
                                                    q25="update hy_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(int(maths)/2.66)))
                        
                                                    cursor.execute(q3)
                                                    cursor.execute(q21)
                                                    cursor.execute(q22)
                                                    cursor.execute(q23)
                                                    cursor.execute(q24)
                                                    cursor.execute(q25)
                                                
                                                    con.commit()
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                            def cance3():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton3=tk.Button(f,text='submit',fg='green',command=update_data3)
                            savebutton3.place(x=100,y=270)
                            cancelbutton3=tk.Button(f,text='cancel',fg='green',command=cance3)
                            cancelbutton3.place(x=200,y=270)
                    elif values[6]=='---' and values[8]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=cs,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=30,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data4():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    cs=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,cs,phy,chem,maths])
                                    for v in lista:
                                            if len(v)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(v)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            

                                    else:
                                            if int(eng)>80 or  int(maths)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(cs)>70 or int(chem)>70 :
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    

                                                    tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,values[6],maths,values[8]))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q4="update halfyearly set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                        maths='{}' where rollno='{}'".format(eng,cs,phy,chem,maths,values[0])
                                                    q31="update hy_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/2.66)))
                                                    q32="update hy_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(int(cs)/2.33)))
                                                    q33="update hy_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2.33)))
                                                    q34="update hy_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2.33)))
                                                    q35="update hy_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(int(maths)/2.66)))
                        
                                                    cursor.execute(q4)
                                                    cursor.execute(q31)
                                                    cursor.execute(q32)
                                                    cursor.execute(q33)
                                                    cursor.execute(q34)
                                                    cursor.execute(q35)
                                                            
                                                    con.commit() 
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                            def cance4():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton4=tk.Button(f,text='submit',fg='green',command=update_data4)
                            savebutton4.place(x=100,y=270)
                            cancelbutton4=tk.Button(f,text='cancel',fg='green',command=cance4)
                            cancelbutton4.place(x=200,y=270)

                                            
                            
    insertbutton=tk.Button(r,text='Update marks',command=insert_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=350,y=300)




    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],\
                                         ro[5],ro[6],ro[7],ro[8]))

        i+=1
    tree.place(x=50,y=40)

def annualexam():
    
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select s.rollno,s.studentname,\
    p.english,p.cs,p.physics,p.chemistry,p.biology,p.maths,p.hindi from annualexam p,studentdetail s \
    where p.rollno=s.rollno')


    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)

    tk.Label(r,text='CLASS XI',fg='red').pack()
    tk.Label(r,text='ANNUAL EXAM Marks ENTRY ',fg='red').pack()
    tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')

    tree['column']\
    =('rollno','studentname','english','cs','physics','chemistry','biology','maths','hindi')

    tree.column('rollno',minwidth=50,width=50,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=150,anchor=tk.CENTER)
    tree.column('english',minwidth=50,width=80,anchor=tk.CENTER)
    tree.column('cs',minwidth=50,width=140,anchor=tk.CENTER)
    tree.column('physics',minwidth=100,width=80,anchor=tk.CENTER)
    tree.column('chemistry',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('biology',width=100,anchor=tk.CENTER)
    tree.column('maths',width=100,anchor=tk.CENTER)
    tree.column('hindi',width=100,anchor=tk.CENTER)

    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student Name',anchor=tk.CENTER)
    tree.heading('english',text='English(80)',anchor=tk.CENTER)
    tree.heading('cs',text='Comupter science(70)',anchor=tk.CENTER)
    tree.heading('physics',text='Physics(70)',anchor=tk.CENTER)
    tree.heading('chemistry',text='Chemistry(70)',anchor=tk.CENTER)
    tree.heading('biology',text='Biology(70)',anchor=tk.CENTER)
    tree.heading('maths',text='Maths(80)',anchor=tk.CENTER)
    tree.heading('hindi',text='Hindi(80)',anchor=tk.CENTER)



    #tree.pack()
    #rollno=tk.StringVar()
    #cs=tk.StringVar()
    eng=tk.StringVar()
    cs=tk.StringVar()
    phy=tk.StringVar()
    chem=tk.StringVar()
    bio=tk.StringVar()
    maths=tk.StringVar()
    hindi=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')


    def insert_data():
            global lista
            curitem=tree.focus()
            values=tree.item(curitem,'values')
            if len(values)==0:
                    messagebox.showwarning('Warning','Select Student to Update marks')
            else:   
                    if values[7]=='---' and values[8]=='---':
                        f=tk.Frame(r,width=400,height=320,background='grey')
                        f.place(x=100,y=280)
                        l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                        l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                        l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                        l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                        l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                        a1=tk.Entry(f,textvariable=eng,width=25)
                        a2=tk.Entry(f,textvariable=cs,width=25)
                        a3=tk.Entry(f,textvariable=phy,width=25)
                        a4=tk.Entry(f,textvariable=chem,width=25)
                        a5=tk.Entry(f,textvariable=bio,width=25)
                        l1.place(x=50,y=50)
                        l2.place(x=30,y=90)
                        l3.place(x=50,y=130)
                        l4.place(x=50,y=170)
                        l5.place(x=50,y=210)
                        a1.place(x=170,y=50)
                        a2.place(x=170,y=90)
                        a3.place(x=170,y=130)
                        a4.place(x=170,y=170)
                        a5.place(x=170,y=210)
                        a1.insert(0,values[2])
                        a2.insert(0,values[3])
                        a3.insert(0,values[4])
                        a4.insert(0,values[5])
                        a5.insert(0,values[6])
                        def update_data1():
                            nonlocal a1,a2,a3,a4,a5,curitem,values
                            eng=a1.get()
                            cs=a2.get()
                            phy=a3.get()
                            chem=a4.get()
                            bio=a5.get()
                            lista.clear()
                            lista.extend([eng,cs,phy,chem,bio])
                            for i in lista:
                                    if len(i)==0:
                                            messagebox.showwarning('Warning','Fill the required detial')
                                            break
                                    try:
                                            error=int(i)
                                            
                                    except:
                                            messagebox.showwarning('Warning','Invalid Marks')
                                            break
                                    
                                    
                            
                            else:
                                    if int(eng)>80:
                                            messagebox.showwarning('warning','Invalid Marks')
                                    elif int(cs)>70 or int(phy)>70 or int(chem)>70 or int(bio)>70:
                                            messagebox.showwarning('warning','invalid Marks')
                                    else:
                                            tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                            #print((values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                            cursor=con.cursor()
                                            q1="update annualexam set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                biology='{}' where rollno='{}'".format(eng,cs,phy,chem,bio,values[0])
                                            q2="update ae_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/1.6)))
                                            q3="update ae_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(int(cs)/2)))
                                            q4="update ae_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2)))
                                            q5="update ae_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2)))
                                            q6="update ae_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(int(bio)/2)))

                                            cursor.execute(q1)
                                            cursor.execute(q2)
                                            cursor.execute(q3)
                                            cursor.execute(q4)
                                            cursor.execute(q5)
                                            cursor.execute(q6)
                                            
                                        
                                            con.commit()
                                            a1.delete(0,tk.END)
                                            a2.delete(0,tk.END)
                                            a3.delete(0,tk.END)
                                            a4.delete(0,tk.END)
                                            a5.delete(0,tk.END)
                                            f.destroy()
                        def cancel1():
                                a1.delete(0,tk.END)
                                a2.delete(0,tk.END)
                                a3.delete(0,tk.END)
                                a4.delete(0,tk.END)
                                a5.delete(0,tk.END)
                                f.destroy()
                               
                        savebutton1=tk.Button(f,text='submit',fg='green',command=update_data1)
                        savebutton1.place(x=100,y=270)
                        cancelbutton1=tk.Button(f,text='cancel',fg='green',command=cancel1)
                        cancelbutton1.place(x=200,y=270)
                    elif values[3]=='---' and values[7]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=bio,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[6])
                            def update_data2():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    bio=a5.get()
                                    lista.clear()
                                    lista.extend([eng,phy,hindi,chem,bio])
                                    for j in lista:
                                            if len(j)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    
                                                    error=int(j)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                    
                                                                                           
                                    else:
                                            if int(eng)>80 or int(hindi)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(chem)>70 or int(bio)>70:
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,bio,values[7],hindi)) 
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q2="update annualexam set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                                biology='{}' where rollno='{}'".format(eng,hindi,phy,chem,bio,values[0])
                                                    q11="update ae_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/1.6)))
                                                    q12="update ae_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(int(hindi)/1.6)))
                                                    q13="update ae_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2)))
                                                    q14="update ae_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2)))
                                                    q15="update ae_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(int(bio)/2)))
                            

                                                    cursor.execute(q2)
                                                    cursor.execute(q11)
                                                    cursor.execute(q12)
                                                    cursor.execute(q13)
                                                    cursor.execute(q14)
                                                    cursor.execute(q15)
                                                
                                                
                                                    con.commit()
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                                                    
                            def cance2():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton2=tk.Button(f,text='submit',fg='green',command=update_data2)
                            savebutton2.place(x=100,y=270)
                            cancelbutton2=tk.Button(f,text='cancel',fg='green',command=cance2)
                            cancelbutton2.place(x=200,y=270)
                    elif values[6]=='---' and values[3]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=hindi,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=50,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[8])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data3():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    hindi=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,hindi,phy,chem,maths])
                                    for k in lista:
                                            if len(k)==0:
                                                    
                                                    
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(k)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            


                                    else:
                                            if int(eng)>80 or int(hindi)>80 or int(maths)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(chem)>70 :
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],eng,values[3],phy,chem,values[6],maths,hindi))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q3="update annualexam set english='{}',hindi='{}',physics='{}',chemistry='{}',\
                                                        maths='{}' where rollno='{}'".format(eng,hindi,phy,chem,maths,values[0])
                                                    q21="update ae_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/1.6)))
                                                    q22="update ae_{} set marks='{}' where subject='HINDI'".format(values[0],str(int(int(hindi)/1.6)))
                                                    q23="update ae_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2)))
                                                    q24="update ae_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2)))
                                                    q25="update ae_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(int(maths)/1.6)))
                        
                                                    cursor.execute(q3)
                                                    cursor.execute(q21)
                                                    cursor.execute(q22)
                                                    cursor.execute(q23)
                                                    cursor.execute(q24)
                                                    cursor.execute(q25)
                                                
                                                    
                                                    con.commit()
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                            def cance3():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton3=tk.Button(f,text='submit',fg='green',command=update_data3)
                            savebutton3.place(x=100,y=270)
                            cancelbutton3=tk.Button(f,text='cancel',fg='green',command=cance3)
                            cancelbutton3.place(x=200,y=270)
                    elif values[6]=='---' and values[8]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l5=tk.Label(f,text='Maths',width=10,font=('Times',11,'bold'))
                            a1=tk.Entry(f,textvariable=eng,width=25)
                            a2=tk.Entry(f,textvariable=cs,width=25)
                            a3=tk.Entry(f,textvariable=phy,width=25)
                            a4=tk.Entry(f,textvariable=chem,width=25)
                            a5=tk.Entry(f,textvariable=maths,width=25)
                            l1.place(x=50,y=50)
                            l2.place(x=30,y=90)
                            l3.place(x=50,y=130)
                            l4.place(x=50,y=170)
                            l5.place(x=50,y=210)
                            a1.place(x=170,y=50)
                            a2.place(x=170,y=90)
                            a3.place(x=170,y=130)
                            a4.place(x=170,y=170)
                            a5.place(x=170,y=210)
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            a5.insert(0,values[7])
                            def update_data4():
                                    nonlocal a1,a2,a3,a4,a5,curitem,values
                                    eng=a1.get()
                                    cs=a2.get()
                                    phy=a3.get()
                                    chem=a4.get()
                                    maths=a5.get()
                                    lista.clear()
                                    lista.extend([eng,cs,phy,chem,maths])
                                    for v in lista:
                                            if len(v)==0:
                                                    messagebox.showwarning('Warning','Fill the required detial')
                                                    break
                                            try:
                                                    error=int(v)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            

                                    else:
                                            if int(eng)>80 or  int(maths)>80:
                                                    messagebox.showwarning('warning','Invalid Marks')
                                            elif int(phy)>70 or int(cs)>70 or int(chem)>70 :
                                                    messagebox.showwarning('warning','invalid Marks')
                                            else:
                                                    

                                                    tree.item(curitem,values=(values[0],values[1],eng,cs,phy,chem,values[6],maths,values[8]))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q4="update annualexam set english='{}',cs='{}',physics='{}',chemistry='{}',\
                                                        maths='{}' where rollno='{}'".format(eng,cs,phy,chem,maths,values[0])
                                                    q31="update ae_{} set marks='{}' where subject='ENGLISH'".format(values[0],str(int(int(eng)/1.6)))
                                                    q32="update ae_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(int(cs)/2)))
                                                    q33="update ae_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(int(phy)/2)))
                                                    q34="update ae_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(int(chem)/2)))
                                                    q35="update ae_{} set marks='{}' where subject='MATHS'".format(values[0],str(int(int(maths)/1.6)))
                        
                                                    cursor.execute(q4)
                                                    cursor.execute(q31)
                                                    cursor.execute(q32)
                                                    cursor.execute(q33)
                                                    cursor.execute(q34)
                                                    cursor.execute(q35)
                                                            
                                                    
                                                    con.commit() 
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    a5.delete(0,tk.END)
                                                    f.destroy()
                            def cance4():
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton4=tk.Button(f,text='submit',fg='green',command=update_data4)
                            savebutton4.place(x=100,y=270)
                            cancelbutton4=tk.Button(f,text='cancel',fg='green',command=cance4)
                            cancelbutton4.place(x=200,y=270)


                                            
                            
    insertbutton=tk.Button(r,text='Update marks',command=insert_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=350,y=300)


    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],\
                                         ro[5],ro[6],ro[7],ro[8]))

        i+=1
    tree.place(x=50,y=40)


def practicalexam():
   
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select s.rollno,s.studentname,\
    p.cs,p.physics,p.chemistry,p.biology from \
    practical p,studentdetail s \
    where p.rollno=s.rollno')


    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)

    tk.Label(r,text='CLASS XI',fg='red').pack()
    tk.Label(r,text='PRACTICAL EXAM Marks ENTRY ',fg='red').pack()
    tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(r)
    s.theme_use('clam')

    tree['column']\
    =('rollno','studentname','cs','physics','chemistry','biology')

    tree.column('rollno',minwidth=50,width=100,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=150,anchor=tk.CENTER)
    tree.column('cs',minwidth=50,width=140,anchor=tk.CENTER)
    tree.column('physics',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('chemistry',minwidth=100,width=100,anchor=tk.CENTER)
    tree.column('biology',width=100,anchor=tk.CENTER)


    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student Name',anchor=tk.CENTER)
    tree.heading('cs',text='Comupter science(30)',anchor=tk.CENTER)
    tree.heading('physics',text='Physics(30)',anchor=tk.CENTER)
    tree.heading('chemistry',text='Chemistry(30)',anchor=tk.CENTER)
    tree.heading('biology',text='Biology(30)',anchor=tk.CENTER)

    #tree.pack()
    #rollno=tk.StringVar()
    #cs=tk.StringVar()
    #eng=tk.StringVar()
    cs=tk.StringVar()
    phy=tk.StringVar()
    chem=tk.StringVar()
    bio=tk.StringVar()
    #Wmaths=tk.StringVar()
    #hindi=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')


    def insert_data():
            global lista
            curitem=tree.focus()
            values=tree.item(curitem,'values')
            
            #print(values)
            if len(values)==0:
                    messagebox.showwarning('Warning','Select Student to Update marks')
            else:
                    if values[2]=='---' and values[5]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            #l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            #l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l1=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            #l3=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            #a1=tk.Entry(f,textvariable=eng,width=25)
                            #a2=tk.Entry(f,textvariable=hindi,width=25)
                            a1=tk.Entry(f,textvariable=phy,width=25)
                            a2=tk.Entry(f,textvariable=chem,width=25)
                            #a3=tk.Entry(f,textvariable=bio,width=25)
                            #l1.place(x=50,y=50)
                            #l2.place(x=50,y=90)
                            l1.place(x=50,y=130)
                            l2.place(x=50,y=170)
                            #l3.place(x=50,y=210)
                            #a1.place(x=170,y=50)
                            #a2.place(x=170,y=90)
                            a1.place(x=170,y=130)
                            a2.place(x=170,y=170)
                            #a3.place(x=170,y=210)
                            #a1.insert(0,values[2])
                            #a2.insert(0,values[8])
                            a1.insert(0,values[3])
                            a2.insert(0,values[4])
                            #a3.insert(0,values[5])
                            def update_data2():
                                    nonlocal a1,a2,curitem,values
                                    #eng=a1.get()
                                    #hindi=a2.get()
                                    phy=a1.get()
                                    chem=a2.get()
                                    #bio=a3.get()
                                    lista.clear()
                                    lista.extend([phy,chem])
                                    for j in lista:
                                            if len(j)==0:
                                                    messagebox.showwarning('Warning','Fill the requigreen detial')
                                                    break
                                            try:
                                                    
                                                    error=int(j)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                    
                                                                                           
                                    else:
                                            
                                            if int(phy)>30 or int(chem)>30 :
                                                    messagebox.showwarning('warning','marks should be /30')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],values[2],phy,chem,values[5])) 
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q2="update practical set physics='{}',chemistry='{}' where rollno='{}'".format(phy,chem,values[0])
                                                    q11="update pe_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/2))
                                                    q12="update pe_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/2))
                                                    
                                                    cursor.execute(q2)
                                                    cursor.execute(q11)
                                                    cursor.execute(q12)
                                                    con.commit()
                                                    #a1.delete(0,tk.END)
                                                    #a2.delete(0,tk.END)
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    #a3.delete(0,tk.END)
                                                    f.destroy()
                                                    
                            def cance2():
                                    #a1.delete(0,tk.END)
                                    #a2.delete(0,tk.END)
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    #a3.delete(0,tk.END)
                                    f.destroy()
                            savebutton2=tk.Button(f,text='submit',fg='green',command=update_data2)
                            savebutton2.place(x=100,y=270)
                            cancelbutton2=tk.Button(f,text='cancel',fg='green',command=cance2)
                            cancelbutton2.place(x=200,y=270)
                    elif values[2]=='---' :
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            #print(values)
                            #l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            #l2=tk.Label(f,text='Hindi',width=10,font=('Times',11,'bold'))
                            l1=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='biology',width=10,font=('Times',11,'bold'))
                            #a1=tk.Entry(f,textvariable=eng,width=25)
                            #a2=tk.Entry(f,textvariable=hindi,width=25)
                            a1=tk.Entry(f,textvariable=phy,width=25)
                            a2=tk.Entry(f,textvariable=chem,width=25)
                            a3=tk.Entry(f,textvariable=bio,width=25)
                            #l1.place(x=50,y=50)
                            #l2.place(x=50,y=90)
                            l1.place(x=50,y=130)
                            l2.place(x=50,y=170)
                            l3.place(x=50,y=210)
                            #a1.place(x=170,y=50)
                            #a2.place(x=170,y=90)
                            a1.place(x=170,y=130)
                            a2.place(x=170,y=170)
                            a3.place(x=170,y=210)
                            #a1.insert(0,values[2])
                            #a2.insert(0,values[8])
                            a1.insert(0,values[3])
                            a2.insert(0,values[4])
                            a3.insert(0,values[5])
                            def update_data3():
                                    nonlocal a1,a2,a3,curitem,values
                                    #eng=a1.get()
                                    #hindi=a2.get()
                                    phy=a1.get()
                                    chem=a2.get()
                                    bio=a3.get()
                                    lista.clear()
                                    lista.extend([phy,chem,bio])
                                    for k in lista:
                                            if len(k)==0:
                                                    
                                                    
                                                    messagebox.showwarning('Warning','Fill the requigreen detial')
                                                    break
                                            try:
                                                    error=int(k)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            


                                    else:
                                            
                                                    
                                            if int(phy)>30 or int(chem)>30 or int(bio)>30:
                                                    messagebox.showwarning('warning','marks should be /30')
                                            else:
                                                    
                                                    tree.item(curitem,values=(values[0],values[1],values[2],phy,chem,bio))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q3="update practical set physics='{}',chemistry='{}',biology='{}'\
                                                      where rollno='{}'".format(phy,chem,bio,values[0])
                                                    q21="update pe_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/2))
                                                    q22="update pe_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/2))
                                                    
                                                    q23="update pe_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/2))
                                                    
                                                    cursor.execute(q3)
                                                    cursor.execute(q21)
                                                    cursor.execute(q22)
                                                    cursor.execute(q23)
                                                    con.commit()
                                                    #a1.delete(0,tk.END)
                                                    #a2.delete(0,tk.END)
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    f.destroy()
                            def cance3():
                                    #a1.delete(0,tk.END)
                                    #a2.delete(0,tk.END)
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    f.destroy()
                            savebutton3=tk.Button(f,text='submit',fg='green',command=update_data3)
                            savebutton3.place(x=100,y=270)
                            cancelbutton3=tk.Button(f,text='cancel',fg='green',command=cance3)
                            cancelbutton3.place(x=200,y=270)
                    elif values[5]=='---':
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            #l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l1=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            #l5=tk.Label(f,text='Maths',width=10,font=('Times',11,'bold'))
                            #a1=tk.Entry(f,textvariable=eng,width=25)
                            a1=tk.Entry(f,textvariable=cs,width=25)
                            a2=tk.Entry(f,textvariable=phy,width=25)
                            a3=tk.Entry(f,textvariable=chem,width=25)
                            #a5=tk.Entry(f,textvariable=maths,width=25)
                            #l1.place(x=50,y=50)
                            l1.place(x=30,y=90)
                            l2.place(x=50,y=130)
                            l3.place(x=50,y=170)
                            #l5.place(x=50,y=210)
                            #a1.place(x=170,y=50)
                            a1.place(x=170,y=90)
                            a2.place(x=170,y=130)
                            a3.place(x=170,y=170)
                            #a5.place(x=170,y=210)
                            #a1.insert(0,values[2])
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            #a5.insert(0,values[7])
                            def update_data4():
                                    nonlocal a1,a2,a3,curitem,values
                                    #eng=a1.get()
                                    cs=a1.get()
                                    phy=a2.get()
                                    chem=a3.get()
                                    #maths=a5.get()
                                    lista.clear()
                                    lista.extend([cs,phy,chem])
                                    for v in lista:
                                            if len(v)==0:
                                                    messagebox.showwarning('Warning','Fill the requigreen detial')
                                                    break
                                            try:
                                                    error=int(v)
                                            
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Entry')
                                                    break
                                            

                                    else:
                                            
                                            if int(phy)>30 or int(cs)>30 or int(chem)>30 :
                                                    messagebox.showwarning('warning','marks should be /30')
                                            else:
                                                    

                                                    tree.item(curitem,values=(values[0],values[1],cs,phy,chem,values[5]))
                                                   
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q4="update practical set cs='{}',physics='{}',chemistry='{}'\
                                                         where rollno='{}'".format(cs,phy,chem,values[0])
                                                    q31="update pe_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/2))
                                                    q32="update pe_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/2))
                                                    
                                                    q33="update pe_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/2))
                                                    
                                                    cursor.execute(q4)
                                                    cursor.execute(q31)
                                                    cursor.execute(q32)
                                                    cursor.execute(q33)
                                                    
                                                    con.commit() 
                                                    #a1.delete(0,tk.END)
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    #a5.delete(0,tk.END)
                                                    f.destroy()
                            def cance4():
                                    #a1.delete(0,tk.END)
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    #a5.delete(0,tk.END)
                                    f.destroy()
                            savebutton4=tk.Button(f,text='submit',fg='green',command=update_data4)
                            savebutton4.place(x=100,y=270)
                            cancelbutton4=tk.Button(f,text='cancel',fg='green',command=cance4)
                            cancelbutton4.place(x=200,y=270)
                    else:
                            f=tk.Frame(r,width=400,height=320,background='grey')
                            f.place(x=100,y=280)
                            #l1=tk.Label(f,text='English',width=8,font=('Times',11,'bold'))
                            l1=tk.Label(f,text='Computer Science',width=14,font=('Times',11,'bold'))
                            l2=tk.Label(f,text='Physics',width=10,font=('Times',11,'bold'))
                            l3=tk.Label(f,text='Chemistry',width=10,font=('Times',11,'bold'))
                            l4=tk.Label(f,text='Biology',width=10,font=('Times',11,'bold'))
                            #a1=tk.Entry(f,textvariable=eng,width=25)
                            a1=tk.Entry(f,textvariable=cs,width=25)
                            a2=tk.Entry(f,textvariable=phy,width=25)
                            a3=tk.Entry(f,textvariable=chem,width=25)
                            a4=tk.Entry(f,textvariable=bio,width=25)
                            #l1.place(x=50,y=50)
                            l1.place(x=30,y=90)
                            l2.place(x=50,y=130)
                            l3.place(x=50,y=170)
                            l4.place(x=50,y=210)
                            #a1.place(x=170,y=50)
                            a1.place(x=170,y=90)
                            a2.place(x=170,y=130)
                            a3.place(x=170,y=170)
                            a4.place(x=170,y=210)
                            #a1.insert(0,values[2])
                            a1.insert(0,values[2])
                            a2.insert(0,values[3])
                            a3.insert(0,values[4])
                            a4.insert(0,values[5])
                            def update_data1():
                                    nonlocal a1,a2,a3,a4,curitem,values
                                    #eng=a1.get()
                                    cs=a1.get()
                                    phy=a2.get()
                                    chem=a3.get()
                                    bio=a4.get()
                                    lista.clear()
                                    lista.extend([cs,phy,chem,bio])
                                    for i in lista:
                                            if len(i)==0:
                                                    messagebox.showwarning('Warning','Fill the requigreen detial')
                                                    break
                                            try:
                                                    error=int(i)
                                                    
                                            except:
                                                    messagebox.showwarning('Warning','Invalid Marks')
                                                    break
                                            
                                            
                                    
                                    else:
                                            
                                            if int(cs)>30 or int(phy)>30 or int(chem)>30 or int(bio)>30:
                                                    messagebox.showwarning('warning','marks should be /30')
                                            else:
                                                    tree.item(curitem,values=(values[0],values[1],cs,phy,chem,bio))
                                                    #print((values[0],values[1],eng,cs,phy,chem,bio,values[7],values[8]))
                                                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                                                    cursor=con.cursor()
                                                    q1="update practical set cs='{}',physics='{}',chemistry='{}',\
                                                        biology='{}' where rollno='{}'".format(cs,phy,chem,bio,values[0])
                                                    q41="update pe_{} set marks='{}' where subject='PHYSICS'".format(values[0],str(int(phy)/2))
                                                    q42="update pe_{} set marks='{}' where subject='CHEMISTRY'".format(values[0],str(int(chem)/2))
                                                    q43="update pe_{} set marks='{}' where subject='BIOLOGY'".format(values[0],str(int(bio)/2))
                                                    q44="update pe_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(values[0],str(int(cs)/2))
                                                    
                                                    cursor.execute(q1)
                                                    cursor.execute(q41)
                                                    cursor.execute(q42)
                                                    cursor.execute(q43)
                                                    cursor.execute(q44)
                                                    
                                                    con.commit()
                                                    #a1.delete(0,tk.END)
                                                    a1.delete(0,tk.END)
                                                    a2.delete(0,tk.END)
                                                    a3.delete(0,tk.END)
                                                    a4.delete(0,tk.END)
                                                    f.destroy()
                            def cancel1():
                                    
                                    a1.delete(0,tk.END)
                                    a2.delete(0,tk.END)
                                    a3.delete(0,tk.END)
                                    a4.delete(0,tk.END)
                                    #a5.delete(0,tk.END)
                                    f.destroy()
                                       
                            savebutton1=tk.Button(f,text='submit',fg='green',command=update_data1)
                            savebutton1.place(x=100,y=270)
                            cancelbutton1=tk.Button(f,text='cancel',fg='green',command=cancel1)
                            cancelbutton1.place(x=200,y=270)                            
                                    
                                                        
    insertbutton=tk.Button(r,text='Update marks',command=insert_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=350,y=300)




    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],\
                                         ro[5]))

        i+=1
    tree.place(x=70,y=40)


def interface4():
    win4=tk.Tk()
    win4.title("RESULT")
    win4.geometry('400x300')
    tk.Label(win4,text='Update Marksheet XI',bg='lightblue')\
                               .pack()
    tk.Button(win4,text='Periodic Text I',bg='lightpink',command=periodic1)\
                               .place(x=150,y=57)
    tk.Button(win4,text='Periodic Text II',bg='lightpink',command=periodic2)\
                               .place(x=150,y=97)
    tk.Button(win4,text='Half Yearly',bg='lightpink',command=halfyearly)\
                               .place(x=160,y=137)
    tk.Button(win4,text='Annual Exam',bg='lightpink',command=annualexam)\
                               .place(x=150,y=177)
    tk.Button(win4,text='Practical Exam',bg='lightpink',command=practicalexam)\
                               .place(x=150,y=217)


def finalresult():
    k=tk.Tk()
    def suppli():
        con2=c.connect(host='localhost',user='root',passwd=a[1],database='result')
        cursor2=con2.cursor()
        querr="select * from grade_{} where marks='E'".format(listb[0])
        cursor2.execute(querr)
        supp=cursor2.fetchall()
        if cursor2.rowcount>1:
            tk.Label(k,text='REMARK: FAIL(SUMMPLIMENTARY IN MORE THAN ONE SUBJECT',fg='red').place(x=30,y=420)
            tk.Label(k,text='RESULT: FAIL',fg='red').place(x=500,y=420)
        elif cursor2.rowcount==1:
            tk.Label(k,text='REMARK: SUMMPLIMENTARY IN {}'.format(supp[0][0],fg='red')).place(x=30,y=420)
            tk.Label(k,text='RESULT: SUMMPLIMENTARY IN MENTION SUBJECT',fg='red').place(x=500,y=420)
        else:
            querry="select marks from grade_{} where marks='A1'".format(listb[0])
            cursor2.execute(querry)
            A1=cursor2.fetchall()
            a1=cursor2.rowcount
            querry1="select marks from grade_{} where marks in ('A1','A2')".format(listb[0])
            cursor2.execute(querry1)
            A2=cursor2.fetchall()
            a2=cursor2.rowcount       
            querry2="select marks from grade_{} where marks in ('A1','A2','B1','B2')".format(listb[0])
            cursor2.execute(querry2)
            B12=cursor2.fetchall()
            b12=cursor2.rowcount
            querry3="select marks from grade_{} where marks in ('A1','A2','B1','B2','C1','C2')".format(listb[0])
            cursor2.execute(querry3)
            C12=cursor2.fetchall()
            c12=cursor2.rowcount
            querry4="select marks from grade_{} where marks in ('A1','A2','B1','B2','C1','C2','D')".format(listb[0])
            cursor2.execute(querry4)
            D=cursor2.fetchall()
            d=cursor2.rowcount
            if a1==5:
                tk.Label(k,text='REMARK: OUTSTANDING',fg='red').place(x=30,y=420)
                tk.Label(k,text='PROMOTED TO CLASS XII',fg='red').place(x=30,y=450)
            elif a2==5:
                tk.Label(k,text='REMARK:  EXCELLENT',fg='red').place(x=30,y=420)
                tk.Label(k,text='PROMOTED TO CLASS XII',fg='red').place(x=30,y=450)
            elif b12==5:
                tk.Label(k,text='REMARK:  VERY GOOD',fg='red').place(x=30,y=420)
                tk.Label(k,text='PROMOTED TO CLASS XII',fg='red').place(x=30,y=450)
            elif c12:
                tk.Label(k,text='REMARK:  GOOD',fg='red').place(x=30,y=420)
                tk.Label(k,text='PROMOTED TO CLASS XII',fg='red').place(x=30,y=450)
            elif d==5:
                tk.Label(k,text='REMARK:  NEED IMPROVEMENT',fg='red').place(x=30,y=420)
                tk.Label(k,text='PROMOTED TO CLASS XII',fg='red').place(x=30,y=450)
            tk.Label(k,text='RESULT: PASS',fg='red').place(x=500,y=420)
            #per=((sum(percent))/5)
            #tk.Label(k,text='{}'.format(per),fg='black').place(x=560,y=420)
        tk.Label(k,text='Date:   ______________',fg='black').place(x=40,y=490)
        tk.Label(k,text='Signature of Class Teacher',fg='black').place(x=400,y=490)
        tk.Label(k,text='Signature of Principal',fg='black').place(x=720,y=490)
                                                                                              
    def schoolview():
        nonlocal k
        con1=c.connect(host='localhost',user='root',passwd=a[1],database='result')
        mycursor=con1.cursor()
        mycursor.execute('select * from schooldetail')
        d=mycursor.fetchall()
        tk.Label(k,text=(d[0][0]).upper(),fg='black').pack()
        tk.Label(k,text='ACADEMIC SESSION {}'.format(d[0][5]),fg='black').pack()
        tk.Label(k,text='REPORT CARD',fg='black').pack()
        #tk.Label(r,text=(d[0][1]).upper(),fg='black').pack()
        
        tk.Label(k,text='CBSE Affiliation NO: {}'.format(d[0][2]),fg='black')\
                              .place(x=10,y=20)
        tk.Label(k,text='School No: {}'.format(d[0][3]),fg='black')\
                                .place(x=700,y=40)
        tk.Label(k,text='School Website: {}'.format(d[0][4]),fg='black')\
                                .place(x=700,y=10)
        
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    query1="select t1.subject,t1.marks,t2.marks,t3.marks,t5.marks,t4.marks,t6.marks,t7.marks from \
    pt1_{} t1,pt2_{} t2,hy_{} t3,ae_{} t4,pe_{} t5,total_{} t6,grade_{} t7 where t1.subject=t2.subject and \
    t1.subject=t3.subject and t1.subject=t4.subject and t1.subject=t5.subject and t1.subject=t6.subject and t1.subject=t7.subject"\
    .format(listb[0],listb[0],listb[0],listb[0],listb[0],listb[0],listb[0])
        

    
    cursor.execute(query1)

   
    con2=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    hercursor=con2.cursor()
    query2='select * from studentdetail where rollno={}'.format(listb[0])
    hercursor.execute(query2)
    d1=hercursor.fetchall()
    #print(d1)
    tk.Label(k,text='ROLL NO:      {}'.format(d1[0][0]),fg='black')\
                          .place(x=10,y=50)
    
    tk.Label(k,text='STUDENT\'S NAME:  {}'.format((d1[0][1]).upper()),fg='black')\
                                .place(x=10,y=80)

    tk.Label(k,text='DATE OF BIRTH:  {}'.format(d1[0][4]),fg='black')\
                          .place(x=10,y=110)
    k1=700
    if len(d1[0][3])>12:
        k1=600
        

    tk.Label(k,text='MOTHER\'S NAME:  Mrs. {}'.format((d1[0][3]).upper()),fg='black')\
                               .place(x=k1,y=80)
    tk.Label(k,text='FATHER\'S NAME:   Mr.  {}'.format((d1[0][2]).upper()),fg='black')\
                               .place(x=k1,y=110)
    schoolview()
    suppli()
    
    #r.title('{}'.format(s[0][0]))
    k.geometry('1000x1000')
    tree=ttk.Treeview(k)

    #tk.Label(r,text='PRACTICAL EXAM Marks ENTRY ',fg='black').pack()
    #tk.Label(r,text='(If Student was Absent Enter The Marks 00)',fg='blue').place(x=700,y=270)
    tree['show']='headings'
    s=ttk.Style(k)
    s.theme_use('clam')
    tree['column']\
    =('subject','mark1','mark2','mark3','mark4','mark5','mark6','mark7')

    tree.column('subject',minwidth=50,width=140,anchor=tk.CENTER)
    tree.column('mark1',minwidth=50,width=100,anchor=tk.CENTER)
    tree.column('mark2',minwidth=50,width=100,anchor=tk.CENTER)
    tree.column('mark3',minwidth=100,width=140,anchor=tk.CENTER)
    tree.column('mark4',minwidth=100,width=140,anchor=tk.CENTER)
    tree.column('mark5',width=140,anchor=tk.CENTER)
    tree.column('mark6',width=120,anchor=tk.CENTER)
    tree.column('mark7',width=90,anchor=tk.CENTER)
    

    tree.heading('subject',text='SUBJECT NAME',anchor=tk.CENTER)
    tree.heading('mark1',text='PT-1(10)',anchor=tk.CENTER)
    tree.heading('mark2',text='PT-2(10)',anchor=tk.CENTER)
    tree.heading('mark3',text='HALF YEARLY(30)',anchor=tk.CENTER)
    tree.heading('mark4',text='PRACTICAL EXAM(15)',anchor=tk.CENTER)
    tree.heading('mark5',text='ANNUAL EXAM(35)',anchor=tk.CENTER)
    tree.heading('mark6',text='GRAND TOTAL(100)',anchor=tk.CENTER)
    tree.heading('mark7',text='GRADE',anchor=tk.CENTER)

    i=0
    for ro in cursor:
        #print(ro)
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))
        
        i+=1
    tree.place(x=20,y=180)


    


def studentresultview():
    
    global listb,listpt1,listpt2,listhy,listae,listpe,total
    listpt1.clear()
    listpt2.clear()
    listhy.clear()
    listae.clear()
    listpe.clear()
    total.clear()
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    try:
        q1='select * from schooldetail'
        cursor.execute(q1)
        a1=cursor.fetchall()
        A=cursor.rowcount
            
            
            
        q2='select * from studentdetail where rollno={}'.format(listb[0])
        cursor.execute(q2)
        b1=cursor.fetchall()
        B=cursor.rowcount
            
            
        q3='select chemistry,physics,biology,hindi,cs,english,maths from pt1 where rollno={}'.format(listb[0])
        cursor.execute(q3)
        for i in cursor:
            for j in i:
                if j!=' ' and j!='---':
                    listpt1.append(j)
            
        q4='select chemistry,physics,biology,hindi,cs,english,maths from pt2 where rollno={}'.format(listb[0])
        cursor.execute(q4)
        for k in cursor:
            for l in k:
                if l!=' ' and l!='---':
                    listpt2.append(l)
            
        q5='select chemistry,physics,biology,hindi,cs,english,maths from halfyearly where rollno={}'.format(listb[0])
        cursor.execute(q5)
        for m in cursor:
            for n in m:
                if n!=' ' and n!='---':
                    listhy.append(n)
            
        q6='select chemistry,physics,biology,hindi,cs,english,maths from annualexam where rollno={}'.format(listb[0])
        cursor.execute(q6)
        for o in cursor:
            for p in o:
                if p!=' ' and p!='---':
                    listae.append(p)
            
        q7='select chemistry,physics,biology,cs from practical where rollno={}'.format(listb[0])
        cursor.execute(q7)
        for r in cursor:
            for s in r:
                if s!=' ' and s!='---':
                    listpe.append(s)
        Break=True
        
        if A!=1:
            messagebox.showwarning('Alert','No School Detail Data Found')
            Break=False
            #print('1st')
        elif B!=1:
            messagebox.showwarning('Alert','No Result Found For Rollno {}'.format(listb[0]))
            Break=False
            
            #print('2nd')
        elif len(listpt1)!=5:
            messagebox.showinfo('Alert','Not Enough Data To Show Result')
            Break=False
            #print('3nd')
        elif len(listpt2)!=5:
            messagebox.showinfo('Alert','Not Enough Data To Show Result')
            Break=False
            #print('4nd')
        elif len(listhy)!=5:
            messagebox.showinfo('Alert','Not Enough Data To Show Result')
            Break=False
            #print('5nd')
        elif len(listae)!=5:
            messagebox.showinfo('Alert','Not Enough Data To Show Result')
            Break=False
            #print('5nd')
        elif len(listpe)!=2 and len(listpe)!=3 and len(listpe)!=4:
            messagebox.showinfo('Alert','Not Enough Data To Show Result')
            Break=False
            #print('6th')
        #print('check')
        

        query80="select t1.marks,t2.marks,t3.marks,t5.marks,t4.marks from \
        pt1_{} t1,pt2_{} t2,hy_{} t3,ae_{} t4,pe_{} t5 where t1.subject=t2.subject and \
        t1.subject=t3.subject and t1.subject=t4.subject and t1.subject=t5.subject"\
        .format(listb[0],listb[0],listb[0],listb[0],listb[0])


        cursor.execute(query80)
        m1=cursor.fetchall()
        #print(m1)
        total.clear()
        for z in m1[0]:
            if z!=' ':
                total.append(float(z))
                
        if sum(total)!=0:
            x1=("update total_{}  set marks={} where subject='BIOLOGY'".format(listb[0],sum(total)))
            cursor.execute(x1)
            if sum(total)>90:
                x11=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'A1'))
                cursor.execute(x11)
            elif sum(total)>80:
                x12=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'A2'))
                cursor.execute(x12)
            elif sum(total)>70:
                x13=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'B1'))
                cursor.execute(x13)
            elif sum(total)>70:
                x14=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'B2'))
                cursor.execute(x14)
            elif sum(total)>60:
                x15=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'C1'))
                cursor.execute(x15)
            elif sum(total)>50:
                x16=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'C2'))
                cursor.execute(x16)
            elif sum(total)>33:
                x17=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'D'))
                cursor.execute(x17)
            else:
                x18=("update grade_{} set marks='{}' where subject='BIOLOGY'".format(listb[0],'E'))
                cursor.execute(x18)
            
        percent=total.copy()      
        #print(total)
        total.clear()

        for zn in m1[1]:
            if zn!=' ':
                total.append(float(zn))
        if sum(total)!=0:
            x2=("update total_{} set marks={} where subject='CHEMISTRY'".format(listb[0],sum(total)))
            cursor.execute(x2)
            if sum(total)>90:
                x21=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'A1'))
                cursor.execute(x21)
            elif sum(total)>80:
                x22=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'A2'))
                cursor.execute(x22)
            elif sum(total)>70:
                x23=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'B1'))
                cursor.execute(x23)
            elif sum(total)>70:
                x24=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'B2'))
                cursor.execute(x24)
            elif sum(total)>60:
                x25=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'C1'))
                cursor.execute(x25)
            elif sum(total)>50:
                x26=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'C2'))
                cursor.execute(x26)
            elif sum(total)>33:
                x27=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'D'))
                cursor.execute(x27)
            else:
                x28=("update grade_{} set marks='{}' where subject='CHEMISTRY'".format(listb[0],'E'))
                cursor.execute(x28)
            
            
            
        #print(sum(total))

        total.clear()
        for nb in m1[2]:
            if nb!=' ':
                total.append(float(nb))
        if sum(total)!=0:
            
            x3=("update total_{} set marks={} where subject='COMPUTER SCIENCE'".format(listb[0],sum(total)))
            cursor.execute(x3)
            if sum(total)>90:
                x31=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'A1'))
                cursor.execute(x31)
            elif sum(total)>80:
                x32=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'A2'))
                cursor.execute(x32)
            elif sum(total)>70:
                x33=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'B1'))
                cursor.execute(x33)
            elif sum(total)>70:
                x34=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'B2'))
                cursor.execute(x34)
            elif sum(total)>60:
                x35=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'C1'))
                cursor.execute(x35)
            elif sum(total)>50:
                x36=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'C2'))
                cursor.execute(x36)
            elif sum(total)>33:
                x37=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'D'))
                cursor.execute(x37)
            else:
                x38=("update grade_{} set marks='{}' where subject='COMPUTER SCIENCE'".format(listb[0],'E'))
                cursor.execute(x38)
            
        #print(total)

        total.clear()

        for na in m1[3]:
            if na!=' ':
                total.append(float(na))
        if sum(total)!=0:
            x4=("update total_{} set marks={} where subject='ENGLISH'".format(listb[0],sum(total)))
            cursor.execute(x4)
            if sum(total)>90:
                x41=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'A1'))
                cursor.execute(x41)
            elif sum(total)>80:
                x42=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'A2'))
                cursor.execute(x42)
            elif sum(total)>70:
                x43=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'B1'))
                cursor.execute(x43)
            elif sum(total)>70:
                x44=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'B2'))
                cursor.execute(x44)
            elif sum(total)>60:
                x45=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'C1'))
                cursor.execute(x45)
            elif sum(total)>50:
                x46=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'C2'))
                cursor.execute(x46)
            elif sum(total)>33:
                x47=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'D'))
                cursor.execute(x47)
            else:
                x48=("update grade_{} set marks='{}' where subject='ENGLISH'".format(listb[0],'E'))
                cursor.execute(x48)
            
        #print(total)
        total.clear()

        for co in m1[4]:
            if co!=' ':
                total.append(float(co))
        if sum(total)!=0:
            x5=("update total_{} set marks={} where subject='HINDI'".format(listb[0],sum(total)))
            cursor.execute(x5)
            if sum(total)>90:
                x51=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'A1'))
                cursor.execute(x51)
            elif sum(total)>80:
                x52=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'A2'))
                cursor.execute(x52)
            elif sum(total)>70:
                x53=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'B1'))
                cursor.execute(x53)
            elif sum(total)>70:
                x54=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'B2'))
                cursor.execute(x54)
            elif sum(total)>60:
                x55=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'C1'))
                cursor.execute(x55)
            elif sum(total)>50:
                x56=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'C2'))
                cursor.execute(x56)
            elif sum(total)>33:
                x57=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'D'))
                cursor.execute(x57)
            else:
                x58=("update grade_{} set marks='{}' where subject='HINDI'".format(listb[0],'E'))
                cursor.execute(x58)
            
            
        #print(total)

        total.clear()
        for fe in m1[5]:
            if fe!=' ':
                total.append(float(fe))
        if sum(total)!=0:
            x6=("update total_{} set marks={} where subject='MATHS'".format(listb[0],sum(total)))
            cursor.execute(x6)
            if sum(total)>90:
                x61=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'A1'))
                cursor.execute(x61)
            elif sum(total)>80:
                x62=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'A2'))
                cursor.execute(x62)
            elif sum(total)>70:
                x63=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'B1'))
                cursor.execute(x63)
            elif sum(total)>70:
                x64=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'B2'))
                cursor.execute(x64)
            elif sum(total)>60:
                x65=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'C1'))
                cursor.execute(x65)
            elif sum(total)>50:
                x66=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'C2'))
                cursor.execute(x66)
            elif sum(total)>33:
                x67=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'D'))
                cursor.execute(x67)
            else:
                x68=("update grade_{} set marks='{}' where subject='MATHS'".format(listb[0],'E'))
                cursor.execute(x68)
        #print(total)
        total.clear()

        for ca in m1[6]:
            if ca!=' ':
                total.append(float(ca))
        if sum(total)!=0:
               x7=("update total_{} set marks={} where subject='PHYSICS'".format(listb[0],sum(total)))
               cursor.execute(x7)
               if sum(total)>90:
                x61=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'A1'))
                cursor.execute(x61)
               elif sum(total)>80:
                    x62=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'A2'))
                    cursor.execute(x62)
               elif sum(total)>70:
                    x63=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'B1'))
                    cursor.execute(x63)
               elif sum(total)>70:
                    x64=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'B2'))
                    cursor.execute(x64)
               elif sum(total)>60:
                    x65=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'C1'))
                    cursor.execute(x65)
               elif sum(total)>50:
                    x66=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'C2'))
                    cursor.execute(x66)
               elif sum(total)>33:
                    x67=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'D'))
                    cursor.execute(x67)
               else:
                    x68=("update grade_{} set marks='{}' where subject='PHYSICS'".format(listb[0],'E'))
                    cursor.execute(x68)
        percent=total
        total.clear()                             
                                                               
       # print(total)
        con.commit()
                
                                
        if Break==True:
            finalresult()
    except:
        messagebox.showwarning('Warning','NO Result Found')
        
        
def studentresult():
    global listb
    def warn6():
        
        if len(listb[0])==0:
            #print(listb)
            messagebox.showwarning('Warning','Enter Rollno')
        else:
            try:
                vari=int(listb[0])
                studentresultview()
                
                
            except:
                messagebox.showwarning('Warning','Rollno Should be Integer')
    def insider5():
        listb.clear()
        listb.append(e1.get())
        warn6()
    r=tk.Tk()
    r.title('STUDENT RESULT')
    r.geometry('300x200')
    tk.Label(r,text='STUDENT ROLLNO',bg='yellow').place(x=20,y=50)
    e1=tk.Entry(r)
    e1.place(x=140,y=50)
    tk.Button(r,text='Check',bg='lightblue',command=insider5).place(x=100,y=90)    

def interface5():
    win5=tk.Tk()
    tk.Label(win5,text='CLASS XI').pack()
    win5.title('RESULT')
    win5.geometry('400x300')
    tk.Button(win5,text='View Student Result',bg='pink',command=studentresult)\
                             .place(x=120,y=60)
    tk.Button(win5,text='View class Result',bg='pink')\
                             .place(x=127,y=100)
    tk.Button(win5,text='View Promoted List',bg='lightpink')\
                              .place(x=120,y=140)
    tk.Button(win5,text='View Supplimentry List',bg='lightpink')\
                              .place(x=117,y=180)

def warn5():
    for i in range(5):
        if len(entries_u2[i])==0 or len(entries_p2[i])==0:
            messagebox.showwarning('warning','Fill Required Detail')
            break
    else:
        messagebox.showinfo('SUCCESSFULL','ENTRY UPDATED SUCCESSFULL')
entries_u2=[]

    
    
def interface3():
   
    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
    cursor=con.cursor()
    cursor.execute('select * from studentdetail')
    r=tk.Tk()
    r.title('STUDENT DETAIL')
    r.geometry('1000x1000')
    tree=ttk.Treeview(r)
    tree['show']='headings'

    tree['column']\
    =('rollno','studentname','fathername','mothername','dob','subject')

    tree.column('rollno',minwidth=50,width=100,anchor=tk.CENTER)
    tree.column('studentname',minwidth=50,width=120,anchor=tk.CENTER)
    tree.column('fathername',minwidth=50,width=200,anchor=tk.CENTER)
    tree.column('mothername',minwidth=50
                ,anchor=tk.CENTER)
    tree.column('dob',minwidth=100,width=150,anchor=tk.CENTER)
    tree.column('subject',minwidth=100,width=150,anchor=tk.CENTER)
    #tree.column('studentname',width=200,anchor=tk.CENTER)

    tree.heading('rollno',text='Rollno',anchor=tk.CENTER)
    tree.heading('studentname',text='Student name',anchor=tk.CENTER)
    tree.heading('fathername',text='Father name',anchor=tk.CENTER)
    tree.heading('mothername',text='Mother name',anchor=tk.CENTER)
    tree.heading('dob',text='Date of Birth',anchor=tk.CENTER)
    tree.heading('subject',text='Subject',anchor=tk.CENTER)
    #tree.heading('studentname',text='SCHOOL-ADDRESS',anchor=tk.CENTER)

    #tree.pack()
    rollno=tk.StringVar()
    stname=tk.StringVar()
    faname=tk.StringVar()
    moname=tk.StringVar()
    dob=tk.StringVar()
    subject=tk.StringVar()
    lista=[]
    s=ttk.Style(r)
    s.theme_use('clam')

    def add_data():
        
        f=tk.Frame(r,width=400,height=320,background='grey')
        f.place(x=100,y=250)
        l1=tk.Label(f,text='rollno',width=8,font=('Times',11,'bold'))
        l2=tk.Label(f,text='Student name',width=10,font=('Times',11,'bold'))
        l3=tk.Label(f,text='Father name',width=10,font=('Times',11,'bold'))
        l4=tk.Label(f,text='Mother name',width=10,font=('Times',11,'bold'))
        l5=tk.Label(f,text='date of birth',width=10,font=('Times',11,'bold'))
        l6=tk.Label(f,text='Subject Select',width=10,font=('Times',11,'bold'))
        tk.Label(f,text='DD\MM\YY').place(x=330,y=190)
        
        
        a1=tk.Entry(f,textvariable=rollno,width=25)
        a2=tk.Entry(f,textvariable=stname,width=25)
        a3=tk.Entry(f,textvariable=faname,width=25)
        a4=tk.Entry(f,textvariable=moname,width=25)
        a5=tk.Entry(f,textvariable=dob,width=25)
        #a6=tk.Entry(f,textvariable=subject,width=25)
        a6=ttk.Combobox(f,textvariable=subject,width=27,)
        a6['state']='readonly'
        a6['values']=('PCM+CS','PCB+CS','PCB+Hindi','PCM+Hindi')
        a6.current(0)

        l1.place(x=50,y=30)
        l2.place(x=50,y=70)
        l3.place(x=50,y=110)
        l4.place(x=50,y=150)
        l5.place(x=50,y=190)
        l6.place(x=50,y=230)

        a1.place(x=170,y=30)
        a2.place(x=170,y=70)
        a3.place(x=170,y=110)
        a4.place(x=170,y=150)
        a5.place(x=170,y=190)
        a6.place(x=170,y=230)
        def cancel():
            f.destroy()
        
        b1=tk.Button(f,text='cancel',command=cancel)
        b1.configure(font=('Times',11,'bold'),bg='green',fg='white')
        b1.place(x=180,y=280)

        

        def insert_data():
            global lista
            
            nonlocal a1,a2,a3,a4,a5,a6
            rollno=a1.get()
            sname=a2.get()
            fname=a3.get()
            mname=a4.get()
            dob=a5.get()
            subject=a6.get()
            lista.clear()
            lista=[rollno,sname,fname,mname,dob,subject]
            for i in lista:
                if len(i)==0:
                    messagebox.showwarning('Warning','fill required Detail')
                    break
                try:
                    variable=int(lista[0])
                except:
                    messagebox.showwarning('Warning',"invalid Entry")
                    break
                
            else:
                
                con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
        
                cursor=con.cursor()
                query="insert into studentdetail values('{}','{}','{}','{}','{}','{}')"\
                   .format(rollno,sname,fname,mname,dob,subject)
                query1="insert into pt1(rollno,studentname) values('{}','{}')".format(rollno,sname)
                query2="insert into pt2(rollno,studentname) values('{}','{}')".format(rollno,sname)
                query3="insert into halfyearly(rollno,studentname) values('{}','{}')".format(rollno,sname)
                query4="insert into annualexam(rollno,studentname) values('{}','{}')".format(rollno,sname)
                query5="insert into practical(rollno,studentname) values('{}','{}')".format(rollno,sname)
                t1="create table pt1_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t2="create table pt2_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t3="create table hy_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t4="create table ae_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t5="create table pe_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t6="create table total_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t7="create table grade_{}(subject varchar(30) primary key,marks varchar(10) default ' ')".format(rollno)
                t11="insert into pt1_{}(subject) values('ENGLISH')".format(rollno)
                t12="insert into pt1_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t13="insert into pt1_{}(subject) values('PHYSICS')".format(rollno)
                t14="insert into pt1_{}(subject) values('BIOLOGY')".format(rollno)
                t15="insert into pt1_{}(subject) values('HINDI')".format(rollno)
                t16="insert into pt1_{}(subject) values('CHEMISTRY')".format(rollno)
                t17="insert into pt1_{}(subject) values('MATHS')".format(rollno)
                t21="insert into pt2_{}(subject) values('ENGLISH')".format(rollno)
                t22="insert into pt2_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t23="insert into pt2_{}(subject) values('PHYSICS')".format(rollno)
                t24="insert into pt2_{}(subject) values('BIOLOGY')".format(rollno)
                t25="insert into pt2_{}(subject) values('HINDI')".format(rollno)
                t26="insert into pt2_{}(subject) values('CHEMISTRY')".format(rollno)
                t27="insert into pt2_{}(subject) values('MATHS')".format(rollno)
                t31="insert into hy_{}(subject) values('ENGLISH')".format(rollno)
                t32="insert into hy_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t33="insert into hy_{}(subject) values('PHYSICS')".format(rollno)
                t34="insert into hy_{}(subject) values('BIOLOGY')".format(rollno)
                t35="insert into hy_{}(subject) values('HINDI')".format(rollno)
                t36="insert into hy_{}(subject) values('CHEMISTRY')".format(rollno)
                t37="insert into hy_{}(subject) values('MATHS')".format(rollno)
                t41="insert into ae_{}(subject) values('ENGLISH')".format(rollno)
                t42="insert into ae_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t43="insert into ae_{}(subject) values('PHYSICS')".format(rollno)
                t44="insert into ae_{}(subject) values('BIOLOGY')".format(rollno)
                t45="insert into ae_{}(subject) values('HINDI')".format(rollno)
                t46="insert into ae_{}(subject) values('CHEMISTRY')".format(rollno)
                t47="insert into ae_{}(subject) values('MATHS')".format(rollno)
                t51="insert into pe_{}(subject) values('ENGLISH')".format(rollno)
                t52="insert into pe_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t53="insert into pe_{}(subject) values('PHYSICS')".format(rollno)
                t54="insert into pe_{}(subject) values('BIOLOGY')".format(rollno)
                t55="insert into pe_{}(subject) values('HINDI')".format(rollno)
                t56="insert into pe_{}(subject) values('CHEMISTRY')".format(rollno)
                t57="insert into pe_{}(subject) values('MATHS')".format(rollno)
                t61="insert into total_{}(subject) values('ENGLISH')".format(rollno)
                t62="insert into total_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t63="insert into total_{}(subject) values('PHYSICS')".format(rollno)
                t64="insert into total_{}(subject) values('BIOLOGY')".format(rollno)
                t65="insert into total_{}(subject) values('HINDI')".format(rollno)
                t66="insert into total_{}(subject) values('CHEMISTRY')".format(rollno)
                t67="insert into total_{}(subject) values('MATHS')".format(rollno)

                t71="insert into grade_{}(subject) values('ENGLISH')".format(rollno)
                t72="insert into grade_{}(subject) values('COMPUTER SCIENCE')".format(rollno)
                t73="insert into grade_{}(subject) values('PHYSICS')".format(rollno)
                t74="insert into grade_{}(subject) values('BIOLOGY')".format(rollno)
                t75="insert into grade_{}(subject) values('HINDI')".format(rollno)
                t76="insert into grade_{}(subject) values('CHEMISTRY')".format(rollno)
                t77="insert into grade_{}(subject) values('MATHS')".format(rollno)                

                try:
                    cursor.execute(query)
                    cursor.execute(query1)
                    cursor.execute(query2)
                    cursor.execute(query3)
                    cursor.execute(query4)
                    cursor.execute(query5)
                    cursor.execute(t1)
                    cursor.execute(t2)
                    cursor.execute(t3)
                    cursor.execute(t4)
                    cursor.execute(t5)
                    cursor.execute(t11)
                    cursor.execute(t12)
                    cursor.execute(t13)
                    cursor.execute(t14)
                    cursor.execute(t15)
                    cursor.execute(t16)
                    cursor.execute(t17)
                    cursor.execute(t21)
                    cursor.execute(t22)
                    cursor.execute(t23)
                    cursor.execute(t24)
                    cursor.execute(t25)
                    cursor.execute(t26)
                    cursor.execute(t27)
                    cursor.execute(t31)
                    cursor.execute(t32)
                    cursor.execute(t33)
                    cursor.execute(t34)
                    cursor.execute(t35)
                    cursor.execute(t36)
                    cursor.execute(t37)
                    cursor.execute(t41)
                    cursor.execute(t42)
                    cursor.execute(t43)
                    cursor.execute(t44)
                    cursor.execute(t45)
                    cursor.execute(t46)
                    cursor.execute(t47)
                    cursor.execute(t51)
                    cursor.execute(t52)
                    cursor.execute(t53)
                    cursor.execute(t54)
                    cursor.execute(t55)
                    cursor.execute(t56)
                    cursor.execute(t57)
                    cursor.execute(t6)
                    cursor.execute(t7)
                    cursor.execute(t61)
                    cursor.execute(t62)
                    cursor.execute(t63)
                    cursor.execute(t64)
                    cursor.execute(t65)
                    cursor.execute(t66)
                    cursor.execute(t67)

                    cursor.execute(t71)
                    cursor.execute(t72)
                    cursor.execute(t73)
                    cursor.execute(t74)
                    cursor.execute(t75)
                    cursor.execute(t76)
                    cursor.execute(t77)
                    print('hello')
                    con.commit()
                    tree.insert('','end',text='',values=(rollno,sname,fname,mname,dob,subject))
            
                
                except:
                    messagebox.showwarning('Warning','ROLLNO {} ALREADY EXISTS'\
                                       .format(rollno))
                con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                cursor=con.cursor()
                if subject=='PCB+CS':
                    q1='update pt1 set maths="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q1)
                    q11='update pt2 set maths="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q11)
                    q21='update halfyearly set maths="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q21)
                    q31='update annualexam set maths="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q31)
                elif subject=='PCB+Hindi':
                    q2='update pt1 set maths="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q2)
                    q12='update pt2 set maths="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q12)
                    q22='update halfyearly set maths="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q22)
                    q32='update annualexam set maths="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q32)
                    q42='update practical set cs="{}" where rollno="{}"'.format('---',rollno)
                    cursor.execute(q42)
                elif subject=='PCM+CS':
                    q3='update pt1 set biology="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q3)
                    q13='update pt2 set biology="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q13)
                    q23='update halfyearly set biology="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q23)
                    q33='update annualexam set biology="{}",hindi="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q33)
                    q43='update practical set biology="{}" where rollno="{}"'.format('---',rollno)
                    cursor.execute(q43)
                elif subject=='PCM+Hindi':
                    q4='update pt1 set biology="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q4)
                    q14='update pt2 set biology="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q14)
                    q24='update halfyearly set biology="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q24)
                    q34='update annualexam set biology="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q34)
                    q44='update practical set biology="{}",cs="{}" where rollno="{}"'.format('---','---',rollno)
                    cursor.execute(q44)
                con.commit()               
                    
                a1.delete(0,tk.END)
                a2.delete(0,tk.END)
                a3.delete(0,tk.END)
                a4.delete(0,tk.END)
                a5.delete(0,tk.END)
                a6.delete(0,tk.END)
                f.destroy()
            
           
        submitbutton=tk.Button(f,text='Submit',command=insert_data)
        submitbutton.configure(font=('Times',11,'bold'),bg='green',fg='white')
        submitbutton.place(x=100,y=280)
            
            
        
    def delete_data():
        try:
            selected_item=tree.selection()[0]
        #print(tree.item(selected_item)['values'])
            uid=tree.item(selected_item)['values'][0]
            sel_data=(uid,)
            tree.delete(selected_item)
            con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
            cursor=con.cursor()
            query='delete from studentdetail where rollno="{}"'.format(uid)
            query1="delete from pt1 where rollno='{}'".format(uid)
            query2="delete from pt2 where rollno='{}'".format(uid)
            query3="delete from halfyearly where rollno='{}'".format(uid)
            query4="delete from annualexam where rollno='{}'".format(uid)
            query5="delete from practical where rollno='{}'".format(uid)
            query11="update  pt1_{} set marks=' ' where subject='ENGLISH'".format(uid)
            query12="update  pt1_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(uid)
            query13="update  pt1_{} set marks=' ' where subject='HINDI'".format(uid)
            query14="update  pt1_{} set marks=' ' where subject='BIOLOGY'".format(uid)
            query15="update  pt1_{} set marks=' ' where subject='MATHS'".format(uid)
            query16="update  pt1_{} set marks=' ' where subject='PHYSICS'".format(uid)
            query17="update  pt1_{} set marks=' ' where subject='CHEMISTRY'".format(uid)
            query21="update  pt2_{} set marks=' ' where subject='ENGLISH'".format(uid)
            query22="update  pt2_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(uid)
            query23="update  pt2_{} set marks=' ' where subject='HINDI'".format(uid)
            query24="update  pt2_{} set marks=' ' where subject='BIOLOGY'".format(uid)
            query25="update  pt2_{} set marks=' ' where subject='MATHS'".format(uid)
            query26="update  pt2_{} set marks=' ' where subject='PHYSICS'".format(uid)
            query27="update  pt2_{} set marks=' ' where subject='CHEMISTRY'".format(uid)
            query31="update  hy_{} set marks=' ' where subject='ENGLISH'".format(uid)
            query32="update  hy_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(uid)
            query33="update  hy_{} set marks=' ' where subject='HINDI'".format(uid)
            query34="update  hy_{} set marks=' ' where subject='BIOLOGY'".format(uid)
            query35="update  hy_{} set marks=' ' where subject='MATHS'".format(uid)
            query36="update  hy_{} set marks=' ' where subject='PHYSICS'".format(uid)
            query37="update  hy_{} set marks=' ' where subject='CHEMISTRY'".format(uid)
            query41="update  ae_{} set marks=' ' where subject='ENGLISH'".format(uid)
            query42="update  ae_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(uid)
            query43="update  ae_{} set marks=' ' where subject='HINDI'".format(uid)
            query44="update  ae_{} set marks=' ' where subject='BIOLOGY'".format(uid)
            query45="update  ae_{} set marks=' ' where subject='MATHS'".format(uid)
            query46="update  ae_{} set marks=' ' where subject='PHYSICS'".format(uid)
            query47="update  ae_{} set marks=' ' where subject='CHEMISTRY'".format(uid)
            query51="update  pe_{} set marks=' ' where subject='ENGLISH'".format(uid)
            query52="update  pe_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(uid)
            query53="update  pe_{} set marks=' ' where subject='HINDI'".format(uid)
            query54="update  pe_{} set marks=' ' where subject='BIOLOGY'".format(uid)
            query55="update  pe_{} set marks=' ' where subject='MATHS'".format(uid)
            query56="update  pe_{} set marks=' ' where subject='PHYSICS'".format(uid)
            query57="update  pe_{} set marks=' ' where subject='CHEMISTRY'".format(uid)


            
        except:
            pass
        try:
            cursor.execute(query)
            cursor.execute(query1)
            cursor.execute(query2)
            cursor.execute(query3)
            cursor.execute(query4)
            cursor.execute(query5)
            cursor.execute(query11)
            cursor.execute(query12)
            cursor.execute(query13)
            cursor.execute(query14)
            cursor.execute(query15)
            cursor.execute(query16)
            cursor.execute(query17)
            cursor.execute(query21)
            cursor.execute(query22)
            cursor.execute(query23)
            cursor.execute(query24)
            cursor.execute(query25)
            cursor.execute(query26)
            cursor.execute(query27)
            cursor.execute(query31)
            cursor.execute(query32)
            cursor.execute(query33)
            cursor.execute(query34)
            cursor.execute(query35)
            cursor.execute(query36)
            cursor.execute(query37)
            cursor.execute(query41)
            cursor.execute(query42)
            cursor.execute(query43)
            cursor.execute(query44)
            cursor.execute(query45)
            cursor.execute(query46)
            cursor.execute(query47)
            cursor.execute(query51)
            cursor.execute(query52)
            cursor.execute(query53)
            cursor.execute(query54)
            cursor.execute(query55)
            cursor.execute(query56)
            cursor.execute(query57)
            con.commit()
            messagebox.showinfo('Successfull','Data deleted Successfully')
        except:
            messagebox.showwarning('warning','Select Data For Delete')


    def select_data():
        curitem=tree.focus()
        values=tree.item(curitem,'values')
        if len(values)==0:
            messagebox.showwarning('Warning','Please select the data')
        else:

            f=tk.Frame(r,width=400,height=320,background='grey')
            f.place(x=100,y=250)
            #l1=tk.Label(f,text='rollno',width=8,font=('Times',11,'bold'))
            l2=tk.Label(f,text='Student name',width=10,font=('Times',11,'bold'))
            l3=tk.Label(f,text='Father name',width=10,font=('Times',11,'bold'))
            l4=tk.Label(f,text='Mother name',width=10,font=('Times',11,'bold'))
            l5=tk.Label(f,text='date of birth',width=10,font=('Times',11,'bold'))
            l6=tk.Label(f,text='Subject Select',width=10,font=('Times',11,'bold'))
            
            
            #a11=tk.Entry(f,textvariable=rollno,width=25)
            a12=tk.Entry(f,textvariable=stname,width=25)
            a13=tk.Entry(f,textvariable=faname,width=25)
            a14=tk.Entry(f,textvariable=moname,width=25)
            a15=tk.Entry(f,textvariable=dob,width=25)
            tk.Label(f,text='DD\MM\YY').place(x=330,y=190)
            #a6=tk.Entry(f,textvariable=subject,width=25)
            a16=ttk.Combobox(f,textvariable=subject,width=27,)
            a16['state']='readonly'
            a16['values']=('PCM+CS','PCB+CS','PCM+Hindi','PCB+Hindi')
            a16.current(0)
            #l1.place(x=50,y=30)
            l2.place(x=50,y=70)
            l3.place(x=50,y=110)
            l4.place(x=50,y=150)
            l5.place(x=50,y=190)
            l6.place(x=50,y=230)

            #a11.place(x=170,y=30)
            a12.place(x=170,y=70)
            a13.place(x=170,y=110)
            a14.place(x=170,y=150)
            a15.place(x=170,y=190)
            a16.place(x=170,y=230)

            #a11.insert(0,values[0])
            a12.insert(0,values[1])
            a13.insert(0,values[2])
            a14.insert(0,values[3])
            a15.insert(0,values[4])
            a16.insert(0,values[5])          
            def update_data():
                nonlocal a12,a13,a14,a15,a16,curitem,values
                #rollno=a11.get()
                sname=a12.get()
                fname=a13.get()
                mname=a14.get()
                dob=a15.get()
                subject=a16.get()
                lista.clear()
                lista.extend([sname,fname,mname,dob,subject])
                for p in lista:
                    if len(p)==0:
                        messagebox.showwarning('Warning','Fill required detail')
                        break
                    
                else:                    
                        
                    tree.item(curitem,values=(values[0],sname,fname,mname,dob,subject))
                    con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
                    cursor=con.cursor()
                    query="update studentdetail set studentname='{}',fathername='{}'\
                    ,mothername='{}',dob='{}',subject='{}' where rollno='{}'".format(sname,fname,mname,dob,subject,values[0])
                    cursor.execute(query)
                    if subject=='PCM+CS':
                        q1="update pt1 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---','---',' ',' ',values[0])
                        cursor.execute(q1)
                        q11="update pt2 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---','---',' ',' ',values[0])
                        cursor.execute(q11)
                        q21="update halfyearly set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---','---',' ',' ',values[0])
                        cursor.execute(q21)
                        q31="update annualexam set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---','---',' ',' ',values[0])
                        cursor.execute(q31)
                        q41="update practical set biology='{}',cs='{}'\
                            where rollno='{}'".format('---',' ',values[0])
                        cursor.execute(q41)
                        query13="update  pt1_{} set marks=' ' where subject='HINDI'".format(values[0])
                        query14="update  pt1_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query13)
                        cursor.execute(query14)
                        query23="update  pt2_{} set marks=' ' where subject='HINDI'".format(values[0])
                        query24="update  pt2_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query23)
                        cursor.execute(query24)
                        query33="update  hy_{} set marks=' ' where subject='HINDI'".format(values[0])
                        query34="update  hy_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query33)
                        cursor.execute(query34)
                        query43="update  ae_{} set marks=' ' where subject='HINDI'".format(values[0])
                        query44="update  ae_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query43)
                        cursor.execute(query44)
                        
                        query54="update  pe_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        
                        cursor.execute(query54)
                        a12.delete(0,tk.END)
                        a13.delete(0,tk.END)
                        a14.delete(0,tk.END)
                        a15.delete(0,tk.END)
                        a16.delete(0,tk.END)
                        f.destroy()                    
                        
                    elif subject=='PCM+Hindi':
                        q2="update pt1 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---',' ',' ','---',values[0])
                        cursor.execute(q2)
                        q12="update pt2 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---',' ',' ','---',values[0])
                        cursor.execute(q12)
                        q22="update halfyearly set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---',' ',' ','---',values[0])
                        cursor.execute(q22)
                        q32="update annualexam set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format('---',' ',' ','---',values[0])
                        q42="update practical set biology='{}',cs='{}'\
                            where rollno='{}'".format('---','---',values[0])
                        cursor.execute(q42)
                    
                        query62="update  pt1_{} set marks=' ' where subject='COMPUTER SCIENCE'".format((values[0]))
                        query63="update  pt1_{} set marks=' ' where subject='BIOLOGY'".format((values[0]))
                        cursor.execute(query62)
                        cursor.execute(query63)
                        query72="update  pt2_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        query73="update  pt2_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query72)
                        cursor.execute(query73)
                        query82="update  hy_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        query83="update  hy_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query82)
                        cursor.execute(query83)
                        query92="update  ae_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        query93="update  ae_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query92)
                        cursor.execute(query93)
                        query102="update  pe_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        query103="update  pe_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        cursor.execute(query102)
                        cursor.execute(query103)
                        a12.delete(0,tk.END)
                        a13.delete(0,tk.END)
                        a14.delete(0,tk.END)
                        a15.delete(0,tk.END)
                        a16.delete(0,tk.END)
                        f.destroy()
                                                                                                
                    elif subject=='PCB+CS':
                        q3="update pt1 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ','---','---',' ',values[0])
                        cursor.execute(q3)
                        q13="update pt2 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ','---','---',' ',values[0])
                        cursor.execute(q13)
                        q23="update halfyearly set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ','---','---',' ',values[0])
                        cursor.execute(q23)
                        q33="update annualexam set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ','---','---',' ',values[0])
                        cursor.execute(q33)
                        q43="update practical set biology='{}',cs='{}'\
                            where rollno='{}'".format(' ',' ',values[0])
                        cursor.execute(q43)
                        query112="update  pt1_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query113="update  pt1_{} set marks=' ' where subject='HINDI'".format(values[0])
                        cursor.execute(query112)
                        cursor.execute(query113)
                        query122="update  pt2_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query123="update  pt2_{} set marks=' ' where subject='HINDI'".format(values[0])
                        cursor.execute(query122)
                        cursor.execute(query123)
                        query132="update  hy_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query133="update  hy_{} set marks=' ' where subject='HINDI'".format(values[0])
                        cursor.execute(query132)
                        cursor.execute(query133)
                        query142="update  ae_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query143="update  ae_{} set marks=' ' where subject='HINDI'".format(values[0])
                        cursor.execute(query142)
                        cursor.execute(query143)
                        query152="update  pe_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                        query153="update  pe_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query152)
                        cursor.execute(query153)
                        a12.delete(0,tk.END)
                        a13.delete(0,tk.END)
                        a14.delete(0,tk.END)
                        a15.delete(0,tk.END)
                        a16.delete(0,tk.END)
                        f.destroy()
                                                                                                                                                            
                    elif subject=='PCB+Hindi':
                        q4="update pt1 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ',' ','---','---',values[0])
                        cursor.execute(q4)
                        q14="update pt2 set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ',' ','---','---',values[0])
                        cursor.execute(q14)
                        q24="update halfyearly set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ',' ','---','---',values[0])
                        cursor.execute(q24)
                        q34="update annualexam set biology='{}',hindi='{}',maths='{}',cs='{}'\
                            where rollno='{}'".format(' ',' ','---','---',values[0])
                        cursor.execute(q34)
                        q44="update practical set cs='{}',biology='{}'\
                            where rollno='{}'".format('---',' ',values[0])
                        cursor.execute(q44)
                        query162="update  pt1_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query163="update  pt1_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query162)
                        cursor.execute(query163)
                        query172="update  pt2_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query173="update  pt2_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query172)
                        cursor.execute(query173)
                        query182="update  hy_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query183="update  hy_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query182)
                        cursor.execute(query183)
                        query192="update  ae_{} set marks=' ' where subject='MATHS'".format(values[0])
                        query193="update  ae_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query192)
                        cursor.execute(query193)
                        query203="update  pe_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                        cursor.execute(query203)
                        a12.delete(0,tk.END)
                        a13.delete(0,tk.END)
                        a14.delete(0,tk.END)
                        a15.delete(0,tk.END)
                        a16.delete(0,tk.END)
                        f.destroy() 

                    upd1="update grade_{} set marks=' ' where subject='ENGLISH'".format(values[0])
                    upd2="update grade_{} set marks=' ' where subject='HINDI'".format(values[0])
                    upd3="update grade_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                    upd4="update grade_{} set marks=' ' where subject='PHYSICS'".format(values[0])
                    upd5="update grade_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                    upd6="update grade_{} set marks=' ' where subject='CHEMISTRY'".format(values[0])
                    upd7="update grade_{} set marks=' ' where subject='MATHS'".format(values[0])
                    upd8="update total_{} set marks=' ' where subject='ENGLISH'".format(values[0])
                    upd9="update total_{} set marks=' ' where subject='HINDI'".format(values[0])
                    upd10="update total_{} set marks=' ' where subject='COMPUTER SCIENCE'".format(values[0])
                    upd11="update total_{} set marks=' ' where subject='PHYSICS'".format(values[0])
                    upd12="update total_{} set marks=' ' where subject='BIOLOGY'".format(values[0])
                    upd13="update total_{} set marks=' ' where subject='CHEMISTRY'".format(values[0])
                    upd14="update total_{} set marks=' ' where subject='MATHS'".format(values[0])
                    cursor.execute(upd1)
                    cursor.execute(upd2)
                    cursor.execute(upd3)
                    cursor.execute(upd4)
                    cursor.execute(upd5)
                    cursor.execute(upd6)
                    cursor.execute(upd7)
                    cursor.execute(upd8)
                    cursor.execute(upd9)
                    cursor.execute(upd10)
                    cursor.execute(upd11)
                    cursor.execute(upd12)
                    cursor.execute(upd13)
                    cursor.execute(upd14)
                    

                    
                                                                                                                      
                        
                    con.commit()
                    messagebox.showinfo('successfull','Successfull Updated')

                    #a11.delete(0,tk.END)
                        
            def cancel1():
                #a11.delete(0,tk.END)
                a12.delete(0,tk.END)
                a13.delete(0,tk.END)
                a14.delete(0,tk.END)
                a15.delete(0,tk.END)
                a16.delete(0,tk.END)
                f.destroy()
                        
            savebutton=tk.Button(f,text='Update',fg='green',command=update_data)
            savebutton.place(x=100,y=270)
            cancelbutton=tk.Button(f,text='cancel',fg='green',command=cancel1)
            cancelbutton.place(x=200,y=270)        

    insertbutton=tk.Button(r,text='Insert',command=add_data)
    insertbutton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
    insertbutton.place(x=200,y=260)

    deletebutton=tk.Button(r,text='delete',command=delete_data)
    deletebutton.configure(font=('calibri',14,'bold'),bg='red',fg='white')
    deletebutton.place(x=300,y=260)

    updatebutton=tk.Button(r,text='Update',command=select_data)
    updatebutton.configure(font=('calibri',14,'bold'),bg='blue',fg='white')
    updatebutton.place(x=400,y=260)

    i=0
    for ro in cursor:
        tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i+=1
    #tree.pack()

    #scroll=ttk.Scrollbar(r)
    #croll.pack(side=tk.RIGHT,fill=tk.Y)


    tree.pack()

def tatabyebye():
    con=c.connect(host='localhost',user='root',passwd=a[1])
    messagebox.showinfo('Successfull','RECORDS SUCCESSFULY DELETED')
    cursor=con.cursor()
    query='drop database result'
    try:
        cursor.execute(query)
        con.commit()
        createtable1()
        #message.showinfo('SUCCESSFULL','DATA SUCCESSFULLY DELETED')
        
    except:
        pass
            
def interface1():
    win1=tk.Tk()
    tk.Label(win1,text='CLASS XI').pack()
    win1.title('RESULT')
    win1.geometry('400x300')
    
    tk.Button(win1,text='SCHOOL DETAIL',bg='lightpink',\
              command=interface2).place(x=150,y=40)

    tk.Button(win1,text='STUDENT DETAIL',bg='lightpink',\
              command=interface3).place(x=150,y=80)
    tk.Button(win1,text='MARKS ENTRY',bg='lightpink',\
              command=interface4).place(x=155,y=120)
    tk.Button(win1,text='VIEW RESULT',bg='lightpink',\
              command=interface5).place(x=159,y=160)
    tk.Button(win1,text='DELETE FULL RECORDS',bg='lightpink',\
              command=tatabyebye).place(x=140,y=200)

def createdb():
    n=0
    
    try:
        con=c.connect(host='localhost',user='root',passwd=a[1])
        
    except:
        messagebox.showwarning('warning','Incorrect Password\n      Try Again')
    try:
        con=c.connect(host='localhost',user='root',passwd=a[1],database='result')
        messagebox.showinfo('Successfull',"Login Successfull")
        n=1
    except:
          try:
              con=c.connect(host='localhost',user='root',passwd=a[1])
              cursor=con.cursor()
              query='Create database result'
              cursor.execute(query)
              con.commit()
              messagebox.showinfo('Successfull',"Login Successfull")
              n=1
          except:
              pass
    if n==1:
        createtable1()

        interface1()          

def warn1():
    if a[0]=='':
        messagebox.showwarning('Warning','Enter User Name')
    elif (a[0]).upper()!='AMISHA':
          messagebox.showwarning('Warning','USER NOT FOUND')
        
    elif a[1]=='':
        messagebox.showwarning('Warning','Enter required Password')
    else:
        createdb()
    
def main():
    def insider1():
        global a
        a.clear()
        a.extend([e1.get(),e2.get()])
        warn1()
    

    win=tk.Tk()
    win.geometry('400x300')
    win.title('RESULT')

    tk.Label(win,text='CLASS XI').pack()
    tk.Label(win,text='User Name',fg='red',bg='pink')\
                        .place(x=100,y=60)
    tk.Label(win,text='Password',fg='red',bg='pink')\
                         .place(x=105,y=90)
    e1=tk.Entry(win,bg='yellow')
    e2=tk.Entry(win,bg='yellow')
    e1.place(x=170,y=60)
    e2.place(x=170,y=90)
    tk.Button(win,text='Login',bg='lightblue',\
              command=insider1).place(x=180,y=130)
    

a=[0]
main()







