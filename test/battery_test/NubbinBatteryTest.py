import unittest
from datetime import datetime

from battery.NubbinBattery import NubbinBattery


class NubbinBatteryTest(unittest.TestCase):
    def battery_should_be_serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year-3)
        bat = NubbinBattery(last_serv_date,today)
        self.assertTrue(bat.needs_service())

    def battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_serv_date = today.replace(year=today.year-1)
        bat = NubbinBattery(last_serv_date,today)
        self.assertFalse(bat.needs_service())
    