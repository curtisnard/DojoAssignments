name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(x, y):
  new_dict = dict(zip(x,y))
  print new_dict
  return new_dict
make_dict(name, favorite_animal)
