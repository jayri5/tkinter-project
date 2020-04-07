from Tkinter import *
root= Tk()
Label(root,text="Zodiac",height=2,width=30,fg="black",bg="red").grid(row=1)

root.title("app")
var=StringVar(root)
var.set("signs")
label_chosen_variable=Label(root,text="signs")
label_chosen_variable.grid(row=2,column=0)

drop_menu=OptionMenu(root,var,"l","c")
drop_menu.grid(row=3,column=0)




root.mainloop()
mainloop()
                 
