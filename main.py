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


def view_stats(*args):
    global you
    print(f"""
        Name: {you.firstname} {you.lastname}
        Age: {you.age}
    
        Happiness: {you.happiness}
        Health: {you.health}
        Smart: {you.smart}
        """)

    print("Jobs: ")
    for i in you.jobs:
        print(i)

    print("Educations: ")
    for i in you.edu:
        print(i)

def view_relations(*args):
    print(args)
    global you
    print(f"""
        {lib.color.underline}PARENTS:{lib.color.reset}
         - {you.parents[0].firstname} {you.parents[0].lastname}
         - Likeness: {you.parents[0].likeness}

         - {you.parents[1].firstname} {you.parents[0].lastname}
         - Likeness: {you.parents[1].likeness}
         
        {lib.color.underline}FRIENDS:{lib.color.reset}
    """)
    for i in you.friends:
        print(f" - {i}")


def do_activity(*args):
    # Create Categories
    c0 = Category(0, "Walk a walk")
    c1 = Category(1, "Read a book")
    c2 = Category(2, "Play Video Games")
    # Add Functions
    c0.setFunc(walk)
    c1.setFunc(read)
    c2.setFunc(games)

    selection(c0, c1, c2).callFunc()

def walk():
    print("You took a walk")
def read():
    print(f"You read the book \"{lib.config.random_entry(lib.config.books)}\"")
def games():
    print(f"You played the game \"{lib.config.random_entry(lib.config.games)}\"")


def job_edu(*args):
    pass


# Define Your Character
first = input("Choose a first name: ").strip().title()
last = input("Choose a last name: ").strip().title()

you = Character(first, last)

# Define Your Parents
parent1 = OtherCharacter("Mom", last, "parent")
you.addParent(parent1)
parent2 = OtherCharacter("Dad", last, "parent")
you.addParent(parent2)

# Create Categories
c0 = Category(0, "View Stats")
c1 = Category(1, "View Relations")
c2 = Category(2, "Do Activities")
c3 = Category(3, "Job/Education")
c4 = Category(4, "Surrender")

# Set Category Functions
c0.setFunc(view_stats)
c1.setFunc(view_relations)
# c2.setFunc()
# c3.setFunc()
c4.setFunc(lambda: exit())


while True:
    selection(c0, c1, c2, c3, c4).callFunc()
