from create import insert

obj=insert()

print("--------- Bank Management System ---------")
print("For Inserting the data enter 1")
print("For Reading the data enter 2")
print("For Updating the data enter 3")
print("For Deleting the data enter 4")

opr = int(input("Please enter your operation: "))

def myopr():
    print("----- For Personal details press 1 --------")
    print("----- For Bank details press 2 ------------")
    print("----- For Transaction details press 3 -----")
    print("----- For Account details press 4 ---------")
    vr = int(input("Please select your table : "))

    if vr == 1:
        return 'personal_detail'
    elif vr == 2:
        return 'bank_detail'
    elif vr == 3:
        return 'transaction_detail'
    elif vr == 4:
        return 'account_detail'


if opr == 1:
    h = myopr()
    if h=='personal_detail':
        cid = int(input("Please enter customer id: "))
        fname = input("Please enter customer first name: ")
        lname = input("Please enter customer last name: ")
        addr = input("Please enter customer address: ")
        pn = int(input("Please enter customer phone number: "))
        an = int(input("Please enter customer aadhar number: "))
        pan = input("Please enter customer pan number: ")

        obj.personal_detail(cid,fname,lname,addr,pn,an,pan)

    elif h=='bank_detail':
        acn = int(input("Please enter account number: "))
        cid = int(input("Please enter customerid: "))
        ifsc = input("Please enter ifsc code: ")
        actype = input("Please enter account type: ")

        obj.bank_detail(acn,cid,ifsc,actype)

    elif h=='transaction_detail':
        tid = int(input("Please enter transaction id: "))
        s_ac = int(input("Please enter sender account number: "))
        r_ac = int(input("Please enter receiver account number: "))
        amt = int(input("Please enter amount: "))
        method = input("Please enter method: ")

        obj.transaction_detail(tid,s_ac,r_ac,amt,method)
    
    elif h=='account_detail':
        acn = int(input("Please enter account number: "))
        tid = int(input("Please enter transaction id: "))
        amt = int(input("Please enter amount: "))
        c_bal = int(input("Please enter closing balance: "))
        tp = input("Please enter transaction type:")

        obj.account_detail(acn,tid,amt,c_bal,tp)
        
from read import read
objread = read()
if opr==2: # user wanted to read the data
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)
    

from update import update
objupdate = update()
if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)
    

from delete import delete
objdelete = delete()

if opr ==4:
    k = myopr()
    cusid = int(input("please enter customer id to fetch data: "))
    objdelete.specific_del(j,cusid)