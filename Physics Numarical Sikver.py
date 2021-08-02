from math import log

#----->formula list<-----#
V={0:['I','R'],1:['P','I'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
V_formula={0:'I*R',1:'P*I',2:'P*R',3:'q*C',4:'P*E*q',5:'q*r'}
C={0:['q','V'],1:['A','d'],2:['U','V'],3:['U','q'],4:['n','V'],5:['q','outer_radius','inner_radius'],6:['outer_radius','inner_radius','L']}
C_formula={0:'q/V',1:'ep*A/d',2:'2*U/(V**2)',3:'q**2/2*U',4:'n*e/V',5:'(4*(3.14)*ep*outer_radius*inner_radius)/(outer_radius - inner_radius)',6:'(2*(3.14)*ep*L)/(log(outer_radius/inner_radius))'}

def compare(a,b):
    x=[i.upper() for i in a]
    y=[i.upper() for i in b]
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

def capacitance(lst,val):
    key=get_key(lst,C)
    if key!=-1:
        temp={'k':9*(10**9),'ep':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        if len(val)==len(C[key]):
            for i in range(len(C[key])):
                temp[C[key][i]]=val[i]
        return eval(C_formula[key],temp)


def Voltage(lst,val):
    key=get_key(lst,V)
    if key!=-1:
        temp={'k':9*(10**9),'ep':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        if len(val)==len(V[key]):
            for i in range(len(V[key])):
                temp[V[key][i]]=val[i]
            return eval(V_formula[key],temp)

#test
it=['Q','v']
val=[4.2,2]
print(capacitance(it,val))

it=['i','r']
val=[4.2,2]
print(Voltage(it,val))







          
  
