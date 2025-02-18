# List untuk menyimpan tugas
tugas = []

# Function untuk menampilkan daftar tugas
def tampilkan_tugas():
    if not tugas:
        print("Daftar tugas kosong.\n")
    else:
        print("\nDaftar Tugas:")
        for i, item in enumerate(tugas):
            print(f"{i + 1}. {item}")
    print()

# Function untuk menambahkan tugas
def tambahkan_tugas():
    tugas_baru = input("Masukkan nama tugas: ").strip()
    if tugas_baru:
        tugas.append(tugas_baru)
        print(f"Tugas '{tugas_baru}' ditambahkan.\n")
    else:
        print("Tugas tidak boleh kosong!\n")

# Function untuk menandai tugas selesai
def selesai_tugas():
    tampilkan_tugas()
    if tugas:
        try:
            nomor = int(input("Masukkan nomor tugas yang selesai: ")) - 1
            if 0 <= nomor < len(tugas):
                print(f"Tugas '{tugas[nomor]}' selesai dan dihapus.\n")
                tugas.pop(nomor)
            else:
                print("Nomor tugas tidak valid!\n")
        except ValueError:
            print("Harap masukkan angka yang benar!\n")

# Function untuk menjalankan program
def main():
    while True:
        print("===== MENU MANAJEMEN TUGAS =====")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Selesaikan Tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            tambahkan_tugas()
        elif pilihan == "2":
            tampilkan_tugas()
        elif pilihan == "3":
            selesai_tugas()
        elif pilihan == "4":
            print("Keluar dari program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-4.\n")

# Menjalankan program
if __name__ == "__main__":
    main()
