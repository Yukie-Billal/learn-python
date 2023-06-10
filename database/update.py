import main;

cursor = main.getCursor()
db = main.getDB()

print("Update berdasarkan email")

email = input("Masukkan Email : ")

sql = "\
	SELECT * FROM users WHERE email = '%s' \
" % (email)

try:
	cek = cursor.execute(sql)

	if cek == 1:
		result = cursor.fetchone()

		id = result[0]
		print("Id : %d, Email : %s, Password : %s"%(id, result[1], result[2]))

		name = input("Masukkan nama : ")
		email = input("Masukkan email : ")
		password = input("Masukkan password : ")
		sql = "\
			UPDATE users SET name='%s', email='%s' , password ='%s' WHERE id = %d \
		" % (name, email, password, id)
		try:
			cursor.execute(sql)

			db.commit()
		except Exception as e:
			print(e)
			db.rollback()
	else:
		print("User Not Found")
	
except Exception as e:
	print(e)

db.close()