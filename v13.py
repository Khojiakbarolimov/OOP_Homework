class book:
    def __init__(self, name: str, pagecount: int, price: float) -> None:
        self.name = name
        self.pagecount = pagecount
        self.price = price
    
    def increase_page(self)->None:
        self.pagecount += 10

    def increase_price(self)->None:
        if self.pagecount > 100:
            self.price //= 2
    
    def get_info(self)->str:
        return f"Kitob nomi: {self.name}\nKitob sahifalari soni: {self.pagecount}\nKitobning narxi: ${self.price:.2f}"
    
books = [
    book("Introduction to Machine Learning", 110, 49.99),
    book("Data Structures and Algorithms", 120, 44.99),
    book("Web Development with Django", 95, 34.99),
    book("Artificial Intelligence Basics", 80, 29.99),
    book("Python Programming", 70, 39.99)
]