class employee:
    def __init__(self, _id: int, fname: str, lname: str, salary: int) -> None:
        self.id = _id
        self.firstname = fname
        self.lastname = lname
        self.salary = salary

    def get_id(self)->int:
        return self.id
    def get_firtsname(self)->int:
        return self.firstname
    def get_lastname(self)->int:
        return self.lastname
    def get_name(self)->int:
        return f"{self.firstname} {self.lastname}"
    def get_salary(self)->int:
        return self.salary

    def set_salary(self, salary: int):
        self.salary = salary
    
    def get_annualsalary(self):
        return self.salary * 12
    
    def raise_salary(self, percent: float)->int:
        self.salary += int((self.salary * (percent / 100)))
    
    def tostring(self)->str:
        return f"Employee[id = {self.get_id()}, name = {self.firstname} {self.lastname}, salary = {self.get_salary()}]"
    
worker = employee(31421, "Hojiakbar", "Olimov", 5000)
worker.raise_salary(20)
print(worker.tostring())