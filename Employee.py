class Person:
    
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
        
class Employee (Person):
    
    def __init__(self, name, idnumber, salary, post):
        
        self.salary = salary
        self.post = post
        Person. __init__(self, name, idnumber)
        
        
a = Employee ("Rahul", 88612, 2000000, "Intern")

a.display()
    
        