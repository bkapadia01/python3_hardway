class Other(object):
    
    def override(self):
        print("other override")

    def implicit(self):
        print("other implicit")
    
    def altered(self):
        print("other altered")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("child overide")

    def altered(self):
        print("child - before other altered function")
        self.other.altered()
        print("child - after other altered function")

son = Child()

son.implicit()
son.override()
son.altered()
son.__init__(self)