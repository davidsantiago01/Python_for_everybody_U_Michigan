
class  PartyAnimal:
    def __init__ (self, nam):
        self.x = 0
        self.name = nam
        print (self.name, "constructed")

    def party (self):
        self.x = self.x+1
        print(self.name, "party count", self.x)

#FotballFan is a class which extends PartyAnimal, it has all the capabilities of PartyAnimal and more.
class FootballFan (PartyAnimal):

  def __init__ (self, nam):
    super().__init__(nam)
    self.points = 0

  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print(self.name, "points", self.points)
    
s = PartyAnimal("Sally")
s.party()
j = FootballFan("Jim")
j.party()
j.touchdown()

Sally constructed
Sally party count 1
Jim constructed
Jim party count 1
Jim party count 2
Jim points 7
