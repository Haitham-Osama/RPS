from tkinter import *
from PIL import Image,ImageTk
import rpslogic
import main

rpsButtonList = []
j=[]
aiChoice = main.aiChoice
result = rpslogic.written_results
score_text = [main.scoreText]


def gameWindowFunction():
    def clearGUI():
        startWindow.rockButton.destroy()
        startWindow.paperButton.destroy()
        startWindow.scissorsButton.destroy()
    aiChoice.clear()

    global j

    startWindow.rockButton = Button(startWindow,image=j[1],border=False,borderwidth=0,highlightthickness=0,
                                    command=lambda:rockChoice() or clearGUI()
                                    )
    startWindow.paperButton = Button(startWindow,image=j[3],border=False,borderwidth=0,highlightthickness=0,
                                     command=lambda:paperChoice() or clearGUI()
                                     )
    startWindow.scissorsButton = Button(startWindow,image=j[5],border=False,borderwidth=0,highlightthickness=0,
                                        command=lambda:scissorsChoice() or clearGUI()
                                        )
    startWindow.scoreLabel = Label(startWindow,text=score_text[-1],font=("Minecraft",25),border=False,borderwidth=0,highlightthickness=0,background='white')

    startWindow.rockButton.place(relx=0.2, rely=0.4, anchor=CENTER)
    startWindow.paperButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    startWindow.scissorsButton.place(relx=0.8, rely=0.4, anchor=CENTER)
    startWindow.scoreLabel.place(relx=0.01, rely=0.95, anchor=W)

    rpsButtonList.append(startWindow.rockButton)
    rpsButtonList.append(startWindow.paperButton)
    rpsButtonList.append(startWindow.scissorsButton)


def fkn_results(p,ai,results):

    def clearGUI():
        startWindow.rockLabel.destroy(),startWindow.paperLabel.destroy(),startWindow.scissorsLabel.destroy(),\
        startWindow.playButton.destroy(),startWindow.quitButton.destroy(),startWindow.drawLabel.destroy(),\
        startWindow.winLabel.destroy(),startWindow.loseLabel.destroy(),startWindow.airockLabel.destroy(),\
        startWindow.aipaperLabel.destroy(),startWindow.aiscissorsLabel.destroy()

    global j

    startWindow.rockLabel = Label(startWindow,image=j[1],border=False,borderwidth=0,highlightthickness=0)
    startWindow.paperLabel =   Label(startWindow,image=j[3],border=False,borderwidth=0,highlightthickness=0)
    startWindow.scissorsLabel =   Label(startWindow,image=j[5],border=False,borderwidth=0,highlightthickness=0)
    startWindow.airockLabel = Label(startWindow,image=j[1],border=False,borderwidth=0,highlightthickness=0)
    startWindow.aipaperLabel = Label(startWindow,image=j[3],border=False,borderwidth=0,highlightthickness=0)
    startWindow.aiscissorsLabel = Label(startWindow,image=j[5],border=False,borderwidth=0,highlightthickness=0)

    startWindow.winLabel = Label(startWindow, image=j[7], border=False, borderwidth=0, highlightthickness=0)
    startWindow.loseLabel = Label(startWindow, image=j[9], border=False, borderwidth=0, highlightthickness=0)
    startWindow.drawLabel = Label(startWindow, image=j[11], border=False, borderwidth=0, highlightthickness=0)

    startWindow.quitButton = Button(startWindow,image=quitButtonImage,border=False,command=quitButtonFunction,highlightthickness=0)
    startWindow.playButton = Button(startWindow, image=playButtonImage, border=False, command=lambda:gameWindowFunction() or clearGUI(),highlightthickness=0)

    if results == 'draw' and p == 'Rock':
        startWindow.rockLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.drawLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'draw' and p == 'Paper':
        startWindow.paperLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.drawLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'draw' and p == 'Scissors':
        startWindow.scissorsLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.drawLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'lost' and p == 'Rock':
        startWindow.rockLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.loseLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'lost' and p == 'Paper':
        startWindow.paperLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.loseLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'lost' and p == 'Scissors':
        startWindow.scissorsLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.loseLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'won' and p == 'Rock':
        startWindow.rockLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.winLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'won' and p == 'Paper':
        startWindow.paperLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.winLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
    elif results == 'won' and p == 'Scissors':
        startWindow.scissorsLabel.place(relx=0.2, rely=0.4, anchor=CENTER)
        startWindow.winLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        if ai == 'Rock':
            startWindow.airockLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Paper':
            startWindow.aipaperLabel.place(relx=0.8, rely=0.4, anchor=CENTER)
        elif ai == 'Scissors':
            startWindow.aiscissorsLabel.place(relx=0.8, rely=0.4, anchor=CENTER)


    startWindow.quitButton.place(relx=0.5, rely=0.83, anchor=CENTER)
    startWindow.playButton.place(relx=0.5, rely=0.69, anchor=CENTER)


def readyButtonFunction():
    startButton.destroy()
    quitButton.destroy()
    logo.destroy()
    gameWindowFunction()


def quitButtonFunction():
    startWindow.destroy()


def rockChoice():
    choice = "Rock"
    main.game(choice)
    fkn_results(choice, aiChoice[-1], result[-1])


def paperChoice():
    choice = "Paper"
    main.game(choice)
    fkn_results(choice, aiChoice[-1], result[-1])


def scissorsChoice():
    choice = "Scissors"
    main.game(choice)
    fkn_results(choice, aiChoice[-1], result[-1])


startWindow = Tk()
iconImage = Image.open("assets/logo.jpg")
icon = ImageTk.PhotoImage(iconImage)

startWindow.geometry("1280x720")
startWindow.minsize(1280,720)
startWindow.config(bg='white'),startWindow.title("Rock, Paper and Scissors"),startWindow.iconphoto(True, icon)


#FIX THE FUCKING CORNERS

logoImage = Image.open("assets/logo.jpg").resize((450,400))

logoPhotoImage = ImageTk.PhotoImage(logoImage)

startImage = Image.open("assets/start.png").resize((250,85))

startButtonImage = ImageTk.PhotoImage(startImage)

playImage = Image.open("assets/play.png").resize((250,85))
playButtonImage = ImageTk.PhotoImage(playImage)

quitImage = Image.open("assets/quit.png").resize((250, 85))
quitButtonImage = ImageTk.PhotoImage(quitImage)

rockImage = Image.open("assets/rock.png")
j.append(rockImage)
rockPhotoImage = ImageTk.PhotoImage(j[0])
j.append(rockPhotoImage)

paperImage = Image.open("assets/paper.png")
j.append(paperImage)
paperPhotoImage = ImageTk.PhotoImage(j[2])
j.append(paperPhotoImage)

scissorsImage = Image.open("assets/scissors.png")
j.append(scissorsImage)
scissorsPhotoImage = ImageTk.PhotoImage(j[4])
j.append(scissorsPhotoImage)

winImage = Image.open("assets/win.png")
j.append(winImage)
winPhotoImage = ImageTk.PhotoImage(j[6])
j.append(winPhotoImage)

loseImage = Image.open("assets/lose.png")

j.append(loseImage)
losePhotoImage = ImageTk.PhotoImage(j[8])
j.append(losePhotoImage)

drawImage = Image.open("assets/draw.png").resize((325, 325))
j.append(drawImage)
drawPhotoImage = ImageTk.PhotoImage(j[10])
j.append(drawPhotoImage)


logo = Label(startWindow,
             image=logoPhotoImage,
             highlightthickness=0,
             border=False)

startButton = Button(startWindow,
                     image=startButtonImage,
                     border=False,
                     borderwidth=0,
                     command=readyButtonFunction,
                     highlightthickness=0
                     )

quitButton = Button(startWindow,
                    image=quitButtonImage,
                    border=False,
                    command=quitButtonFunction,
                    highlightthickness=0
                    )


startButton.place(relx=0.5, rely=0.69, anchor=CENTER)
quitButton.place(relx=0.5, rely=0.83, anchor=CENTER)
logo.place(relx=0.5,rely=0.33,anchor=CENTER)
startWindow.mainloop()