#!/usr/bin/env python
# -*- codes: utf-8 -*-
# File name: Start.py
# Author: Lee.HJ

import Class
import sys
import MySQLdb


#Check the MySQL:
def CheckMySQL():
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='1992110    2',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	print "MySQL connect OK"
	
	conn.close()

# Linkman Module
def LinkmanModule(Group):

	while True:
		ChoiceLinkman = None
		SearchID = None
		DeleteID = None
		print "   Show all Linkmans   ----------  [L]"
		print "   Add new Linkman     ----------  [A]"
		print "   Search Linkman      ----------  [S]"
		print "   Delete Linkman      ----------  [D]"
		print "   Exit                ----------  [E]\n"
		ChoiceLinkman = raw_input("Please put into your Choice (L/A/S/D/E):")

		if ChoiceLinkman == 'E':
			break
		
		elif ChoiceLinkman == 'L':
			Group.ShowAllLinkman()
		
		elif ChoiceLinkman == 'A':
			Group.AddLinkman()

		elif ChoiceLinkman == 'S':
			SearchID = raw_input("Please put into ID of Linkman you want to Search:")
			Group.SearchInLinkman(SearchID)

		elif ChoiceLinkman == 'D':
			DeleteID = raw_input("Please put into ID of Linkman you want to Delete:")
			Group.DeleteLinkman(DeleteID)

		else:
			print "Input Error, pleae try again!\n"
			continue

	print "Linkman End!\n"


# Add Module
def AddModule():

	print "      Welcome to add a new Customer! \n"
	
	while True:
		ChoiceAddType = None
		Personal = None
		Group = None

		print "   Add a new Personal Customer  ---------  [P]"
		print "   Add a new Group Customer     ---------  [G]"
		print "   Exit                         ---------  [E]"
		ChoiceAddType = raw_input("Please put into your Choice (P/G/E):")
		
		if ChoiceAddType == 'E':
			break
		
		elif ChoiceAddType == 'P':
			Personal = Class.Personal()
			Personal.Add()
		
		elif ChoiceAddType == 'G':
			Group = Class.Group()
			Group.Add()
		
		else:
			print "Input Error, please try again"
			continue

		print "Add End!\n"


# Search Module
def SearchModule():
	
	print "    Welcome to search a Customer!\n"

	while True:
		SearchID = None
		ChoiceSearchType = None
		Personal = None
		Group = None

		print "   Search a Personal Customer  --------  [P]"
		print "   Search a Group Customer     --------  [G]"
		print "   Exit                        --------  [E]\n"
		ChoiceSearchType = raw_input("Please put into your Choice(P/G/E):")

		if ChoiceSearchType == 'E':
			break

		elif ChoiceSearchType == 'P':
			Personal = Class.Personal()
			SearchID = raw_input("Please put into ID of Personal you want to Search:")
			Personal.Search(SearchID)
		
		elif ChoiceSearchType == 'G':
			Group = Class.Group()
			SearchID = raw_input("Please put into ID of Group you want to Search:")
			Group.Search(SearchID)

			LinkmanModule(Group)  #    Linkman
		
		else:
			print "Input Error, Plears try again"
			continue

	print "Search End\n"

# Delete Module
def DeleteModule():
	
	print "    Welcome to Delete Customer!\n"
	
	while True:
		DeleteID = None
		ChoiceDelType = None
		Personal = None
		Group = None

		print "   Delete Personal Customer  ---------  [P]"
		print "   Delete Group Customer     ---------  [G]"
		print "   Exit                      ---------  [E]"
		ChoiceDelType = raw_input("Please put into your Choice (P/G/E):")
		
		if ChoiceDelType == 'E':
			break
		
		elif ChoiceDelType == 'P':
			Personal = Class.Personal()
			DeleteID = raw_input("Please put into ID of Personal you want to Delete:")
			Personal.Delete(DeleteID)
		
		elif ChoiceDelType == 'G':
			Group = Class.Group()
			DeleteID = raw_input("Please put into ID of Group you want to Delete:")
			Group.Delete(DeleteID)
		
		else:
			print "Input Error, please try again"
			continue

		print "Delete End!\n"



# Begin from there
if __name__ == '__main__':
	
	print "Start!"
	#CheckMySQL()
	print "\n\n\n\n********** Welcome to the Customer Operation System **********\n\n\n\n"

	while True:
		print "    Add a new Customer  ----------   [A]"
		print "    Search Customer     ----------   [S]"
		print "    Delete Customer     ----------   [D]"
		print "    Exit                ----------   [E]"
		ChoiceModule = raw_input("Please put into your Choice ([A/S/D/E]:")

		if ChoiceModule == 'E':
			break
		
		elif ChoiceModule == 'A':
			AddModule()
		
		elif ChoiceModule == 'S':
			SearchModule()

		elif ChoiceModule == 'D':
			DeleteModule()
		
		else:
			print "Input Error! Please put into again!"
			continue
	
	print " Good bye!"

