class Pet :
    def __init__ (self,name,age,rasa) :
        self.age = age
        self.name = name
        self.rasa = rasa

        def names(name):
            print(f"the name of dog is {name}")
        self.names = names(name)
tofik = Pet("Tofik",21,"Bullterier")
tofik.names
