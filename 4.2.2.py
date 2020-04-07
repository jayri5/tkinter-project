#result of student
from Tkinter import *
#student details of class

from Tkinter import *

root=Tk()
fa1=Button(root,text="FA 1",fg="white",bg="black").grid(row=0,column=1)
fa2=Button(root,text="FA 2",fg="white",bg="black").grid(row=0,column=2)
fa3=Button(root,text="FA 3",fg="white",bg="black").grid(row=0,column=3)
fa4=Button(root,text="FA 4",fg="white",bg="black").grid(row=0,column=4)
sa1=Button(root,text="SA 1",fg="white",bg="black").grid(row=0,column=5)
sa2=Button(root,text="SA 2",fg="white",bg="black").grid(row=0,column=6)
final=Button(root,text="Final",fg="white",bg="black").grid(row=0,column=7)

for i in range(5,55):
    for j in range(1,11):
        b=Entry(root)
        b.grid(row=i,column=j)


Label(root,text="S.No").grid(row=4,column=1)
sno=Entry(root)
sno.grid(row=5,column=1)
Label(root,text="Name").grid(row=4,column=2)
name=Entry(root)
name.grid(row=5,column=2)
Label(root,text="English").grid(row=4,column=3)
eng=Entry(root)
eng.grid(row=5,column=3)
Label(root,text="Math").grid(row=4,column=4)
math=Entry(root)
math.grid(row=5,column=4)
Label(root,text="Science").grid(row=4,column=5)
sci=Entry(root)
sci.grid(row=5,column=5)
Label(root,text="Social Science").grid(row=4,column=6)
ssci=Entry(root)
ssci.grid(row=5,column=6)
Label(root,text="2nd language").grid(row=4,column=7)
nd=Entry(root)
nd.grid(row=5,column=7)
Label(root,text="Computer").grid(row=4,column=8)
compt=Entry(root)
compt.grid(row=5,column=8)
Label(root,text="Total").grid(row=4,column=9)
total=Entry(root)
total.grid(row=5,column=9)
Label(root,text="Average").grid(row=4,column=10)
avg=Entry(root)
avg.grid(row=5,column=10)
mainloop()
