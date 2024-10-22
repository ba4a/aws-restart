import random
number = random.randint(1,10)
print(number)
isGuessRight = False
while isGuessRight != False :
    guess=input("guess number between 1 : 10")
    if guess == number:
        print("you guess right")
        isGuessRight = True
    else :
        print("you guess wrong")


