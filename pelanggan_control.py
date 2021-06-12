import eq_trycatch
import login_control
import pelanggan_model

class PelangganController(eq_trycatch.TryCatcher):
    def __init__(self, username):
        self.username = username
        print("Selamat datang, {}. Anda berhasil login.".format(self.username))
        super().__init__()
        self.pelangganModel = pelanggan_model.PelangganModel()
        

    def lihat_hewan_username(self):
        hasil = self.pelangganModel.ambil_username_data_hewan(self.username)

        id_hasil = [i[0] for i in hasil]
        hasil = [[i[1], i[4], i[7], i[8]] for i in hasil]

        return id_hasil, hasil


    def lihat_riwayat_username(self):
        hasil = self.pelangganModel.ambil_username_data_riwayat(self.username)

        
        id_hasil = [i[0] for i in hasil]
        hasil = [[i[1], i[2], i[5], i[8], i[9]] for i in hasil]

        return id_hasil, hasil





