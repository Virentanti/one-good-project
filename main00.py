C={0:['q','V'],1:['A','d'],2:['U','V'],3:['U','q'],4:['n','V'],5:['q','r1','r2'],6:['r1','r2','L']}
C_formula={0:'q/V',1:'e0*A/d',2:'2*U/(V**2)',3:'q**2/2*U',4:'n*e/V',5:'(4*(3.14)*e0*r1*r2)/(r1 - r2)',6:'(2*(3.14)*e0*L)/(math.log(r2/r1))'}

def compare(a,b):
    x=[]
    y=[]
    for i in range(len(a)):
        x.append(a[i].upper())
        y.append(b[i].upper())
    x.sort()
    y.sort()
    if x==y:
        return True
    else:
        return False

def get_key(val):
    for key, value in C.items():
        print(val)
        print(value)
        print(compare(val, value))
        if compare(val,value):
            return key
    else:
        return -1

def capacitance(lst):
    key=get_key(lst)
    print(key)
    if key!=-1:
        temp={}
        for i in C[key]:
            a=float(input(f'enter value of {i}:'))
            temp[i]=a
        return eval(C_formula[key],temp)

print(capacitance(['v','q']))

V={0:['I','R'],1:['P','I'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
V_formula={0:'I*R',1:'P*I',2:'P*R',3:'q*C',4:'P*E*q',5:'q*r'}

def Voltage(lst):
    key=get_key(lst)
    if key!=-1:
        temp={}
        for i in V[key]:
            a=float(input(f'enter value of {i}:'))
            temp[i]=a
        return eval(V_formula[key],temp)
    else:
        return -1
