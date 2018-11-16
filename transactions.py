from validation import *
from dbServices import *
#MAIN MENU STARTS--------------------
def  transMenu( ):
    print("          ======RANSACTION MENU============")
    print("                1... Deposit")
    print("                2... Withdraw ")
    print("                3... Balance Enquiry")
    print("                4... Logout")
    print("          ==================================")
    c=int(input("          Enter Your Choice...."))
    return c
#MAIN MENU ENDS--------------------

#LOGIN FOR TRANSACTION STARTS--------------------
def  transLogin( ):
    while 1:
            act=input("          Enter your Account Num: ")
            x=validateLogin(act)
            if x==0:
                y=tranLogin(act)
                if y==0:
                    
                    break
    return act
    #print("          Welcome : Name...")    
    
#LOGIN FOR TRANSACTION ENDS--------------------
