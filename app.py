import mariadb
import dbcreds


newItem = input("What is the new item you wanna insert? ")
newPrice = input("What is the price? ")

# Holds a connection to our database
conn = mariadb.connect(
 user=dbcreds.user, 
 password=dbcreds.password,
 host=dbcreds.host, 
 port=dbcreds.port, 
 database=dbcreds.database
);

cursor = conn.cursor()
# I am running a SQL query directly

sql= "CALL insert_item(?,?)"
data= (newItem, float(newPrice))
cursor.execute(sql, data) 
# Commit the transaction
conn.commit()

cursor.execute('call get_items()')
result = cursor.fetchall()
print(result)

for item in result:
 print(item)
 

cursor.close();
conn.close();
