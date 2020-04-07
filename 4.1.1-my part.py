
#Entry of Marks
from Tkinter import *
def bye():
    root.destroy()
def entry_box():
    def bye():
        root.destroy()
    root=Tk()
    Label(root,text="ENTER Marks",fg="white",bg="black").grid(row=0,column=1)
    Label(root,text="Class").grid(row=2,column=0)
    Class=Entry(root)
    Class.grid(row=2,column=1)
    Label(root,text="Section").grid(row=2,column=2)
    section=Entry(root)
    section.grid(row=2,column=3)
    Label(root,text="Subject name").grid(row=5,column=0)
    sub_name=Entry(root)
    sub_name.grid(row=5,column=1)
    Label(root,text="Exam").grid(row=5,column=2)
    exam=Entry(root)
    exam.grid(row=5,column=3)
    Label(root,text="S.no",fg="black",bg="white").grid(row=20,column=1)
    Label(root,text="Name",fg="black",bg="white").grid(row=20,column=2)
    Label(root,text="Marks",fg="black",bg="white").grid(row=20,column=3)
    save=Button(root,text="SAVE",fg="black",bg="blue").grid(row=1,column=1)
    cancel=Button(root,text="CANCEL",fg="black",bg="blue",command=bye).grid(row=1,column=3)
    for i in range(21,79):
        for j in range(1,4):
            b=Entry(root)
            b.grid(row=i, column=j)                                                                        
root= Tk()
Enter=Button(root,text="ENTER",fg="red",bg="black",command=entry_box).grid(row=10,column=1)
cancel=Button(root,text="CANCEL",fg="red",bg="black",command=bye).grid(row=10,column=2)
root.title("drop down")
var=StringVar(root)
var.set("Class")
def grab_and_assign(event):
    Class=var.get()
    label_chosen_variable=Label(root,text="Class")
    label_chosen_variable.grid(row=0,column=1)
    print Class
drop_menu=OptionMenu(root,var,"I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII",command=grab_and_assign)
drop_menu.grid(row=1,column=1)
Label_left=Label(root,text="chosen variable=")
Label_left.grid(row=2,column=1)
root.title("drop down")
var=StringVar(root)
var.set("section")
def grab_and_assign(event):
    section=var.get()
    label_chosen_variable=Label(root,text="section")
    label_chosen_variable.grid(row=0,column=3)
    print section
drop_menu=OptionMenu(root,var,"A1","A2","A3","A","B","C",command=grab_and_assign)
drop_menu.grid(row=1,column=3)
Label_left=Label(root,text="chosen variable=")
Label_left.grid(row=2,column=3)
root.title("drop down")
var=StringVar(root)
var.set("Subject")
def grab_and_assign(event):
    Subject=var.get()
    label_chosen_variable=Label(root,text="Subject")
    label_chosen_variable.grid(row=3,column=1)
    print Subject
drop_menu=OptionMenu(root,var,"MATH","PHYSICS","CHEMISTRY","BIOLOGY","COMPUTER SCIENCE","ENGLISH","SOCIAL SCIENCE","EVMS","NEPALI","HINDI","SANSKRIT","SCIENCE",command=grab_and_assign)
drop_menu.grid(row=4,column=1)
Label_left=Label(root,text="chosen variable=")
Label_left.grid(row=5,column=1)
root.title("drop down")
var=StringVar(root)
var.set("Exam")
def grab_and_assign(event):
    Exam=var.get()
    label_chosen_variable=Label(root,text="Exam")
    label_chosen_variable.grid(row=6,column=1)
    print Exam
drop_menu=OptionMenu(root,var,"FA1","FA2","FA3","SA1","SA2",command=grab_and_assign)
drop_menu.grid(row=7,column=1)
Label_left=Label(root,text="chosen variable=")
Label_left.grid(row=8,column=1)
root.mainloop()
mainloop()
                                                                            
    
   
