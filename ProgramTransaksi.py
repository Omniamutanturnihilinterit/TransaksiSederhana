# Inisialisasi variabel saldo awal
saldo = 0

def cek_saldo():
    print("Saldo Anda saat ini adalah: Rp", saldo)

def setor_tunai():
    global saldo
    jumlah = float(input("Masukkan jumlah uang yang akan disetor: Rp"))
    saldo += jumlah
    print("Setor tunai sebesar Rp", jumlah, "berhasil.")
    cek_saldo()

def tarik_tunai():
    global saldo
    jumlah = float(input("Masukkan jumlah uang yang akan ditarik: Rp"))
    if saldo >= jumlah:
        saldo -= jumlah
        print("Tarik tunai sebesar Rp", jumlah, "berhasil.")
    else:
        print("Saldo tidak mencukupi.")
    cek_saldo()

def transfer():
    global saldo
    rekening_tujuan = input("Masukkan nomor rekening tujuan: ")
    jumlah = float(input("Masukkan jumlah uang yang akan ditransfer: Rp"))
    if saldo >= jumlah:
        saldo -= jumlah
        print("Transfer sebesar Rp", jumlah, "ke rekening", rekening_tujuan, "berhasil.")
    else:
        print("Saldo tidak mencukupi.")
    cek_saldo()

# Program Utama
while True:
    print("=== Menu Transaksi ===")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Transfer")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        cek_saldo()
    elif pilihan == "2":
        setor_tunai()
    elif pilihan == "3":
        tarik_tunai()
    elif pilihan == "4":
        transfer()
    elif pilihan == "0":
        print("Terima kasih. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
