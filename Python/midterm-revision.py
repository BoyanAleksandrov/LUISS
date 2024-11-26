class Wallet:
    def __init__(self):
        self.credit = 0
    def load(self, amount):
        self.credit += amount
    def get_credit(self):
        return self.credit
    def purchase(self, price):
        if self.balance >= price:
            self.credit -= price
            return True
        else:
            return False
        

        
class Barrel:
    def __init__(self, capacity):
        self.capacity = capacity
    def draw(self, bottle_capacity):
        if self.capacity >= bottle_capacity:
            self.capacity -= bottle_capacity
        else:
            result = self.capacity
            self.capacity = 0
            return result
    