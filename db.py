import mysql.connector as msql
import os

conn=msql.connect(host="localhost",
                  user="root",
                  passwd="root",
                  database="questionbank")
cur=conn.cursor()

file=open(r'C:\Users\Rashmi\Desktop\Development\one-good-project\finaldb\em.txt','r')

x=' '
count=0
while x:
    count+=1
    x = file.readline()
    x=x.split()
    query=f'insert into electromagnetic(Sno,question,answer) values({count},"{x[0]}","{x[1]}")'
    cur.execute(query)
    print(x)
    conn.commit()