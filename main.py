##### Rock-Paper-Scissors game #####
### Haythem Abu Al-Ragheb ###

##### To-do:GUI, Session history, make it an actual app, all-time score button #####

import random
import rpslogic
import json


### Game start ###
choices = ["Rock", "Paper", "Scissors"]

aiChoice = []
score = []
scoree=[]
scoreText = []


def game(choice):
    global scoreText
    pChoice = str(choice)
    aiChoice.append(random.choice(choices))
    ### Return score data ###
    # mylines = []
    # with open("log.txt", "rt") as f:
    #     for myline in f:
    #         mylines.append(myline)
    # dData, lData, wData = mylines[-4], mylines[-3], mylines[-2]  # d,l,w respective line in the log.txt file
    # d, l, w = int(dData[12:]), int(lData[12:]), int(wData[12:])  # d,l,w full value in the log.txt file
    with open("score.json") as f:
        data = json.load(f)
    with open("score.json") as f:
        d = json.load(f)["draw"]
    with open("score.json") as f:
        l = json.load(f)["lose"]
    with open("score.json") as f:
        w = json.load(f)["won"]

    score.append(d),score.append(l),score.append(w)
    print(score)
    rpslogic.game_logic(aiChoice[-1], pChoice,d,l,w,data)

    with open("score.json") as f:
        d = json.load(f)["draw"]
    with open("score.json") as f:
        l = json.load(f)["lose"]
    with open("score.json") as f:
        w = json.load(f)["won"]
    scoreT = "W:" + str(w) + " L:" + str(l) + " D:" + str(d)
    scoreText.clear()
    scoreText.append(scoreT)


    ### Game End ###













