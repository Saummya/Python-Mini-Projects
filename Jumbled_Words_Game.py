#Remember the childhood days when solving jumbled words was a great fun !!
#Let's try a code for this.

import random
def choose():
    words=["rainbow","computer", "science", "programming","player", "condition","reverse","water","chocolate","board"]
    pick= random.choice(words)
    return pick

def jumble(word):
    jumbled= " ".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n, p2n,p1,p2):
    print(p1)
    

def play():
    p1name= input("Player 1, Please enter your name: ")
    p2name= input("Player 2, Please enter your name: ")
    pp1=0    #points of player 1
    pp2=0
    turn=0
    while(1):
        picked_word= choose()
        #create function
        qn= jumble(picked_word)
        print(qn)
        if(turn%2==0):
            #player 1
            print(p1name, ", it's your turn! [REMEMBER THE ANSWER IS CASE SENSITIVE]")
            ans=input("Tell what's on my mind? : ")
            if ans==picked_word:
                print("Wo hoo!! correct answer")
                pp1=pp1+1
                print("Your score is : ",pp1)
            else:
                print("Better luck next time, I thought: ", picked_word)
        c= int(input("Press 1 to continue and 0 to quit: "))
        if c==0:
             thank(p1name,p2name,pp1,pp2)
             break
            
        else:
            #player2
            print(p2name, ", it's your turn!   [REMEMBER THE ANSWER IS CASE SENSITIVE]")
           
            ans=input("Tell what's on my mind? : ")
            if ans==picked_word:
                print("Wo hoo!! correct answer")
                pp2=pp2+1
                print("Your score is : ",pp2)
            else:
                print("Better luck next time, I thought: ", picked_word)
        c= int(input("Press 1 to continue and 0 to quit: "))
        if c==0:
            thank(p1name,p2name,pp1,pp2)
            break
        turn=turn+1
        
play()
            
