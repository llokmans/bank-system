from datetime import datetime

class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds in the bank account."""
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.transaction_history = []
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        self.transaction_history.append((datetime.now(), 'withdrawal', amount))
        return self.balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transaction_history.append((datetime.now(), 'deposit', amount))
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    

account = BankAccount(100)
try:
    amount = int(input("Enter amount to deposit: "))
    account.deposit(amount)
    print(f"Deposit successful. New balance: {account.balance}")
except ValueError as e:
    print(f"Error: {e}")
    
try:
    withdraw = int(input("Enter a withdrawal amount: "))
    account.withdraw(withdraw)
    print(f"Withdrawal successful. New balance: {account.balance}")
except ValueError as e:
    print(f"Error: {e}")
except InsufficientFundsError as e:
    print(f"Error: {e}")
    
for transaction in account.get_transaction_history():
    timestamp, transaction_type, amount = transaction
    print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {transaction_type} of {amount}")