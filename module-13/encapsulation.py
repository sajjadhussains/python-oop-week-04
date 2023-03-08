# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.

class Account:
    def __init__(self,holder,balance,account_number) -> None:
        self.holder = holder
        self.account_number = account_number #__is private in python and single underscore is protected and by default other is publilc
        self.__balance = balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    @property
    def get_balance(self):
        return self.__balance
class StudentAccount(Account):
    def __init__(self, holder, balance, account_number,school) -> None:
        self.school=school
        super().__init__(holder, balance, account_number)

rafsan = StudentAccount('rafsan',50000,165,'KZS')
rafsan.deposit(2000)
rafsan.deposit(3000)
rafsan.deposit(2000)
print(rafsan.get_balance)