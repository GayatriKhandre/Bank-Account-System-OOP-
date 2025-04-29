class Bank:
    Bank_name = "Reserve Bank of India"
    Bank_address = "Main Office Building, Dr. Raghavendra Road Reserve Bank Civil Square, Civil Lines, Nagpur, Maharashtra 440001"

    def __init__(self,username,pan_no,address):
        self.username = username
        self.pan_no = pan_no
        self.address = address
        self.Account_balance = 0.0
        print(f"Hello {self.username} congratulations! your account is created Successfully")

    def deposite(self,amount):
        self.Account_balance += amount
        print(f"{amount} deposited Successfully!")

    def withdraw(self,amount):
        if amount < self.Account_balance:
            self.Account_balance -= amount
            print(f"{amount} withdraw successfully!")
            print(f"Amount Balance in your account is ₹{self.Account_balance:.2f}")
        else:
            print("Insufficient Balance!")

    def mini_statement(self):
        print(f"Your account balance is {self.Account_balance}")

print(f"Welcome to {Bank.Bank_name}!")
username = input("Enter your Name: ")
pan_no = input("Enter your Pan Card Number: ")
address = input("Enter your Address: ")

b = Bank(username,pan_no,address)

while True:
    print("""Bank Account System
          
          1. Deposit
          2. Withdraw
          3. Mini Statement 
          4. Stop """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter the amount you want to deposite: "))
        b.deposite(amount)

    elif choice == 2:
        amount = float(input("Enter the amount you want to withdraw: "))
        b.withdraw(amount)

    elif choice == 3:
        b.mini_statement()

    elif choice == 4:
        print("Thank you!")
        print(f"For using {Bank.Bank_name}!")
        break

    else:
        print("Please enter valid input!")