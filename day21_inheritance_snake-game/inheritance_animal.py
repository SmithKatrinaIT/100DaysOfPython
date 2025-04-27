"""
Concepts: Class inheritance
 -- Class that are related. Inheriting class attributes and methods from a generic class to a more specific class
 -- Establish Class Inheritance
    -- The class to be inherited goes in parenthesis after the class declaration
        class Fish(Animal) <-- Fish class is inheriting from the Animal class
    -- [Recommended by not strictly required] Call the 'super().__init__() method in the sub-class (inheriting class) constructor
        -- def __init__(self):
               super().__init__()
"""




class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")



class Fish(Animal):
    def __init__(self):
        super().__init__() #not strickly required; but best practice

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe() # because of inheritance; able to call the breath method on the Fish object


