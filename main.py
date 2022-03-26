from lib.categories import Category
from lib.categories import ChildCategory
from lib.character import Character
from lib.character import OtherCharacter
import lib.color
import lib.config

def clearConsole():
    print("\n\n", end="")


def selection(*choices):
    msg = ""
    for i, v in enumerate(choices):
        msg += f"[{i}] " + v.name + "\n"

    clearConsole()
    print(msg)
    while True:
        number = input("Select Action: ")
        if number.isnumeric():
            if int(number) < len(choices):
                choice = choices[int(number)]
                if len(choice.children) > 0:
                    return selection(*choice.children)
                else:
                    return choice
        print("Not a valid choice")
