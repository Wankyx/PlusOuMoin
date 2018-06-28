#coding:utf-8  
import random 
import os 
def integerInput(promptMessage):
    integerValueStreamInput = 0
    quit = False 

    while not quit:
        try: 
            integerValueStreamInput = int(input(promptMessage))
        except ValueError: 
            print("Please do not enter a text.")
        except KeyboardInterrupt:
            print("You quit the application.")
            exit()
        else:
            quit = True 
    return integerValueStreamInput


quit = False 
randomNumber = 0
proposition = 0
count = 0
while not quit:
    randomNumber = random.randint(0, 100)

    while proposition != randomNumber:
        proposition = integerInput("{} > ".format(count+1))
        count +=1

        if proposition < randomNumber:
            print("It's more !")
        elif proposition > randomNumber:
            print("It's less !")
        else:
            print("You win with {} try !".format(count))
        
    _quit = input("Do you want quit ? (y/N)")

    if not (_quit == ""):
        quit = True 
    else:
        count = 0




        


