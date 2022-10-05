import time
import logging
import main
import json
k=[]


def game_logic(ai,p,d,l,w,djson):
    if ai == p:
        print("Computer chose: " + ai + ". It's a draw")
        k.append('draw')
        d += 1
        # return result,d,l,w
    # lost
    elif p == "Rock" and ai == "Paper":
        print("Computer chose: " + ai + ". You lost")
        k.append('lost')
        l += 1

    elif p == "Scissors" and ai == "Rock":
        print("Computer chose: " + ai + ". You lost")
        k.append('lost')
        l += 1

    elif p == "Paper" and ai == "Scissors":
        print("Computer chose: " + ai + ". You lost")
        k.append('lost')
        l += 1

    # won
    else:
        print("Computer chose:" + ai + ". You Won")
        k.append('won')
        w += 1


    newData = {"draw": d, "lose": l, "won": w}
    djson.update(newData)
    with open("score.json", 'w') as f:
        json.dump(djson, f, indent=2)

    # runTime = time.ctime(time.time())
    # logging.basicConfig(filename="log.txt", level=logging.INFO, filemode='w')
    # logging.info(runTime)
    # logging.info("D:" + str(d))
    # logging.info("L:" + str(l))
    # logging.info("W:" + str(w))
    # logging.info("-----------------")
    # It'll only log the data in the file when the user doesn't wish to continue #
    # it'll add every game (multiple entries/lines) but the [-x] in line 12 makes it read the last added line #
    # with x to choose the correct line for each value #



written_results = k

