# bank-system

A bank account built four times, each version adding one concept on top of the last. The point of the repo is the progression.

| Version | What it adds |
| --- | --- |
| `bank.py` | `BankAccount` class, withdrawals, a custom `InsufficientFundsError` exception, input validation |
| `bank_v2.py` | Deposits and an in-memory, timestamped transaction history |
| `bank_v3.py` | Persistence: every transaction is written to a SQLite `transactions` table with parameterised queries |
| `bank_v4.py` | PIN protection: the PIN is stored only as a SHA-256 hash and checked before any withdrawal |

## Tech

Python · OOP · custom exceptions · sqlite3 · hashlib

## Run it

No dependencies beyond the standard library.

```
python bank_v4.py
```

Versions 3 and 4 create `bank.db` on first run.

## What I'd change for production

A plain SHA-256 hash is fast, which makes it easy to brute-force a 4-digit PIN. A real system would use a slow, salted hash such as bcrypt or argon2, and lock the account after repeated failures.
