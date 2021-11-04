from typing import AsyncContextManager


class bankaccount:
    balance = 0
    interest_rate = 0.01
    accounts = []

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        bankaccount.accounts.append(self)

    def deposit(self, balance):
        self.balance += balance
        return self

    def withdraw(self, balance):
        if balance <= self.balance:
            self.balance -= balance
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            print(self.display_account_info())
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.interest_rate *= self.balance
            self.balance += self.interest_rate
            return self

# accounts
savings = bankaccount(0, 0)
checking = bankaccount(0, 0)

# account activity
savings.deposit(100).deposit(240).deposit(590).withdraw(40).yeild_interest().display_account_info()
checking.deposit(200).deposit(300).withdraw(30).withdraw(200).withdraw(400).withdraw(10).yeild_interest().display_account_info()

@classmethod
def print_all_accounts(cls):
    for accounts in cls.accounts:
        accounts.display_account_info()



# user
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankaccount(0, 0.02)

    def make_deposit(self, amount):
        self.account.deposit
        return self

    def withdraw_amount(self, amount):
        self.account.withdraw
        return self

    def display_user_balance(self):
        self.account.display_account_info
        # print(f"User: {self.name}, Balance: ${self.account.display_account_info}")
        return self


# user info
john = User('John smith', 'js@mail.com')
daniel = User('Daniel roth', 'dr@mail.com')
bob = User('robert nickels', 'robnic@mail.com')

# deposit/withdraw amount
john.make_deposit(100).withdraw_amount(30).withdraw_amount(10).make_deposit(290)
daniel.make_deposit(500).make_deposit(900).withdraw_amount(190).withdraw_amount(20)
bob.make_deposit(1000).withdraw_amount(10).withdraw_amount(20).withdraw_amount(90)


# print users name and account balance
john.display_user_balance()
daniel.display_user_balance()
bob.display_user_balance()

# use __dict__ to print all of a users info(instead of having to write each instance [like, john.name ect.])
# print(john.__dict__)

