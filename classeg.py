class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)

account = BankAccount("Pari", 5000)

account.deposit(1000)
account.withdraw(700)

account.display()