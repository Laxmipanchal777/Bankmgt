
# installed library mysql-connector-python
import mysql.connector

#creating connection

class insert:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user="root",
            password="Google#8756",
            database="bank"
        )
    def personal_detail(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAIL VALUES({cid},'{fname}','{lname}','{addr}',{pn},{an},'{pan}')")
        self.conn.commit()
        print("Personal information has been saved successfully.")

    def bank_detail(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAIL VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("Bank details have been saved successfully.")

    def transaction_detail(self,tid,s_ac,r_ac,amt,method):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAIL VALUES({tid},{s_ac},{r_ac},{amt},'{method}')")
        self.conn.commit()
        print("Transaction details have been saved successfully.")

    def account_detail(self,acn,tid,amt,c_bal,tp):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAIL VALUES({acn},{tid},{amt},{c_bal},'{tp}')")
        self.conn.commit()
        print("Account details have been saved successfully.")