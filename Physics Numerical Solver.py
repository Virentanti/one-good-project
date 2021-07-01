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
data=str(input("Which Values do Question have: "))
lst= data.split(',')
print(lst)
want=str(input("What Do Question want: "))
k=9*(10**9)
e0=8.85*(10**-12)
e=1.6*10**-19
try:
  if want=='V'or'emf':
    V=[['I','R'],['P','I'],['P','R'],['q','C'],['P','E','q'],['q','r']]
    for i in range(0,len(V)):
        lst.sort()
        V[i].sort()
        if lst == V[i]:
          print ("We can find Voltage from Given Information")
          Vnew=[]
          Vnew.append(V[i])
          if Vnew ==[['I','R']]:
            I=float(input('I='))
            R=float(input('R='))
            Volt=I*R
            print('Voltage(I*R) is ',Volt,'V')
          if Vnew ==[['I','P']]:
            I=float(input('I='))
            P=float(input('P='))
            Volt=P/I
            print('Voltage(P/I) is ',Volt,'V')
          if Vnew ==[['P','R']]:
            R=float(input('R='))
            P=float(input('P='))
            Volt=P*R
            print('Voltage(P*R) is ',Volt,'V')
          if Vnew ==[['I','R']]:
            I=float(input('I='))
            R=float(input('R='))
            Volt=I*R
            print('Voltage(I*R) is ',Volt,'V')
          if Vnew ==[['P','E','q']]:
            P=float(input('P='))
            E=float(input('E='))
            q=float(input('q='))
            Volt=P*E/q
            print('Voltage is(P*E/q) ',Volt,'V')
          if Vnew ==[['q','r']]:
            q=float(input('q='))
            r=float(input('r='))
            Volt=(k)*q/r
            print('Voltage is(k*q/r) ',Volt,'V')
          else:
            if lst != V[i]:
              print('We cannot find Voltage from Given Information')
            break
  elif want=='C':
    C=[['q','V'],['A','d'],['U','V'],['U','q'],['n','V'],['r1r2'],['r1r2','L']]
    for i in range(0,len(C)):
        lst.sort()
        C[i].sort()
        if lst == C[i]:
          print ("We can find Capacitance from Given Information")
          Cnew=[]
          Cnew.append(C[i])
          if Cnew ==[['q','V']]:
            q=float(input('q='))
            V=float(input('V='))
            Cap=q/V
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['U','V']]:
            U=float(input('U='))
            V=float(input('V='))
            Cap=2*U/(V**2)
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['q','U']]:
            q=float(input('q='))
            U=float(input('U='))
            Cap=q**2/2*U
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['n','V']]:
            n=float(input('n='))
            V=float(input('V='))
            Cap=n*e/V
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['A','d']]:
            A=float(input('A='))
            d=float(input('d='))
            Cap=e0*A/d
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['q','r1r2']]:
            q=float(input('q='))
            r1=float(input('r1(inner)='))
            r2=float(input('r2(outer)='))
            Cap=(4*(3.14)*e0*r1*r2)/r1 - r2
            print('Capacitance is() ',Cap,'F')
          if Cnew ==[['L','r1r2']]:
            L=float(input('L='))
            r1=float(input('r1(inner)='))
            r2=float(input('r2(outer)='))
            Cap=(2*(3.14)*e0*L)/(math.log(r2/r1))
            print('Capacitance is() ',Cap,'F')
          else:
            if lst != C[i]:
              print('We cannot find Capacitance from Given Information')
            break
      

except:
  print('invalid datatype provided')













          
  
