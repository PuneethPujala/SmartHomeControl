from smart_device import SmartDevice

class AC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temp = 24
        self.mode = "Cool"
        
    def set_temperature(self,temp):
        self.temp=temp
        print(f"Ac is set to {self.temp} degrees")
    
    def set_mode(self,mode):
        self.mode=mode
        print(f"Ac is set to {self.mode} mode")
    
    def __str__(self):
       return f"{self.name} is currently set to {self.temp} degrees and {self.mode} mode"
    

    

    