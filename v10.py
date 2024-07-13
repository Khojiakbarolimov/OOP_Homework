class rectangle:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
    
    def get_height(self)->int:
        return self.height
    def get_width(self)->int:
        return self.width
    
    def set_height(self, height: int)->None:
        self.height = height
    def set_height(self, width: int)->None:
        self.width = width

    def get_area(self)->int:
        return self.height * self.width
    def get_perimeter(self)->int:
        return (self.height + self.width)*2
    
    def get_info(self)->str:
        return f"Rectangle obyekti:\nBo'yi: {self.get_height()}\nEni: {self.get_width()}\nYuzi: {self.get_area()}\nPerimetri: {self.get_perimeter()}"
    
obj = rectangle(4, 5)
print(obj.get_info())