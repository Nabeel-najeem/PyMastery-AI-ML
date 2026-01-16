class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def new_student(self):
        print(f"Name : {self.name} \n age : {self.age}")

        
        
class details(student):
    def details(self):
        print(f"Name : {self.name}\nAge : {self.age}")
        
        
        
        
        
        
        
student01=details(name="Nabeel",age=20)
student01.details()