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
        print(f'{self.full_name} \nAccount No.: ****{last_4_digits_of_account_number} \nBalance: ${self.balance} ')

# Instantiate 3 bank accounts
investment_account = BankAccount('Mitchell Hudson', '03141592', 0)
chequing = BankAccount('Sam Bologna', '54789384', 467.92)
savings = BankAccount('Pia Singh', '34508962', 1673.07)

chequing.get_balance()
chequing.withdraw(50)
chequing.deposit(12.50)
chequing.get_balance()

savings.get_balance()
savings.add_interest()
savings.print_statement()

investment_account.deposit(400000)
investment_account.print_statement()
investment_account.add_interest()
investment_account.print_statement()
investment_account.withdraw(150)
investment_account.print_statement()

