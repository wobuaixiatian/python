#!/usr/bin/env python3
#coding=utf-8
import MySQLdb

def connectdb():
	print('start connect db。。。')
	db=MySQLdb.connect('localhost','root','123456','dbName')
	print('successful...')
	return db
	
def queryTable(db,tableName):
	cursor = db.cursor()
	sql = "select * from %s" %(tableName)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			ID = row[0]
			NAME = row[1]
			DESC = row[2]
			ISACTIVE = row[3]
			print "ID:%s,NAME:%s,DESC:%s,ISACTIVE:%d" % \
				(ID,NAME,DESC,ISACTIVE)
	except:
		print "Error:unable to fetch data"

def main():
	db = connectdb()
	queryTable(db,'component')
	
if __name__ == '__main__':
    main()
