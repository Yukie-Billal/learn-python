import main;

cursor = main.getCursor()
db = main.getDB()

search = input("Masukkan Nama atau email : ")

try:
	sql = "SELECT * FROM users WHERE email = '%s' OR name = '%s'" % (search, search)
	data = cursor.execute(sql)
	if data:
		result = cursor.fetchone()
		print("Hapus Data dengan nama : %s dan email :  %s dan password : %s ?" % (result[1], result[2], result[3]))
		confirm = input("(Y/N)")
		if confirm == 'Y' || confirm == 'y':
			delete = cursor.execute("DELETE FROM users WHERE id = %d" % (result[0]))
			if delete: print("users deleted")
	db.commit()
except Exception as e:
	print(e)
	db.rollback()
db.close()