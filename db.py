import mysql.connector as msql
import os
import pickle
from shutil import copy
from cryptography.fernet import Fernet


def backend(passwd):
    conn=msql.connect(host="localhost",
                    user="root",
                    passwd=passwd)
    cur=conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS questionbank;')
    cur.execute('use questionbank')
    chapters=["electrostatics","electromagnetic","current","aphy", "allquestion"]
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
                #print(x)
                conn.commit()
        except EOFError: print("done")

    admin_table=f'create table auth(username varchar(255) primary key, password varchar(255));'
    query=f'insert into auth(username, password) values("root","gAAAAABhKf60jFpEaosPLqgIuvPAnyxAPAf76yxtBdZbBwbhBvAG0GspfhbSpWhc87ydxjEmuBs_vF4P0fGJhHpUugdPenw0AQ==");'
    cur.execute(admin_table)
    cur.execute(query)

def add(chap,question,answer):

    with open('count.dat', 'rb+') as count_file:
        conn=msql.connect(host="localhost",
                        user="root",
                        passwd="root",
                        db="questionbank")
        cur=conn.cursor()
        question=os.path.basename(question)
        answer=os.path.basename(answer)
        qdst=os.path.join(os.path.join(os.getcwd(),'finaldb'),question)
        adst=os.path.join(os.path.join(os.getcwd(),'finaldb'),answer)
        count=pickle.load(count_file)
        chapters=["electrostatics","electromagnetic","current","aphy", "allquestion"]
        try:
            if chap in chapters:
                copy(question,qdst)
                copy(answer,adst)
                query=f'insert into {chap}(Sno,question,answer) values({count[chap]+1},"{question}","{answer}")'
                cur.execute(query)
                cur.commit()
                count_file.seek(0)
                count[chap]+=1
                count_file.seek(0)
                pickle.dump(count.count_file)
                return True
        except: return False

def authenticate(username,password):
    conn=msql.connect(host="localhost",
                            user="root",
                            passwd="root",
                            db="questionbank")
    cur=conn.cursor()
    query= f'select * from auth'
    cur.execute(query)
    authtbl=cur.fetchall()
    key=b"rIAyt0uH1sgM8bC-WPQfSFomx5BGSz6_2MW2geye3I4="
    fernet=Fernet(key)
    authtbl=[(i[0],fernet.decrypt(authtbl[0][1].encode()).decode()) for i in authtbl]

    if (username,password) in authtbl: return True
    else: return False

if __name__=='__main__':
    passwd=str(input('Enter your MySQL password: '))
    backend(passwd)