# class SampleClass:
#     def sampleMethod(self):
#         print("this method is created to demonstrate methods in class")

# print(SampleClass.sampleMethod(None))
# obj1=SampleClass()
# obj1.sampleMethod()

class BankAccount:
    def __init__(self,accountNo,accountName,ifscCode,balance) -> None:
        self.accountNo=accountNo
        self.accountName=accountName
        self.ifscCode=ifscCode
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
    def checkBalance(self):
        print(self.balance)
        
obj1=BankAccount(1234,'Dhoni','ABC1234',10000)
obj2=BankAccount(3456,'Virat','MN1223',12000) 
print(obj1.accountName)
print(obj2.accountName)


obj1.checkBalance()
obj1.deposit(2000)
obj1.checkBalance()
obj1.withdraw(1000)
obj1.checkBalance()
print('Bal:')
print(BankAccount.checkBalance(obj1))