import datetime
data_list = ["Yukie",18,True]

data_dict = {
	"key" :"value",
	"string" : "ini adalah string",
	"boolean" : True,
	"number" : 18,
	"list" : data_list,
	"nested" : {
		"string" : "Nested - string",
		"boolean" : True,
		"number" : 0,
		"list" : ["Nested - list"]
	}
}

friends = {
	"yukie" : "Yukie muhammad billal",
	"fadhil" : "Fadhil zaelani",
	"gre" : "greyrat"
}

mahasiswa1 = {
	"nama" : "Yukie",
	"nim" : '19022002',
	"sks_lulus" : 130,
	"beasiswa" : True,
	"lahir" : datetime.datetime(2003,2,11)
}

mahasiswa2 = {
	"nama" : "Fadhil",
	"nim" : '19023002',
	"sks_lulus" : 140,
	"beasiswa" : True,
	"lahir" : datetime.datetime(2002,6,10)
}

mahasiswa3 = {
	"nama" : "Billal",
	"nim" : '19021196',
	"sks_lulus" : 110,
	"beasiswa" : False,
	"lahir" : datetime.datetime(2000,8,9)
}

data_mahasiswa = {
	"MAH001" : mahasiswa1,
	"MAH002" : mahasiswa2,
	"MAH003" : mahasiswa3,
}

# print(data_dict)
# print(friends)