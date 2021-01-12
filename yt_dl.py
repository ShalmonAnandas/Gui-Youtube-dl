# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		self.SetBackgroundColour( wx.Colour( 82, 90, 105 ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Youtube Downloader", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.title.Wrap( -1 )
		self.title.SetFont( wx.Font( 20, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.title.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.title, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.link_label = wx.StaticText( self, wx.ID_ANY, u"Paste link :", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.ALIGN_LEFT )
		self.link_label.Wrap( -1 )
		self.link_label.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.link_label.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.link_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.link_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 370,-1 ), 0 )
		gbSizer1.Add( self.link_box, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		quality_selection_drop_downChoices = [ u"720p", u"Best Quality Available", u"Audio (mp3)", u"Non Youtube" ]
		self.quality_selection_drop_down = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), quality_selection_drop_downChoices, 0 )
		self.quality_selection_drop_down.SetSelection( 4 )
		gbSizer1.Add( self.quality_selection_drop_down, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.select_quality_label = wx.StaticText( self, wx.ID_ANY, u"Select Quality :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.select_quality_label.Wrap( -1 )
		self.select_quality_label.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.select_quality_label.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.select_quality_label, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gbSizer1.Add( self.m_dirPicker1, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Set Download Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.m_staticText6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.dl_button = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		self.dl_button.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.dl_button.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.dl_button.SetBackgroundColour( wx.Colour( 94, 104, 121 ) )
		
		gbSizer1.Add( self.dl_button, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 2 )
		
		self.clip_start_label = wx.StaticText( self, wx.ID_ANY, u"Clip Start (00:00) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clip_start_label.Wrap( -1 )
		self.clip_start_label.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.clip_start_label.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.clip_start_label, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.clip_start_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 115,-1 ), 0 )
		self.clip_start_box.SetMaxLength( 5 ) 
		gbSizer1.Add( self.clip_start_box, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clip_end_label = wx.StaticText( self, wx.ID_ANY, u"Clip End (00:00) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clip_end_label.Wrap( -1 )
		self.clip_end_label.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.clip_end_label.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.clip_end_label, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.clip_end_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,-1 ), 0 )
		self.clip_end_box.SetMaxLength( 5 ) 
		gbSizer1.Add( self.clip_end_box, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.clip_dl_button = wx.Button( self, wx.ID_ANY, u"Download Clip", wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		self.clip_dl_button.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.clip_dl_button.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.clip_dl_button.SetBackgroundColour( wx.Colour( 94, 104, 121 ) )
		
		gbSizer1.Add( self.clip_dl_button, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.clip_dl_mp3_button = wx.Button( self, wx.ID_ANY, u"Download Clip mp3", wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		self.clip_dl_mp3_button.SetFont( wx.Font( 14, 74, 90, 92, False, "Bahnschrift SemiBold Condensed" ) )
		self.clip_dl_mp3_button.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.clip_dl_mp3_button.SetBackgroundColour( wx.Colour( 94, 104, 121 ) )
		
		gbSizer1.Add( self.clip_dl_mp3_button, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Custom Args (advanced) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		
		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_custom_args = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_custom_args, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		gbSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.dl_button.Bind( wx.EVT_BUTTON, self.video_dl )
		self.clip_dl_button.Bind( wx.EVT_BUTTON, self.clip_dl )
		self.clip_dl_mp3_button.Bind( wx.EVT_BUTTON, self.clip_dl_mp3 )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def video_dl( self, event ):
		event.Skip()
	
	def clip_dl( self, event ):
		event.Skip()
	
	def clip_dl_mp3( self, event ):
		event.Skip()
	

