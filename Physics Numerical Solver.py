import math

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
want=str(input("What Do Question want: "))  #getting what user wants
want=want.upper()   #making sure the data is in uppercase
print(want)
#----->DEFINED CONSTANTS
k=9*(10**9)
e0=8.85*(10**(-12))
e=1.6*(10**(-19))
constants={'k':k,'e0':e0,'e':e}

#----->function to compare lists
def compare(a,b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i].upper()!=b[i].upper():
            return False
            break
    else:
        return True


def com(lst):
    if len(lst)==2:
        return True
    else:
        return False

def co2(a,b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i].upper()!=b[i].upper():
            return False
            break
    else:
        return True

def volt2var(lst):
    val=1
    for i in lst:
        temp=float(input(f'enter value of {i}:'))
        val*=temp
    return val


def volt3var(lst):
    if co2(lst,['P','E','q']):
        P=float(input('P='))
        E=float(input('E='))
        q=float(input('q='))
        return P*E/q
    elif co2(lst,['P','I']):
        P=float(input(f'Enter value of P:'))
        I=float(input(f'Enter value of I:'))
        val=P/I
        return val
    else:
        val=1
        for i in lst:
            temp=float(input(f'Enter value of {i}:'))
            val*=temp
        return val*constants['k']

def capacitance(lst):
    if co2(lst,['q','V']):
        q=float(input('q='))
        V=float(input('V='))
        Cap=q/V

    if co2(lst,['U','V']):
        U=float(input('U='))
        V=float(input('V='))
        Cap=2*U/(V**2)

    if co2(lst,['q','U']):
        q=float(input('q='))
        U=float(input('U='))
        Cap=q**2/2*U

    if co2(lst,['n','V']):
        n=float(input('n='))
        V=float(input('V='))
        Cap=n*e/V

    if co2(lst,['A','d']):
        A=float(input('A='))
        d=float(input('d='))
        Cap=e0*A/d

    if co2(lst,['q','r1r2']):
        q=float(input('q='))
        r1=float(input('r1(inner)='))
        r2=float(input('r2(outer)='))
        Cap=(4*(3.14)*e0*r1*r2)/r1 - r2

    if co2(lst,['L','r1r2']):
        L=float(input('L='))
        r1=float(input('r1(inner)='))
        r2=float(input('r2(outer)='))
        Cap=(2*(3.14)*e0*L)/(math.log(r2/r1))

    return Cap

try:
    if want=='V'or want=='emf':
        V=[['I','R'],['P','I'],['P','R'],['q','C'],['P','E','q'],['q','r']]

        if compare(data,V):
            if com(data)==True:
                print(f'Voltage is {volt2var(data)}V')
            else:
                print(f'Voltage is {volt3var(data)}V')
        else:
            print('We cannot find Voltage from Given Information')

    elif want=='C':
        C=[['q','V'],['A','d'],['U','V'],['U','q'],['n','V'],['r1r2'],['r1r2','L']]

        if compare(data,C):
            print(f'Capacitance is{capacitance(data)}*10**(-6)F')

except:
    print('invalid datatype provided')











          
  
