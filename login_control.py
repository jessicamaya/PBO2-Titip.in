import eq_database
import eq_trycatch
import login_model
import pelanggan_control
import petugas_control
import login_view

class LoginController(eq_trycatch.TryCatcher):
    def __init__(self):
        super().__init__()
        self.loginModel = login_model.LoginModel()
        print()

    def verifikasi_login(self, list_user_data):
        self.usernameLogin = list_user_data[0]
        self.__passwordLogin = list_user_data[1]
        self.loginSebagai = list_user_data[2]
        if self.loginSebagai == 0:
            self.loginSebagai = "Petugas"
        elif self.loginSebagai == 1:
            self.loginSebagai = "Pelanggan"
            
        print()
        if self.loginModel.verifikasi_akun(self.loginSebagai, self.usernameLogin, self.__passwordLogin) == True:
            return True

        elif self.loginModel.verifikasi_akun(self.loginSebagai, self.usernameLogin, self.__passwordLogin) == "Nodata":
            return 'Data tidak ada di sistem'
        else:
            # print("Password atau username salah. Silahkan coba login lagi.")
            # self.tampilkan_menu_login_inputan()
            return 'Password atau username salah. Silahkan coba login lagi.'
                
        
    def tampilkan_menu_login(self):
        tampilan_login = login_view.LoginView()
        self.login_data = login_view.list_user_data
        print(self.login_data)

    def tampilkan_menu_utama(self):
        """
        kelas ini digunakan untuk menampilkan menu utama.
        Menu utama bisa untuk petugas atau pelanggan, tergantung dari login.
        Apakah sebagai petugas, atau pelanggan.
        """
        raise NotImplementedError
    
# if __name__=='__main__':
#     login = LoginController()
#     login.tampilkan_menu_login()


    
