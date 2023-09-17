import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine

class CapuletEngineTest(unittest.TestCase):
    def engine_should_be_serviced(self):
        last_serviced_date = datetime.today().date()
        curr_mileage = 30001 
        last_service_mileage = 0
        engine = CapuletEngine(last_serviced_date,curr_mileage,last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced()) 
        

    def engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        curr_mileage = 30000
        last_service_mileage = 0 
        engine = CapuletEngine(last_service_date,curr_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced)