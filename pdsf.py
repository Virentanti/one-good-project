from fpdf import FPDF
# from fpdf import cell,image,set_font

# def ques(img):
#     set_font('helvetica', size=10)
#     cell(10,10,txt='Q1')
#     image(name=img, x=20, y=10, w=170)
#     cell(0,10,txt="1 mark",align="R")


# def ans(img):
#     set_font('helvetica', size=10)
#     cell(10,10,txt='Q1')
#     image(name=img, x=20, y=10, w=170)
#     cell(0,10,txt="1 mark",align="R")


# imq="q_EM Waves Question Bank Mock Test - Electromagnetic Waves and Dual Nature26327.png"
# ima="a_EM Waves Question Bank Mock Test - Electromagnetic Waves and Dual Nature26327.png"
# # Create a PDF object
# pdf = FPDF('P', 'mm', 'Letter')

# # get total page numbers
# pdf.alias_nb_pages()

# # Set auto page break
# pdf.set_auto_page_break(auto = True, margin = 15)

# #Add Page
# pdf.add_page()

# # specify font
# pdf.set_font('helvetica', 'BIU', 16)

# pdf.set_font('times', '', 12)
# ques(imq)
# ans(ima)

# pdf.output('pdf_2.pdf')


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

def pdf_gen(pdf_name,img,no):
    imq="q_EM Waves Question Bank Mock Test - Electromagnetic Waves and Dual Nature26327.png"
    ima="a_EM Waves Question Bank Mock Test - Electromagnetic Waves and Dual Nature26327.png"

    # Create a PDF object
    pdf = PDF('P', 'mm', 'Letter')

    # get total page numbers
    pdf.alias_nb_pages()

    # Set auto page break
    pdf.set_auto_page_break(auto = True, margin = 15)

    #Add Page
    pdf.add_page()

    # specify font
    pdf.set_font('helvetica', 'BIU', 16)

    pdf.set_font('times', '', 12)
    pdf.cell(txt="Question paper",w=0,align="C")
    pdf.ln(10)
    for i in range(10):
        pdf.ques(imq,i)
        pdf.ln()
    pdf.add_page()
    pdf.cell(txt="Answers",w=0,align="C")
    pdf.ln()
    for i in range(10):
        pdf.ans(ima,i)
        pdf.ln()
    pdf.set_title(title='Question paper')

    pdf.output('pdf_2.pdf')
