#implicit inheritace

class Parent(object):
    def override(self):
        print ("parent implicit()")

class Child(Parent):
    def override(self):
        print("child override()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
