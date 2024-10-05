"""
Concept: Creating Classes
 -- 'class' keyword to create a class
 -- class name is capitalize the first letter of every word - PascalCase
 -- follow class name with semicolon
 -- All code following the class declaration must be indented
 -- NOTE: to bypass an empty class or function - use the keyword `pass`

 -- CONSTRUCTOR: the way to initialize an object with certain predefined attributes and methods
    -- Syntax: def __init__(self):
        -- the init function is a special function; it gets called everytime you create an object of that class (blueprint)
        -- it's where you initialize attributes

 -- ATTRIBUTES: what the object HAS - (basically variables that associated with a particular object)
    -- Option 1: add attributes as parameters in the constructor
        -- syntax:
            def __init__(self, user_id, username)
                self.user_id = user_id
                self.username = username
        -- this option will require every object will have to initial (set) a value for user_id and username
    -- Option 2:
        --Don't add attributes to the constructor; just set a default values for the attributes
        -- syntax:
            def __init__(self, user_id, username)
                self.user_id = user_id
                self.username = username
                self.followers = 0 <-- followers is a attribute of the class with a default value of zero
 --METHODS: what the object DOES; it performs certain functionality of the object
    -- Syntax:  def method_name(self):  <--methods always have to have `self` as the first parameter; when called it knows which object called it
"""

class User:
    #def __init__(self):
    #    print("new user being created")
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


# user1 = User() <-- no longer valid with attributes passed in the constructor
user1 = User("001","angela")

print(user1.user_id)
print(user1.username)