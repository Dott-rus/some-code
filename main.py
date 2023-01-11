from tkinter import *
from random import randint

root = Tk()
root.geometry('1900x600')
#Variables, variables and variables!
Money = 1000
SelectedMoney = 100

step1 = 1
step2 = 1
step3 = 1

winner = 0

voteFor = IntVar()
voteFor.set(1)
#----------------------------------------------------------------

#Importing images from img folder
Background = PhotoImage(file='img/background.png')

CH1fr1 = PhotoImage(file='img/ch_fr1.png')
CH1fr2 = PhotoImage(file='img/ch_fr2.png')

CH2fr1 = PhotoImage(file='img/ch2_fr1.png')
CH2fr2 = PhotoImage(file='img/ch2_fr2.png')

CH3fr1 = PhotoImage(file='img/ch3_fr1.png')
CH3fr2 = PhotoImage(file='img/ch3_fr2.png')

FinishLINE = PhotoImage(file='img/Finish.png')
#----------------------------------------------------------------

def restart():
    #Basic restart
    global step1, step2, step3, winner, Xcar1, Xcar2, Xcar3
    step1 = 1
    step2 = 1
    step3 = 1

    Xcar1 = Xcar2 = Xcar3 = 100

    winner = 0
    c.coords(car1, 100, 5)
    c.coords(car2, 100, 155)
    c.coords(car3, 100, 305)

def yaUstal():
    global Money, SelectedMoney
    #Just printing user wins or lose
    if voteFor.get() == winner: 
        
        Money = Money + int(SelectedMoney)
        LabelMoney.config(text='Money: ' + str(Money))
    if voteFor.get() != winner: 
        
        Money = Money - int(SelectedMoney)
        LabelMoney.config(text='Money: ' + str(Money))

def CheckBTW():
    #Just some poor stuff
    global winner, Xcar1, Xcar2, Xcar3, SelectedMoney
    SelectedMoney = Scale.get()
    if Xcar1 > Xcar2 > Xcar3:
        winner = 1
        print('Xcar1')
        yaUstal()
    if Xcar1 > Xcar3 > Xcar2:
        winner = 1
        print('Xcar1')
        yaUstal()
    if Xcar2 > Xcar1 > Xcar3:
        winner = 1
        print('Xcar2')
        yaUstal()
    if Xcar2 > Xcar3 > Xcar1:
        winner = 2
        print('Xcar2')
        yaUstal()
    if Xcar3 > Xcar1 > Xcar2:
        winner = 3
        print('Xcar3')
        yaUstal()
    if Xcar3 > Xcar2 > Xcar1:
        winner = 3
        print('Xcar3')
        yaUstal()
        
def Check():
    #Checking for winner
    global Xcar1, Xcar2, Xcar3, winner
    if Xcar1 > 1500:
        CheckBTW()

    elif Xcar2 > 1500:
        CheckBTW()

    elif Xcar3 > 1500:
        CheckBTW()

    else:
        MLoop()


def MLoop():
    global Xcar1, Xcar2, Xcar3, step1, step2, step3
    
    # Movment a character 
    Xcar1 = Xcar1 + randint(10, 80)
    c.coords(car1, Xcar1, randint(5, 25))
    if step1 % 2 == 0:
        c.itemconfig(car1, image=CH1fr1)
    else:
        c.itemconfig(car1, image=CH1fr2)
    step1 = step1 + 1
    
    # Movment a character 2
    Xcar2 = Xcar2 + randint(10, 80)
    c.coords(car2, Xcar2, randint(155, 175))
    if step2 % 2 == 0:
        c.itemconfig(car2, image=CH2fr1)
    else:
        c.itemconfig(car2, image=CH2fr2)
    step2 = step2 + 1
    
    # Movment a character 3
    Xcar3 = Xcar3 + randint(10, 80)
    c.coords(car3, Xcar3, randint(305, 325))
    if step3 % 2 == 0:
        c.itemconfig(car3, image=CH3fr1)
    else:
        c.itemconfig(car3, image=CH3fr2)
    step3 = step3 + 1
    print(str(Scale.get()))
    root.after(200, Check)

#Adding canvas and background
c = Canvas(root, width=1900, height=800)
c.place(x=0, y=0)
c.create_image(0, 0, anchor=NW, image=Background)

Finish = c.create_image(1900, 285, anchor=W, image=FinishLINE)

car1 = c.create_image(100, 5, anchor=N, image=CH1fr1)
car2 = c.create_image(100, 155, anchor=N, image=CH2fr1)
car3 = c.create_image(100, 305, anchor=N, image=CH3fr1)

Xcar1 = Xcar2 = Xcar3 = 100

StartButton = Button(text='Start', command=MLoop)
StartButton.place(x=10, y=580, anchor=W)

Vote1RadioButton = Radiobutton(root, text='Yellow', variable=voteFor, value=1)
Vote1RadioButton.place(x=50, y=580)
Vote2RadioButton = Radiobutton(root, text='Purple', variable=voteFor, value=2)
Vote2RadioButton.place(x=100, y=580)
Vote3RadioButton = Radiobutton(root, text='Orange', variable=voteFor, value=3)
Vote3RadioButton.place(x=150, y=580)

LabelMoney = Label(text='Money: ' + str(Money))
LabelMoney.place(x=200,y=580)


RestartButton = Button(text='Restart', command=restart)
RestartButton.place(x=300, y=580)

Slider = Scale(width=10, variable=SelectedMoney, from_=100, to=Money, resolution=100, orient=HORIZONTAL)
Slider.place(x=300,y=550)



root.mainloop()