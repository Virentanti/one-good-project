from fpdf import FPDF
from fpdf import cell,image,set_font

def ques(img):
    set_font('helvetica', size=10)
    cell(10,10,txt='Q1')
    im=".\assertion_and_reason\"+img
    image(name=im, x=20, y=10, w=170)
    cell(0,10,txt="1 mark",align="R")


def ans():
    set_font('helvetica', size=10)
    cell(10,10,txt='Q1')
    image(name=r".\assertion_and_reason\a_Assertion_and_Reason_84237.png", x=20, y=10, w=170)
    cell(0,10,txt="1 mark",align="R")


# Create a PDF object
pdf = FPDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page
pdf.add_page()

# specify font
pdf.set_font('helvetica', 'BIU', 16)

pdf.set_font('times', '', 12)

pdf.output('pdf_2.pdf')