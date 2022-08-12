import mysql.connector

def db_connection():
    conn=mysql.connector.connect(host='localhost',username='root',password='',database='demo')
    return conn






print('DB created')

def store_data(name,email,role):
    conn=db_connection()
    cursor=conn.cursor()

    query='create table if not exists Employee(name varchar(100) ,email varchar(50),role varchar(50))'
    cursor.execute(query)
    print('Table created')

    query=f"insert into Employee(name,email,role) values('{name}','{email}','{role}')"
    cursor.execute(query)
    conn.commit()
    print('data inserted')

def fetch_employee():
    conn=db_connection()
    cursor=conn.cursor()
    
    query='select * from Employee'
    cursor.execute(query)
    return cursor.fetchall()
    # if data>0:
    #     info=cursor.fetch_all()
    # return info

    





