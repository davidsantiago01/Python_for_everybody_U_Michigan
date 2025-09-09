class PartyAnimal:
  def __init__(self):
    self.x=0
    print ("I am constructed")

  def party(self):
    self.x = self.x+1
    print("So far", self.x)

  def __del__(self):
    print("I am destructed",self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print("an contains",an)
#the constructor and destructor are optional. The constructor is typically used to set up variables. The destructor is seldom used.
I am constructed
So far 1
So far 2
I am destructed 2
an contains 42
