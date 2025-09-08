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


# We can give dir() to find teh capabilities of our newly class created

print ("Type", type(an))
print ("Dir", dir(an))
print ("X", an.x)
print ("Type", type (an.party))

Type <class '__main__.PartyAnimal'>
Dir ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'party', 'x']
X 0
Type <class 'method'>
