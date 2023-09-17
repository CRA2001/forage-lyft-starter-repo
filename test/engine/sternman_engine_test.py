import unittest
from datetime import datetime

from engine.sternman_engine import SternmanEngine

class SternmanEngineTest(unittest.TestCase):
    def engine_should_be_serviced(self):
        last_serviced_date = datetime.today().date()
        warning_light_is_on = True
        engine = SternmanEngine(last_serviced_date,warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced()) 
        

    def engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date,warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced)