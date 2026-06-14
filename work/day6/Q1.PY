import random 
game = random.randint(1,20)

while(True):
    guess =int(input("guess a number: "))
    if(guess<game):
        print("try a high number")
    elif(guess>game):
        print("try a lower number")
    else:
        print("you guessed it right")
        break