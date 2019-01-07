import cx_Oracle
import pymysql


def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")

def get_mysql_conn(db):
    return pymysql.connect(
        host='localhost',
        user='doo',
        password='11',
        port=3306,
        db=db,
        charset='utf8')

def get_count(conn, tbl, where = ''):
    cur = conn.cursor()
    sql = "select count(*) from " + tbl
    if where != '' :
        sql = sql + " where " + where
        
    cur.execute(sql)
    return cur.fetchone()[0]

def get_all(conn, tbl, where = '', order = '') :
    cur = conn.cursor()
    sql = "select * from " + tbl
    if where != '' :
        sql = sql + " where " + where
    
    elif order != '' :
        sql = sql + " order by " + order
    
    cur.execute(sql)

    return cur.fetchall()