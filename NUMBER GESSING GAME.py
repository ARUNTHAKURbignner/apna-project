print('''
WELCOME TO THE GAME
👇👇👇
''')

import random
cnumber=random.randrange(1,1001)
userInput = int(input("ENTER THE NUMBER 👉 "))
if userInput>cnumber:
    print("COMPUTER NUMBER",cnumber)
    print("YOUR GUESS NUMBER IS TOO HIGH")
elif cnumber>userInput:
    print("COMPUTER NUMBER", cnumber)
    print("YOUR GUESS NUMBER IS TOO LOW")
else:
    print("COMPUTER NUMBER", cnumber)
    print("YOUR GUESS IS EQUAL")