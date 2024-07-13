class time:
    def __init__(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_hour(self)->int:
        return self.hour
    def get_minute(self)->int:
        return self.minute
    def get_second(self)->int:
        return self.second

    def set_hour(self, hour)->None:
        self.hour = hour
    def set_minute(self, minute)->None:
        self.minute = minute
    def set_second(self, second)->None:
        self.second = second
    def set_time(self, hour: int, minute: int, second: int) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def tostring(self)->str:
        return f"{self.get_hour():02d}:{self.get_minute():02d}:{self.get_second():02d}"

    def nextsecond(self) -> None:
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.hour = 0

    def previoussecond(self) -> None:
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.minute -= 1
            if self.minute < 0:
                self.minute = 59
                self.hour -= 1
                if self.hour < 0:
                    self.hour = 23
    
arrival = time(12, 42, 13)
print(arrival.tostring())