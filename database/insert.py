import main;

cursor = main.getCursor()
db = main.getDB()

name = input("Masukkan Nama : ")
email = input("Masukkan Email : ")
password = input("Masukkan password : ")

sql = "\
	INSERT INTO users (`name`,`email`,`password`) VALUES ('%s','%s', '%s')\
" % (name, email, password)

try:
	cursor.execute(sql)
	db.commit()
	print("success insert data")
except Exception as e:
	print(e)
	db.rollback()

db.close()