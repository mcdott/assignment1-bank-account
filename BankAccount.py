class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount} new balance: ${self.balance}')
        else:
            self.balance -= 10

    