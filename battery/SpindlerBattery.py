from battery.battery import Battery
from datetime import datetime,date

class SpindlerBattery(Battery):
    def __init__(self,last_service_date,current_date):
     super().__init__(last_service_date)
     self.current_date = current_date
    
    def needs_service(self):
        try:
            date_of_expected_service = self.last_service_date.replace(year=self.last_service_Date.year+4)
        except ValueError:
            #preserving calendar day (if feb 29th does not exist, set to 28th)
            date_of_expected_service = self.last_service_date.replace(year=self.last_service_Date.year+4,day=28)
        return True if date_of_expected_service < self.current_date else False
       
       
