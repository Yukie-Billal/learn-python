import main;

cursor = main.getCursor()
cursor.execute("DROP TABLE IF EXISTS users")

sql = """
	CREATE TABLE users (
		id int NOT NULL AUTO_INCREMENT,
		name varchar(50) NOT NULL,
		email varchar(50) NOT NULL,
		password varchar(50) NOT NULL,
		PRIMARY KEY (`id`)
	) AUTO_INCREMENT=1 ;
"""

cursor.execute(sql)

db = main.getDB()
db.close()