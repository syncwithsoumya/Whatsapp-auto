sql_add_customer = "INSERT INTO CUSTOMERS_TEMP(`NAME`,`PHONE`,`EXISTING`,`SUB_FLAG`) VALUES(%s,%s,%s,%s)"
sql_del_customer = "DELETE FROM CUSTOMERS_TEMP WHERE ID = (SELECT ID FROM (SELECT * FROM CUSTOMERS_TEMP) as CT WHERE NAME = %s)"
sql_mod_customer = "UPDATE CUSTOMERS_TEMP SET NAME=%s ,PHONE=%s, EXISTING=%s, SUB_FLAG=%s WHERE ID = (SELECT ID FROM (SELECT * FROM CUSTOMERS_TEMP) as CT WHERE NAME = %s)"
default_prefix = 'Cust-'
