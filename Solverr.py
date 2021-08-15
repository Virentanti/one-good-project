from math import log

# print('*-------------------------------THE BASIC PHYSICS NUMERICAL SOLVER--------------------------------*')
# print("Chapter 1. Electric Charges and Fields")
# print("Chapter 2. Electrostatic Potential And Capacitance")
# print("Chapter 3. Current Electricity")
# print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print('For:-')
# print('Volt=V, Current=I, Resistance=R, Charge=q, Radius=r, Electric Field=E, Power=P, Capacitance=C, Force=F')
# print('Area=A, Distance=d, Drift velocity=Vd, Dielectric constant=K, Work done=W, Electric flux=Ef, Length=L')
# print("Charge density=p, Induced charge=q', Polarisation=P', Volume=V, Two Charges=q1q2, Two Radius=r1r2")
# print('Electromotive force=emf, Stored energy=u, No. of Electron=n ,Potential difference=U ')
# print('*Shape=shape, Angle=x')
# print('#Note: All value must be in Standard Unit')
# print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# data=str(input("Which Values do Question have: "))  #Getting available data from the user
# data=data.split(',')    #converting available data to list
# print(data)
# want=str(input("What Do Question want: ")).upper()  #getting what user wants
#want=want.upper()   #making sure the data is in uppercase
#----->Defined Constants
k=9*(10**9)
e0=8.85*(10**-12)
e=1.6*10**-19
m=9.11*10**-31

#- ---->formula list<-----#
V={0:['i','R'],1:['P','i'],2:['P','R'],3:['q','C'],4:['P','E','q'],5:['q','r']}
C={0:['q','V'],1:['A','d'],2:['U','V'],3:['U','q'],4:['n','V'],5:['r1r2'],6:['r1r2','l']}
Vd={0:['i','A','q','n'],1:['l','t'],2:['E','t'],3:['j','n']}

def compare(a,b):
    x=[i.upper() for i in a]
    y=[i.upper() for i in b]
    x.sort()
    y.sort()
    if x==y:
        return True
    else:
        return False
    
def Voltage(data,val):
        val=val.replace('[','').replace(']','')
        val=val.split(',')
        val=[int(i) for i in val]
        if compare(data ,V.get(0)):
          volt=val[0]*val[1]
          value=str(round (volt,2))+'V'
        if compare(data ,V.get(1)):
          volt=val[0]/val[1]
          value=str(round (volt,2))+'V'
        if compare(data ,V.get(2)):
          volt=val[0]*val[1]
          value=str(round (volt,2))+'V'
        if compare(data ,V.get(3)):
          volt=val[0]/val[1]
          value=str(round (volt,2))+'V'
        if compare(data ,V.get(4)):
          volt=val[0]*val[1]/val[2]
          value=str(round (volt,2))+'V'
        if compare(data ,V.get(5)):
          volt=(k)*val[1]/val[2]
          value=str(round (volt,2))+'V'
        return value
data=["i","r"]
val='[1,2]'
print(Voltage(data,val))
# if want=='C':
#         if compare(data ,C.get(0)):
#           q=float(input('q='))
#           V=float(input('V='))
#           Cap=q/V
#           print('Capacitance is(q/V) ',round(Cap, 2),'F')
#         if data ==C.get(1):
#           U=float(input('U='))
#           V=float(input('V='))
#           Cap=2*U/(V**2)
#           print('Capacitance is(2U/(V^2)) ',round(Cap, 2),'F')
#         if data ==C.get(2):
#           q=float(input('q='))
#           U=float(input('U='))
#           Cap=q**2/(2*U)
#           print('Capacitance is(q^2/(2U)) ',round(Cap, 2),'F')
#         if data ==C.get(3):
#           n=int(input('n='))
#           V=float(input('V='))
#           Cap=n*e/V
#           print('Capacitance is(n*e/V) ',round(Cap, 2),'F')
#         if data ==C.get(4):
#           A=float(input('A='))
#           d=float(input('d='))
#           Cap=e0*A/d
#           print('Capacitance is(e0*A/d) ',round(Cap, 2),'F')
#         if data ==C.get(5):
#           r1=float(input('r1(Outer)='))
#           r2=float(input('r2(Inner)='))
#           if r1==r2:
#               print('Both radius can not have same value ')
#           else:
#               Cap=(4*(3.14)*e0*r1*r2)/(r1 - r2)
#               print('Capacitance is((4π*e0*r1*r2)/(r1 - r2)) ',round(Cap*10**10, 4),'x10^-4 uF')
#         if data ==C.get(6):
#           l=float(input('l='))
#           r1=float(input('r1(Outer)='))
#           r2=float(input('r2(Inner)='))
#           Cap=(2*(3.14)*e0*l)/(math.log(r1/r2))
#           print('Capacitance is(2π*e0*l)/log(r2/r1) ',round(Cap*10**10, 4),'x10^-4 uF')
# if want=='vd':
#         if data ==[['i','A','q','n']]:
#           i=float(input('i='))
#           A=float(input('A='))
#           q=float(input('q='))
#           n=int(input('n='))
#           Veld=i/(A*q*n)
#           print('Drift Velocity is() ',round(Veld, 2),'m/sec')
#         if data ==[['l','t']]:
#           l=float(input('Distane='))
#           t=int(input('Av. Collision time='))
#           Veld=l/t
#           print('Drift Velocity is() ',round(Veld, 2),'m/sec')
#         if data ==[['E','t']]:
#           E=float(input('E='))
#           t=float(input('t='))
#           Veld=0.5*(e*E*t/m)
#           print('Drift Velocity is((e*E*t/2m)) ',round(Veld, 2),'m/sec')
#         if data ==[['j','n']]:
#           j=float(input('j='))
#           n=int(input('n='))
#           Veld=j/(n*e)
#           print('Drift Velocity is(j/(n*e)) ',round(Veld, 2),'m/sec')
    

