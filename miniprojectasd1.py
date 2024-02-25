class perabot:
    def __init__(self, nomor, nama, harga, stok, kualitas):
        self.nomor = nomor
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.kualitas = kualitas

class crud:
       
    def __init__(self):
        self.perabot = [{"nomor": 1, "nama": "Pisau dapur", "harga": 15000, "kualitas": "baru", "stok": 10},
                        {"nomor": 2, "nama": "Sapu", "harga": 20000, "kualitas": "baru", "stok": 20},
                        {"nomor": 3, "nama": "Panci besar", "harga": 12000, "kualitas": "baru", "stok": 15},
                        {"nomor": 4, "nama": "Panci kecil", "harga": 7000, "kualitas": "baru", "stok": 25},
                        {"nomor": 5, "nama": "Piring", "harga": 6000, "kualitas": "lama", "stok": 30}]

    def tambah_barang(self, nomor, nama, harga, stok, kualitas):
        barang_baru = perabot(nomor, nama, harga, stok, kualitas)
        self.perabot.append(barang_baru.__dict__)
        
    def hapus_barang(self, nomor):
        for i, item in enumerate(self.perabot):
            if item['nomor'] == nomor:
                del self.perabot[i]
                return True
        return False
    
    def lihat_barang(self):
        return self.perabot
    
    def update_stok(self, nomor, stok):
         for item in self.perabot:
            if item['nomor'] == nomor:
               item['stok'] = stok
            return True
         return False

def main_menu():
    crud_instance = crud()  
    while True:
        print("==== Menu ====")
        print("1. Tambah barang")
        print("2. Lihat barang")
        print("3. Hapus barang")
        print("4. Update stok")
        print("5. Keluar")

        menu = int(input("Pilih 1/2/3/4/5: "))

        if menu == 1:
            tambah_barang_menu(crud_instance)  
        elif menu == 2:
            lihat_barang_menu(crud_instance)  
        elif menu == 3:
            hapus_barang_menu(crud_instance)  
        elif menu == 4:
            update_stok_menu(crud_instance)  
        elif menu == 5:
            print("Terima kasih!")
            break

def tambah_barang_menu(crud_instance): 
    nomor = int(input("Nomor: "))
    nama = input("Nama: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    kualitas = input("Kualitas: ")
    
    crud_instance.tambah_barang(nomor, nama, harga, stok, kualitas)
    print("Barang telah ditambahkan.")

def lihat_barang_menu(crud_instance):  
    daftar_barang = crud_instance.lihat_barang()
    for barang in daftar_barang:
        print(barang)

def hapus_barang_menu(crud_instance): 
    nomor = int(input("Nomor barang yang akan dihapus: "))
    if crud_instance.hapus_barang(nomor):
        print("Barang telah dihapus.")
    else:
        print("Barang tidak ditemukan.")

def update_stok_menu(crud_instance):  
    nomor = int(input("Nomor barang yang akan diupdate stok: "))
    stok_baru = int(input("Stok baru: "))
    if crud_instance.update_stok(nomor, stok_baru):
        print("Stok barang telah diupdate.")
    else:
        print("Barang tidak ditemukan.")

if __name__ == "__main__":
    main_menu()