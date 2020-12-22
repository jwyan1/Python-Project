

class Animal:
    def intro(self):
        print("There are a lot of animals.")

    def kind(self):
        print("Animals come in different shape and sizes.")


class carnivore(Animal):
    def kind(self):
        print("Carnivores eat meat.")

class herbivore(Animal):
    def kind(self):
        print("Herbivores eat veggies.")
        

obj_an = Animal()
obj_carn = carnivore()
obj_herba = herbivore()

obj_an.intro()
obj_an.kind()

obj_carn.intro()
obj_carn.kind()

obj_herba.intro()
obj_herba.kind()




    