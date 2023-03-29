"""
    NAME: Darelle Gochuico
    IDNO: 20259388
"""

from os import system
from sys import exit
import platform

def main():
    while(True):
        if platform.system() == "Windows": system("cls")
        else: system("clear")

        print("----- MAIN MENU -----\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n0. Quit/End\n---------------------")

        try:
            selection:int = int(input("Enter Option(0..4): "))
            
            if selection > 0 and selection < 5:
                num1:int = int(input("\nEnter number 1: "))
                num2:int = int(input("Enter number 2: "))
                if (num1 > -1 and num1 < 101) or (num2 > -1 and num2 < 101): choices(num1,num2,selection)
            else:
                print("\nProgram Terminated")
                break
        except:
            print("\nOnly accepts integers!")
            
        prompt()
        
def addition(num1:int, num2:int): return num1+num2
def subtraction(num1:int, num2:int): return num1-num2
def multiplication(num1:int, num2:int): return num1*num2
def division(num1:int, num2:int): return num1/num2
def prompt(): input("\nPress any key to continue...")

def choices(num1,num2,selection):
    if selection == 1: print(f"\nThe sum of {num1} and {num2} is {addition(num1,num2)}")
    elif selection == 2: print(f"\nThe difference of {num1} and {num2} is {subtraction(num1,num2)}")
    elif selection == 3: print(f"\nThe product of {num1} and {num2} is {multiplication(num1,num2)}")
    elif selection == 4: print(f"\nThe quotient of {num1} and {num2} is {division(num1,num2)}")

main()