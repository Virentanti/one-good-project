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
C={0:['q','V'],1:['U','V'],2:['A','d'],3:['q','U'],4:['n','V'],5:['r1r2'],6:['r1r2','l']}
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
    
def strtolist(data):
    data=data.replace('[','').replace(']','')
    data=data.split(',')
    return data
def Voltage(data,val):
        data=strtolist(data)
        val=strtolist(val)
        val=[float(i) for i in val]
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

def Capacitance(data,val):
        data=strtolist(data)
        val=strtolist(val)
        val=[float(i) for i in val]
        if compare(data ,C.get(0)):
          cap=val[0]/val[1]
          value=str(round (cap,2))+'F'
        if compare(data ,C.get(1)):
          cap=2*val[0]/val[1]**2
          value=str(round (cap,2))+'F'
        if compare(data ,C.get(2)):
          cap=e0*val[0]/val[1]
          value=str(round (cap,2))+'F'
        if compare(data ,C.get(3)):
          cap=val[0]**2/val[1]*2
          value=str(round (cap,2))+'F'
        if compare(data ,C.get(4)):
          cap=e*val[0]/val[1]
          value=str(round (cap,2))+'F'
        if compare(data ,C.get(5)):
          cap=(4*(3.14)*e0*val[0]*val[1])/(val[0] - val[1])
          value=str(round(Cap*10**10, 4)),'x10^-4 uF'
        if compare(data ,C.get(4)):
          cap=(2*(3.14)*e0*val[2])/(math.log(val[0]/val[1]))
          value=str(round(Cap*10**10, 4)),'x10^-4 uF'
        return value

def DriftVelocity(data,val):
        data=strtolist(data)
        val=strtolist(val)
        val=[float(i) for i in val]
        if compare(data ,Vd.get(0)):
          vd=val[0]/val[1]*val[2]*val[3]
          value=str(round (vd,2))+'F'
        if compare(data ,Vd.get(1)):
          vd=val[0]/val[1]
          value=str(round (vd,2))+'F'
        if compare(data ,Vd.get(2)):
          vd=val[0]*val[1]*e*0.5/m
          value=str(round (vd,2))+'F'
        if compare(data ,Vd.get(3)):
          vd=val[0]/val[1]*e
        return value
