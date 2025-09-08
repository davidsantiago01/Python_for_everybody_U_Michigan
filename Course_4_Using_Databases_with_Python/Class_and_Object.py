#class is reserved as a word that defines a template for making things
class PartyAnimal:

# when the object is constructed, a specially name method is called to allocate and intialize   attributes
  def __init__(self):
    self.x = 0
    
#each PartyAnimal has a bit of code
  def party(self) :
    self.x = self.x+1
    print ("So far", self.x)
               
#Construct a PartyAnimal object and store in an
#Tell the an object to run  the party code within it
an = PartyAnimal()
an.party()
an.party()
an.party()

So far 1
So far 2
So far 3   
