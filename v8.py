class date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def get_day(self)->int:
        return self.day
    def get_month(self)->int:
        return self.month
    def get_year(self)->int:
        return self.year
    
    def set_day(self, update: int):
        self.day = update
    def set_month(self, update: int):
        self.month = update
    def set_year(self, update: int):
        self.year = update
    
    def set_date(self, new_day: int, new_month: int, new_year: int):
        self.day = new_day
        self.month = new_month
        self.year = new_year

    def tostring(self)->str:
        return f"{self.get_day():02d}/{self.get_month():02d}/{self.get_year()}"
    
birthday = date(12, 6, 2004)

print(birthday.tostring())