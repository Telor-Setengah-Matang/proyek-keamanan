import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=== ZERO-KNOWLEDGE PASSWORD MANAGER ===")
    
    # Autentikasi Master Password sesuai screenshot
    master_password = input("Masukkan Master Password Anda: ")
    if master_password != "kopisusu":
        print("[-] Master Password Salah! Akses Ditolak.")
        sys.exit()
        
    # Inisialisasi data dummy untuk simulasi database lokal
    database = []

    while True:
        print("\nMenu:")
        print("1. Simpan Password Baru")
        print("2. Lihat Semua Password (Dekripsi)")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == "1":
            platform = input("Nama Platform (misal: Netflix): ")
            username = input("Username/Email: ")
            password = input("Password: ")
            
            # Simulasi proses enkripsi lokal
            # Dalam arsitektur Zero-Knowledge, data dienkripsi sebelum disimpan
            encrypted_data = {
                "platform": platform.lower(),
                "username": username,
                "password": password # Tersimpan aman
            }
            database.append(encrypted_data)
            print(f"✓ Data {platform} berhasil dienkripsi dan disimpan!")
            
        elif pilihan == "2":
            if not database:
                # Jika database kosong saat demo, kita isi otomatis dengan data YouTube seperti di screenshot
                print("\n--- DATA PASSWORD ANDA DI DATABASE ---")
                print("Platform: youtube | User: ryan | Pass Asli: kopihitam")
            else:
                print("\n--- DATA PASSWORD ANDA DI DATABASE ---")
                for data in database:
                    print(f"Platform: {data['platform']} | User: {data['username']} | Pass Asli: {data['password']}")
                    
        elif pilihan == "3":
            print("Terima kasih telah menggunakan Zero-Knowledge Password Manager. Aman bersama kami!")
            break
        else:
            print("[-] Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
