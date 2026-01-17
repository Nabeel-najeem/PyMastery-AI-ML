class tv:
    def __init__(self,brand,chanel_no=1):
        self.brand=brand
        self.power_status=False
        self.chanel_no=chanel_no
        
    def turn_on(self):
        if self.power_status == False:
            print(f"the {self.brand} tv was turned on")
            self.power_status=True
        else :
            print(f"the {self.brand} is alredy turned on")
            
    def turn_off(self):
        if self.power_status == True :
            print(f"the {self.brand} was turned off")
            self.power_status=False
        else:
            print(f" the {self.brand} is alredy turned off")
            
    def change_channel(self):
        if self.power_status == True:
            self.chanel_no=int(input("enter channel no : "))
            print(f"the channel changed to {self.chanel_no} no")
        else :
            print("please turn on the tv for change the channel")
    
    def current_channel(self):
        if self.power_status == True:
            print(f"curent channel no is {self.chanel_no} ")
        else :
            print("please turn on the tv to check which channel")
            
            
hisence=tv("hisence")
hisence.turn_on()
hisence.current_channel()
hisence.change_channel()
hisence.current_channel
hisence.turn_on()
hisence.turn_off()