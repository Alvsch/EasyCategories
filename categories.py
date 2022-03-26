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

    def removeChild(self, cc):
        self.children.remove(cc)

    def setParent(self, parent):
        self.parent = parent

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

    def callFunc(self, *args):
        if callable(self.func):
            if len(args) > 0:
                return self.func(*args)
            else:
                return self.func()
        else:
            print("FUNCTION IS NOT SET/CALLABLE")
            return None
