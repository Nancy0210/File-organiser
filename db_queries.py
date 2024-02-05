import mysql.connector as mqc

def __init__():
    pass

mydb=mqc.connect(
    host="localhost",
    user="root",
    password="1234"
)
mycursor=mydb.cursor()

def traverse():
    
    mycursor.execute("show databases LIKE 'login';")
    for _ in mycursor:
        pass
    if mycursor.rowcount==0:
        mycursor.execute("create database login;")
    mycursor.execute("use login")
    for _ in mycursor:
        pass
    mycursor.execute("show tables LIKE 'data';")
    for _ in mycursor:
        pass
    if mycursor.rowcount==0:
        mycursor.execute("Create table data (Name varchar(50) , User_ID varchar(70) NOT NULL , Password varchar(50) NOT NULL );")

def insert_info(name , email , password):
    sql="insert into data(Name , User_ID , Password) values (%s , %s , MD5(%s));"
    val=[name , email , password]
    mycursor.execute(sql , val)
    
    mydb.commit()


def check_info(email , password):
    val=[email , password]
    mycursor.execute("Select * from data where User_ID=%s AND Password=MD5(%s);", val)
    result=mycursor.fetchall()
    for x in result:
        if mycursor.rowcount==0:
             i=0
             return i
        else:
            i=1
            return 1


    
    

