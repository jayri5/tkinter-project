from Tkinter import *

def register_user():
    userinfo=username_entry.get()
    passwordinfo=password_entry.get()

    file=open(userinfo+".txt","w")
    file.write(userinfo)
    file.write(passwordinfo)
    file.close
    
    if userinfo=="" or passwordinfo=="":
        screen5=Tk()
        screen5.title("Message")
        screen5.geometry('500x500')
        Label(screen5,text="Please fill in the details",font='arial 20 bold').pack()
    else:
        screen5=Tk()
        screen5.title("Message")
        screen5.geometry('500x500')
        Label(screen5,text="You have successfully logged in.",font='arial 20 bold').pack()
    
def register():
    screen1=Tk()
    screen1.title("Log in")
    screen1.geometry('500x500')
    global username
    global password

    global username_entry
    global password_entry
    
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Enter required fields below",bg="yellow",fg="blue",font='arial 20 bold').pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username",font='arial 20 bold').pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Password",font='arial 20 bold').pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="                                             ",bg="red").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="").pack()
    Button(screen1,text="login here",width=10,height=2,bg="cyan",fg="black",command=register_user,font='arial 20 ').pack()

def login_verify():
    user1=username_entry1.get()
    pw1=password_entry1.get()
    if user1=="" or pw1=="":
        screen6=Tk()
        screen6.geometry('500x500')
        Label(screen6,text="Please fill in the details",font='arial 20 bold').pack()
    else:
        global pastbc
        global pasc
        pasw=StringVar()
        screen3=Tk()
        screen3.title("Confirmation")
        screen3.geometry('500x500')
        pasc=password_entry1.get()
        Label(screen3,text="Enter your password again",font='arial 20 bold',height=2).pack()
        Label(screen3,text="").pack()
        Label(screen3,text="").pack()
        pastbc=Entry(screen3,textvariable=pasw)
        pastbc.pack()
        Label(screen3,text="").pack()
        Label(screen3,text="").pack()
        Label(screen3,text="").pack()
        Label(screen3,text="").pack()
        Label(screen3,text="").pack()
        Button(screen3,text="Proceed here",width=60,height=2,bg="cyan",fg="black",command=nextf,font='arial 20 bold').pack()

def nextf():
    screen4=Tk()
    screen4.title("Message")
    screen4.geometry('500x500')
    pastc=pastbc.get()
    if pastc==pasc:
        Label(screen4,text="You have successfully signed up",font='arial 20 bold').pack()
    else:
        Label(screen4,text="Incorrect password",font='arial 20 bold').pack()
    
def login():
    global username_entry1
    global password_entry1
    screen2=Tk()
    screen2.title("Sign up")
    screen2.geometry('500x500')
    Label(screen2,text="Sign up Here",font='arial 20 bold').pack()
    Label(screen2,text="").pack()

    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()
    
    Label(screen2,text="Username",font='arial 20 bold').pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password",font='arial 20 bold').pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Confirm password",width=60,height=2,bg="cyan",fg="black",command=login_verify,font='arial 20 bold').pack() 
    
    
def main_screen():
    screen=Tk()
    screen.title("Sign up and Login system")
    screen.geometry('500x500')
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Button(screen,text="Sign up",command=login,width=60,height=2,bg="red",fg="black",font='arial 20 bold').pack()
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Label(screen,text="                                         ",bg="blue").pack()
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Label(screen,text="").pack()
    Button(screen,text="Login",command=register,width=60,height=2,bg="green",fg="black",font='arial 20 bold').pack()

    screen.mainloop()

main_screen()    
