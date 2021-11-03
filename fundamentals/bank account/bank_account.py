class bankaccount:
    balance = 0
    interest_rate = 0.01
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
    def deposit(self, balance):
        self.balance += balance
        return self
    def withdraw(self, balance):
        # self.balance -= balance
        if balance <= self.balance:
            self.balance -= balance
        elif balance > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
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
dan = bankaccount(1090, 0.05)
sam = bankaccount(12800, 0.09)

# account activity
dan.deposit(100).deposit(240).deposit(590).withdraw(40).yeild_interest().display_account_info()
sam.deposit(200).deposit(300).withdraw(30).withdraw(200).withdraw(400).withdraw(10).yeild_interest().display_account_info()

