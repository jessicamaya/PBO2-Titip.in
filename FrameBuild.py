# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,50 ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		bSizer4.Add( ( 0, 2), 0, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Halaman Login Titip.in", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer9.Add( ( 0, 100), 0, 0, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,150 ) )
		self.label_username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_username.Wrap( -1 )

		self.label_username.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway Medium" ) )
		self.label_username.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		fgSizer2.Add( self.label_username, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 100, 50), 1, wx.EXPAND, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.label_password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
		self.label_password.Wrap( -1 )

		self.label_password.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway Medium" ) )
		self.label_password.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		fgSizer2.Add( self.label_password, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.input_password, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.label_login_as = wx.StaticText( self, wx.ID_ANY, u"Login Sebagai :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_login_as.Wrap( -1 )

		self.label_login_as.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_login_as.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer91.Add( self.label_login_as, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer91.Add( ( 0, 15), 0, wx.EXPAND, 5 )

		login_choiceChoices = [ u"Petugas", u"Pelanggan" ]
		self.login_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), login_choiceChoices, 0 )
		self.login_choice.SetSelection( 1 )
		self.login_choice.SetMinSize( wx.Size( 125,-1 ) )

		bSizer91.Add( self.login_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer9.Add( bSizer91, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.login_button = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( 175,50 ), 0 )
		self.login_button.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.login_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer7.Add( self.login_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )


		bSizer9.Add( bSizer7, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login_button.Bind( wx.EVT_BUTTON, self.login_verify )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_verify( self, event ):
		event.Skip()


###########################################################################
## Class Home_Pelanggan
###########################################################################

class Home_Pelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Hewan Dititipkan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button18, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button13, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Hewan yang dititipkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.m_button18.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_hewan_dititipkan )
		self.m_button13.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_riwayat_hewan_dititipkan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		event.Skip()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		event.Skip()


###########################################################################
## Class Pelanggan_Lihat_Riwayat_Hewan_Dititipkan
###########################################################################

class Pelanggan_Lihat_Riwayat_Hewan_Dititipkan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Hewan Dititipkan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button18, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button13, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Riwayat Penitipan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_riwayat_pet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_riwayat_pet.CreateGrid( 10, 5 )
		self.grid_daftar_riwayat_pet.EnableEditing( True )
		self.grid_daftar_riwayat_pet.EnableGridLines( True )
		self.grid_daftar_riwayat_pet.EnableDragGridSize( True )
		self.grid_daftar_riwayat_pet.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_riwayat_pet.SetColSize( 0, 200 )
		self.grid_daftar_riwayat_pet.SetColSize( 1, 200 )
		self.grid_daftar_riwayat_pet.SetColSize( 2, 125 )
		self.grid_daftar_riwayat_pet.SetColSize( 3, 75 )
		self.grid_daftar_riwayat_pet.SetColSize( 4, 150 )
		self.grid_daftar_riwayat_pet.EnableDragColMove( False )
		self.grid_daftar_riwayat_pet.EnableDragColSize( True )
		self.grid_daftar_riwayat_pet.SetColLabelSize( 45 )
		self.grid_daftar_riwayat_pet.SetColLabelValue( 0, u"Jam Mulai" )
		self.grid_daftar_riwayat_pet.SetColLabelValue( 1, u"Jam Selesai" )
		self.grid_daftar_riwayat_pet.SetColLabelValue( 2, u"Nama Pet" )
		self.grid_daftar_riwayat_pet.SetColLabelValue( 3, u"Hari" )
		self.grid_daftar_riwayat_pet.SetColLabelValue( 4, u"Biaya Total" )
		self.grid_daftar_riwayat_pet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_riwayat_pet.SetRowSize( 0, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 1, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 2, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 3, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 4, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 5, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 6, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 7, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 8, 35 )
		self.grid_daftar_riwayat_pet.SetRowSize( 9, 35 )
		self.grid_daftar_riwayat_pet.EnableDragRowSize( True )
		self.grid_daftar_riwayat_pet.SetRowLabelSize( 60 )
		self.grid_daftar_riwayat_pet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_riwayat_pet.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_daftar_riwayat_pet.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_daftar_riwayat_pet.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_riwayat_pet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_daftar_riwayat_pet, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.m_button18.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_hewan_dititipkan )
		self.m_button13.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_riwayat_hewan_dititipkan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		event.Skip()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		event.Skip()


###########################################################################
## Class Pelanggan_Lihat_Hewan_Dititipkan
###########################################################################

class Pelanggan_Lihat_Hewan_Dititipkan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Hewan Dititipkan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button18, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 150), 0, wx.EXPAND, 5 )

		self.m_button13 = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.m_button13, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Penitipan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_pet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_pet.CreateGrid( 10, 4 )
		self.grid_daftar_pet.EnableEditing( True )
		self.grid_daftar_pet.EnableGridLines( True )
		self.grid_daftar_pet.EnableDragGridSize( True )
		self.grid_daftar_pet.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_pet.SetColSize( 0, 200 )
		self.grid_daftar_pet.SetColSize( 1, 200 )
		self.grid_daftar_pet.SetColSize( 2, 75 )
		self.grid_daftar_pet.SetColSize( 3, 150 )
		self.grid_daftar_pet.EnableDragColMove( False )
		self.grid_daftar_pet.EnableDragColSize( True )
		self.grid_daftar_pet.SetColLabelSize( 45 )
		self.grid_daftar_pet.SetColLabelValue( 0, u"Jam Mulai" )
		self.grid_daftar_pet.SetColLabelValue( 1, u"Nama Pet" )
		self.grid_daftar_pet.SetColLabelValue( 2, u"Hari" )
		self.grid_daftar_pet.SetColLabelValue( 3, u"Biaya Total" )
		self.grid_daftar_pet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_pet.SetRowSize( 0, 35 )
		self.grid_daftar_pet.SetRowSize( 1, 35 )
		self.grid_daftar_pet.SetRowSize( 2, 35 )
		self.grid_daftar_pet.SetRowSize( 3, 35 )
		self.grid_daftar_pet.SetRowSize( 4, 35 )
		self.grid_daftar_pet.SetRowSize( 5, 35 )
		self.grid_daftar_pet.SetRowSize( 6, 35 )
		self.grid_daftar_pet.SetRowSize( 7, 35 )
		self.grid_daftar_pet.SetRowSize( 8, 35 )
		self.grid_daftar_pet.SetRowSize( 9, 35 )
		self.grid_daftar_pet.EnableDragRowSize( True )
		self.grid_daftar_pet.SetRowLabelSize( 60 )
		self.grid_daftar_pet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_pet.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_daftar_pet.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_daftar_pet.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_pet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_daftar_pet, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.m_button18.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_hewan_dititipkan )
		self.m_button13.Bind( wx.EVT_BUTTON, self.window_pelanggan_lihat_riwayat_hewan_dititipkan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_pelanggan_lihat_hewan_dititipkan( self, event ):
		event.Skip()

	def window_pelanggan_lihat_riwayat_hewan_dititipkan( self, event ):
		event.Skip()


###########################################################################
## Class Home_Petugas
###########################################################################

class Home_Petugas ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 20), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Hewan yang dititipkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Tambah_Data_Hewan
###########################################################################

class Petugas_Tambah_Data_Hewan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 100), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Form Pendaftaran Hewan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,150 ) )
		self.label_username = wx.StaticText( self, wx.ID_ANY, u"Username Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_username.Wrap( -1 )

		self.label_username.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_username.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_username.SetMinSize( wx.Size( -1,30 ) )

		fgSizer2.Add( self.label_username, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 70, 50), 1, wx.EXPAND, 5 )

		self.input_username_pelanggan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.input_username_pelanggan, 0, wx.ALL, 5 )

		self.label_password = wx.StaticText( self, wx.ID_ANY, u"Nama Hewan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_password.Wrap( -1 )

		self.label_password.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_password.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_password.SetMinSize( wx.Size( -1,45 ) )

		fgSizer2.Add( self.label_password, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_nama_hewan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.input_nama_hewan, 0, wx.ALL, 5 )

		self.label_password1 = wx.StaticText( self, wx.ID_ANY, u"Kategori Hewan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_password1.Wrap( -1 )

		self.label_password1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_password1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_password1.SetMinSize( wx.Size( -1,50 ) )

		fgSizer2.Add( self.label_password1, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		kategori_choiceChoices = [ u"Kucing", u"Anjing", u"Burung Beo", u"Musang" ]
		self.kategori_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), kategori_choiceChoices, 0 )
		self.kategori_choice.SetSelection( 0 )
		self.kategori_choice.SetMinSize( wx.Size( 200,-1 ) )

		fgSizer2.Add( self.kategori_choice, 0, wx.ALL, 5 )


		bSizer22.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.daftar_pet_button = wx.Button( self, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.daftar_pet_button.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.daftar_pet_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer7.Add( self.daftar_pet_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )


		bSizer22.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )
		self.daftar_pet_button.Bind( wx.EVT_BUTTON, self.daftar_pet_baru )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()

	def daftar_pet_baru( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Tambah_Data_Pelanggan
###########################################################################

class Petugas_Tambah_Data_Pelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 100), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Form Pendaftaran Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer2.SetMinSize( wx.Size( -1,150 ) )
		self.label_username = wx.StaticText( self, wx.ID_ANY, u"Username Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_username.Wrap( -1 )

		self.label_username.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_username.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_username.SetMinSize( wx.Size( -1,30 ) )

		fgSizer2.Add( self.label_username, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 70, 50), 1, wx.EXPAND, 5 )

		self.input_username_pelanggan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.input_username_pelanggan, 0, wx.ALL, 5 )

		self.label_password = wx.StaticText( self, wx.ID_ANY, u"Nama Lengkap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_password.Wrap( -1 )

		self.label_password.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_password.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_password.SetMinSize( wx.Size( -1,45 ) )

		fgSizer2.Add( self.label_password, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_nama_lengkap_pelanggan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer2.Add( self.input_nama_lengkap_pelanggan, 0, wx.ALL, 5 )

		self.label_password1 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_password1.Wrap( -1 )

		self.label_password1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_password1.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.label_password1.SetMinSize( wx.Size( -1,50 ) )

		fgSizer2.Add( self.label_password1, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.input_password_pelanggan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ),  wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		fgSizer2.Add( self.input_password_pelanggan, 0, wx.ALL, 5 )


		bSizer22.Add( fgSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.daftar_pelanggan_button = wx.Button( self, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.Size( 150,50 ), 0 )
		self.daftar_pelanggan_button.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.daftar_pelanggan_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer7.Add( self.daftar_pelanggan_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )


		bSizer22.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )
		self.daftar_pelanggan_button.Bind( wx.EVT_BUTTON, self.daftar_pelanggan_baru )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()

	def daftar_pelanggan_baru( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Hapus_Data_Hewan
###########################################################################

class Petugas_Hapus_Data_Hewan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 25), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Pet Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_pet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_pet.CreateGrid( 10, 5 )
		self.grid_daftar_pet.EnableEditing( True )
		self.grid_daftar_pet.EnableGridLines( True )
		self.grid_daftar_pet.EnableDragGridSize( True )
		self.grid_daftar_pet.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_pet.SetColSize( 0, 200 )
		self.grid_daftar_pet.SetColSize( 1, 125 )
		self.grid_daftar_pet.SetColSize( 2, 125 )
		self.grid_daftar_pet.SetColSize( 3, 75 )
		self.grid_daftar_pet.SetColSize( 4, 150 )
		self.grid_daftar_pet.EnableDragColMove( False )
		self.grid_daftar_pet.EnableDragColSize( True )
		self.grid_daftar_pet.SetColLabelSize( 45 )
		self.grid_daftar_pet.SetColLabelValue( 0, u"Jam Mulai" )
		self.grid_daftar_pet.SetColLabelValue( 1, u"Username Cust" )
		self.grid_daftar_pet.SetColLabelValue( 2, u"Nama Pet" )
		self.grid_daftar_pet.SetColLabelValue( 3, u"Hari" )
		self.grid_daftar_pet.SetColLabelValue( 4, u"Biaya Total" )
		self.grid_daftar_pet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_pet.SetRowSize( 0, 35 )
		self.grid_daftar_pet.SetRowSize( 1, 35 )
		self.grid_daftar_pet.SetRowSize( 2, 35 )
		self.grid_daftar_pet.SetRowSize( 3, 35 )
		self.grid_daftar_pet.SetRowSize( 4, 35 )
		self.grid_daftar_pet.SetRowSize( 5, 35 )
		self.grid_daftar_pet.SetRowSize( 6, 35 )
		self.grid_daftar_pet.SetRowSize( 7, 35 )
		self.grid_daftar_pet.SetRowSize( 8, 35 )
		self.grid_daftar_pet.SetRowSize( 9, 35 )
		self.grid_daftar_pet.EnableDragRowSize( True )
		self.grid_daftar_pet.SetRowLabelSize( 60 )
		self.grid_daftar_pet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_pet.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_daftar_pet.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_daftar_pet.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_pet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_daftar_pet, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer91.Add( ( 250, 0), 0, wx.EXPAND, 5 )

		self.label_hapus = wx.StaticText( self, wx.ID_ANY, u"ID yang Akan Dihapus : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_hapus.Wrap( -1 )

		self.label_hapus.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.label_hapus.SetForegroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer91.Add( self.label_hapus, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		hapus_pet_choiceChoices = [ u"1", u"2", u"3", u"4", u"5", u"6" ]
		self.hapus_pet_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), hapus_pet_choiceChoices, 0 )
		self.hapus_pet_choice.SetSelection( 5 )
		self.hapus_pet_choice.SetMinSize( wx.Size( 125,-1 ) )

		bSizer91.Add( self.hapus_pet_choice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer22.Add( bSizer91, 1, wx.EXPAND, 5 )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.hapus_pet_button = wx.Button( self, wx.ID_ANY, u"HAPUS", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		self.hapus_pet_button.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )
		self.hapus_pet_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		bSizer71.Add( self.hapus_pet_button, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )


		bSizer22.Add( bSizer71, 1, wx.EXPAND, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )
		self.hapus_pet_button.Bind( wx.EVT_BUTTON, self.hapus_hewan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()

	def hapus_hewan( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Lihat_Data_Pelanggan
###########################################################################

class Petugas_Lihat_Data_Pelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_pelanggan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_pelanggan.CreateGrid( 10, 3 )
		self.grid_daftar_pelanggan.EnableEditing( True )
		self.grid_daftar_pelanggan.EnableGridLines( True )
		self.grid_daftar_pelanggan.EnableDragGridSize( True )
		self.grid_daftar_pelanggan.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_pelanggan.SetColSize( 0, 200 )
		self.grid_daftar_pelanggan.SetColSize( 1, 100 )
		self.grid_daftar_pelanggan.SetColSize( 2, 400 )
		self.grid_daftar_pelanggan.EnableDragColMove( False )
		self.grid_daftar_pelanggan.EnableDragColSize( True )
		self.grid_daftar_pelanggan.SetColLabelSize( 45 )
		self.grid_daftar_pelanggan.SetColLabelValue( 0, u"Username Cust" )
		self.grid_daftar_pelanggan.SetColLabelValue( 1, u"Transaksi" )
		self.grid_daftar_pelanggan.SetColLabelValue( 2, u"Nama Cust" )
		self.grid_daftar_pelanggan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_pelanggan.SetRowSize( 0, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 1, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 2, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 3, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 4, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 5, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 6, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 7, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 8, 35 )
		self.grid_daftar_pelanggan.SetRowSize( 9, 35 )
		self.grid_daftar_pelanggan.EnableDragRowSize( True )
		self.grid_daftar_pelanggan.SetRowLabelSize( 60 )
		self.grid_daftar_pelanggan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_pelanggan.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_daftar_pelanggan.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_daftar_pelanggan.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_pelanggan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_daftar_pelanggan, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Lihat_Data_Riwayat_Hewan
###########################################################################

class Petugas_Lihat_Data_Riwayat_Hewan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Pet Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_riwayat_pet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_riwayat_pet.CreateGrid( 10, 6 )
		self.grid_riwayat_pet.EnableEditing( True )
		self.grid_riwayat_pet.EnableGridLines( True )
		self.grid_riwayat_pet.EnableDragGridSize( True )
		self.grid_riwayat_pet.SetMargins( 0, 0 )

		# Columns
		self.grid_riwayat_pet.SetColSize( 0, 150 )
		self.grid_riwayat_pet.SetColSize( 1, 150 )
		self.grid_riwayat_pet.SetColSize( 2, 125 )
		self.grid_riwayat_pet.SetColSize( 3, 125 )
		self.grid_riwayat_pet.SetColSize( 4, 75 )
		self.grid_riwayat_pet.SetColSize( 5, 150 )
		self.grid_riwayat_pet.EnableDragColMove( False )
		self.grid_riwayat_pet.EnableDragColSize( True )
		self.grid_riwayat_pet.SetColLabelSize( 45 )
		self.grid_riwayat_pet.SetColLabelValue( 0, u"Jam Mulai" )
		self.grid_riwayat_pet.SetColLabelValue( 1, u"Jam Selesai" )
		self.grid_riwayat_pet.SetColLabelValue( 2, u"Username Cust" )
		self.grid_riwayat_pet.SetColLabelValue( 3, u"Nama Pet" )
		self.grid_riwayat_pet.SetColLabelValue( 4, u"Hari" )
		self.grid_riwayat_pet.SetColLabelValue( 5, u"Biaya Total" )
		self.grid_riwayat_pet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_riwayat_pet.SetRowSize( 0, 35 )
		self.grid_riwayat_pet.SetRowSize( 1, 35 )
		self.grid_riwayat_pet.SetRowSize( 2, 35 )
		self.grid_riwayat_pet.SetRowSize( 3, 35 )
		self.grid_riwayat_pet.SetRowSize( 4, 35 )
		self.grid_riwayat_pet.SetRowSize( 5, 35 )
		self.grid_riwayat_pet.SetRowSize( 6, 35 )
		self.grid_riwayat_pet.SetRowSize( 7, 35 )
		self.grid_riwayat_pet.SetRowSize( 8, 35 )
		self.grid_riwayat_pet.SetRowSize( 9, 35 )
		self.grid_riwayat_pet.EnableDragRowSize( True )
		self.grid_riwayat_pet.SetRowLabelSize( 60 )
		self.grid_riwayat_pet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_riwayat_pet.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_riwayat_pet.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_riwayat_pet.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_riwayat_pet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_riwayat_pet, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Lihat_Data_Hewan
###########################################################################

class Petugas_Lihat_Data_Hewan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Pet Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_daftar_pet = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_daftar_pet.CreateGrid( 10, 5 )
		self.grid_daftar_pet.EnableEditing( True )
		self.grid_daftar_pet.EnableGridLines( True )
		self.grid_daftar_pet.EnableDragGridSize( True )
		self.grid_daftar_pet.SetMargins( 0, 0 )

		# Columns
		self.grid_daftar_pet.SetColSize( 0, 200 )
		self.grid_daftar_pet.SetColSize( 1, 125 )
		self.grid_daftar_pet.SetColSize( 2, 125 )
		self.grid_daftar_pet.SetColSize( 3, 75 )
		self.grid_daftar_pet.SetColSize( 4, 150 )
		self.grid_daftar_pet.EnableDragColMove( False )
		self.grid_daftar_pet.EnableDragColSize( True )
		self.grid_daftar_pet.SetColLabelSize( 45 )
		self.grid_daftar_pet.SetColLabelValue( 0, u"Jam Mulai" )
		self.grid_daftar_pet.SetColLabelValue( 1, u"Username Cust" )
		self.grid_daftar_pet.SetColLabelValue( 2, u"Nama Pet" )
		self.grid_daftar_pet.SetColLabelValue( 3, u"Hari" )
		self.grid_daftar_pet.SetColLabelValue( 4, u"Biaya Total" )
		self.grid_daftar_pet.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_daftar_pet.SetRowSize( 0, 35 )
		self.grid_daftar_pet.SetRowSize( 1, 35 )
		self.grid_daftar_pet.SetRowSize( 2, 35 )
		self.grid_daftar_pet.SetRowSize( 3, 35 )
		self.grid_daftar_pet.SetRowSize( 4, 35 )
		self.grid_daftar_pet.SetRowSize( 5, 35 )
		self.grid_daftar_pet.SetRowSize( 6, 35 )
		self.grid_daftar_pet.SetRowSize( 7, 35 )
		self.grid_daftar_pet.SetRowSize( 8, 35 )
		self.grid_daftar_pet.SetRowSize( 9, 35 )
		self.grid_daftar_pet.EnableDragRowSize( True )
		self.grid_daftar_pet.SetRowLabelSize( 60 )
		self.grid_daftar_pet.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_daftar_pet.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_daftar_pet.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_daftar_pet.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_daftar_pet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_daftar_pet, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()


###########################################################################
## Class Petugas_Lihat_Data_Harga
###########################################################################

class Petugas_Lihat_Data_Harga ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Titip.in", pos = wx.DefaultPosition, size = wx.Size( 1080,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		self.SetBackgroundColour( wx.Colour( 213, 229, 249 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel10.SetMaxSize( wx.Size( -1,75 ) )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 20, 0), 0, wx.EXPAND, 5 )

		self.greeting_user = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Selamat Datang, Pengguna!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.greeting_user.Wrap( -1 )

		self.greeting_user.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Raleway" ) )

		bSizer4.Add( self.greeting_user, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer4.Add( ( 550, 0), 0, wx.EXPAND, 5 )

		self.btn_logout = wx.Button( self.m_panel10, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_logout, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel10.SetSizer( bSizer4 )
		self.m_panel10.Layout()
		bSizer4.Fit( self.m_panel10 )
		bSizer9.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 0 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer14.SetMinSize( wx.Size( -1,615 ) )

		bSizer14.Add( ( 0, 5), 0, wx.EXPAND, 5 )

		self.btn_tambah_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 0, wx.EXPAND, 5 )

		self.btn_tambah_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data Pet Baru", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_tambah_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_hapus_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Hapus Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_hapus_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pelanggan = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pelanggan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pelanggan, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_pet = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Data Pet", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_pet, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_lihat_riwayat = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Riwayat Penitipan", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_lihat_riwayat, 0, wx.ALL, 5 )


		bSizer14.Add( ( 0, 30), 1, wx.EXPAND, 5 )

		self.btn_harga_kategori = wx.Button( self.m_panel7, wx.ID_ANY, u"Lihat Daftar Harga", wx.DefaultPosition, wx.Size( 190,50 ), 0 )
		bSizer14.Add( self.btn_harga_kategori, 0, wx.ALL, 5 )


		self.m_panel7.SetSizer( bSizer14 )
		self.m_panel7.Layout()
		bSizer14.Fit( self.m_panel7 )
		bSizer21.Add( self.m_panel7, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.LI_VERTICAL )
		bSizer21.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 0 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )


		bSizer22.Add( ( 0, 50), 0, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tabel Daftar Harga Per Hari", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Raleway SemiBold" ) )

		bSizer22.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer22.Add( ( 0, 40), 0, wx.EXPAND, 5 )

		self.grid_harga_kategori = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_harga_kategori.CreateGrid( 10, 2 )
		self.grid_harga_kategori.EnableEditing( True )
		self.grid_harga_kategori.EnableGridLines( True )
		self.grid_harga_kategori.EnableDragGridSize( True )
		self.grid_harga_kategori.SetMargins( 0, 0 )

		# Columns
		self.grid_harga_kategori.SetColSize( 0, 300 )
		self.grid_harga_kategori.SetColSize( 1, 300 )
		self.grid_harga_kategori.EnableDragColMove( False )
		self.grid_harga_kategori.EnableDragColSize( True )
		self.grid_harga_kategori.SetColLabelSize( 45 )
		self.grid_harga_kategori.SetColLabelValue( 0, u"Kategori Hewan" )
		self.grid_harga_kategori.SetColLabelValue( 1, u"Harga Per Hari" )
		self.grid_harga_kategori.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_harga_kategori.SetRowSize( 0, 35 )
		self.grid_harga_kategori.SetRowSize( 1, 35 )
		self.grid_harga_kategori.SetRowSize( 2, 35 )
		self.grid_harga_kategori.SetRowSize( 3, 35 )
		self.grid_harga_kategori.SetRowSize( 4, 35 )
		self.grid_harga_kategori.SetRowSize( 5, 35 )
		self.grid_harga_kategori.SetRowSize( 6, 35 )
		self.grid_harga_kategori.SetRowSize( 7, 35 )
		self.grid_harga_kategori.SetRowSize( 8, 35 )
		self.grid_harga_kategori.SetRowSize( 9, 35 )
		self.grid_harga_kategori.EnableDragRowSize( True )
		self.grid_harga_kategori.SetRowLabelSize( 60 )
		self.grid_harga_kategori.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.grid_harga_kategori.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.grid_harga_kategori.SetLabelFont( wx.Font( 11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "PT Sans" ) )
		self.grid_harga_kategori.SetLabelTextColour( wx.Colour( 255, 255, 255 ) )

		# Cell Defaults
		self.grid_harga_kategori.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer22.Add( self.grid_harga_kategori, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer21.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer21, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_logout.Bind( wx.EVT_BUTTON, self.logout_verify )
		self.btn_tambah_pelanggan.Bind( wx.EVT_BUTTON, self.window_tambah_data_pelanggan )
		self.btn_tambah_pet.Bind( wx.EVT_BUTTON, self.window_tambah_data_pet )
		self.btn_hapus_pet.Bind( wx.EVT_BUTTON, self.window_hapus_data_pet )
		self.btn_lihat_pelanggan.Bind( wx.EVT_BUTTON, self.window_lihat_data_pelanggan )
		self.btn_lihat_pet.Bind( wx.EVT_BUTTON, self.window_lihat_data_pet )
		self.btn_lihat_riwayat.Bind( wx.EVT_BUTTON, self.window_lihat_riwayat_penitipan )
		self.btn_harga_kategori.Bind( wx.EVT_BUTTON, self.window_lihat_daftar_harga )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def logout_verify( self, event ):
		event.Skip()

	def window_tambah_data_pelanggan( self, event ):
		event.Skip()

	def window_tambah_data_pet( self, event ):
		event.Skip()

	def window_hapus_data_pet( self, event ):
		event.Skip()

	def window_lihat_data_pelanggan( self, event ):
		event.Skip()

	def window_lihat_data_pet( self, event ):
		event.Skip()

	def window_lihat_riwayat_penitipan( self, event ):
		event.Skip()

	def window_lihat_daftar_harga( self, event ):
		event.Skip()


