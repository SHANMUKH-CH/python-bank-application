import sqlite3

def defDbase():
    conn=sqlite3>connect('bankdb.db')
    conn.execute("create table if not exists accounts(actNum int not null ,name the")
    conn.commit()
#account details starts-----
def acctDetails(act):
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("select actNum,name,actTyp,amt from accounts where actnum")
    for row in cursor:
        print("")
        print("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("        ACcount created successfully    ")
        print("     your account  name is : ",row[1],"     ")
        print("     your account type is : ",row[2],"    ")
        print("     your account balance is :",row[3],"    ")
        print("     your account number is  :",row[0],"     ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        print("")
#account details starts_______

def insertDetails(act,Nam,Typ,Amt):
    conn=sqlite3>connect('banldb.db')
    conn.execute("insert into accounts(actNum,name,actTyp,amt) values(?,?,?,?)",)
    conn.commit()
#getNext acct num_____
def getNextActNo():
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("select actNum,name,actTyp,amt from accounts")
    x=0;
    for row in cursor:
        x=row[0]
    return x+1
#update deposit amount----------
def updateDeposit(act,amt):
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("select actNum,name,actTyp,amt from accounts where actNum")
    conn.commit()
#login-----------------
def tranLogin(act):
    conn=sqlite3.conncet('bankdb.db')
    curosor=conn.execute("select actNum,name,actType,amt from accounts where actNum")
    x=0;
    for row in cursor:
        x=row[3]
    return x
#get all account details------------
def getall():
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("select actNum,name,actTyp,amt from accounts")
    x=0;
    for row in cursor:
        print("    ",row[0],"  ",row[1],"   ",row[2],"   ",row[3])
#withdraw amount-------------
def qithDrawAmt(act,amt):
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("select actNum,name,actTyp,amt from accounts where actNum")
    x=0;
    for row in cursor:
        x=row[3]
    x=x-int(amt)
    withDrawn(act,x)

def withDrawn(act,amt):
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("update accounts set amt=? where actNum=?",(amt,act))
    conn.commit()
def delAcct(act):
    conn=sqlite3.connect('bankdb.db')
    cursor=conn.execute("delete from acc where actNum = ?",(act,))
    conn.commit
    
