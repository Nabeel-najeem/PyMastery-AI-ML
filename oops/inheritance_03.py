class project:
    def __init__(self,project_name):
        self.project=project_name
        self.developer="nabeel"
        
class PaidProject(project):
    def __init__(self, project_name,price):
        super().__init__(project_name)
        self.price=price
        
    def invoice(self):
        print(f"{self.project} was {self.price} RS and developed by {self.developer}")
        
eye_mouse=PaidProject("eye controlled mouse ",7500)
eye_mouse.invoice()

jarvis=PaidProject("jarvis",12500)
jarvis.invoice()