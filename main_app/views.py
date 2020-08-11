from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def experts_index (request):
    return render(request, 'experts/index.html')


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