class Wallet:
    def __init__(self):
        self.credit = 0
    def load(self, amount):
        self.credit += amount
    def get_credit(self):
        return self.credit
    def purchase(self, price):
        if self.credit >= price:
            self.credit -= price
            return True
        else:
            return False
        
my_wallet = Wallet()

my_wallet.load(100)
current_credit = my_wallet.get_credit()
print(f"Current credit: {current_credit}")

item_price = 50
if my_wallet.purchase(item_price):
    print(f"Purchased item for: {item_price}")
else:
    print("insufficent")

class Barrel:
    def __init__(self, capacity):
        self.capacity = capacity
    def draw(self, bottle_capacity):
        if self.capacity >= bottle_capacity:
            self.capacity -= bottle_capacity
            return bottle_capacity
        else:
            result = self.capacity
            self.capacity = 0
            return result
    
my_barrel = Barrel(100)
print(f"Barrel capacity is: {my_barrel.capacity}")

drawn_ammount = my_barrel.draw(50)
print(f"Drawn ammount: {drawn_ammount}")
print(f"Barrel capacity is: {my_barrel.capacity}")
second_ammount = my_barrel.draw(50)
print(f"Drawn ammount: {second_ammount}")
print(f"Barrel capacity is: {my_barrel.capacity}")

def first_recursive(l):
    if len(l) < 3:
        return 0
    if l[1] < l[0] and l[1] < l[2]:
        return l[1] + first_recursive(l[1:])
    else:
        return 0 + first_recursive(l[1:])
    
print(first_recursive([3,4,5,1,3,2,6]))

def second_recursive(L,K):
    if len(L) == 0:
        return L
    else:
        return [L[0] - K] + second_recursive(L[1:],K)
    
print(second_recursive([], 2))