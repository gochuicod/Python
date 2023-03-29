from random import randint

def main()->None:
    num:list = []
    count:int = 0
    guess:int = 0
    randomNumber:int = randint(0,20)

    while(True):
        if(guess == randomNumber):
            print(f"You guessed it correctly after {count} tries!")
            break
        if(guess > 20 or guess < 0):
            print("Values must positive and not greater than 20")
            count-=1
        guess = int(input("Enter a guess: "))
        print(isHighOrLow(guess,randomNumber))
        count+=1


def isHighOrLow(num1:int, num2:int)->None:
    if(num1 < num2): return "Higher"
    return "Lower"

if __name__ == "__main__": main()