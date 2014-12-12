#!/usr/bin/env python
# -*- codes: utf-8 -*-
# File name: Class.py
# Author: Lee.HJ

import Include
import Operate

class Customer(object):

	def __init__(self):
		pass

	def Add(self):
		pass

	# Search information and show it
	def Search(self, ID):
		self.SearchID = ID
		if ID == 0:
			Table = self.Linkman_Table
		else:
			Table = self.Table

		self.SearchInfo = Operate.Search(self.SearchID, Table)#  2
		
		if self.SearchInfo:
			for info in self.SearchInfo:

				self.ID = int(info[0])
				print "Id: %d" % self.ID

				Len =  len(info)

				#Group
				if Len == 2:
					self.Linkman_Table = info[1]
					print "Linkman_Table: %s" % self.Linkman_Table
					self.Linkman = Linkman(self.Linkman_Table)

				# Personal
				else:
					self.Name = info[1]
					self.Phone = info[2]
					self.Email = info[3]
					print "Name: %s" % self.Name
					print "Phone: %s" % self.Phone
					print "Email:%s" % self.Email

				# Linkman
				if Len == 6:
					self.Official_Phone = info[4]
					self.Position = info[5]
					print "Official Phone: %s" % self.Official_Phone
					print "Position: %s" % self.Position
		else:
			print "No information! Please try again!"
	
	# Delete if it named ID is exist and show it
	def Delete(self):
		self.DeleteID = raw_input("Please put into ID you want to Delete:")
		self.DeleteInfo = Operate.Delete(self.DeleteID, self.Table)#  3
		
		if self.DeleteInfo:
			print "The customer is deleted"
			#for info in self.SearchInfo:
			#	print "Id: %s" % self.SearchInfo[0][0]
			#	print "Name: %s" % self.SearchInfo[0][1]
			#	print "Phone: %s" % self.SearchInfo[0][2]
			#	print "Email:%s" % self.SearchInfo[0][3]
		else:
			print "No finding with ID = %s! Please try again!" % self.DeleteID
	
	def ShowID(self):
		return self.ID

class Personal(Customer):
	
	def __init__(self):
		self.ID = None
		self.Name = None
		self.Phone = None
		self.Email = None
		self.Table = 'Personal_table'
		Operate.Personal_Create(self.Table)
	
	def Add(self):
		self.Name = raw_input("Please put into your name:")	
		self.Phone = raw_input("Please put into your Phone number:")
		self.Email = raw_input("Please put into your Email:")
		self.ID = Operate.NextID(self.Table)
		self.AddInfo = Operate.Personal_Add(self.ID, self.Name, self.Phone, self.Email, self.Table)
		if self.AddInfo == 1:
			print "Add success!"
		else:
			print "Add Error!"

	def ShowName(self):
		return self.Name
	
	def ShowPhone(self):
		return self.Phone
	
	def ShowEmail(self):
		return self.Email

	def ShowInfo(self):
		print "ID: %s" % self.ShowID()
		print "Name: %s" % self.ShowName()
		print "Phone: %s" % self.ShowPhone()
		print "Email: %s" % self.ShowEmail()


class Group(Customer):
	
	def __init__(self):
		self.ID = None
		self.Linkman_Table = None
		self.Table = 'Group_table'
		Operate.Group_Create(self.Table)

	def Add(self):
		self.ID = Operate.NextID(self.Table)
		self.Linkman_Table = ('Linkman_' + str(self.ID))
		self.AddInfo = Operate.Group_Add(self.ID, self.Table, self.Linkman_Table)
		
		print self.AddInfo
		if self.AddInfo == 1:
			self.Linkman = Linkman(self.Linkman_Table)#  1 Init Linkman
			print "Add Group Success!"
		else:
			print "Add Group Error"

	def AddLinkman(self):
		self.Linkman.Add(self.Linkman_Table)

	def SearchLinkman(self):
		self.Linkman.Search()
	
	def ShowAllLinkman(self):
		self.Search(0)


class Linkman(Personal):
	
	def __init__(self, Table):
		super(Linkman, self).__init__()
		self.OfficialPhone = None
		self.Position = None
		self.Table = Table#  1
		Operate.Linkman_Create(self.Table)

	def Add(self, Table):
		self.Table = Table
		self.Name = raw_input("Please put into your name:")	
		self.Phone = raw_input("Please put into your phone number:")
		self.Email = raw_input("Please put into your e-mail:")
		self.OfficialPhone = raw_input("Please put into your official phone number:")
		self.Position = raw_input("Please put into your position:")
		self.ID = Operate.NextID(self.Table)
		self.AddInfo = Operate.Linkman_Add(self.ID, self.Name, self.Phone, self.Email, self.OfficialPhone, self.Position, self.Table)
		
		if self.AddInfo == 1:
			print "Add Linkman success!"
		else:
			print "Add Linkman Error"

	def ShowOfficialPhone(self):
		return self.OfficialPhone
	
	def ShowPosition(self):
		return self.Position

	def ShowInfo(self):
		print "ID: %d" % self.ShowID()
		print "Name: %s" % self.ShowName()
		print "Phone: %s" % self.ShowPhone()
		print "Email: %s" % self.ShowEmail()
		print "Official phone: %s" % self.ShowOfficialPhone()
		print "Position: %s" % self.ShowPosition()

if __name__ == '__main__':
	Per_1 = Group()
	Per_1.Add()
	Per_1.AddLinkman()
	








