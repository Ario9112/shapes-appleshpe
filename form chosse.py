from tkinter import *
from tkinter import  ttk
def submitbutton():
    print('added to the wallet.',format(iphone_type.get()))

main_windows =  Tk()
main_windows.title("Shopping app")
main_windows.configure(bg="#42f2f5")
main_windows.geometry("600x500")
greeting=Label(text="Hello fellow customer !",
               fg="white",
               bg="#42f2f5",
               padx=5,
               pady=5,
               font=("Arial 25 bold"))
greeting.grid(row=0,column=1,pady=5)

question=Label(text="Chosse your item ?",
               fg="white",
               bg="#42f2f5",
               padx=5,
               pady=5,
               font=("Arial ",25))
question.grid(row=0,column=2,pady=5)

selected_iphone = StringVar()
iphone_type = ttk.Combobox(main_windows,textvariable=selected_iphone)

iphone_type['values']=["Vision Pro:3499$(pre order)","iphone 11 price:260$","iphone 12 price:400","iphone 13 price :500$ ","iphone 14 price:700$",'iphone 15 price:989$']
iphone_type['state']='redonly'
iphone_type.grid(row=1,column=1,columnspan=2)

submit = Button(text ="submit", width=10,height=1,bg ="red",border=5,activebackground="darkgreen", command=submitbutton )
submit.grid(row=6, column=0,columnspan=2)

main_windows.mainloop()