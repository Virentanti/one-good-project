from math import log

print('*-------------------------------THE BASIC PHYSICS NUMERICAL SOLVER--------------------------------*')
print("Chapter 1. Electric Charges and Fields")
print("Chapter 2. Electrostatic Potential And Capacitance")
print("Chapter 3. Current Electricity")
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('For:-')
print('Volt=V, Current=I, Resistance=R, Charge=q, Radius=r, Electric Field=E, Power=P, Capacitance=C, Force=F')
print('Area=A, Distance=d, Drift velocity=Vd, Dielectric constant=K, Work done=W, Electric flux=Ef, Length=L')
print("Charge density=p, Induced charge=q', Polarisation=P', Volume=V, Two Charges=q1q2, Two Radius=r1r2")
print('Electromotive force=emf, Stored energy=u, No. of Electron=n ,Potential difference=U ')
print('*Shape=shape, Angle=x')
print('#Note: All value must be in Standard Unit')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

data=str(input("Which Values do Question have: "))  #Getting available data from the user
data=data.upper().split(',')    #converting available data to list
print(data)
want=str(input("What Do Question want: ")).upper()  #getting what user wants
#want=want.upper()   #making sure the data is in uppercase
print(want)

#----->formula list<-----#
V={0:['I','R'],1:['P','I'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
V_formula={0:'I*R',1:'P*I',2:'P*R',3:'q*C',4:'P*E*q',5:'q*r'}
C={0:['q','V'],1:['A','d'],2:['U','V'],3:['U','q'],4:['n','V'],5:['q','r1','r2'],6:['r1','r2','L']}
C_formula={0:'q/V',1:'e0*A/d',2:'2*U/(V**2)',3:'q**2/2*U',4:'n*e/V',5:'(4*(3.14)*e0*r1*r2)/(r1 - r2)',6:'(2*(3.14)*e0*L)/(log(r2/r1))'}

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

def get_key(val,a):
    for key, value in a.items():
        if compare(val,value):
            return key
    else:
        return -1

def capacitance(lst):
    key=get_key(lst,C)
    if key!=-1:
        temp={'k':9*(10**9),'e0':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        for i in C[key]:
            a=float(input(f'enter value of {i}:'))
            temp[i]=a
        return eval(C_formula[key],temp)

def Voltage(lst):
    key=get_key(lst,V)
    if key!=-1:
        temp={'k':9*(10**9),'e0':8.85*(10**(-12)),'e':1.6*(10**(-19)),'log':log}
        for i in V[key]:
            a=float(input(f'enter value of {i}:'))
            temp[i]=a
        return eval(V_formula[key],temp)
    else:
        return -1

try:
    if want=='V'or want=='emf':
        print(Voltage(data))

    elif want=='C':
        print(capacitance(data))
except:
    print('invalid datatype provided')











          
  
