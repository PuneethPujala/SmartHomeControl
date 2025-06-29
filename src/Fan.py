from smart_device import SmartDevice

class Fan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 0 
    
    def turn_on(self,speed):
        if speed < 0 or speed > 5:
            print(f"{self.name}: Invalid speed! Please set between 0 and 5.")
            return
        self.status = "ON"
        self.speed=speed
        print(f"{self.name} turned ON with speed {self.speed}")
        
    def turn_off(self):
        self.status = "OFF"
        self.speed=0
        print(f"{self.name} turned OFF")

    def set_speed(self, speed):
        if speed < 0 or speed > 5:
            print(f"{self.name}: Invalid speed! Please set between 0 and 5.")
        else:
            self.speed = speed
            print(f"{self.name} speed is set to {self.speed}")

    def __str__(self):
        return f"{self.name} is currently {self.status}, speed: {self.speed}"
