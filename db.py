import mysql.connector as msql
import os

conn=msql.connect(host="localhost",
                  user="root",
                  passwd="root")
cur=conn.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS questionbank;')
cur.execute('use questionbank')
cwd=os.getcwd()
ch=["current","electrostatics","electromagnetic","aphy", "allquestion"]
chapters=["electrostatics","electromagnetic","aphy", "allquestion"]
for chapter in chapters:
    fl=chapter+'.txt'
    file=open(fl,'r')
    x=' '
    count=0
    table=f'create table {chapter}(sno int primary key, question varchar(255), answer varchar(255))'
    cur.execute(table)
    try :
        while x:
            count+=1
            x = file.readline()
            x=x.split()
            query=f'insert into {chapter}(Sno,question,answer) values({count},"{x[0]}","{x[1]}")'
            cur.execute(query)
            print(x)
            conn.commit()
    except:
        pass
