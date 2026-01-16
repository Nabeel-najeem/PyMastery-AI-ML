class basic_robot:
    def __init__(self,name):
        self.name= name
        self.battery= 100
        
    def report(self):
        print(f"my name {self.name} and my battery persentage is {self.battery}%")
        

class advance_bot(basic_robot):
    def advance(self):
        print(f"{self.name} was advanced robot")
        
new_bot = advance_bot("hexer v2")

new_bot.advance()
new_bot.report()

