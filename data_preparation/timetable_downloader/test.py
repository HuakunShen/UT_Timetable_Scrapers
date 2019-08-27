import mysql.connector as SQL

import pymysql

# mydb = SQL.connect(host='mysqldb.cqcfrqhijmrx.us-east-2.rds.amazonaws.com', user='admin',
#                        password='admin', database='public')

conn = pymysql.connect('mysqldb.cqcfrqhijmrx.us-east-2.rds.amazonaws.com', user='admin', db='public', passwd='admin', connect_timeout=5)