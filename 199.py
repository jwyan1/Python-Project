


# Question: while digging for how this would work i stumbled onto "super". to my understanding
# what is happening is by calling super it is allowing donor to basically connect to
# the above parent class. I am a little uncertain why this would be necessary as i figured it
# would implicitly do so but I can't call on "d1" without using super()


#defining the parent class as 'member' we give it's attributes
class member:    
    def __init__(self, fName, mName, lName, idNumber):
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.idNumber = idNumber

#defining the first child class we add donoTotal & occupation, then the parent class
#attributes
class donor(member):
    def __init__(self,donoTotal, occupation, fName, mName, lName, idNumber):
        self.donoTotal = donoTotal
        self.occupation = occupation
        super(donor, self).__init__(fName, mName, lName, idNumber) 


class volunteer(member):
    def __init__(self, helpHours, project, fName, mName, lName, idNumber):
        self.helpHours = helpHours
        self.project = project
        super(volunteer, self).__init__(fName, mName, lName, idNumber)




#creating an instance of the member class and using .format for a sentence. 
m1 = member("John","L","Lewis",1)
print ("Our first member is {} {}. His id is {}.".format(m1.fName,m1.lName,m1.idNumber))

#creating an instance of the donor class and using .format for a sentence. 
d1 = donor(500, "Dentist", "Bill", "W", "Wilbur", 2)
print ("Our first donor is {} {} {}, id # {}, his total is {} and he works as {}.".format(d1.fName,d1.mName,d1.lName,d1.idNumber,\
                                                                                          d1.donoTotal, d1.occupation))
#creating a volunteer instance.
v1 = volunteer(10, "Park Cleaning", "Suzy", "Q", "Davis", 3)
print ("Our first volunteer is {} {}, who helped on {} for {} hours!".format(v1.fName,v1.lName, v1.project, v1.helpHours))


