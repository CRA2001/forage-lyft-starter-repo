from tires.tires import Tires 

class CarriganTires(Tires):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear

    #Carrigan tires should be serviced only when one or more of the values in the tire
    #wear array is greater than or equal to 0.9
    def needs_servicing(self):
        for t in self.tire_wear:
            if t >= 0.9:
                return True
        return False