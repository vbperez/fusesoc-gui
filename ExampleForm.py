# -*- coding: utf-8 -*- 

import wx

class subclase_frame(wx.Frame):
	def __init__(self):
		# Call the init (constructor code) of the wx.Frame inherited.
		# Create a panel that contain all the widget
		wx.Frame.__init__(self, None, -1, 'Registro (Subclase de Frame)',
		pos=wx.Point(200, 200),size=wx.Size(400,340))
		self.panel = wx.Panel(self, -1)
		
		# We create  3 widget wx.StaticText,
		# 3 widget wx.TextCtrl and one widget wx.Button,

		# Name.
		self.labelName = wx.StaticText(id=-1,label='Name',
		name='labelName', parent=self.panel,pos=wx.Point(16, 20),
		size=wx.Size(54, 18), style=0)

		self.textName = wx.TextCtrl(id=-1, name='textName',
		parent=self.panel, pos=wx.Point(80, 20), size=wx.Size(288, 21))

		# Surname.
		self.labelSurname = wx.StaticText(id=-1,label='Surname',
		name='labelSurname', parent=self.panel,pos=wx.Point(16, 50),
		size=wx.Size(56, 18), style=0)

		self.textSurname = wx.TextCtrl(id=-1, name='textSurname',
		parent=self.panel, pos=wx.Point(80, 50), size=wx.Size(288, 21))

		# ID.
		self.labelID = wx.StaticText(id=-1,label='ID',
		name='labelID', parent=self.panel,pos=wx.Point(16, 80),
		size=wx.Size(54, 18), style=0)

		self.textID = wx.TextCtrl(id=-1, name='textID',parent=self.panel,
		pos=wx.Point(80, 80), size=wx.Size(288, 21))

		# Addres.
		self.labelAddres = wx.StaticText(id=-1,label='Addres',
		name='labelAddres', parent=self.panel,pos=wx.Point(16, 110),
		size=wx.Size(54, 18), style=0)

		self.textAddres = wx.TextCtrl(id=-1, name='textAddres',
		parent=self.panel,pos=wx.Point(80, 110), size=wx.Size(288, 21))

		# Postal code.
		self.labelPC = wx.StaticText(id=-1,label='Post.code',
		name='labelPC', parent=self.panel,pos=wx.Point(16, 140),
		size=wx.Size(54, 18), style=0)

		self.textPC = wx.TextCtrl(id=-1, name='textPC',
		parent=self.panel,pos=wx.Point(80, 140), size=wx.Size(50, 21))

		# City.
		self.etiquetaPoblacion = wx.StaticText(id=-1,label='City',
		name='labelCity', parent=self.panel,pos=wx.Point(140, 140),
		size=wx.Size(54, 18), style=0)

		self.textCity = wx.TextCtrl(id=-1, name='textCity',
		parent=self.panel,pos=wx.Point(200, 140), size=wx.Size(170, 21))

		# Country.
		self.labelCountry = wx.StaticText(id=-1,label='Country',
		name='labelCountry', parent=self.panel,pos=wx.Point(16, 170),
		size=wx.Size(54, 18), style=0)

		self.textCountry = wx.TextCtrl(id=-1, name='textCountry',
		parent=self.panel,pos=wx.Point(80, 170), size=wx.Size(288, 21))

		
		# Button save
		self.botonSave = wx.Button(parent=self.panel,id=-1,label="Save",
		pos=wx.Point(200,210),size=wx.Size(75,23))
		
		# Button exit
		self.botonExit = wx.Button(parent=self.panel,id=-1,label="Exit",
		pos=wx.Point(296,210),size=wx.Size(75,23))

		# We create event handlers, linking events to methods that have the associated code.
		self.Bind(wx.EVT_BUTTON, self.OnButtonExit, self.botonExit)
		self.Bind(wx.EVT_BUTTON, self.OnButtonSave, self.botonSave)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		
		
	# We define the methods that contain code that is executed 
	# when called at the request of the events defined above.

	def OnButtonExit(self, event):
		# Close window.
		self.Close(True)
		
		
	def OnButtonSave(self, event):
		# Save information in a file
		archivo = open("file.txt", "a")
		data="Name: "
		data+=self.textName.GetValue()
		data+="  Surname: "
		data+=self.textSurname.GetValue()
		data+="  Id: "
		data+=self.textID.GetValue()
		data+="  Addres: "
		data+=self.textAddres.GetValue()
		data+="  Postal Code: "
		data+=self.textPC.GetValue()
		data+="  City: "
		data+=self.textCity.GetValue()
		data+="  Country: "
		data+=self.textCountry.GetValue()
		data+="\n"
	
		archivo.write(data)
		archivo.close()
		
		self.textName.Clear()
		self.textSurname.Clear()
		self.textID.Clear()
		self.textAddres.Clear()
		self.textPC.Clear()
		self.textCity.Clear()
		self.textCountry.Clear()
		

	def OnClose(self, event):
		# Destroy widget.
		self.Destroy()


# Create a simple aplication wx.
aplicacion = wx.PySimpleApp()

# Create frame object, result of the  instantiation  of
# subclase_frame.
frame = subclase_frame()

# Show the  instantiation of subclase_frame.
frame.Show()

# Launch the MainLoop to hear requests for events.
aplicacion.MainLoop()	
