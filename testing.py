import random
from math import log

V={0:['I','R'],1:['P','I'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
V_formula={0:'I*R',1:'P*I',2:'P*R',3:'q*C',4:'P*E*q',5:'q*r'}
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

def Voltag(lst):
    res_lis=[]
    key=get_key(lst,V)
    res_lis.append(lst)
    if key!=-1:
        temp={'k':9*(10**9),'ep':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        for i in V[key]:
            a=random.uniform(0.1,100)
            res_lis.append(a)
            temp[i]=a
        res_lis.append(eval(V_formula[key],temp))
        return res_lis
    else:
        res_lis.append(-1)
        return res_lis


for i in range(1000):
    x= V[random.randint(0,5)]
    file.write(str(Voltag(x)))


