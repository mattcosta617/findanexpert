from django.db import models

# Create your models here.
class Expert:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, age, location, description):
    self.name = name
    self.age = age
    self.location = location
    self.description = description

experts = [
  Expert('Lolo', 42, 'Boston', 'CSS Master'),
  Expert('Sachi', 22, 'Kentucky', 'Javascript Wizard'),
  Expert('Raven', 31, 'Blackstone', 'Python Addict'),
]