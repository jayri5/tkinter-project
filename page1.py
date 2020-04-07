#anyone opens either teacher or office

from Tkinter import *
root= Tk()
def bye():
    root.destroy()

def entry_box():
   
    root=Tk()
    
    Label(root,text="Teacher").grid(row=0,column=0)
    Label(root,text="Student").grid(row=0,column=2)
    Label(root,text="Fee").grid(row=0,column=4)
    Label(root,text="Result").grid(row=0,column=6)
    Label(root,text="Update").grid(row=0,column=8)
    teacher=Button(root,text="Teacher",fg="white",bg="black").grid(row=2,column=8)
    clas=Button(root,text="Class",fg="white",bg="black").grid(row=4,column=8)
    new=Button(root,text="New",fg="white",bg="black").grid(row=2,column=0)
    edit=Button(root,text="Edit",fg="white",bg="black",command=bye).grid(row=4,column=0)
    remove=Button(root,text="Remove",fg="white",bg="black").grid(row=6,column=0)
    new=Button(root,text="New",fg="white",bg="black").grid(row=2,column=4)
    edit=Button(root,text="Edit",fg="white",bg="black").grid(row=4,column=4)
    remove=Button(root,text="Remove",fg="white",bg="black").grid(row=6,column=4)
    
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
back=Button(root,text="BACK",fg="white",bg="black",command=bye).grid(row=6,column=1)
mainloop()
