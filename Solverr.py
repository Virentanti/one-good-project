from math import log

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
    data=data.replace('[','').replace(']','').replace("'",'').replace('"','').replace(' ','').split(',')
    return data
def Voltage(data,val):
    try:
        data=strtolist(data)
        val=strtolist(val)
        print(data)
        print(val)
        val=[float(i) for i in val]
        if compare(data ,V.get(0)):
          volt=val[0]*val[1]
          value=str(round (volt,2))+'V'
        elif compare(data ,V.get(1)):
          volt=val[0]/val[1]
          value=str(round (volt,2))+'V'
        elif compare(data ,V.get(2)):
          volt=val[0]*val[1]
          value=str(round (volt,2))+'V'
        elif compare(data ,V.get(3)):
          volt=val[0]/val[1]
          value=str(round (volt,2))+'V'
        elif compare(data ,V.get(4)):
          volt=val[0]*val[1]/val[2]
          value=str(round (volt,2))+'V'
        elif compare(data ,V.get(5)):
          volt=(k)*val[1]/val[2]
          value=str(round (volt,2))+'V'
        else:
          value="not a valid value type"
    except:
        value="invalid value given"
    return value

def Capacitance(data,val):
    try:
        data=strtolist(data)
        val=strtolist(val)
        val=[float(i) for i in val]
        if compare(data ,C.get(0)):
          Cap=val[0]/val[1]
          value=str(round (Cap,2))+'F'
        elif compare(data ,C.get(1)):
          Cap=2*val[0]/val[1]**2
          value=str(round (Cap,2))+'F'
        elif compare(data ,C.get(2)):
          Cap=e0*val[0]/val[1]
          value=str(round (Cap,2))+'F'
        elif compare(data ,C.get(3)):
          Cap=val[0]**2/val[1]*2
          value=str(round (Cap,2))+'F'
        elif compare(data ,C.get(4)):
          Cap=e*val[0]/val[1]
          value=str(round (Cap,2))+'F'
        elif compare(data ,C.get(5)):
          Cap=(4*(3.14)*e0*val[0]*val[1])/(val[0] - val[1])
          value=str(round(Cap*10**10, 4)),'x10^-4 uF'
        elif compare(data ,C.get(4)):
          Cap=(2*(3.14)*e0*val[2])/(log(val[0]/val[1]))
          value=str(round(Cap*10**10, 4)),'x10^-4 uF'
        else:
          value="not a valid value type"
    except:
        value="invalid value given"
    return value

def DriftVelocity(data,val):
    try:
        data=strtolist(data)
        val=strtolist(val)
        val=[float(i) for i in val]
        if compare(data ,Vd.get(0)):
          vd=val[0]/val[1]*val[2]*val[3]
          value=str(round (vd,2))+'F'
        elif compare(data ,Vd.get(1)):
          vd=val[0]/val[1]
          value=str(round (vd,2))+'F'
        elif compare(data ,Vd.get(2)):
          vd=val[0]*val[1]*e*0.5/m
          value=str(round (vd,2))+'F'
        elif compare(data ,Vd.get(3)):
          vd=val[0]/val[1]*e
          value=str(round (vd,2))+'F'
        else:
          value="not a valid value type"
    except:
        value="invalid value given"
    return value
