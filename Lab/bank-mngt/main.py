"""Manages Bank Account"""

class Account:
    accId=1
    def __init__(self,name,NID,balance,age) -> None:
        self.name=name
        self.nid_number=NID
        self.balance=balance
        self.age=age
        self.account_id=Account.accId
        Account.accId+=1
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount

acc1=Account('Rahim',1234,500,23)
acc2=Account('Karim',1235,1000,25)
# deposit
acc1.deposit(333)
acc2.deposit(666)
print(acc1.balance,acc2.balance)
# withdrawing
print('withraw')
acc1.withdraw(111)
acc2.withdraw(222)
print(acc1.balance,acc2.balance)

