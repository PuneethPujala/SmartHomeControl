from smart_device import SmartDevice

class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 0   
        self.color = "white"  

    def turn_on(self):
        self.status = "ON"
        print(f"{self.name} turned ON")

    def turn_off(self):
        self.status = "OFF"
        print(f"{self.name} turned OFF")

    def get_status(self):
        return self.status

    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"{self.name} brightness set to {self.brightness}")

    def change_color(self, color):
        self.color = color
        print(f"{self.name} color changed to {self.color}")

    def __str__(self):
        return f"{self.name} is currently {self.status}, brightness: {self.brightness}, color: {self.color}"
