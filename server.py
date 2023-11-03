class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        print(f"You have deposited: ${amount}")
        self.balance += amount
        return self

    def withdraw(self, amount):
        print(f"You Withdrew: ${amount}")
        if (self.balance < amount):
            print("Insufficient Funds... Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Your Balance is: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.05, balance=0)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(f" {self.name} has a balance of {self.balance}.")

    def make_deposit(self, amount):
        self.account.deposit(amount)

