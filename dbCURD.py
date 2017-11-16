#!/usr/bin/env python3
#coding=utf-8
import MySQLdb

def connectdb():
	print('start connect db...')
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
		
def createtable(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # 如果存在表table先删除
    cursor.execute("DROP TABLE IF EXISTS tableName")
    sql = """CREATE TABLE tableName (
            ... )"""

    # 创建table表
    cursor.execute(sql)
		
def insertdb(db):
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO component
         VALUES (4,'TEST', 'test',1)"""

    #sql = "INSERT INTO component(name, desc, isactive) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()

    except:
        # Rollback in case there is any error
        print 'insert failed!'
        db.rollback()
		
def closedb(db):
    db.close()

def main():
	db = connectdb()
	#insertdb(db)
	queryTable(db,'component')
	closedb(db)
	
if __name__ == '__main__':
    main()
