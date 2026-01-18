class project:
    def __init__(self,project_name):
        self.project=project_name
        self.developer="nabeel"
        
    def show_info(self):
        print(f"{self.project} develped by {self.developer}")
    
class eye_controlled_mouse(project):
    def is_completed(self):
        print("this project was completed ")
        
class Jarvis(project):
    def is_completd(self):
        print("the project was not complted")
        
        
eye_cont=eye_controlled_mouse("vision x")
eye_cont.is_completed()
eye_cont.show_info()

jarvis_ai=Jarvis("jarvis")
jarvis_ai.is_completd()
jarvis_ai.show_info()