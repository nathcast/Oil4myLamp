'''
Created on 24 Mar 2020

@author: natha_xt0h72h
'''
import connect

if __name__ == '__main__':
    newTag = input('new tag? ')
    sql = "insert into tags (tag) values ('" + newTag + "')"
    print (sql)
    con = connect.connect()
    cur = connect.getCursor()
    cur.execute(sql)
    con.commit()
   