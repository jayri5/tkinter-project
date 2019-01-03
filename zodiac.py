from Tkinter import *

class Application(Frame):
    
    def get(self):
        s=self.z.get()
        if str(s)=="Aries":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n')
            self.zodiac.insert(END,('fighting for beliefs,fearlessly facing situations'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Libra":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('seeking peace, harmony and cooperation'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Taurus":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('seeking security and enjoying earthly pleasures'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Scorpio":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('diving deep and forming bonds that are built to last'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Gemini":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('communicating and collaborating at full mast'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Sagittarius":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('dreaming big, chasing the impossible and taking fearless risks'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Cancer":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('connecting with feelings, planting deep roots and feathering family nests'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Capricorn":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('master planning and achieving goals irrespective of conditions'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Leo":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('warm and action - oriented'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Aquarius":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('innovating and uniting for social justice'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Virgo":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('teaching to serve and doing impeccable work'))
            self.zodiac.insert(END,'\n')

        elif str(s)=="Pisces":
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,'\n') 
            self.zodiac.insert(END,('awakening compassion, imagination and artistry'))
            self.zodiac.insert(END,'\n')         
        else:
            self.zodiac.delete(0.0,END)
            self.zodiac.insert(END,('This is not a Zodiac sign'))

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Enter your Zodiac sign below--and get to know about yourself",
        

        self.hi_there.pack({"side": "left"},padx=20,pady=20)


        Entry(self.master,bd=10,bg='cyan',width=50,font='arial',textvar=self.z).pack()
        self.zodiac=Text(self.master,height=15,width=50,bd=10,bg="green",font="arial")
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
