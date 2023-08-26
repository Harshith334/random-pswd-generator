from tkinter import *
import string
import random


def generator():
    num=string.digits
    spclchar=string.punctuation
    salpha=string.ascii_lowercase
    capalpha=string.ascii_uppercase

    comb=num+spclchar+salpha+capalpha
    pswdlen=int(length_box.get())
    


    if choice.get()==1:
        password = ''.join(random.choices(salpha, k=pswdlen))
        pswdfield.delete(0, END) 
        pswdfield.insert(0, password)



    if choice.get()==2:
        password = ''.join(random.choices(comb, k=pswdlen))
        pswdfield.delete(0, END) 
        pswdfield.insert(0, password)








root=Tk()
root.config(bg="pink")
choice=IntVar()
Font=('bricolage grotesque',12,'bold')
passwordlabel=Label(root,width=20,text='password Generetor',font=('roboto',20,'italic'),bg='mediumseagreen',fg='#008080')
passwordlabel.grid(padx=25,pady=25)


weakradioBUtton=Radiobutton(root,width=10,text='weak',value=1,variable=choice,font=Font)
weakradioBUtton.grid(pady=5,row=1,column=0)
strongradioBUtton=Radiobutton(root,width=10,text='strong',value=2,variable=choice,font=Font)
strongradioBUtton.grid(pady=5,row=1,column=1)

lengthlabel=Label(root,text='password Length',font=Font,bg='mediumseagreen',fg='#008080')
lengthlabel.grid(pady=5,row=2,column=0)

length_box=Spinbox(root,from_=9,to_ =25,width=5,font=Font)
length_box.grid(pady=5,row=2,column=1)
generteButton=Button(root,text='GENERATE',font=Font,command=generator)
generteButton.grid(pady=5,row=3,column=0)  
pswdfield=Entry(root,width=50,bd=2)
pswdfield.grid(row=3,column=1)
root.mainloop()
