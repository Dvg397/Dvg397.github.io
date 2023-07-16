# tulisan judul tools
print(":::::::::::::::::::::::::::::::::::")
print(":: tools pemesan makanan ::")
print(":: good food atractive tools ::")
print(":: by deven ganendra wibowo ::")
print(":: the future indonesian programer ::")
print(":::::::::::::::::::::::::::::::::::")

# menu tools
print("1. pizza khas italia: 10$")
print("2. nasi goreng khas indonesia: 8$")
print("3. croisant khas prancis: 20$")
print("4. sushi khas jepang: 15$")
print("5. naan chiken  curry khas india: 9$")

choice = input("pilih 1 menu yang akan dipilih: ")

#finsihing tools
if choice == '1':
	print("pizza italia segera datang")
elif choice == '2':
	print("nasi goreng khas indonesia segera datang. ")	
elif choice == '3':
	print("croisant segera datang. ")
elif choice == '4':
	print("sushi khas jepang segera datang. ")
elif choice == '5':
	print("naan chiken kari khas india segera datang. ")
else:
	print("kamu pilih apa sih")
	print("nanti pesananmu salah loh")
	print ("jangan masukan apa apa dulu loh ya ")
	print("sekarang ulang lagi! ")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	print("x")
	
	
#alamat penerima
alamat = input("masukkan alamat anda: ")
	
# toppings
toppings = input("apakah makanan anda mau diberi toping tambahan namun akan menambah 5$ tambahan uang? ")
if toppings == "yes":
	print("toping lezat tambahan akan ditambahkan. ")
	print("makanan segera datang mohon ditunggu. terima kasih")
else:
	print("baiklah makanan akan segera datang tanla toping sesuai permintaan anda")

#kalkulator untuk menghitung jumlah harga

print("ini kalkulator penjumlahan untuk menghitung total harga makanan  ya")

# Memasukkan Inputan Angka
angka1 = input('Tulis harga makan yang dipilih: ')
angka2 = input('Tulis jumlah makanan: ')
angka3 = input('tulis harga toppings yang telah dikali jumlah makanan: ')
 
# Mengkonversi Angka lalu Menjumlahkannya
sum = int(angka1) * int(angka2) + int(angka3)
 
# Menampilkan Hasil harga
print('total harga makanannya adalah {0} dan {1} dan {2} adalah {3}'.format(angka1, angka2,angka3, sum))

# penutupan
print(".")
print(".")
print(".")
print("terima kasih telah menggunakan tools")
print("tunggu update selanjutnya! ")

