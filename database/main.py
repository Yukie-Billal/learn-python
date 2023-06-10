import pymysql.cursors;

# Koneksi kedalam database, mirip seperti php mysqli
db = pymysql.connect(host='localhost',
					user='root',
					password='',
					database='belajar_python')

# Prepare a cursor object using cursor() method

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)