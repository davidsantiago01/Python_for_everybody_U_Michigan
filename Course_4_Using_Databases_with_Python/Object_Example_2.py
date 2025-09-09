#Constructors can have additional parameters. These can be used to set up instance variables for teh particular instance of the class (i.e. for a particular object) 
class  PartyAnimal:
    def __init__ (self, z):
        self.x = 0
        self.name = z
        print (self.name, "constructed")

    def party (self):
        self.x = self.x+1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()
j = PartyAnimal("Jim")

j.party()
s.party()

Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Sally party count 2
