from tkinter import *
import random
from tkinter import messagebox as msg

root = Tk()
root.geometry('500x500')
root.title('TicTacToe')
info = Label(root, font='lucida 10 bold', pady=10,
             text='Welcome to TicTacToe Game:\nRules:\n1.This is a 2 player Game, Player who plays first is player1 and has symbol X.\n2:One has to try making a streak of 3 in a row ,column or diagonal.\n3.One who completes step 2 first wins the game.')
info.pack()
Label(root, font='lucida 13 bold', pady=15, text='Player1 - X\t\tPlayer2 - O').pack()
root.wm_iconbitmap('icon.ico')


def cellselection(text, ch):
    global l
    if text == '1':
        b1['text'] = ch
        l.remove(text)
    elif text == '2':
        b2['text'] = ch
        l.remove(text)
    elif text == '3':
        b3['text'] = ch
        l.remove(text)
    elif text == '4':
        b4['text'] = ch
        l.remove(text)
    elif text == '5':
        b5['text'] = ch
        l.remove(text)
    elif text == '6':
        b6['text'] = ch
        l.remove(text)
    elif text == '7':
        b7['text'] = ch
        l.remove(text)
    elif text == '8':
        b8['text'] = ch
        l.remove(text)
    else:
        b9['text'] = ch
        l.remove(text)


def checkwinner(player1list, player2list):
    if '1' in player1list and '2' in player1list and '3' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '1' in player2list and '2' in player2list and '3' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '4' in player1list and '5' in player1list and '6' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '4' in player2list and '5' in player2list and '6' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '7' in player1list and '8' in player1list and '9' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '7' in player2list and '8' in player2list and '9' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '1' in player1list and '4' in player1list and '7' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '1' in player2list and '4' in player2list and '7' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '2' in player1list and '5' in player1list and '8' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '2' in player2list and '5' in player2list and '8' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '3' in player1list and '6' in player1list and '9' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '3' in player2list and '6' in player2list and '9' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '1' in player1list and '5' in player1list and '9' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '1' in player2list and '5' in player2list and '9' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif '3' in player1list and '5' in player1list and '7' in player1list:
        msg.showinfo('Winner info', 'Player 1 wins the Game !!!')
    elif '3' in player2list and '5' in player2list and '7' in player2list:
        msg.showinfo('Winner info', 'Player 2 wins the Game !!!')
    elif l == []:
        msg.showinfo('Winner info', 'Game Draw !!!')
    else:
        pass


def replay():
    global l, player1list, player2list
    b1['text'] = '1'
    b2['text'] = '2'
    b3['text'] = '3'
    b4['text'] = '4'
    b5['text'] = '5'
    b6['text'] = '6'
    b7['text'] = '7'
    b8['text'] = '8'
    b9['text'] = '9'
    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1list = []
    player2list = []


def Author():
    msg.showinfo('AboutUs', 'Developer:Dhairyashil Anil Ghatage.')


def player1(text):
    global player2list
    player1list.append(text)
    print(player1list)
    cellselection(text, 'X')
    checkwinner(player1list, player2list)


def player2(text):
    global curr_player, player1list
    player2list.append(text)
    print(player2list)
    curr_player = 1
    cellselection(text, 'O')
    checkwinner(player1list, player2list)


def click(event):
    text = event.widget.cget("text")
    global curr_player
    if curr_player == 1:
        curr_player = 2
        player1(text)
    else:
        player2(text)


l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
curr_player = 1
player1list = []
player2list = []
# ------------------------------------------------------------------------
f = Frame(root, padx=10, pady=15, bg='grey')
f.pack()
b1 = Button(f, text='1', font='lucida 20 bold', padx=10)
b1.pack(side=LEFT, padx=10, pady=10)
b1.bind('<Button-1>', click)

b2 = Button(f, text='2', font='lucida 20 bold', padx=10)
b2.pack(side=LEFT, padx=10, pady=10)
b2.bind('<Button-1>', click)

b3 = Button(f, text='3', font='lucida 20 bold', padx=10)
b3.pack(side=LEFT, padx=10, pady=10)
b3.bind('<Button-1>', click)
# ------------------------------------------------------------------------
f = Frame(root, padx=10, pady=15, bg='grey')
f.pack()
b4 = Button(f, text='4', font='lucida 20 bold', padx=10)
b4.pack(side=LEFT, padx=10, pady=10)
b4.bind('<Button-1>', click)

b5 = Button(f, text='5', font='lucida 20 bold', padx=10)
b5.pack(side=LEFT, padx=10, pady=10)
b5.bind('<Button-1>', click)

b6 = Button(f, text='6', font='lucida 20 bold', padx=10)
b6.pack(side=LEFT, padx=10, pady=10)
b6.bind('<Button-1>', click)

# ------------------------------------------------------------------------
f = Frame(root, padx=10, pady=15, bg='grey')
f.pack()
b7 = Button(f, text='7', font='lucida 20 bold', padx=10)
b7.pack(side=LEFT, padx=10, pady=10)
b7.bind('<Button-1>', click)

b8 = Button(f, text='8', font='lucida 20 bold', padx=10)
b8.pack(side=LEFT, padx=10, pady=10)
b8.bind('<Button-1>', click)

b9 = Button(f, text='9', font='lucida 20 bold', padx=10)
b9.pack(side=LEFT, padx=10, pady=10)
b9.bind('<Button-1>', click)
# ------------------------------------------------------------------------
menubar = Menu(root)
submenu = Menu(menubar, tearoff=0)
submenu.add_command(label="Replay", command=replay)
submenu.add_command(label="quit", command=quit)
menubar.add_cascade(label="File", menu=submenu)

submenu1 = Menu(menubar, tearoff=0)
submenu1.add_command(label="Author", command=Author)
root.config(menu=menubar)

menubar.add_cascade(label="About", menu=submenu1)
root.mainloop()
