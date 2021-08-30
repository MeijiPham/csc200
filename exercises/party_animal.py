class PartyAnimal:
  x = 0

  def party(self):
    self.x += 1
    if self.x <= 5:
      print(f'Number of occupants: {self.x} animal')
      if self.x == 5:
        print('Let\'s get this party started!')
    else:
      print('Party is full.')

an = PartyAnimal()

for i in range(6):
  an.party()