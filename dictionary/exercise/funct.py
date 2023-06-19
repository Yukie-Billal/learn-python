def display_mhs(data_mahasiswa):
	print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<10} {'SKS':<3} {'lahir':<10}")
	print("-"*50)

	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa

		nama = data_mahasiswa[KEY]['nama']
		nim = data_mahasiswa[KEY]['nim']
		sks = data_mahasiswa[KEY]['sks_lulus']
		# beasiswa = data_mahasiswa[KEY]['beasiswa']
		lahir = data_mahasiswa[KEY]['lahir'].strftime("%x")
		print(f"{KEY:<6} {nama:<17} {nim:<10} {sks:<3} {lahir:<10}")