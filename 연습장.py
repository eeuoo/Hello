class Bank:
    def __init__(self):
        self.money = 0

    def deposit (self, money):
        self.money = self.money + money

    def withdraw (self, money):
        self.money = self.money - money

bank1 = Bank()

bank1.deposit(100)
bank1.withdraw(50)

print (bank1.money)

bank2 = Bank()

bank2.deposit(80)
bank2.withdraw(50)

print(bank2.money)