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

    def get_balance(self):
        print(f'Your account balance is: ${self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        last_4_digits_of_account_number = self.account_number[4:8]
        print(f'{self.full_name} \nAccount No.: ****{last_4_digits_of_account_number} \nBalance: {self.balance} ')