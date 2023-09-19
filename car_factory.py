from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.CarriganTires import CarriganTires
from tires.OctoprimeTires import OctoprimeTires

class CarFactory:
    #creating Calliope car
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage,last_service_mileage,tire_wear):
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tires=CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
 
    #creating Glissade car
    @staticmethod 
    def create_Glissade(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear):
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        tires=OctoprimeTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
    #creating Palindrome car - has a Sternman engine and a Spindler battery
    @staticmethod
    def create_Palindrome(current_date,last_service_date,warning_light_is_on,tire_wear):
        engine = SternmanEngine(last_service_date,warning_light_is_on)
        battery = SpindlerBattery(last_service_date,current_date)
        tires=CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car

    #creating Rorschach car - has a Willoughby engine and a Nubbin battery
    @staticmethod
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear):
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tires=OctoprimeTires(tire_wear)
        car = Car(engine,battery,tires)
        return car
    #creating Thovex car - has a Capulet Engine and a Nubbin battery
    @staticmethod
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage,tire_wear):
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        tires=CarriganTires(tire_wear)
        car = Car(engine,battery,tires)
        return car