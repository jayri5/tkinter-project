#student details of class

from Tkinter import *
root= Tk()
for i in range(5,55):
        for j in range(1,8):
            b=Entry(root)
            b.grid(row=i,column=j)



Label(root,text="S.No").grid(row=0,column=1)
sno=Entry(root)
sno.grid(row=1,column=1)
Label(root,text="Name").grid(row=0,column=2)
name=Entry(root)
name.grid(row=1,column=2)
Label(root,text="Father's Name").grid(row=0,column=3)
fname=Entry(root)
fname.grid(row=1,column=3)
Label(root,text="Mother's Name").grid(row=0,column=4)
mname=Entry(root)
mname.grid(row=1,column=4)
Label(root,text="DOB").grid(row=0,column=5)
dob=Entry(root)
dob.grid(row=1,column=5)
Label(root,text="contact").grid(row=0,column=6)
contact=Entry(root)
contact.grid(row=1,column=6)
Label(root,text="Email ID").grid(row=0,column=7)
email=Entry(root)
email.grid(row=1,column=7)
Label(root,text="Address").grid(row=0,column=7)
add=Entry(root)
add.grid(row=1,column=7)
mainloop()
