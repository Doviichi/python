
# oop user
class User:
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
        return self
    def withdraw_amount(self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.amount}")
        return self


# user info
john = User('John smith', 'js@mail.com', 0)
daniel = User('Daniel roth', 'dr@mail.com', 0 )
bob = User('robert nickels', 'robnic@mail.com', 0)

# deposit/withdraw amount
john.make_deposit(100)
john.make_deposit(290)
john.withdraw_amount(10)
john.withdraw_amount(30)
daniel.make_deposit(500)
daniel.make_deposit(900)
daniel.withdraw_amount(190)
daniel.withdraw_amount(20)
bob.make_deposit(1000)
bob.withdraw_amount(10)
bob.withdraw_amount(20)
bob.withdraw_amount(90)


# print(john.amount)
# print(john.name)
# print(john.email)
# print(john.display_user_balance)
john.display_user_balance()
daniel.display_user_balance()
bob.display_user_balance()


