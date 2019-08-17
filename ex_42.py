#animal is object type - sorta
class animal(object):
    pass

## dog is-a animal
class dog(animal):    
    def __init__(self, name):
        #dog has-a name
        self.name = name

## cat is-a animal
class cat(animal):
    def __init__(self, name):
        #cat has-a name
        self.name = name

## person is-a object
class person(object):
    def __init__(self, name):
        #person has-a name
        self.name = name
        ## person has-a pet of some kind
        self.pet = None

## employee is-a person
class employee(person):
    def __init__ (self, name, salary):
        ## ?? hm whas is this strange maigc? 
        ## this runs the __init__ mehtod of the parent class reliably 
        super(employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is-a object
class fish(object):
    pass

## salmon is-a fish
class salmon(fish):
    pass

## halibut is-a fish
class halibut(fish):
    pass

## rover is-a dog
rover = dog("rover")

## stan is-a cat
satan = cat("satan")

## mary is-a person
mary = person("mary")

## mary has-a pet named satan
mary.pet = satan
## frank is-a employee with 120000 salary
frank = employee("frank", 1200000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
#flipper is-a instance of fish
flipper = fish()

## crouse is-a salmon
# crouse is-a instance of salmon
crouse = salmon()

## harry is-a halibut
# harry is-a instance of halibut
harry = halibut()

#    "class %%%{%%%}:":
#         "make a clase named %%% that is a %%%",
#     "class %%%(object):\n\tdef __init__(self, ***)":
#         "class %%% has a __init__ that takes self and *** params:",
#     "class %%%(object):\n\tdef ***(self, @@@)":
#         "class %%% has a function *** that takes self and @@@ params:",
#     "*** = %%%()":
#         "set *** to an instance of class %%%",
#     "***.***(@@@)":
#         "from *** get the *** function, call it with the params self and @@@",
#     "***.*** = '***'":
#         "from *** get the *** attributes and set it to '***'"



