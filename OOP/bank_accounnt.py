"""
Practice Problem: Bank Account System

Concepts Practiced:
- Classes and Objects
- Attributes
- Methods
- self keyword
- Methods with parameters
- Modifying object state

This program simulates basic banking operations such as
depositing money, withdrawing money, and checking account balance.
"""


class BankAccount:

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposited {amount}")

  def withdraw(self, amount):
    self.balance -= amount
    print(f"Withdrawn : {amount}")
  
  def check_balance(self):
    print(f"Balance : {self.balance}")

account = BankAccount()

account.account_holder = "sumith"
account.balance = 0

account.check_balance()
account.deposit(1000)
account.withdraw(300)
account.check_balance()

#Output:
# Balance : 0
# Deposited 1000
# Withdrawn : 300
# Balance : 700