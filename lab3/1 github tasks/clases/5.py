"""Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance. Instantiate your class, 
make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    pass
"""

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} made. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. New balance is {self.balance}.")

    # Method to display account information
    def __str__(self):
        return f"My Account: {self.owner}\nAccount balance: {self.balance}"

# Example usage
acc = Account("Liza", 1000)

print(acc)  # Displays account owner and initial balance

# Making deposits
acc.deposit(500)  # Adds 500 to the balance
acc.deposit(200)  # Adds 200 to the balance

# Making withdrawals
acc.withdraw(300)  # Withdraws 300
acc.withdraw(1500) # Tries to withdraw more than available balance (should fail)

# Trying to overdraw the account
acc.withdraw(2000)  # Insufficient funds

# Print final account details
print(acc)
