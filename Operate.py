#!/usr/bin/env python
# -*- codes: utf-8 -*-
# File name: Operate.py
# Author: Lee.HJ

import sys, string, os
import MySQLdb
from warnings import filterwarnings 

filterwarnings('error', category = MySQLdb.Warning)

#***********************  Search  **************************

def Search(ID, Table): #  2
	#MySQL Search in 'Table' which ID is 'ID' and return the information
	
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Search ID in Table
	sql_Search = None

	if ID == 0:  #Search all linkman information
		sql_Search = "Select *from %s" % Table
	else:
		sql_Search = "Select *from %s where (ID = '%s')" % (Table, ID)
	
	cursor.execute(sql_Search)
	sql_Info = cursor.fetchall()
	
	conn.commit()

	cursor.close()
	conn.close()

	return sql_Info

#**********************  Delete  ***********************

def Delete(ID, Table): #  3
	#MySQL Delete in 'Table' which ID is 'ID' in Customer_table
	
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Search ID in Table and Delete

	sql_Search = "Select *from %s where (ID = '%s')" % (Table, ID)
	cursor.execute(sql_Search)
	sql_Info = cursor.fetchall()
	
	if sql_Info:
		sql_Delete = "Delete from %s where (ID = '%s')" % (Table, ID)
		try:
			cursor.execute(sql_Delete)
		except Exception, e:
			print e
			sys.exit()

		if Table == 'Group_table':
			Linkman_table = sql_Info[0][1]
			sql_Delete = "Drop table %s" % Linkman_table
			try:
				cursor.execute(sql_Delete)
			except Exception, e:
				print e
				sys.exit()
		else:
			pass
	else:
		pass

	conn.commit()
	
	cursor.close()
	conn.close()
		
	return sql_Info

#***************    NextID   ****************
# Return the next ID in table

def NextID(Table):
	#MySQL Search in Customer_table
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	
	
	#
	cursor = conn.cursor()
	
	#Search next id ~~~~~~~~~~Need to change !!! 
	sql_NextID = "Select MAX(ID) from %s" % Table
	cursor.execute(sql_NextID)
	ID = cursor.fetchall()
	
	if ID[0][0] == None:
		NextID = 1
	else:
		NextID = int(ID[0][0]) + 1
	
	return NextID

#****************  Personal  *************************

def Personal_Create(Table):
	#MySQL Create a new table if not exist
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Create table
	sql_create = "Create table if not exists %s(ID int(10) primary key, Name varchar(10), Phone varchar(20), Email varchar(20))" % Table
	try:
		cursor.execute(sql_create)
	except MySQLdb.Warning:
		pass

	conn.commit()
	
	cursor.close()
	conn.close()

def Personal_Add(ID, Name, Phone, Email, Table):
	#MySQL Add in Customer_table
	
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	sql_insert = "Insert into %s values ('%d', '%s', '%s', '%s')" % (Table, ID, Name, Phone, Email)
	#print sql_insert
	try:
		cursor.execute(sql_insert)
		Return = 1
	except Exception, e:
		print e
		Return = 0
	
	conn.commit()	

	cursor.close()
	conn.close()

	return Return


#*******************  Group  *************************

def Group_Create(Table):
	#MySQL Create a new table if not exist
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Create table
	sql_create = "Create table if not exists %s(ID int(10) primary key, Linkman_table varchar(10))" % Table
	try:
		cursor.execute(sql_create)
	except MySQLdb.Warning:
		pass

	conn.commit()
	
	cursor.close()
	conn.close()

def Group_Add(ID, Table, Linkman_Table):
	#MySQL Add in Group_table
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Insert information
	sql_insert = "Insert into %s values ('%d', '%s')" % (Table, ID, Linkman_Table)
	#print sql_insert
	try:
		cursor.execute(sql_insert)
		Return = 1
	except Exception, e:
		print e
		Return = 0
	
	conn.commit()	

	cursor.close()
	conn.close()

	return Return

#*******************  Linkman  ***********************

def Linkman_Create(Table):
	#MySQL Create a new table if not exist
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Create table
	sql_create = "Create table if not exists %s(ID int(10) primary key,Name varchar(10),Phone varchar(20),Email varchar(20),O_Phone varchar(20),Position varchar(20))" % Table
	try:
		cursor.execute(sql_create)
	except MySQLdb.Warning:
		pass

	conn.commit()
	
	cursor.close()
	conn.close()

def Linkman_Add(ID, Name, Phone, Email, OfficialPhone, Position, Table):
	#MySQL Add in Linkman_table
	#Connect
	try:
		conn = MySQLdb.connect(host='localhost',user='root',passwd='19921102',db='Customer_Operation',port=0)
	except Exception, e:
		print e
		sys.exit()
	#print "Connect MySQL success!"	

	#Cursor
	cursor = conn.cursor()
	
	#Insert information
	sql_insert = "Insert into %s values ('%d','%s','%s','%s','%s','%s')" % (Table, ID, Name, Phone, Email, OfficialPhone, Position)
	#print sql_insert
	try:
		cursor.execute(sql_insert)
		Return = 1
	except Exception, e:
		print e
		Return = 0
	
	conn.commit()	

	cursor.close()
	conn.close()

	return Return
	
	

