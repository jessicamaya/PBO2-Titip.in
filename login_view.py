import FrameBuild as v
import wx
import wx.xrc

import login_control
import petugas_control
import pelanggan_control

###########################################################################
## Class Login
###########################################################################

class SubClassFrame_Login(v.Login):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.controller = login_control.LoginController()
		
	def login_verify( self, event ):
		list_user_data = list()
		list_user_data.append(self.input_username.GetValue())
		list_user_data.append(self.input_password.GetValue())
		list_user_data.append(self.login_choice.GetSelection())
		
		self.input_username.SetValue('')
		self.input_password.SetValue('')

		verdict = self.controller.verifikasi_login(list_user_data)
		
		if verdict == True:
			if self.login_choice.GetSelection() == 0:
				show = SubClassFrame_Home_Petugas(list_user_data[0])
				show.Show()
				self.Close()

			elif self.login_choice.GetSelection() == 1:
				show = SubClassFrame_Home_Pelanggan(list_user_data[0])
				show.Show()
				self.Close()

###########################################################################
## Class Petugas - Change Frame
###########################################################################

class Petugas_Change_Frame_Home(v.Home_Petugas):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()


class Petugas_Change_Frame_Tambah_Hewan(v.Petugas_Tambah_Data_Hewan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Tambah_Data_Pelanggan(v.Petugas_Tambah_Data_Pelanggan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Hapus_Data_Hewan(v.Petugas_Hapus_Data_Hewan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Lihat_Data_Pelanggan(v.Petugas_Lihat_Data_Pelanggan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Lihat_Data_Hewan(v.Petugas_Lihat_Data_Hewan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Lihat_Data_Riwayat_Hewan(v.Petugas_Lihat_Data_Riwayat_Hewan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

class Petugas_Change_Frame_Lihat_Data_Harga(v.Petugas_Lihat_Data_Harga):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_tambah_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_tambah_data_pet( self, event ):
		show = SubClassFrame_Petugas_Tambah_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_hapus_data_pet( self, event ):
		show = SubClassFrame_Petugas_Hapus_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pelanggan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Pelanggan(self.username)
		show.Show()
		self.Close()

	def window_lihat_data_pet( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_riwayat_penitipan( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def window_lihat_daftar_harga( self, event ):
		show = SubClassFrame_Petugas_Lihat_Data_Harga(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()


###########################################################################
## Class Petugas
###########################################################################

class SubClassFrame_Home_Petugas(Petugas_Change_Frame_Home):
	def __init__(self, username, parent=None):
		super().__init__(username, parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)


class SubClassFrame_Petugas_Tambah_Data_Hewan(Petugas_Change_Frame_Tambah_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

	def daftar_pet_baru( self, event ):
		usernameInput = self.input_username_pelanggan.GetValue()
		hewanInput = self.input_nama_hewan.GetValue()
		kategoriInput = self.kategori_choice.GetSelection()
		
		self.input_username_pelanggan.SetValue('')
		self.input_nama_hewan.SetValue('')

		self.controller.tambah_hewan(self.username, usernameInput, hewanInput, kategoriInput)
		

class SubClassFrame_Petugas_Tambah_Data_Pelanggan(Petugas_Change_Frame_Tambah_Data_Pelanggan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

	def daftar_pelanggan_baru( self, event ):
		usernameInput = self.input_username_pelanggan.GetValue()
		namaInput = self.input_nama_lengkap_pelanggan.GetValue()
		passwordInput = self.input_password_pelanggan.GetValue()
		
		self.input_username_pelanggan.SetValue('')
		self.input_nama_lengkap_pelanggan.SetValue('')
		self.input_password_pelanggan.SetValue('')

		self.controller.tambah_pelanggan(usernameInput, namaInput, passwordInput)


class SubClassFrame_Petugas_Hapus_Data_Hewan(Petugas_Change_Frame_Hapus_Data_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.id_available, self.data_hewan = self.controller.lihat_semua_hewan()

		for i in range(len(self.id_available)):
			self.grid_daftar_pet.SetRowLabelValue(i, str(self.id_available[i]))

		for i in range(len(self.data_hewan)):
			for j in range(len(self.data_hewan[0])):
				self.grid_daftar_pet.SetCellValue(i,j, str(self.data_hewan[i][j]))
			
		self.hapus_pet_choice.SetItems([str(i) for i in self.id_available])

	def hapus_hewan( self, event ):
		id_hapus = self.hapus_pet_choice.GetSelection()
		id_hapus = self.id_available[int(id_hapus)]
		self.controller.hapus_hewan(id_hapus)
		

class SubClassFrame_Petugas_Lihat_Data_Pelanggan(Petugas_Change_Frame_Lihat_Data_Pelanggan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.data_pelanggan = self.controller.lihat_semua_pelanggan()

		for i in range(len(self.data_pelanggan)):
			for j in range(len(self.data_pelanggan[0])):
				self.grid_daftar_pelanggan.SetCellValue(i,j, str(self.data_pelanggan[i][j]))


class SubClassFrame_Petugas_Lihat_Data_Hewan(Petugas_Change_Frame_Lihat_Data_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.id_available, self.data_hewan = self.controller.lihat_semua_hewan()

		for i in range(len(self.id_available)):
			self.grid_daftar_pet.SetRowLabelValue(i, str(self.id_available[i]))

		for i in range(len(self.data_hewan)):
			for j in range(len(self.data_hewan[0])):
				self.grid_daftar_pet.SetCellValue(i,j, str(self.data_hewan[i][j]))


class SubClassFrame_Petugas_Lihat_Data_Riwayat_Hewan(Petugas_Change_Frame_Lihat_Data_Riwayat_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.id_available, self.data_hewan = self.controller.lihat_riwayat()

		for i in range(len(self.id_available)):
			self.grid_riwayat_pet.SetRowLabelValue(i, str(self.id_available[i]))

		for i in range(len(self.data_hewan)):
			for j in range(len(self.data_hewan[0])):
				self.grid_riwayat_pet.SetCellValue(i,j, str(self.data_hewan[i][j]))
			

class SubClassFrame_Petugas_Lihat_Data_Harga(Petugas_Change_Frame_Lihat_Data_Harga):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = petugas_control.PetugasController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.data_harga = self.controller.lihat_harga()

		for i in range(len(self.data_harga)):
			for j in range(len(self.data_harga[0])):
				self.grid_harga_kategori.SetCellValue(i,j, str(self.data_harga[i][j]))



###########################################################################
## Class Pelanggan - Change Frame
###########################################################################

class Pelanggan_Change_Frame_Home(v.Home_Pelanggan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()



class Pelanggan_Change_Frame_Lihat_Data_Hewan(v.Pelanggan_Lihat_Hewan_Dititipkan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()



class Pelanggan_Change_Frame_Lihat_Data_Riwayat_Hewan(v.Pelanggan_Lihat_Riwayat_Hewan_Dititipkan):

	def __init__(self, username, parent=None):
		super().__init__(parent)

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Hewan(self.username)
		show.Show()
		self.Close()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		show = SubClassFrame_Pelanggan_Lihat_Data_Riwayat_Hewan(self.username)
		show.Show()
		self.Close()

	def logout_verify( self, event ):
		self.username = 'Logout'
		show = SubClassFrame_Login()
		show.Show()
		self.Close()

###########################################################################
## Class Pelanggan
###########################################################################



class SubClassFrame_Home_Pelanggan(Pelanggan_Change_Frame_Home):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = pelanggan_control.PelangganController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)


class SubClassFrame_Pelanggan_Lihat_Data_Hewan(Pelanggan_Change_Frame_Lihat_Data_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = pelanggan_control.PelangganController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.id_available, self.data_hewan = self.controller.lihat_hewan_username()

		for i in range(len(self.id_available)):
			self.grid_daftar_pet.SetRowLabelValue(i, str(self.id_available[i]))

		for i in range(len(self.data_hewan)):
			for j in range(len(self.data_hewan[0])):
				self.grid_daftar_pet.SetCellValue(i,j, str(self.data_hewan[i][j]))


class SubClassFrame_Pelanggan_Lihat_Data_Riwayat_Hewan(Pelanggan_Change_Frame_Lihat_Data_Riwayat_Hewan):
	def __init__(self, username, parent=None):
		super().__init__(parent)
		self.username = username
		self.controller = pelanggan_control.PelangganController(self.username)
		x = str('Selamat datang, {}'.format(username))
		self.greeting_user.SetLabel(x)

		self.id_available, self.data_hewan = self.controller.lihat_riwayat_username()

		for i in range(len(self.id_available)):
			self.grid_daftar_riwayat_pet.SetRowLabelValue(i, str(self.id_available[i]))

		for i in range(len(self.data_hewan)):
			for j in range(len(self.data_hewan[0])):
				self.grid_daftar_riwayat_pet.SetCellValue(i,j, str(self.data_hewan[i][j]))



###########################################################################
## Class Main
###########################################################################

class LoginView():
    def __init__(self):
        app = wx.App(clearSigInt = True)
        frame = SubClassFrame_Login()
        frame.Show()
        app.MainLoop()

if __name__ == "__main__":
	login = LoginView()

