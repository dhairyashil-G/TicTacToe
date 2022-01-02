from tkinter import *
import random
root=Tk()
root.geometry('500x500')
root.title('TicTacToe')

def cellselection(text,ch):
    global l
    if text=='1':
        b1['text']=ch
        l.remove(text)
        comp()
    elif text=='2':
        b2['text']=ch
        l.remove(text)
        comp()
    elif text=='3':
        b3['text']=ch
        l.remove(text)
        comp()
    elif text=='4':
        b4['text']=ch
        l.remove(text)
        comp()
    elif text=='5':
        b5['text']=ch
        l.remove(text)
        comp()
    elif text=='6':
        b6['text']=ch
        l.remove(text)
        comp()
    elif text=='7':
        b7['text']=ch
        l.remove(text)
        comp()
    elif text=='8':
        b8['text']=ch
        l.remove(text)
        comp()
    else:
        b9['text']=ch
        l.remove(text)
        comp()

def click(event):
    text = event.widget.cget("text")
    cellselection(text,'X')

def comp():
    global l
    s=random.choice(l)
    cellselection(s,'O')
    l.remove(s)


l=['1','2','3','4','5','6','7','8','9']
#------------------------------------------------------------------------
f=Frame(root,padx=10,pady=15,bg='grey')
f.pack()
b1=Button(f,text='1',font='lucida 20 bold',padx=10)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',click)

b2=Button(f,text='2',font='lucida 20 bold',padx=10)
b2.pack(side=LEFT,padx=10,pady=10)
b2.bind('<Button-1>',click)

b3=Button(f,text='3',font='lucida 20 bold',padx=10)
b3.pack(side=LEFT,padx=10,pady=10)
b3.bind('<Button-1>',click)
#------------------------------------------------------------------------
f=Frame(root,padx=10,pady=15,bg='grey')
f.pack()
b4=Button(f,text='4',font='lucida 20 bold',padx=10)
b4.pack(side=LEFT,padx=10,pady=10)
b4.bind('<Button-1>',click)

b5=Button(f,text='5',font='lucida 20 bold',padx=10)
b5.pack(side=LEFT,padx=10,pady=10)
b5.bind('<Button-1>',click)

b6=Button(f,text='6',font='lucida 20 bold',padx=10)
b6.pack(side=LEFT,padx=10,pady=10)
b6.bind('<Button-1>',click)

#------------------------------------------------------------------------
f=Frame(root,padx=10,pady=15,bg='grey')
f.pack()
b7=Button(f,text='7',font='lucida 20 bold',padx=10)
b7.pack(side=LEFT,padx=10,pady=10)
b7.bind('<Button-1>',click)

b8=Button(f,text='8',font='lucida 20 bold',padx=10)
b8.pack(side=LEFT,padx=10,pady=10)
b8.bind('<Button-1>',click)

b9=Button(f,text='9',font='lucida 20 bold',padx=10)
b9.pack(side=LEFT,padx=10,pady=10)
b9.bind('<Button-1>',click)
#------------------------------------------------------------------------



root.mainloop()