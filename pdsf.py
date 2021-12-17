from fpdf import FPDF
import mysql.connector as msql
import os
import random
import sys
import datetime

sys.stdout=open(f'log {datetime.date.today()}.txt','a')


class PDF(FPDF):
    def ques(self,img,no):
        self.set_font('helvetica', size=10)
        self.cell(10,10,txt=str(no))
        self.image(name=img,w=190)#, x=20, y=10, w=170)

    def ans(self,img,no):
        rel_posy=50
        self.set_font('helvetica', size=10)
        self.cell(10,10,txt=str(no))
        self.image(name=img,w=190)#, x=25, y=rel_posy, w=170)


def ques(chcode):
    conn=msql.connect(host="localhost",user="root",passwd="root",db="questionbank")
    cur=conn.cursor()
    cur.execute("select * from %s"%(chcode))
    data=cur.fetchall()

    ques_lis=[]
    for _ in range(25):
        ques=random.choice(data)
        if ques not in ques_lis:
            ques_lis.append(ques)

    return ques_lis

def pdf_gen(chcode,dir_name):
    cwd=os.getcwd()
    print(f'[{datetime.datetime.now()}]: Current working directory: {cwd}')
    # Create a PDF object
    pdf = PDF('P', 'mm', 'Letter')
    print(f'[{datetime.datetime.now()}]: PDF object created')

    pdf.set_title(title='Question paper')
    print(f'[{datetime.datetime.now()}]: Title set')

    pdf.set_author(author='Moonshine')
    # get total page numbers
    pdf.alias_nb_pages()
    print(f'[{datetime.datetime.now()}]: Total pages set')

    # Set auto page break
    pdf.set_auto_page_break(auto = True, margin = 15)
    print(f'[{datetime.datetime.now()}]: Auto page break set')

    #Add Page
    pdf.add_page()
    print(f'[{datetime.datetime.now()}]: Page added')

    #specify font
    font_style='helvetica'
    font_size=16
    pdf.set_font( font_style, 'BIU', font_size)
    print(f'[{datetime.datetime.now()}]: Font set to {font_style} {font_size}')

    ques_lis=ques(chcode)
    print(f'[{datetime.datetime.now()}]: Question list generated')

    pdf.cell(txt="Question paper",w=0,align="C")
    pdf.ln(10)
    for i in range(len(ques_lis)):
        q=os.path.join(cwd,os.path.join("finaldb",ques_lis[i][1]))
        pdf.ques(q,i+1)
        pdf.ln()
    pdf.add_page()
    pdf.cell(txt="Answers",w=0,align="C")
    pdf.ln()
    for i in range(len(ques_lis)):
        a=os.path.join(cwd,os.path.join("finaldb",ques_lis[i][2]))
        pdf.ans(a,i+1)
        pdf.ln()

    pdf.output(os.path.join(dir_name,'question_paper.pdf'))
    print(f'[{datetime.datetime.now()}]: pdf generated')
