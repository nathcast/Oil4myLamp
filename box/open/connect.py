'''
Created on 24 Mar 2020

@author: natha_xt0h72h
'''
'''
Created on 24 Mar 2020

@author: natha_xt0h72h
'''
import pymysql
import pymysql.cursors
 
 
def connect():
    
    # ERA database
    host = 'localhost'
    user = 'root'
    pwd= ''
    db = 'o4ml'
    Con = pymysql.connect(host=host,user=user,password=pwd,db=db,cursorclass=pymysql.cursors.DictCursor)
    
    return Con




def getCursor():
    con = connect()
    cur = con.cursor()
    return cur

 
if __name__ == '__main__':
    
    cur = getCursor()
    cur.execute("""select tag from tags""")
    results = cur.fetchall()  
    documents = []  
    for row in results: 
        documents.append( row['tag'])
    print (documents)
    print 