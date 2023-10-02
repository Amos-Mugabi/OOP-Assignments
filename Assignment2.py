# Write a python program that creates a class called Person which contains Name, Sex and Profession as states (attributes) and working, study and leave as its behaviours. 
# Demonstrate with examples the use of classes and objects.

class Person:
    def __init__(self, name, sex, profession):
        self.Name = name
        self.Sex = sex
        self.Profession = profession

    def working(self):
        return f"{self.Name} is working as  an {self.Profession}" 
    def study(self):
        return f"{self.Name} is studying."
    def leave(self):
        return f"{self.Name} is on leave."


Persona = Person("Amos", "Male", "Engineer")
Personb = Person("Tom", "Male", "Doctor")


print(Personb.study())
print(Persona.working())

