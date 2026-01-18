class Ai_tools:
    def __init__(self):
        self.name="nabeel"

class EyeTracker(Ai_tools):
    def work(self):
        print("its tracking eyes")

class translator(Ai_tools):
    def work(self):
        print("its translating")
        
models=[EyeTracker(),translator()]

for m in models:
    m.work()
    