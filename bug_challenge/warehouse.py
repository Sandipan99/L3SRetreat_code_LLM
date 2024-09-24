class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if amount > self.balance or (self.balance - amount) < 10:  
            print(f"Withdrawal of ${amount:.2f} denied. Insufficient funds.")
            return False
        
        self.balance -= amount
        print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

if __name__ == "__main__":
    account = BankAccount("123456")
    
    # Test deposit
    account.deposit(100)
    
    # Test withdrawals
    account.withdraw(50)   # Should succeed
    account.check_balance() # Should be $50
    
    account.withdraw(45)   
    account.check_balance() # Should be $5
    
    account.withdraw(40)   # Should deny
    account.check_balance() # Should be $5
    
    account.withdraw(30)   # Should deny
    account.check_balance() # Should be $5
