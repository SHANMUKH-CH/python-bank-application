#NAME VALIDATION STARTS----------------
def validateName(nam):
    if nam.isdigit():
        print("          Name must be only alphabet")
    elif len(nam)==0:
        print("          Field can not be blank")
    else:
        return 0
#NAME VALIDATION ENDS----------------

#ACOUNT TYPE VALIDATION STARTS----------------
def validateActTyp(typ):
    if len(typ)>1:
        print("          Please enter 'S' or 'C' only")
    elif len(typ)==0:
        print("          Field can not be blank")
    else:
        return 0
#ACOUNT NUMBER VALIDATION ENDS---------------

#DEPOSIT AMOUNT VALIDATION STARTS----------------
def validateDepAmt(amt,typ):
    if amt.isalpha():
        print("          Please enter amount in digits only",typ)
    elif len(amt)==0:
        print("          Field can not be blank")
    elif typ=='S'  and int(amt)<1000 :
        print("          Opening Balance Amt for S should not be less than 1000 ")
    elif typ=='C'  and int(amt)<5000:
        print("          Opening Balance Amt For C should not be less than 5000 ")
    else:
        return 0
#DEPOSIT AMOUNT VALIDATION ENDS---------------

#DEPOSIT VALIDATION STARTS----------------
def validateDeposit(amt):
    if amt.isalpha():
        print("          Amount must be digit only")
    elif len(amt)==0:
        print("          Field can not be blank")
    else:
        return 0
#DEPOSIT VALIDATION ENDS----------------
    
#LOGIN VALIDATION STARTS----------------
def validateLogin(act):
    if act.isalpha():
        print("          Account Num must be digit only")
    elif len(act)==0:
        print("          Field can not be blank")
    else:
        return 0
#LOGIN VALIDATION ENDS----------------


