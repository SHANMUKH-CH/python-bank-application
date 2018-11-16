from mainmenu import *
from validation import *
from dbServices import *


#MAIN PROGRAMM
Nam=""
Typ=""
Amt=""
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
        acctDetails(Nam,Typ,Amt)

    elif ch==2:
        print("          This is UserDeatail")
    elif ch==3:
        print("          Finished")
        break
    else :
        print("          Invalid choice, Please enter only 1 2 or 3 only")
        print("          ...")
        print("          ...")
