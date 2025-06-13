from smart_device import SmartDevice

class SecurityCamera(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
    
    def start_recording(self):
        self.is_recording = True
        print(f"{self.name} started recording...")

    def stop_recording(self):
        self.is_recording = False
        print(f"{self.name} stopped recording.")

    def rotate_camera(self):
        print(f"{self.name} is rotating...")

    def __str__(self):
        if self.is_recording:
            rec_status = "recording"  
        else:
            rec_status = "not recording"
        return f"{self.name} is currently {self.status} and {rec_status}"

    
    


    

    