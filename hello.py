from Tkinter import *

class Application(Frame):
    
    def get(self):
        
        s=self.z.get()
        if str(s)=="leo":
            self.zodiac.insert(END,'\n')
            self.zodiac.insert(END,('best'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="capricorn":
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('good'))
            self.zodiac.insert(END,'\n')    
        else:
            self.zodiac.insert(END,('Done'))

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Enter your Zodiac sign below",
        

        self.hi_there.pack({"side": "left"})


        Entry(self.master,bd=10,bg='yellow',width=30,font='arial',textvar=self.z).pack()
        self.zodiac=Text(self.master,height=15,width=30,bd=10,bg="green",font="arial")
        self.zodiac.pack()
        Button(self.master,text='Show the truth of my zodiac sign',command=self.get).pack()
        
            

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.z=StringVar()
        self.pack()
        self.createWidgets()

root = Tk()
root.config(bg="blue")
app = Application(master=root)
app.mainloop()
root.destroy()
