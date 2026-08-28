class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.balance -= amount
        return self.balance
    
account_balance = BankAccount(100)
try:
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw <= 0:
        raise ValueError("Must be a number from 1 and")
    account_balance.withdraw(withdraw)
    
    print(f"Withdrawal successful. New balance: {account_balance.balance}")
except ValueError as e:
    print(f"Error: {e}")
except InsufficientFundsError as e:
    print(f"Error: {e}")