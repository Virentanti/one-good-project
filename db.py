import mysql.connector as msql
import os
import pickle
from shutil import copy

def backend():
    conn=msql.connect(host="localhost",
                    user="root",
                    passwd="root")
    cur=conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS questionbank;')
    cur.execute('use questionbank')
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
        except EOFError:
            print("done")

def add(img,chap,question,answer):

    with open('count.DAT', 'rb+') as count_file:
        conn=msql.connect(host="localhost",
                        user="root",
                        passwd="root",
                        db="questionbank")
        cur=conn.cursor()
        dst=os.path.join(os.getcwd(),'finaldb')
        count=pickle.load(count_file)
        chapters=["electrostatics","electromagnetic","aphy", "allquestion"]
        if chap in chapters:
            copy(img,dst)
            query=f'insert into {chapter}(Sno,question,answer) values({count[chap]},"{ques}","{answer}")'
            cur.execute(query)
            cur.commit()
            count_file.seek(0)
            count[chap]+=1
            count_file.seek(0)
            pickle.dump(count.count_file)
            return 1

def authenticate(username,password):
    conn=msql.connect(host="localhost",
                            user="root",
                            passwd="root",
                            db="questionbank")
    cur=conn.cursor()
    query= f'select * from auth'
    cur.execute()
    authtbl=cur.fetchall()
    if (username,password) in authtbl:
        return True
    else:
        return False

if __name__=='__main__':
    backend()