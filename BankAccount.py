
class BankAccount:
    def __init__(self, full_name, account_type, account_number, balance = 0):
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

# Stretch challenge 3 - helper functions
def get_first_name():
    print("Thank you for opening an account at Super Bank")
    while True:
        try:
            return input("Enter your first name: ")
        except ValueError:
            print("Invalid entry")

def get_last_name():
    while True:
        try:
            return input("Enter your last name: ")
        except ValueError:
            print("Invalid entry")

def get_full_name():
    first_name = get_first_name()
    last_name = get_last_name()
    full_name = f'{first_name} {last_name}'
    return full_name

def get_account_type():
    print("Would you like a savings account or a chequing account?")
    account_type_code = ''
    while account_type_code.upper() != 'S' and account_type_code.upper() != 'C':
        account_type_code = input("Enter S for savings or C for chequing: ")

    if account_type_code.upper() == 'S':
        return 'savings'
    else:
        return 'chequing'

def generate_account_number(current_highest_account_number ):
    account_number = current_highest_account_number + 1
    return account_number


def get_initial_balance():
    while True:
        try:
            return float(input("Initial deposit amount: $"))
        except ValueError:
            print("Please enter an amount in dollars and cents ex. $43.52")
# Assignment requirement 5: Instantiate 3 bank accounts
investment_account = BankAccount('Mitchell Hudson', 'Savings', '03141592', 0)
chequing = BankAccount('Sam Bologna', 'Chequing','54789384', 467.92)
savings = BankAccount('Pia Singh', 'Savings', '34508962', 1673.07)

# Assignment requirement 6: Include example code
# chequing.get_balance()
# chequing.withdraw(50)
# chequing.deposit(12.50)
# chequing.get_balance()
# chequing.add_interest()
# chequing.print_statement()

# savings.get_balance()
# savings.add_interest()
# savings.print_statement()

# investment_account.deposit(400000)
# investment_account.print_statement()
# investment_account.add_interest()
# investment_account.print_statement()
# investment_account.withdraw(150)
# investment_account.print_statement()


# Stretch challenge 2
def add_interest_to_list_of_accounts(list):
    for account in list:
     account.add_interest()

bank = [investment_account, chequing, savings]
add_interest_to_list_of_accounts(bank)

# Stretch challenge 3
def main():
    current_highest_account_number = 60027839

    # Get information to instantiate a new BankAccount object
    full_name = get_full_name()
    account_type = get_account_type()
    account_number = generate_account_number(current_highest_account_number)
    current_highest_account_number = account_number
    initial_balance = get_initial_balance()

    print(f'{full_name} {account_type} {account_number} {initial_balance} ')
    print(current_highest_account_number)


main()



     



