# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiCondensed" ) )
		self.SetBackgroundColour( wx.Colour( 148, 180, 226 ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Video Downloader", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.link_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.link_box, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		quality_selection_drop_downChoices = [ u"4k", u"2k", u"1080p", u"720p", u"480p", u"360p", u"240p", u"144p" ]
		self.quality_selection_drop_down = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, quality_selection_drop_downChoices, 0 )
		self.quality_selection_drop_down.SetSelection( 2 )
		gbSizer1.Add( self.quality_selection_drop_down, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Mp3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_checkBox1, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Non-youtube", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_checkBox2, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_button1, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Clip Downloader", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.clip_start_box = wx.TextCtrl( self, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gbSizer1.Add( self.clip_start_box, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Clip Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.clip_end_box = wx.TextCtrl( self, wx.ID_ANY, u"00:00", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		gbSizer1.Add( self.clip_end_box, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Clip End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Download Clip Mp4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_button2, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Download Clip mp3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_button3, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Bahnschrift SemiBold SemiConden" ) )

		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_custom_args, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.video_dl )
		self.m_button2.Bind( wx.EVT_BUTTON, self.clip_dl )
		self.m_button3.Bind( wx.EVT_BUTTON, self.clip_mp3_dl )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def video_dl( self, event ):
		event.Skip()

	def clip_dl( self, event ):
		event.Skip()

	def clip_mp3_dl( self, event ):
		event.Skip()


