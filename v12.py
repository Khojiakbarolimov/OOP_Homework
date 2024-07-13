class mashina:
    def __init__(self, model: str, type: str, year: int, price: int = 4000) -> None:
        self.model = model
        self.type = type
        self.year = year
        self.price = price
    def get_info(self) ->str:
        return f"Model: {self.model}\nType: {self.type}\nYear: {self.year}\nPrice: {self.price}"
    
uzbek_gm_cars = [
    mashina("Chevrolet Captiva", 2023, 32000),
    mashina("Chevrolet Lacetti", 2023, 18000),
    mashina("Chevrolet Tracker", 2023, 25000),
    mashina("Chevrolet Gentra", 2023, 15000),
    mashina("Chevrolet Malibu", 2023, 28000),
    mashina("Chevrolet Spark", 2023, 12000),
    mashina("Chevrolet Aveo", 2023, 17000),
    mashina("Chevrolet Onix", 2023, 20000),
    mashina("Chevrolet Cobalt", 2023, 22000)
]

uzbek_gm_cars.sort(key=lambda i: i.year)

for i in uzbek_gm_cars:
    print(i.get_info())
    print("=" * 20)