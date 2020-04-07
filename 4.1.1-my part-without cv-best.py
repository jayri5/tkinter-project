
#Entry of Marks
from Tkinter import *
def bye():
    root.destroy()
def entry_box():
    
    
    
    def bye():
        root.destroy()
    
    Label(root,text="S.no",fg="black",bg="white").grid(row=24,column=1)
    Label(root,text="Name",fg="black",bg="white").grid(row=24,column=2)
    Label(root,text="Marks",fg="black",bg="white").grid(row=24,column=3)
    for i in range(25,79):
        for j in range(1,4):
            b=Entry(root)
            b.grid(row=i, column=j)
    save=Button(root,text="SAVE",fg="black",bg="blue").grid(row=20,column=1)
    cancel=Button(root,text="CANCEL",fg="black",bg="blue",command=bye).grid(row=20,column=3)        
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

Enter=Button(root,text="ENTER",fg="red",bg="black",command=entry_box).grid(row=10,column=1)
cancel=Button(root,text="CANCEL",fg="red",bg="black",command=bye).grid(row=10,column=2)
root.mainloop()
mainloop()
                                                                            
    
   
