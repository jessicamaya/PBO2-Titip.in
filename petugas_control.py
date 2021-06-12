import eq_trycatch
import login_control
import petugas_model

class PetugasController(eq_trycatch.TryCatcher):
    def __init__(self, username):
        self.username = username
        print("Selamat datang, {}. Anda berhasil login.".format(self.username))
        super().__init__()
        self.petugasModel = petugas_model.PetugasModel()
        
#Menu1 : Tambah hewan

    def tambah_hewan(self, usernamePetugas, usernameInput, hewanInput, kategoriInput):
        input_hewan = []

        if kategoriInput == 0:
            kategoriInput = "Kucing"
            
        elif kategoriInput == 1:
            kategoriInput = "Anjing"
            
        elif kategoriInput == 2:
            kategoriInput = "Burung Beo"
            
        elif kategoriInput == 3:
            kategoriInput = "Musang"

        
#         tambah_lagi = True
#         while True:
#             usernameInput = self.check_str("Masukkan username pelanggan : ")
#             verif = self.petugasModel.verifikasi_username(usernameInput)
#             if verif == True:
#                 break
#             elif verif == False:
#                 print("Username tidak ada di data kami. Mohon coba lagi")

#         while tambah_lagi == True:
#             while True:
#                 hewanInput = self.check_str("Masukkan nama hewan : ")
#                 verif = self.petugasModel.verifikasi_hewan(usernameInput, hewanInput)
#                 if verif == True:
#                     break
#                 elif verif == False:
#                     print("Hewan sedang dititipkan sekarang.")
            
#             while True:
#                 kategoriInput = self.check_str("Masukkan kategori hewan : ")
#                 verif = self.petugasModel.verifikasi_kategori(kategoriInput)
#                 if verif == True:
#                     break
#                 elif verif == False:
#                     print("Kategori ini tidak ditemukan pada data kami. Mohon coba lagi")
    
        input_hewan.append([hewanInput, kategoriInput])
#             print("""Apakah anda ingin menambahkan peliharaan lain dari pelanggan ini?
# 1. Ya
# 2. Tidak""")
#             input_lagi = self.check_int(1,2)
#             if input_lagi == 2:
#                 break


        sukses = self.petugasModel.tambah_data_hewan(usernamePetugas, usernameInput, input_hewan)
        print(sukses)
        if sukses == True:
            return ("Data hewan sukses ditambahkan.\n")
        elif sukses == False:
            return ("Terjadi kesalahan. Coba lagi.\n")



    def tambah_pelanggan(self, usernameInput, namaInput, passwordInput):
        # while True:
        #     usernameInput = self.check_str("Masukkan username pelanggan : ")
        #     verif = self.petugasModel.verifikasi_username_kosong(usernameInput)
        #     if verif == True:
        #         break
        #     elif verif == False:
        #         print("Username tidak tersedia. Mohon coba lagi")
        
        # namaInput = self.check_str("Masukkan nama lengkap pelanggan : ")
        # passwordInput = self.check_str("Masukkan password pelanggan : ")

        sukses = self.petugasModel.tambah_data_pelanggan(usernameInput, namaInput, passwordInput)
        if sukses == True:
            print("Data pelanggan sukses ditambahkan.\n")
        elif sukses == False:
            print("Terjadi kesalahan. Coba lagi.")
    
#Menu2 : Hapus hewan

    def hapus_hewan(self, pilih):
        #hapus hewan dengan caraa pasang date dikembalikan ke pemiliknya ya. jangan lupa bayarnya juga dicatet!
        # self.lihat_semua_hewan()
        
        hasil = self.petugasModel.hapus_hewan(pilih)
        if hasil == True:
            print("Data hewan telah berhasil dihapus\n")


#Menu3 : Lihat hewan & pelanggan

    def lihat_semua_hewan(self):
        hasil = self.petugasModel.ambil_semua_data_hewan()

        id_hasil = [i[0] for i in hasil]
        hasil = [[i[1], i[3], i[4], i[7], i[8]] for i in hasil]

        return id_hasil, hasil

    # def lihat_username_hewan(self):
    #     usernameInput = self.check_str("Masukkan username yang dicari : ")
    #     header, hasil = self.petugasModel.ambil_username_data_hewan(usernameInput)

    #     print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*header))
    #     for i in hasil:
    #         print("{:^4} {:^24} {:<20} {:<20} {:<20} {:<15} {:<15} {:<15} {:<15}".format(*i))

    def lihat_semua_pelanggan(self):
        hasil = self.petugasModel.ambil_semua_data_pelanggan()

        hasil = [[i[1], i[2], i[3]] for i in hasil]

        return hasil

#Menu4 : Lihat riwayat
    
    def lihat_riwayat(self):
        hasil = self.petugasModel.ambil_semua_data_riwayat()

        id_hasil = [i[0] for i in hasil]
        hasil = [[i[1], i[2], i[4], i[5], i[8], i[9]] for i in hasil]

        return id_hasil, hasil

    def lihat_harga(self):
        hasil = self.petugasModel.ambil_data_harga()

        hasil = [[i[1], i[2]] for i in hasil]
        
        return hasil


