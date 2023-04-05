import string

# Copyright (c) 2022 Alvsch

class Category:
    def __init__(self, id, name, req=""):
        self.name = str(name)
        self.id = int(id)
        self.req = req

        self.func = None

        self.children = []

    @property
    def getName(self):
        return self.name

    def addChild(self, cc):
        self.children.append(cc)
        cc.setParent(self)

    def removeChild(self, cc):
        self.children.remove(cc)

    @property
    def hasChild(self):
        if len(self.children) > 0:
            return True
        else:
            return False

    @property
    def isChild(self):
        return False

    def setFunc(self, func):
        if callable(func):
            self.func = func
        else:
            print("ERROR, Func is not a callable")
        return self

    def callFunc(self, *args):
        if callable(self.func):
            if len(args) > 0:
                return self.func(*args)
            else:
                return self.func()
        else:
            print("FUNCTION IS NOT SET/CALLABLE")
            return None


class ChildCategory:
    def __init__(self, id, name, req=""):
        self.name = str(name)
        self.id = int(id)
        self.req = req

        self.func = None

        self.parent = object
        self.children = []

    @property
    def getName(self):
        return self.name

    def addChild(self, cc):
        self.children.append(cc)
        cc = ChildCategory(cc)
        cc.setParent(self)

    def removeChild(self, cc):
        self.children.remove(cc)

    def setParent(self, pc):
        self.parent = pc

    @property
    def hasChild(self):
        if len(self.children) > 0:
            return True
        else:
            return False

    @property
    def isChild(self):
        return True

    def setFunc(self, func):
        if callable(func):
            self.func = func
        else:
            print("ERROR, Func is not a callable")
        return self

    def callFunc(self, *args):
        if callable(self.func):
            if len(args) > 0:
                return self.func(*args)
            else:
                return self.func()
        else:
            print("FUNCTION IS NOT SET/CALLABLE")
            return None


def clearConsole():
    print("\n\n", end="")


def selection(*tuple_choices):
    choices = list(tuple_choices)
    msg = ""
    index = 0
    for i, v in enumerate(choices):
        # Requirement Test
        if v.req != "":
            req = ""
            for x in v.req.split(" "):
                if x[0] in string.ascii_letters + "_":
                    req += "\"" + x + "\""
                else:
                    req += x
            if not eval(req):
                choices.pop(index)

        msg += f"[{index}] " + choices[index].name + "\n"
        index += 1
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
