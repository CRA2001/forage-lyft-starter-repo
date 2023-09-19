from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear

    #Tires should be serviced only when the sum of all values in tire wear arr is >= 3
    #get sum of arr
    #checking if sum is >= 3
    def needs_service(self):
        return True if sum(self.tire_wear) else False 