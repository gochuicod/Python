import platform, os

def main():
    while(True):
        if platform.system() == "Windows": os.system("cls")
        else: os.system("clear")

        data:int = int(input("Input: "))
        fill:str = []

        for i in range(1,data+1): fill.append(str(i)) # stores input into the array fill

        for i in range(1,data+1):
            print(" ".join(fill)) # prints stored input in string form
            fill = shift(fill) # shifts stored array input forward by one

        input("\nPress any key to continue...")


def shift(data:str): return data[1:] + data[:1]

main()