import random
from colorama import Fore, Back,Style, init

init(autoreset=True)

print("               "+Fore.BLACK+ Back.WHITE+Style.BRIGHT+" Welcome To Number Guessing Game \n"+Back.RESET)
print(Fore.YELLOW+"You have to guess number between 1 to 100.")
print(Fore.YELLOW+"You have to guess in 10 chances.\n")
x='y'
while x=='y':
    target=random.randint(1,100)
    chances=10

    while chances:
        guess=int(input("Guess the number: "))
        if guess <1 or guess>100:
            print(Fore.RED+"Guess the number between 1 to 100.")
            continue
        chances-=1
        if guess==target:
            print(Fore.GREEN+Style.BRIGHT+f"Congratulations! you guess in {10-chances} chances\n")
            break
        if guess>target:
            print(Fore.MAGENTA+"Try Again! You guessed too high")
            print(Fore.MAGENTA+f"Reminaing chances: {chances}\n")
        if guess<target:
            print(Fore.MAGENTA+"Try Again! You guessed too low")
            print(Fore.MAGENTA+f"Reminaing chances: {chances}\n")

        
    else:
        print(Fore.RED+f"Better Luck Next Time! The number was {target}")
    
    x = input(Fore.CYAN+"Do you want to play again? (y/n): ").lower()


print(Fore.YELLOW+"Thanks for playing!")

