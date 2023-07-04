#A Python program to create an Emp class with employee details as instance variables.
#Emp Class - Save this as Emp.py
class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
        
    def display(self):
        print("{:5d} {:20s} {:10.2f}".format(self.id, self.name, self.sal))