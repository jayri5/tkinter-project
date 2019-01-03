from Tkinter import *

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnclear():
    global operator
    operator=""
    text_input.set("")

def btnequal():
    global operator
    result=eval(operator)
    text_input.set(result)
    


calc=Tk()
calc.title("Calculator")
operator=""
text_input=StringVar()
textdisplay=Entry(calc,font='arial 20 bold',textvar=text_input,bd=30,fg="black",justify="right").grid(columnspan=4)

button7=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='7',command=lambda:btnclick(7))
button7.grid(row=1,column=0)

button8=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='8',command=lambda:btnclick(8))
button8.grid(row=1,column=1)


button9=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='9',command=lambda:btnclick(9))
button9.grid(row=1,column=2)

buttonAdd=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='+',command=lambda:btnclick("+"))
buttonAdd.grid(row=1,column=3)
 

button4=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='4',command=lambda:btnclick(4))
button4.grid(row=2,column=0)

button5=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='5',command=lambda:btnclick(5))
button5.grid(row=2,column=1)

button6=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='6',command=lambda:btnclick(6))
button6.grid(row=2,column=2)

buttonSub=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='-',command=lambda:btnclick('-'))
buttonSub.grid(row=2,column=3)



button1=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='1',command=lambda:btnclick(1))
button1.grid(row=3,column=0)

button2=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='2',command=lambda:btnclick(2))
button2.grid(row=3,column=1)


button3=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='3',command=lambda:btnclick(3))
button3.grid(row=3,column=2)

buttonMul=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='*',command=lambda:btnclick('*'))
buttonMul.grid(row=3,column=3)


button0=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='0',command=lambda:btnclick(0))
button0.grid(row=4,column=0)

buttonC=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='C',command=btnclear)
buttonC.grid(row=4,column=1)

buttonEqual=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='=',command=btnequal)
buttonEqual.grid(row=4,column=2)


buttonDiv=Button(calc,padx=16,bd=8,fg="blue",font='arial 20 bold',text='/',command=lambda:btnclick('/'))
buttonDiv.grid(row=4,column=3)


calc.mainloop()
