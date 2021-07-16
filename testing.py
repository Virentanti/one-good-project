import random
from math import log

V={0:['I','R'],1:['P','I'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
V_formula={0:'I*R',1:'P*I',2:'P*R',3:'q*C',4:'P*E*q',5:'q*r'}
C={0:['q','V'],1:['A','d'],2:['U','V'],3:['U','q'],4:['n','V'],5:['q','r1','r2'],6:['r1','r2','L']}
C_formula={0:'q/V',1:'ep*A/d',2:'2*U/(V**2)',3:'q**2/2*U',4:'n*e/V',5:'(4*(3.14)*ep*r1*r2)/(r1 - r2)',6:'(2*(3.14)*ep*L)/(log(r2/r1))'}
d=[['I','R'],['P','I'],['P','R'],['q','C'],['P','E','q'],['q','r']]
result=[]

file=open('res.txt','a')

def compare(a,b):
    x=[]
    y=[]
    for i in range(len(a)):
        try:
            x.append(a[i].upper())
            y.append(b[i].upper())
        except: 
            return False
    x.sort()
    y.sort()
    if x==y:
        return True
    else:
        return False

def get_key(val,a):
    for key, value in a.items():
        if compare(val,value):
            return key
    else:
        return -1

def Voltage(lst):
    res_lis=[]
    key=get_key(lst,V)
    res_lis.append(lst)
    if key!=-1:
        temp={'k':9*(10**9),'ep':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        for i in V[key]:
            a=random.uniform(0.1,10000)
            res_lis.append(a)
            temp[i]=a
        res_lis.append(eval(V_formula[key],temp))
        return res_lis
    else:
        res_lis.append(-1)
        return res_lis

def capacitance(lst):
    resc_lis=[]
    resc_lis.append(lst)
    key=get_key(lst,C)
    resc_lis.append(key)
    if key!=-1:
        temp={'k':9*(10**9),'ep':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        for i in C[key]:
            a=random.uniform(0.1,10000)
            resc_lis.append(a)
            temp[i]=a
        resc_lis.append(eval(C_formula[key],temp))
    return resc_lis
        

for i in range(10000):
    x= V[random.randint(0,5)]
    file.write(str(Voltage(x)))
    y= C[random.randint(0,6)]
    file.write(str(capacitance(y)))



