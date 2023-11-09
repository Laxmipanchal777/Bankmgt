# installed library mysql-connector-python
import mysql.connector

#creating connection 

class read:
    def __init__(self):
        self.conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Google#8756",
                database = "bank"
                )
    
    def specific_info(self,customer_id,table_name):
        cur = self.conn.cursor()
        if table_name=='personal_detail' or table_name=='bank_detail':
            cur.execute(f"SELECT * FROM {table_name} WHERE CUSTOMER_ID={customer_id}")
            print(cur.fetchall())

        if table_name=='transaction_detail':
            
                cur.execute(f'''SELECT * FROM TRANSACTION_DETAIL WHERE TRANSACTIONID IN
                (SELECT TRANSACTION_ID FROM ACCOUNT_DETAIL WHERE ACCOUNT_NUMBER IN 
                (SELECT ACCOUNT_NUMBER FROM BANK_DETAIL WHERE CUSTOMER_ID={customer_id}));
                        ''')
                print(cur.fetchall())
            
