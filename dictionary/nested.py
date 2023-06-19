from main import data_mahasiswa

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'lahir':<10}")
print("-"*50)

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	nama = data_mahasiswa[KEY]['nama']
	nim = data_mahasiswa[KEY]['nim']
	sks = data_mahasiswa[KEY]['sks_lulus']
	beasiswa = data_mahasiswa[KEY]['beasiswa']
	lahir = data_mahasiswa[KEY]['lahir'].strftime("%x")
	print(f"{KEY:<6} {nama:<17} {sks:<3} {beasiswa:^9} {lahir:<10}")