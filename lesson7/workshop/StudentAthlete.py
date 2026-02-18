from lesson7.workshop.Athlete import Athlete
from lesson7.workshop.Student import Student


# Child class
class StudentAthlete(Student, Athlete):  # Inheritance from multiple classes


def __init__(self, name):


# Student.__init__(self, name)
super().__init__(name)  # Executing constructor from parent class


def introduce(self):
    print(f"I'm {self.name}, and I'm both a student and an athlete!")

