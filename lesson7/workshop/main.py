from lesson7.workshop.Athlete import Athlete
from lesson7.workshop.Student import Student
from lesson7.workshop.StudentAthlete import StudentAthlete


# Polymorphism
def introduce_person(person):
    person.introduce()


s = Student("Anna")
a = Athlete("Anna")
sa = StudentAthlete("Mike")

s.introduce()
a.introduce()
sa.introduce()

print()
print()

introduce_person(s)
introduce_person(a)
introduce_person(sa)

