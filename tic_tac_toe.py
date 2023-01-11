import copy
import time
from tkinter import *
from ai_is_playing import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")
possible_actions=[[i,j] for i in range(3) for j in range(3)]
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)

def get_state():
    button=[button1,button2,button3,button4,button5,button6,button7,button8,button9]
    state=[['-']*3 for i in range(3)]
    count=0
    for b in button:
        state[int(count/3)][int(count%3)]=b['text']
        count+=1
    return state
def get_action(button_pressed):
    #print(button_pressed)
    #button=[button1,button2,button3,button4,button5,button6,button7,button8,button9]
#    print(button)
    for i in range(len(button)):
#        print(i)
        if button_pressed==button[i]:
            return int(i/3),int(i%3)
def get_possible_action():
    possible_actions=[]
    for i in range(len(button)):
        if button[i]['text']==' ':
            possible_actions.append(list([int(i/3),int(i%3)]))
    return possible_actions
def btnClick(buttons):
#    print(get_action(buttons))
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "x"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        #time.sleep(2)
        action=list(get_action(buttons))
        state=get_state()
        possible_actions=get_possible_action()
        #print("posssible")
        #print(possible_actions)
        possible_actions=remove_action(possible_actions,action)
	    #if [1,1] in possible_actions == True :
		 #   action=[1,1]
	        #    else: '''
	    action=choose_action(copy.deepcopy(state),copy.deepcopy(possible_actions))
        #print("button is pressed:"+str(action[0]*3+action[1]+1))
        btnClick(button[action[0]*3+action[1]])
        possible_actions=remove_action(possible_actions,action)
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        print("is it checking?")
        buttons["text"] = "o"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
        button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x' or
        button7['text'] =='x' and button8['text'] == 'x' and button9['text'] == 'x' or
        button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x' or
        button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x' or
        button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or
        button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x' or
        button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x' or
        button7['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe It is a Tie because you can not win it")

    elif (button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
          button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o' or
          button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o' or
          button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o' or
          button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o' or
          button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
          button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o' or
          button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o' or
          button7['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


buttons = StringVar()

label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)
button=[button1,button2,button3,button4,button5,button6,button7,button8,button9]

tk.mainloop()
