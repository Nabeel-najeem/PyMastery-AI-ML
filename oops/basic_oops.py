class basic_robot:
    def __init__(self,name):
        self.name= name
        self.battery= 100
        
    def report(self):
        print(f"my name {self.name} and my battery persentage is {self.battery}%")
        
my_bot= basic_robot("hexer v-1")
my_bot.report()