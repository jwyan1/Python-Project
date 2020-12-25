#defining parent class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunction(self):
        print("Hello my name is " + self.name + ".")
        
    def getAge(self):
        print("I am " + str(self.age))

#creating child class
class child(Person):
    def __init__(self, name, age, grade, classroom):
        super().__init__(name, age)
        self.grade = grade
        self.classroom = classroom

# polymorphism on myFunction    
    def myFunction(self):
        print("Hey there! How ya do'n?")
    
    def getGrade(self):
        print("I am in the {} grade.".format(self.grade))

#defining the second child class class
class spouse(Person):
    def __init__(self, name, age, friend, partner):
        super().__init__(name, age)
        self.friend = friend
        self.partner = partner

# polymorphism on myFunction
    def myFunction(self):  
        print("Yo! How's it going?")
        
    def getFriend(self):
        print("I am friends with {}.".format(self.friend))
 
#creating an object "Jon"       
Jon = Person("Jon", 43)
print("This guy is {} and he is {}!".format(Jon.name, Jon.age))
Jon.myFunction()
Jon.getAge()

#creating an object "Lucy"
Lucy = child("Lucy", 12, 8, "Math")
print ("\nThis girl is {} and she is {}, in Grade {}, class {}".format(Lucy.name, Lucy.age, Lucy.grade, Lucy.classroom))
Lucy.myFunction()
Lucy.getAge()
Lucy.getGrade()

#creating an object "Joan"
Joan = spouse("Joan", 39, "Trish", "Jon")
print ("\nThis woman is {}, she is {}. Her friend is {} and she is married to {}".format(Joan.name, Joan.age, Joan.friend, Joan.partner))
Joan.myFunction()
Joan.getAge()
Joan.getFriend()