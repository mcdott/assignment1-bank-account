class BankAccount:
    def __init__(self, full_name, account_type, account_number, balance):
        self.full_name = full_name
        self.account_type = account_type #Stretch challenge 1
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${round(self.balance, 2)}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount} new balance: ${round(self.balance, 2)}')
        else:
            self.balance -= 10

    def get_balance(self):
        print(f'Your account balance is: ${round(self.balance, 2)}')
        return self.balance

    def add_interest(self):
        if self.account_type == 'Savings':
            interest = self.balance * 0.001
        elif self.account_type == 'Chequing':
            interest = self.balance * 0.00083

        self.balance += interest

    def print_statement(self):
        last_4_digits_of_account_number = self.account_number[4:8]
        print(f'{self.full_name} \n{self.account_type} Account No.: ****{last_4_digits_of_account_number} \nBalance: ${round(self.balance, 2)} ')

# Instantiate 3 bank accounts
investment_account = BankAccount('Mitchell Hudson', 'Savings', '03141592', 0)
chequing = BankAccount('Sam Bologna', 'Chequing','54789384', 467.92)
savings = BankAccount('Pia Singh', 'Savings', '34508962', 1673.07)

chequing.get_balance()
chequing.withdraw(50)
chequing.deposit(12.50)
chequing.get_balance()
chequing.add_interest()
chequing.print_statement()

savings.get_balance()
savings.add_interest()
savings.print_statement()

investment_account.deposit(400000)
investment_account.print_statement()
investment_account.add_interest()
investment_account.print_statement()
investment_account.withdraw(150)
investment_account.print_statement()


# Stretch challenge 2
def add_interest_to_list_of_accounts(list):
    for account in list:
     account.add_interest()

bank = [investment_account, chequing, savings]
add_interest_to_list_of_accounts(bank)
