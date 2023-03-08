class Account:
    def __init__(self,holder,account_number,balance) -> None:
        self.holder = holder
        self.account_number = account_number
        self.__balance = balance
    def withdraw(self,amount):
        self.__balance+=amount
    def deposit(self,amount):
        self.__balance -=amount
    def get_balance(self):
        return self.__balance    
class StudentAccount(Account):
    def __init__(self, holder, account_number, balance,school) -> None:
        self.school=school
        super().__init__(holder, account_number, balance)
    
hatim = StudentAccount('hatim',123,100000,'ulb')
# print(hatim.__balance)
# print(dir(hatim))
print(hatim._Account__balance)