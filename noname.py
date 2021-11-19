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

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid = wx.Button( self, wx.ID_ANY, u"Single Video", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.vid, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_vid = wx.Button( self, wx.ID_ANY, u"Multiple Videos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_vid.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.mul_vid, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.clip = wx.Button( self, wx.ID_ANY, u"Single Clip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clip.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.clip, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_clip = wx.Button( self, wx.ID_ANY, u"Multiple Clips", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mul_clip.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.mul_clip, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.aud = wx.Button( self, wx.ID_ANY, u"Single Audio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.aud.SetMinSize( wx.Size( 200,50 ) )

		gbSizer1.Add( self.aud, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.mul_aud = wx.Button( self, wx.ID_ANY, u"Multiple Audio", wx.DefaultPosition, wx.DefaultSize, 0 )
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


###########################################################################
## Class vid_frame
###########################################################################

class vid_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Video Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid_sizer = wx.StaticText( self, wx.ID_ANY, u"Single Video Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_sizer.Wrap( -1 )

		gbSizer2.Add( self.vid_sizer, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 10 )

		self.vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link_label.Wrap( -1 )

		gbSizer2.Add( self.vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.vid_link, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"2160p (4K)", u"1440p (2K)", u"1080p (FHD)", u"720p (HD)", u"480p", u"360p", u"240p", u"144p" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		gbSizer2.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer2.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.vid_dl_button, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


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

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.mul_vid_label = wx.StaticText( self, wx.ID_ANY, u"Multiple Video Downloader", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.mul_vid_label.Wrap( -1 )

		gbSizer3.Add( self.mul_vid_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Links", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Paste link :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.mul_vid_link_label.Wrap( -1 )

		gbSizer3.Add( self.mul_vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_textCtrl2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.add_link_button = wx.Button( self, wx.ID_ANY, u"Add Link", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.add_link_button, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gbSizer3.Add( self.m_richText2, wx.GBPosition( 1, 3 ), wx.GBSpan( 3, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"2160p (4K)", u"1440p (2K)", u"1080p (FHD)", u"720p (HD)", u"480p", u"360p", u"240p", u"144p" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 2 )
		gbSizer3.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer3.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.mul_vid_dl_button, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button10, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()
		gbSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.add_link_button.Bind( wx.EVT_BUTTON, self.add_link_func )
		self.mul_vid_dl_button.Bind( wx.EVT_BUTTON, self.mul_vid_dl )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clear_links )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def add_link_func( self, event ):
		event.Skip()

	def mul_vid_dl( self, event ):
		event.Skip()

	def clear_links( self, event ):
		event.Skip()


###########################################################################
## Class clip_frame
###########################################################################

class clip_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Clip Downloader", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.vid_sizer = wx.StaticText( self, wx.ID_ANY, u"Clip Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_sizer.Wrap( -1 )

		gbSizer2.Add( self.vid_sizer, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 10 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Clip Settings", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText19.Wrap( -1 )

		gbSizer2.Add( self.m_staticText19, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Link :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vid_link_label.Wrap( -1 )

		gbSizer2.Add( self.vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_link = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.vid_link, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer2.Add( self.m_staticline2, wx.GBPosition( 0, 2 ), wx.GBSpan( 3, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		gbSizer2.Add( self.m_staticText20, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_timePicker2 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.TP_DEFAULT )
		gbSizer2.Add( self.m_timePicker2, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Quality :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		m_comboBox1Choices = [ u"BEST", u"WORST" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		gbSizer2.Add( self.m_comboBox1, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		gbSizer2.Add( self.m_staticText21, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker3 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.TP_DEFAULT )
		gbSizer2.Add( self.m_timePicker3, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer2.Add( self.m_staticline3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer2.Add( self.m_dirPicker1, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.vid_dl_button, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


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

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.mul_vid_label = wx.StaticText( self, wx.ID_ANY, u"Multi Clip Download", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.mul_vid_label.Wrap( -1 )

		gbSizer3.Add( self.mul_vid_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		gbSizer3.Add( self.m_staticline3, wx.GBPosition( 0, 3 ), wx.GBSpan( 5, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Clip List", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText10.Wrap( -1 )

		gbSizer3.Add( self.m_staticText10, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_link_label = wx.StaticText( self, wx.ID_ANY, u"Paste link :", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.mul_vid_link_label.Wrap( -1 )

		gbSizer3.Add( self.mul_vid_link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_textCtrl2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )

		self.m_richText2 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gbSizer3.Add( self.m_richText2, wx.GBPosition( 1, 4 ), wx.GBSpan( 4, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Start :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer3.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker3 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )
		gbSizer3.Add( self.m_timePicker3, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Add Clip", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button18, wx.GBPosition( 2, 2 ), wx.GBSpan( 2, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"End :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		gbSizer3.Add( self.m_staticText28, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_timePicker4 = wx.adv.TimePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )
		gbSizer3.Add( self.m_timePicker4, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer3.Add( self.m_staticText7, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer3.Add( self.m_dirPicker1, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.mul_vid_dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.mul_vid_dl_button, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button10, wx.GBPosition( 5, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()
		gbSizer3.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.mul_vid_dl_button.Bind( wx.EVT_BUTTON, self.mul_vid_dl )
		self.m_button10.Bind( wx.EVT_BUTTON, self.clear_links )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def mul_vid_dl( self, event ):
		event.Skip()

	def clear_links( self, event ):
		event.Skip()


