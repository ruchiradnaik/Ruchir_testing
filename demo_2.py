class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount


account = BankAccount(500)
account.withdraw(200)
# CodeSentinal: created for you by RuchirAdnaik.