from abc import ABC, abstractmethod 
class Member(ABC): 
    def join(self):
        print("I am joining up!")
          
    @abstractmethod
    def action(self): 
        pass
  
class Donor(Member): 
  
    def action(self): 
        print("I donate to campaigns.") 
  
class Fundraiser(Member): 
  
    def action(self): 
        print("I fundraise for campaigns.") 
  
class Staff(Member): 
  
    def action(self): 
        print("I use the funds.") 
  

D = Donor()
D.join()
D.action()

F = Fundraiser()
F.action()

S = Staff()
S.action()

