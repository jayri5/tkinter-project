#View subject mark
from Tkinter import *
def bye():
    root.destroy()
def get_det():
    root=Tk()
    fa1=Button(root,text="FA 1",fg="white",bg="black",command=get_list).grid(row=0)
    fa2=Button(root,text="FA 2",fg="white",bg="black",command=get_list).grid(row=0,column=1)
    fa3=Button(root,text="FA 3",fg="white",bg="black",command=get_list).grid(row=0,column=2)
    fa4=Button(root,text="FA 4",fg="white",bg="black",command=get_list).grid(row=0,column=3)
    sa1=Button(root,text="SA 1",fg="white",bg="black",command=get_list).grid(row=0,column=4)
    sa2=Button(root,text="SA 2",fg="white",bg="black",command=get_list).grid(row=0,column=5)


def get_list():    
    Label(root,text="S.No.",fg="black",bg="white").grid(row=9,column=1)
    Label(root,text="Name",fg="black",bg="white").grid(row=9,column=3)
    Label(root,text="Marks",fg="black",bg="white").grid(row=9,column=5)


    for i in range(10,55):
        for j in range(1,6,2):
            b=Entry(root)
            b.grid(row=i,column=j)
            
root= Tk()
root.title("drop down")
var=StringVar(root)
var.set("Class")
label_chosen_variable=Label(root,text="Class")
label_chosen_variable.grid(row=0,column=1)

drop_menu=OptionMenu(root,var,"I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII",)
drop_menu.grid(row=1,column=1)

root.title("drop down")
var=StringVar(root)
var.set("section")

label_chosen_variable=Label(root,text="section")
label_chosen_variable.grid(row=0,column=3)

drop_menu=OptionMenu(root,var,"A1","A2","A3","A","B","C")
drop_menu.grid(row=1,column=3)

root.title("drop down")
var=StringVar(root)
var.set("Subject")

label_chosen_variable=Label(root,text="Subject")
label_chosen_variable.grid(row=3,column=1)

drop_menu=OptionMenu(root,var,"MATH","PHYSICS","CHEMISTRY","BIOLOGY","COMPUTER SCIENCE","ENGLISH","SOCIAL SCIENCE","EVMS","NEPALI","HINDI","SANSKRIT","SCIENCE")
drop_menu.grid(row=4,column=1)


root.title("drop down")
var=StringVar(root)
var.set("Exam")

label_chosen_variable=Label(root,text="Exam")
label_chosen_variable.grid(row=6,column=1)
    
drop_menu=OptionMenu(root,var,"FA1","FA2","FA3","SA1","SA2")
drop_menu.grid(row=7,column=1)

getdetails=Button(root,text="GET DETAILS",fg="black",bg="white",command=get_det).grid(row=10,column=1)
cancel=Button(root,text="CANCEL",fg="black",bg="white",command=bye).grid(row=10,column=2)
root.mainloop()
mainloop()
                                                                            
    
   

