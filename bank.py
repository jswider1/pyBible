# bank apparently
# reminder: self is an instance of a class, accessing its' attributes and methods
# reminder: __init__ is python method, a "constructor", allows class to
#           initialize the attributes of the class

# create new member account: J = Current("Justin", 1000)
# deposit funds: J.deposit(5000)
# check account balance: J.statement()
# withdraw: J.withdraw(400)

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, insufficient funds.")

    def statement(self):
        print("Account Balance: ${}".format(self.balance))

# Current class inherits Account class
class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)

    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)

# Savings class inherits Account class
class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
        
    def __str__(self):
        return "{}'s Savings Account: Balance ${}".format(self.name, self.balance)
