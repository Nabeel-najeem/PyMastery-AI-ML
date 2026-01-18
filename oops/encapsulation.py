class AssistantSetting:
    def __init__(self):
        self.__volume=100
        
    def GetVolume(self):
        print(f"{self.__volume}%")
        
    def ChangeVolume(self,new_vol):
        if 0 <= new_vol <=100 :
            self.__volume=new_vol
            print(f"the volume changed to {self.__volume}%")
        else :
            print("chnage the value only between 0 to 100 %")


vol=AssistantSetting()
vol.GetVolume()
vol.ChangeVolume(int(input("enter volume between 0 to 100 : ")))