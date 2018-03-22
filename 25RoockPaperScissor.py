from tkinter import *
import tkinter.messagebox
import random
k=0
k=random.randint(1,10)



#display the results
def messageWindow(message):
    win = Toplevel()
    win.title('result')
    #message = "This will delete stuff"
    Label(win, text=message).pack()
    Button(win, text='OK!!', command=win.destroy).pack()

    def trial():
        win.destroy
        start()
    Button(win,text="replay!",command=trial).pack


#input to display the results
def rockSelect():
    #p2=Toplevel()

    if k == 1 or k == 4 or k == 7:
        messageWindow("Draw\nBoth chose Rock")
    elif k == 2 or k == 5 or k==8:
        messageWindow("You Lose\nYou chose Rock\nCPU chose Paper")

     elif k == 3 or k == 6 or k == 9:
        messageWindow("You Win\nYou chose Rock\nCPU chose Scissor")

    #p2.pack()
    #p2.destroy()

def paperSelect():
    #p3=Toplevel()
    if k == 2 or k == 5 or k == 8 :
        messageWindow("Draw\nBoth chose Paper")
    elif k == 3 or k == 6 or k == 9:
        messageWindow("You Lose\nYou chose Paper\nCPU chose Scissor")

    elif k == 1 or k == 4 or k == 7:
        messageWindow("You Win\nYou chose Paper\nCPU chose Rock")

    '''p3.pack()
    p3.destroy()'''
def scissorSelect():
    #p4.TopLevel()
    if k == 3 or k == 6 or k == 9:
        messageWindow("Draw\1nBoth chose Scissor")
    elif k == 1 or k ==4 or k==7:
        messageWindow("You Lose\nYou chose Scissor\nCPU chose Rock")

    elif k == 2 or k == 5 or k == 8:
        messageWindow("You Win\nYou chose Scissor\nCPU chose Paper")

    #p4.pack()
    #p4.destroy()'''

#second window to start game
def start():
    p1=Toplevel()


    l1=Message(p1,text="Choose any of the following:")

    rock=PhotoImage(file="rock.png")
    rockButton=Button(p1,image=rock,command=rockSelect)
    rockButton.pack(fill=BOTH, expand=1)
    Label(p1, text="Rock:").pack(fill=BOTH, expand=1)

    paper=PhotoImage(file="paper.png")
    paperButton=Button(p1,image=paper,command=paperSelect)
    paperButton.pack(fill=BOTH, expand=1)
    Label(p1, text="Paper:").pack(fill=BOTH, expand=1)

    scissor=PhotoImage(file="scissor.png")
    scissorButton=Button(p1,image=scissor,command=scissorSelect)
    scissorButton.pack(fill=BOTH, expand=1)
    Label(p1, text="Scissor:").pack(fill=BOTH, expand=1)

    p1.pack(fill=BOTH, expand=1)
    #p1.quit()


#main window starts here
root=Tk()
one=Label(root,text="Welcome")
one.pack()
two=Button(root,text="start!!",command=start)
two.pack()
root.mainloop()