from mainmenu import *
from validation import *
from dbServices import *
from transactions import *


Nam=""
Typ=""
Amt=""
mt=0
amt=0
acctNo=0
while 1:
    ch=displayMenu()
    if ch==1:#FOR New User
        while 1:
            nam=input("          Enter account holder name:")
            x=validateName(nam)
            if x==0:
                Nam=nam
                break
        while 1:
            typ=input("          Enter account type ('S' for Savings / 'C' for Current):")
            x=validateActTyp(typ)
            if x==0:
                Typ=typ
                break
        while 1:
            amt=input("          Enter the opening balance (in rupees): ")
            x=validateDepAmt(amt,Typ)
            if x==0:
                Amt=amt
                break
        defDbase()
        act=getNextActNo()
        insertDetails(act,Nam,Typ,Amt)#pass to DB
        acctDetails(act)

    elif ch==2:
        
        while 1:
            acctNo=transLogin( )
            while 1:
                ch=transMenu()
                if ch==1:
                    while 1:
                        amt=input("          Enter the deposit Amount (in rupees): ")
                        x=validateDeposit(amt)
                        if x==0:
                            Amt=amt#pass to DB
                            mt=getBal(acctNo)
                            print("          Curren balance is ",mt)
                            updateDeposit(acctNo,amt)
                            mt=getBal(acctNo)
                            print("          Amount Deposited suuccessfuly Curren balance is ",mt)
                            break
                    #Amt=getBal(acctNo)
                    #print("          Amount Deposited suuccessfuly Curren balance is ",Amt)
                if ch==2:
                    while 1:
                        print("          Curren balance is.... ")
                        amt=input("          Enter the withdrawel amount (in rupees): ")
                        x=validateDeposit(amt)
                        if x==0:
                            Amt=amt#pass to DB
                            mt=getBal(acctNo)
                            print("          Curren balance is ",mt)
                            withDrawAmt(acctNo,amt)
                            mt=getBal(acctNo)
                            print("          Amount Withdrawn suuccessfuly Curren balance is ",mt)
                            break
                    
                if ch==3:
                    x=getBal(acctNo)
                    print("          Balance is.. ",x)
                if ch==4:
                    print("          Bye")
                    break
            break
                
                    
    elif ch==3:
        defDbase()
        act=input("          Enter your Account Num: ")
        x=validateLogin(act)
        if x==0:
            delAcct(act);
            print("          Account Deleted")
                
        
                
    elif ch==4:
        defDbase()
        actDetails()#pass to DB
        print("          Finished")
        break
    else :
        print("          Invalid choice, Please enter only 1 2 or 3 only")
        print("          ...")
        print("          ...")
