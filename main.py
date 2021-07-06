import os
from scrapy_thingy import scrape

chapter_lst=['Physics Electrostatics & Capacitance','Current Electricity, Charging & Discharging Of Capacitors']
#types=[['Assertion and Reason', 'Critical Thinking','Grouping of Capacitors','Capacitance','Electric Flux and Gausss Law','Electric Dipole','Electric Field and Potential','Charge and Coulombs Law','Electric Charges and Field Conceptual Problems'],['Assertion and Reason', 'Critical Thinking','Thermo Electricity','Chemical Effect of Current','Heating Effect of Current','Assertion and Reason', 'Critical Thinking','Different Measuring Instruments',"Kirchhoff's Law, Cells",'Grouping of Resistances',"Electric Conduction, Ohm's and Resistance",'Different Measuring Instruments','Kirchhoffs Law Cells','Grouping of Resistances','Electric Conduction Ohms and Resistance']]

dat={'Assertion_and_Reason':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1162/84237',21],'Critical Thinking':['https://www.studyadda.com/question-bank/critical-thinking_q1/1160/84183',45],'Thermo Electricity':['https://www.studyadda.com/question-bank/thermo-electricity_q1/1159/84139',44],'Chemical Effect of Current':['https://www.studyadda.com/question-bank/chemical-effect-of-current_q1/1158/84080',59],'Heating Effect of Current':['https://www.studyadda.com/question-bank/heating-effect-of-current_q1/1157/83927',153],'Assertion and Reason_2':['https://www.studyadda.com/question-bank/assertion-and-reason_q1/1068/77282',17],'Critical Thinking_2':['https://www.studyadda.com/question-bank/critical-thinking_q1/1066/77208',54],'Different Measuring Instruments':['https://www.studyadda.com/question-bank/different-measuring-instruments_q1/1065/77065',143],'Kirchhoff Law, Cells':['https://www.studyadda.com/question-bank/kirchhoffs-law-cells_q1/1064/76980',85],'Grouping of Resistances':['https://www.studyadda.com/question-bank/grouping-of-resistances_q1/1063/76839',141],'Electric Conduction & Ohm and Resistance':['https://www.studyadda.com/question-bank/electric-conduction-ohms-and-resistance_q1/1062/76706',133],'Different Measuring Instruments_2':['https://www.studyadda.com/question-bank/different-measuring-instruments_q1/1051/75677',143],'Kirchhoffs Law Cells':['https://www.studyadda.com/question-bank/kirchhoffs-law-cells_q1/1050/75592',85],'Grouping of Resistances':['https://www.studyadda.com/question-bank/grouping-of-resistances_q1/1049/75451',141],'Electric Conduction Ohms and Resistance':['https://www.studyadda.com/question-bank/electric-conduction-ohms-and-resistance_q1/1048/75318',133]}
type=list(dat.keys())
directory = chapter_lst[1]
parent_dir = r"C:\Users\Rashmi\Desktop\Development\one-good-project\content"
path = os.path.join(parent_dir, directory)
#os.mkdir(path)
for j in type:
    x=os.path.join(r"C:\Users\Rashmi\Desktop\Development\one-good-project\content\Current Electricity", j)
    scrape(dat[j][0],x,dat[j][1]+1)
    