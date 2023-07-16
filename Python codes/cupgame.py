from random import shuffle
def cupwithball():
    cup = ["","O",""]
    shuffle(cup)
    return cup

def guessfromuser():
    guess = ''
    while guess not in ["0","1","2"]:
        guess = input("Hey ! guess one no please from 0 or 1 or 2: ")

    return int(guess)

def checkguess(a,b):
    if a[b] == "O" :
        return " You are Right !!!!" 
    else:
        print(a)
        return "You are wrong "      

a = cupwithball()
b = guessfromuser()
c = checkguess(a,b)
print(c)
