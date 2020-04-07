

from Tkinter import *
root= Tk()
Zodiac=""
def bye():
    root.destroy()
def entry_box():
    
    
    
    def bye():
        root.destroy()
    global Zodiac
    Label(root,text="Zodiac",fg="black",bg="white").grid(row=1,column=1)
    
    root.title("Z")
    var=StringVar(root)
    var.set("Zodiac")
    label_chosen_variable=Label(root,text="Zodiac")
    label_chosen_variable.grid(row=0,column=1)
    

    drop_menu=OptionMenu(root,var,"l","c")
    drop_menu.grid(row=1,column=1)
    print drop_menu
    

    



Enter=Button(root,text="ENTER",fg="red",bg="black",command=entry_box).grid(row=10,column=1)
cancel=Button(root,text="CANCEL",fg="red",bg="black",command=bye).grid(row=10,column=2)
root.mainloop()
mainloop()
                                                                            
    
   
