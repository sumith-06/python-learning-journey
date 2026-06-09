balance = 0
transactions = []

def check_balance(balance):
  print(f"balance : {balance}")


def deposit(balance):
  amount = int(input("Enter amount to be deposited: "))
  if amount>0:
    balance+=amount
    print(f"sucessfully deposited. new balance = {balance}")
    return balance, amount, True
  else:
    print("Enter valid amount")
    return balance, amount, False
  

def withdraw(balance):
  amount = int(input("Enter the amount to be withdrawn: "))
  if amount<=0:
    print("Invalid amount entered")
  elif amount <= balance:
    balance-=amount
    print(f"successfully withdrawn. new balance = {balance}")
    return balance, amount, True
  else:
    print(f"Insufficient balance, balance = {balance}")
  return balance, amount, False


while True:
  print("What do you want to do?",
        "1.check balance",
        "2. Deposit",
        "3. Withdraw",
        "4. Show Transaction history",
        "5. Exit",
        sep="\n")
  operation = input("").lower()

  if operation == "exit" or operation ==  "5":
    print("Program terminated")
    break
  elif operation == "check balance" or operation == "1":
    check_balance(balance)
  elif operation == "deposit" or operation == "2":
    balance, amount, success= deposit(balance)
    if success: 
      transactions.append(f"{amount} deposited")
  elif operation == "withdraw" or operation == "3":
    balance, amount, success = withdraw(balance)
    if success:
      transactions.append(f"{amount} withdrawn")
  elif operation == "show transaction history" or operation == "4":
    if transactions:
      print("No transactions yet")
    else:
      print("Transaction history:")
      for transaction in transactions:
        print(transaction)
  else:
    print("invalid input")
