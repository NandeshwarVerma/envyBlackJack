from bankaccount import *
def usercred():
    global acct1
    name=input("what is your name ")
    print("Welcome ***{}***".format(name))
    acct1=Account(name,0)
    userAction()
def userAction():
    inp=input("what do you want to do . choose 1 for Withdraw and 2 for deposit and 0 to exit")
    if int(inp)==1:
        print("you have chosen withdrawal")
        wa=float(input("how much you want to withdraw?"))
        acct1.withdrawal(wa)
        usercont()
    elif int(inp)==2:
        print("you have chosen deposit")
        da=float(input("how much you want to deposit?"))
        acct1.deposit(da)
        usercont()
    elif int(inp)==0:
        print("thanks for using . GOOD BYE!")
        exit
    else:
        print("wrong input. choose from 1 or 2 or 0")
        userAction()
def usercont():
    check=input("Do you want to continue Y or N? ")
    if check.lower()=='y':
        userAction()
    else:
        print("HAVE A NICE DAY {}")
        exit
def main():
    global name
    print("welcome to the bank account ")
    usercred()

main()
