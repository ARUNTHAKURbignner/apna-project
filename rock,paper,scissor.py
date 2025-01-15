print('''
WELCOME TO THE ADVENTURES GAME
🪨📜✂️
''')
import random
i=["rock","paper","scissr"]
'''
rock.vs.paper -> .paper.wins
rock.vs.scissor -> .rock.wins
paper vs scissor -> scissor wins.
'''


while True:
    ccount=0
    ucount=0
    uc=int(input('''
    GAME START----
    1 Yes
    2 NO / Exit
     
     '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 -> rock
2 -> paper
3 -> scissor
              '''))
            if userInput==1:
                unchoice="rock"
            elif userInput==2:
                unchoice="paper"
            elif userInput==2:
                unchoice="scissor"
            Cchoice=random.choice(1)
            if Cchoice ==uchoice:
                print("COMPUTER VALUE =>",Cchoice)
                print("USER VALUE=>",uchoice)
                print("GAME DRAW")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock"  and  cchoice=="scissor")  or  (uchoice=="paper"  and  cchoice=="rock")  or  (uchoice=="scissor"  and  cchoice=="paper"):
                print("COMPUTER VALUE =>",Cchoice)
                print("USER VALUE =>",uchoice)
                print("YOU WIN")
                ucount=ucount+1
            else:
                print("COMPUTER VALUE =>", Cchoice)
                print("USER VALUE=>", uchoice)
                print("COMPUTER WIN")
                ccount = ccount + 1

          if ucount==ccount:
              print("FINAL GAME DRAW ....")
              print("USER SCORE =>",ucount)
              print("COMPUTER SCORE =>",ccount)
          elif ucount>ccount:
              print("FINAL YOU WON THE GAME ...")
              print("USER SCORE =>",ucount)
              print("COMPUTER SCORE =>",ccount)
          else:
              print("FINAL COMPUTER WON THE GAME ...")
              print("USER SCORE =>", ucount)
              print("COMPUTER SCORE =>", ccount)





    else:
        break
