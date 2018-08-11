class BankAccount:
    def __init__(self, name, account_no, account_balance=0):
        self.name = name
        self.account_no = account_no
        self.account_balance = account_balance

    def deposit(self, my_deposit):
        # my_deposit = 20000
        self.account_balance += my_deposit
        print(self.account_balance)

    def withdrawal(self, withdrawal):
        if self.account_balance > withdrawal:
            self.account_balance -= withdrawal
            print(self.account_balance)
        else:
            print(f"Sorry, {self.name} your account balance is too low!")    
            
acc = BankAccount("savings", 101)
acc1 = BankAccount("Investment", 102)
acc.deposit(50000)
acc1.deposit(300000)
acc1.deposit(500000)
acc.withdrawal(100000)


        
        
