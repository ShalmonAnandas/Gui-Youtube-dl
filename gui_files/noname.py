# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import wx.adv

###########################################################################
## Class home_frame
###########################################################################

class home_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GUI Youtube-dl", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid = wx.Button( self, wx.ID_ANY, u"Single Video", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid.SetLabelMarkup( u"Single Video" )
		self.vid.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.vid.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.vid.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.vid, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_vid = wx.Button( self, wx.ID_ANY, u"Multiple Videos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_vid.SetLabelMarkup( u"Multiple Videos" )
		self.mul_vid.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.mul_vid.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.mul_vid.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.mul_vid, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.clip = wx.Button( self, wx.ID_ANY, u"Single Clip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clip.SetLabelMarkup( u"Single Clip" )
		self.clip.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.clip.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.clip.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.clip.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.clip, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_clip = wx.Button( self, wx.ID_ANY, u"Multiple Clips", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_clip.SetLabelMarkup( u"Multiple Clips" )
		self.mul_clip.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_clip.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.mul_clip.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.mul_clip.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.mul_clip, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.aud = wx.Button( self, wx.ID_ANY, u"Single Audio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aud.SetLabelMarkup( u"Single Audio" )
		self.aud.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.aud.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.aud.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.aud.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.aud, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_aud = wx.Button( self, wx.ID_ANY, u"Multiple Audio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_aud.SetLabelMarkup( u"Multiple Audio" )
		self.mul_aud.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_aud.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.mul_aud.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )
		self.mul_aud.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.mul_aud, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.vid.Bind( wx.EVT_BUTTON, self.single_vid_func )
		self.mul_vid.Bind( wx.EVT_BUTTON, self.mul_vid_func )
		self.clip.Bind( wx.EVT_BUTTON, self.clip_func )
		self.mul_clip.Bind( wx.EVT_BUTTON, self.mul_clip_func )
		self.aud.Bind( wx.EVT_BUTTON, self.aud_func )
		self.mul_aud.Bind( wx.EVT_BUTTON, self.mul_aud_func )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def single_vid_func( self, event ):
		event.Skip()

	def mul_vid_func( self, event ):
		event.Skip()

	def clip_func( self, event ):
		event.Skip()

	def mul_clip_func( self, event ):
		event.Skip()

	def aud_func( self, event ):
		event.Skip()

	def mul_aud_func( self, event ):
		event.Skip()


###########################################################################
## Class vid_frame
###########################################################################

class vid_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Video Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid_sizer = wx.StaticText( self, wx.ID_ANY, u"Single Video Download", wx.DefaultPosition, wx.Size( 300,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.vid_sizer.Wrap( -1 )

		self.vid_sizer.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_SEMIBOLD, False, "Quicksand SemiBold" ) )
		self.vid_sizer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		gbSizer2.Add( self.vid_sizer, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.EXPAND|wx.ALL, 10 )

		self.vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link_label.Wrap( -1 )

		self.vid_link_label.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid_link_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		gbSizer2.Add( self.vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.vid_link, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"2160p (4K)", u"1440p (2K)", u"1080p (FHD)", u"720p (HD)", u"480p", u"360p", u"240p", u"144p" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"11; Default; Quicksand SemiBold; Normal; Normal; Not Underlined", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		self.m_comboBox1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_dirPicker1.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer2.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_dl_button.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid_dl_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.vid_dl_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer2.Add( self.vid_dl_button, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Cookies :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText31.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer2.Add( self.m_staticText31, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Replace with your cookies file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.cookie_picker.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.cookie_picker, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText32.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer2.Add( self.m_staticText32, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"asddasd" )
		self.custom_args.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.custom_args, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( gbSizer2 )
		self.Layout()
		gbSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.vid_dl_button.Bind( wx.EVT_BUTTON, self.vid_dl )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def vid_dl( self, event ):
		event.Skip()


###########################################################################
## Class mul_vid_frame
###########################################################################

class mul_vid_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multi-Vid Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.mul_vid_label = wx.StaticText( self, wx.ID_ANY, u"Multi Video Downloader", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.mul_vid_label.Wrap( -1 )

		self.mul_vid_label.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer3.Add( self.m_staticline4, wx.GBPosition( 0, 3 ), wx.GBSpan( 5, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Links", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.mul_vid_link_label.Wrap( -1 )

		self.mul_vid_link_label.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_link_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_textCtrl2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.add_link_button = wx.Button( self, wx.ID_ANY, u"Add Link", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.add_link_button.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.add_link_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.add_link_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.add_link_button, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_richText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_richText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer3.Add( self.m_richText2, wx.GBPosition( 1, 4 ), wx.GBSpan( 5, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"2160p (4K)", u"1440p (2K)", u"1080p (FHD)", u"720p (HD)", u"480p", u"360p", u"240p", u"144p" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		self.m_comboBox1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( -1,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_vid_dl_button.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_dl_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.mul_vid_dl_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.mul_vid_dl_button, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Cookies :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText33.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText33, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.cookie_picker.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.cookie_picker, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText34.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText34, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom_args.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.custom_args, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button10.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button10, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button101 = wx.Button( self, wx.ID_ANY, u"Clear All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button101.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button101.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button101.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button101, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()
		gbSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_link_button.Bind( wx.EVT_BUTTON, self.add_link_func )
		self.mul_vid_dl_button.Bind( wx.EVT_BUTTON, self.mul_vid_dl )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clear_link )
		self.m_button101.Bind( wx.EVT_BUTTON, self.clear_all_links )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_link_func( self, event ):
		event.Skip()

	def mul_vid_dl( self, event ):
		event.Skip()

	def clear_link( self, event ):
		event.Skip()

	def clear_all_links( self, event ):
		event.Skip()


###########################################################################
## Class clip_frame
###########################################################################

class clip_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Clip Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid_sizer = wx.StaticText( self, wx.ID_ANY, u"Clip Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_sizer.Wrap( -1 )

		self.vid_sizer.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid_sizer.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.vid_sizer, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 10 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Clip Settings", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.m_staticText19, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link_label.Wrap( -1 )

		self.vid_link_label.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid_link_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.vid_link, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer2.Add( self.m_staticline2, wx.GBPosition( 0, 2 ), wx.GBSpan( 3, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.m_staticText20, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_timePicker2 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.TP_DEFAULT )
		self.m_timePicker2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.m_timePicker2, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"BEST", u"WORST" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		self.m_comboBox1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.m_staticText21, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker3 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 125,-1 ), wx.adv.TP_DEFAULT )
		self.m_timePicker3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.m_timePicker3, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer2.Add( self.m_staticline3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.m_dirPicker1, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Cookies: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText35.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer2.Add( self.m_staticText35, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.cookie_picker.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.cookie_picker, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Custom Args: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText36.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer2.Add( self.m_staticText36, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom_args.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer2.Add( self.custom_args, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )

		self.vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_dl_button.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.vid_dl_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.vid_dl_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer2.Add( self.vid_dl_button, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer2 )
		self.Layout()
		gbSizer2.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.vid_dl_button.Bind( wx.EVT_BUTTON, self.clip_dl )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def clip_dl( self, event ):
		event.Skip()


###########################################################################
## Class mul_clip_frame
###########################################################################

class mul_clip_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multi-Clip Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.mul_vid_label = wx.StaticText( self, wx.ID_ANY, u"Multi Clip Download", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.mul_vid_label.Wrap( -1 )

		self.mul_vid_label.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer3.Add( self.m_staticline3, wx.GBPosition( 0, 3 ), wx.GBSpan( 8, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Clip List", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Paste link :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.mul_vid_link_label.Wrap( -1 )

		self.mul_vid_link_label.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_link_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_textCtrl2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_richText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		gbSizer3.Add( self.m_richText2, wx.GBPosition( 1, 4 ), wx.GBSpan( 6, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker3 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.TP_DEFAULT )
		self.m_timePicker3.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_timePicker3, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Add Clip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.SetFont( wx.Font( 17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button18.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button18, wx.GBPosition( 2, 2 ), wx.GBSpan( 2, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		self.m_staticText28.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText28.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText28, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker4 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )
		self.m_timePicker4.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_timePicker4, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_dirPicker1, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Cookies : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		self.m_staticText37.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText37.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText37, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.cookie_picker.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.cookie_picker, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText38.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText38, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom_args.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.custom_args, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_vid_dl_button.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_dl_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.mul_vid_dl_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.mul_vid_dl_button, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button10.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button10, wx.GBPosition( 7, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Clear All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button20.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button20.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button20.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button20, wx.GBPosition( 7, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()
		gbSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.add_clip_func )
		self.mul_vid_dl_button.Bind( wx.EVT_BUTTON, self.mul_clip_dl )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clear_link )
		self.m_button20.Bind( wx.EVT_BUTTON, self.clear_all_links )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_clip_func( self, event ):
		event.Skip()

	def mul_clip_dl( self, event ):
		event.Skip()

	def clear_link( self, event ):
		event.Skip()

	def clear_all_links( self, event ):
		event.Skip()


###########################################################################
## Class aud_frame
###########################################################################

class aud_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Single Audio Download", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer6.Add( self.m_staticText31, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer6.Add( self.m_staticText32, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl5.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer6.Add( self.m_textCtrl5, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_dirPicker5 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 250,-1 ), wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker5.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer6.Add( self.m_dirPicker5, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Cookies :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		self.m_staticText39.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText39.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer6.Add( self.m_staticText39, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.cookie_picker.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer6.Add( self.cookie_picker, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		self.m_staticText40.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText40.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer6.Add( self.m_staticText40, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.custom_args.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer6.Add( self.custom_args, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText33.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer6.Add( self.m_staticText33, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button18.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer6.Add( self.m_button18, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer6 )
		self.Layout()
		gbSizer6.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.audio_dl )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def audio_dl( self, event ):
		event.Skip()


###########################################################################
## Class mul_aud_frame
###########################################################################

class mul_aud_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Multi-Vid Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.mul_vid_label = wx.StaticText( self, wx.ID_ANY, u"Multi Audio Downloader", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.mul_vid_label.Wrap( -1 )

		self.mul_vid_label.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer3.Add( self.m_staticline4, wx.GBPosition( 0, 3 ), wx.GBSpan( 7, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Links", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Paste link :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.mul_vid_link_label.Wrap( -1 )

		self.mul_vid_link_label.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_link_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.mul_vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_textCtrl2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.add_link_button = wx.Button( self, wx.ID_ANY, u"Add Link", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.add_link_button.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.add_link_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.add_link_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.add_link_button, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_richText2.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_richText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_richText2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		gbSizer3.Add( self.m_richText2, wx.GBPosition( 1, 4 ), wx.GBSpan( 5, 2 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"2160p (4K)", u"1440p (2K)", u"1080p (FHD)", u"720p (HD)", u"480p", u"360p", u"240p", u"144p" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		self.m_comboBox1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.m_dirPicker1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )

		gbSizer3.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Cookies :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText41.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText41, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.cookie_picker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer3.Add( self.cookie_picker, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Custom Args :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_staticText42.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gbSizer3.Add( self.m_staticText42, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.custom_args, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_vid_dl_button.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.mul_vid_dl_button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.mul_vid_dl_button.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.mul_vid_dl_button, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button10.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_button10.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button10, wx.GBPosition( 6, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Clear All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Quicksand SemiBold" ) )
		self.m_button24.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_button24.SetBackgroundColour( wx.Colour( 46, 52, 64 ) )

		gbSizer3.Add( self.m_button24, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()
		gbSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_link_button.Bind( wx.EVT_BUTTON, self.add_link_func )
		self.mul_vid_dl_button.Bind( wx.EVT_BUTTON, self.mul_aud_dl )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clear_link )
		self.m_button24.Bind( wx.EVT_BUTTON, self.clear_all_links )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_link_func( self, event ):
		event.Skip()

	def mul_aud_dl( self, event ):
		event.Skip()

	def clear_link( self, event ):
		event.Skip()

	def clear_all_links( self, event ):
		event.Skip()


