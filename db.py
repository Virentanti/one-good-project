import mysql.connector as msql
import os
import pickle
from shutil import copy
from cryptography.fernet import Fernet
import sys


def backend(passwd):
    conn=msql.connect(host="localhost",
                    user="root",
                    passwd=passwd)
    cur=conn.cursor()
    cur.execute('drop database if exists questionbank;')
    cur.execute('CREATE DATABASE questionbank;')
    cur.execute('use questionbank')
    chapters=["electrostatics","electromagnetic","current","aphy", "allquestion"]
    for chapter in chapters:
        fl=chapter+'.txt'
        file=open(fl,'r')
        x=' '
        count=0
        table=f'create table {chapter}(sno int primary key, question varchar(255), answer varchar(255))'
        cur.execute(table)
        with open('count.dat', 'wb') as count_file:
            pickle.dump({'electrostatics': 670, 'current': 981, 'electromagnetic': 70, 'aphy': 140, 'allquestion': 1861},count_file)

        try :
            while x:
                x = file.readline()
                x=x.split()
                if len(x)==2:
                    count+=1
                    query=f'insert into {chapter}(Sno,question,answer) values({count},"{x[0]}","{x[1]}")'
                    cur.execute(query)
                    conn.commit()
        except EOFError: print("done")

    admin_table=f'create table auth(username varchar(255) primary key, password varchar(255));'
    query=f'insert into auth(username, password) values("root","gAAAAABhKf60jFpEaosPLqgIuvPAnyxAPAf76yxtBdZbBwbhBvAG0GspfhbSpWhc87ydxjEmuBs_vF4P0fGJhHpUugdPenw0AQ==");'
    cur.execute(admin_table)
    cur.execute(query)
    conn.commit()

def add(chap,question,answer):

    with open('count.dat', 'rb+') as count_file:
        conn=msql.connect(host="localhost",
                        user="root",
                        passwd="root",
                        db="questionbank")
        cur=conn.cursor()
        question_name =os.path.basename(question)
        answer_name =os.path.basename(answer)
        qdst=os.path.join(os.path.join(os.getcwd(),'finaldb'),question_name)
        adst=os.path.join(os.path.join(os.getcwd(),'finaldb'),answer_name)
        count=pickle.load(count_file)
        chapters=["electrostatics","electromagnetic","current","aphy", "allquestion"]

        if chap in chapters:
            copy(question,qdst)
            copy(answer,adst)
            query=f'insert into {chap}(Sno,question,answer) values({count[chap]+2},"{question}","{answer}")'
            cur.execute(query)

            query=f'insert into allquestion(Sno,question,answer) values({count["allquestion"]+2},"{question}","{answer}")'
            cur.execute(query)
            conn.commit()
            count[chap]+=1
            count["allquestion"]+=1
            count_file.seek(0)
            pickle.dump(count,count_file)
            return True


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

def add_admin(username,password,passwd):
    conn=msql.connect(host="localhost",
                        user="root",
                        passwd=passwd,
                        db="questionbank")
    cur=conn.cursor()
    key=b"rIAyt0uH1sgM8bC-WPQfSFomx5BGSz6_2MW2geye3I4="
    fernet=Fernet(key)
    enc_password=fernet.encrypt(password.encode())
    query=f'insert into auth(username, password) values({username},{enc_password};'


        

if __name__=='__main__':

    if len(sys.argv)>1:
        if sys.argv[1]=='-h' or '--help':
            print('''
            use:
            \t<mysql password> -c to create backend 
            \t<mysql password> -a <username> <password> to add admin''')

        elif sys.argv[2]=='-c': backend(sys.argv[1])

        elif sys.argv[2]=='-c': add_admin(sys.argv[3],sys.argv[4],sys.argv[1])
    else:
        passwd=str(input('Enter your MySQL password: '))
        while True:
            op=str(input(' 1. Create Backend \n 2. Add Admin \n 3. Exit \n Enter your choice: '))

            if op=='1' or op=='1.': backend(passwd)
            
            elif op=='2' or op=='2.':
                username=str(input('enter username for admin'))
                password=str(input('enter password for admin'))
                add_admin(username,password,passwd)
            elif op=='3' or op=='3.': break

