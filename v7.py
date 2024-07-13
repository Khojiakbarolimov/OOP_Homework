class circle():
    def __init__(self, radius: int, color: str) -> None:
        self.radius = radius
        self.color = color
    def get_radius(self)->int:
        return self.radius
    def set_radius(self, amount: int):
        self.radius = amount
    def get_color(self)->str:
        return self.color
    def set_color(self, new: str):
        self.color = new
    def get_area(self):
        return 3.14 * (self.radius**2)
    def get_circumference(self)->int:
        return 2 * 3.14 * self.radius
    def get_info(self):
        return f"Radius: {self.get_radius()}\nColor: {self.get_color()}\nArea: {self.get_area():.2f}\nCircumference: {self.get_circumference():.2f}"
    
obj = circle(5, "Green")
print(obj.get_info())