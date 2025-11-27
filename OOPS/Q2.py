class Account:

    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"Was Debited")
        print("Total Balance",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"Was Credited")
        print("Total Balance",self.balance)

    def get_balance(self):
        return self.balance

Acc1 = Account(10000,1234)
print("Account Balance",Acc1.balance)
print("Account No",Acc1.account_no)

Acc1.credit(500)
Acc1.debit(300)
