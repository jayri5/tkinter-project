#Remove teacher

from Tkinter import *
root= Tk()
def bye():
    root.destroy()

def entry_box():
   
    root=Tk()
    
    Label(root,text="DETAILS").grid(row=0,column=3)
    Label(root,text="Personal Details").grid(row=2,column=0)
    Label(root,text="First name").grid(row=3,column=0)
    f1name=Entry(root)
    f1name.grid(row=3,column=1)
    Label(root,text="Last name").grid(row=3,column=4)
    lname=Entry(root)
    lname.grid(row=3,column=5)
    Label(root,text="Father's name").grid(row=4,column=0)
    fname=Entry(root)
    fname.grid(row=4,column=1)
    Label(root,text="Mother's Name").grid(row=4,column=4)
    mname=Entry(root)
    mname.grid(row=4,column=5)
    Label(root,text="DOB").grid(row=5,column=0)
    dob=Entry(root)
    dob.grid(row=5,column=1)
    Label(root,text="Address").grid(row=6,column=0)
    add=Entry(root)
    add.grid(row=6,column=1)

    Label(root,text="Contact Details").grid(row=9,column=0)
    Label(root,text="tel no").grid(row=10,column=0)
    tel=Entry(root)
    tel.grid(row=10,column=1)
    Label(root,text="mobile no").grid(row=10,column=4)
    mno=Entry(root)
    mno.grid(row=10,column=5)
    Label(root,text="Email ID").grid(row=11,column=0)
    email=Entry(root)
    email.grid(row=11,column=1)
    Label(root,text="ID proof").grid(row=12,column=0)
    idp=Entry(root)
    idp.grid(row=12,column=1)

    Label(root,text="Designation").grid(row=15,column=0)
    Label(root,text="Teacher ID").grid(row=16,column=0)
    tid=Entry(root)
    tid.grid(row=16,column=1)
    Label(root,text="Qualification").grid(row=17,column=0)
    qua=Entry(root)
    qua.grid(row=17,column=1)
    Label(root,text="grade").grid(row=18,column=0)
    grade=Entry(root)
    grade.grid(row=18,column=1)
    Label(root,text="subject").grid(row=18,column=4)
    sub=Entry(root)
    sub.grid(row=18,column=5)
    Label(root,text="Initial").grid(row=19,column=0)
    ini=Entry(root)
    ini.grid(row=19,column=1)
    Label(root,text="Year of join").grid(row=20,column=0)
    join=Entry(root)
    join.grid(row=20,column=1)

    Label(root,text="Subject Teaching").grid(row=22,column=0)
    Label(root,text="Class").grid(row=23,column=0)
    clas=Entry(root)
    clas.grid(row=23,column=1)
    Label(root,text="section").grid(row=23,column=4)
    sec=Entry(root)
    sec.grid(row=23,column=5)

    Label(root,text="Class Teaching").grid(row=26,column=0)
    Label(root,text="Class").grid(row=27,column=0)
    clas=Entry(root)
    clas.grid(row=27,column=1)
    Label(root,text="section").grid(row=27,column=4)
    sec=Entry(root)
    sec.grid(row=27,column=5)

    remove=Button(root,text="Remove",fg="white",bg="black").grid(row=28,column=2)
    cancel=Button(root,text="Cancel",fg="white",bg="black",command=bye).grid(row=28,column=5)
    
Label(root,text="Teacher ID").grid(row=2,column=0)
tid=Entry(root)
tid.grid(row=2,column=1)

getdetails=Button(root,text="Get Details",fg="white",bg="black",command=entry_box).grid(row=4,column=0)



mainloop()
