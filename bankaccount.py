""" this is for acount holder and methds as deposit and withdrawal"""

class Account():

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,depositVal):
        #print("amount won and added to account initiated")
        self.balance += depositVal
        print("amount added to acount is {0:10.2f} and total amount now is {1:10.2f}".format(depositVal,self.balance))

    def withdrawal(self,withdrawVal):
        #print("amount deduction initiated")
        if withdrawVal > self.balance:
            print("ERROR ERROR ***withdrawal amount {0:10.2f} exceeds balance {1:10.2f}".format(withdrawVal,self.balance))
        else:
            self.balance -= withdrawVal
            print("amount lost {0:10.2f} and remaining balance {1:10.2f}".format(withdrawVal,self.balance))



"""acct1=Account("jose",100)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdrawal(200)
acct1.withdrawal(20)
"""
