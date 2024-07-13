class account:
    def __init__(self, _id: str, name: str, balance: int = 0)-> None:
        self._id = _id
        self.name = name
        self.balance = balance
    def get_id(self):
        return self._id
    def get_name(self):
        return self.name
    def get_balance(self):
        return self.balance
    
    def credit(self, amount: int)->int:
        set.balance += amount
        return self.balance
    
    def debit(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return f'Amount exceeded balance {self.balance}'
    
    def transferto(self, another: str, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            another.balance += amount
            return self.balance
        else:
            return f"Amount exceeded balance: {self.balance}"
    
    def tostring(self):
        return f"Account[id = {self.get_name}, name = {self.get_name}, balance = {self.get_balance}]"
    
user1 = account(454213, "Eshmat", 15000)
user2 = account(2311412, "Toshmat", 100)