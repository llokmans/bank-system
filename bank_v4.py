import sqlite3
from datetime import datetime
import hashlib

DB_NAME = 'bank.db'

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL
)''')

conn.commit()
conn.close()

class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin_hash = hashlib.sha256(str(pin).encode()).hexdigest()
        
    def verify_pin(self, entered_pin):
        entered_pin_hash = hashlib.sha256(str(entered_pin).encode()).hexdigest()
        return entered_pin_hash == self.pin_hash
        
        
        
    def deposit(self, amount):
        if amount <=0:
            raise ValueError("...")
        self.balance += amount
        self._save_transaction('deposit', amount)  # save to DB
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
        self._save_transaction('withdraw', amount) # save to DB
        return self.balance
    
    def _save_transaction(self, transaction_type, amount):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transactions (timestamp, transaction_type, amount) "
            "VALUES (?, ?, ?)",
            (datetime.now().isoformat(), transaction_type, amount),
        )
        conn.commit()
        conn.close()
        
        
account = BankAccount(100, 1234)
entered = int(input("enter your PIN" ))

if account.verify_pin(entered):
    amount = int(input("Enter withdrawal amount: "))
    account.withdraw(amount)
    print(f"Withdrawal successful. New balance: {account.balance}")
else:
    print("Wrong PIN. Access denied.")