#Remove teacher

from Tkinter import *
root= Tk()
def bye():
    root.destroy()

def entry_box():
   
    root=Tk()
    
    Label(root,text="My Subject").grid(row=0,column=0)
    Label(root,text="My Class").grid(row=0,column=4)
    Label(root,text="Teacher Name").grid(row=0,column=8)
    profile=Button(root,text="Profile",fg="white",bg="black").grid(row=2,column=8)
    logout=Button(root,text="Logout",fg="white",bg="black").grid(row=4,column=8)
    entrymarks=Button(root,text="Entry Marks",fg="white",bg="black").grid(row=2,column=0)
    viewmark=Button(root,text="View Mark",fg="white",bg="black",command=bye).grid(row=4,column=0)
    editmark=Button(root,text="Edit Marks",fg="white",bg="black").grid(row=6,column=0)
    details=Button(root,text="Details",fg="white",bg="black").grid(row=2,column=4)
    Result=Button(root,text="Result",fg="white",bg="black").grid(row=4,column=4)
    coscholastic=Button(root,text="Co-Scholastic",fg="white",bg="black").grid(row=6,column=4)
    
Label(root,text="session").grid(row=0,column=0)
session=Entry(root)
session.grid(row=0,column=1)
Label(root,text="User Name").grid(row=2,column=0)
uname=Entry(root)
uname.grid(row=2,column=1)
Label(root,text="Password").grid(row=4,column=0)
password=Entry(root)
password.grid(row=4,column=1)
ok=Button(root,text="DONE",fg="white",bg="black",command=entry_box).grid(row=6,column=0)
mainloop()
