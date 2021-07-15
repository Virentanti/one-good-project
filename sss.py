import math

print('*______________________________THE BASIC PHYSICS NUMERICAL SOLVER______________________________*')
print("Chapter 1. Electric Charges and Fields")
print("Chapter 2. Electrostatic Potential And Capacitance")
print("Chapter 3. Current Electricity")
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('For:')
print('Volt=V, Current=i, Resistance=R, Charge=q, Radius=r, Electric Field=E, Power=P, Capacitance=C, Force=F')
print('Area=A, Distance=d, Drift velocity=Vd, Dielectric constant=K, Work done=W, Electric flux=Ef, Length=L')
print("Charge density=p, Induced charge=q', Polarisation=P', Volume=V, Two Charges=q1q2, Two Radius=r1r2")
print('Electromotive force=emf, Stored energy=u, No. of Electron=n ,Potential difference=U ')
print('*Shape=shape, Angle=x, Time=t,Current density=j ')
print('#Note: All value must be in Standard Unit')
data=str(input("Which Values do Question have: "))  #Getting available data from the user
lst= data.split(',')    #converting available data to list
print(lst)
want=str(input("What Do Question want: "))  #getting what user wants
#----->Defined Constants
k=9*(10**9)
e0=8.85*(10**-12)
e=1.6*10**-19
m=9.11*10**-31
#----->To Compare Lists
if want=='V'or want=='emf' or want=='V':
  V=[['i','R'],['P','i'],['P','R'],['q','c'],['P','E','q'],['q','r']]
  for i in range(0,len(V)):
      lst.sort()
      V[i].sort()
      if lst == V[i]:
        print ("We can find Voltage from Given Information")
        Vnew=[]
        Vnew.append(V[i])
        if Vnew ==[['i','R']]:
          i=float(input('i='))
          R=float(input('R='))
          Volt=i*R
          print('Voltage(I*R) is ',round(Volt, 2),'V')
        if Vnew ==[['i','P']]:
          i=float(input('i='))
          P=float(input('P='))
          Volt=P/i
          print('Voltage(P/I) is ',round(Volt, 2),'V')
        if Vnew ==[['P','R']]:
          R=float(input('R='))
          P=float(input('P='))
          Volt=P*R
          print('Voltage(P*R) is ',round(Volt, 2),'V')
        if Vnew ==[['q','c']]:
          q=float(input('q='))
          c=float(input('c='))
          Volt=q/c
          print('Voltage(q/C) is ',round(Volt, 2),'V')
        if Vnew ==[['P','E','q']]:
          P=float(input('P='))
          E=float(input('E='))
          q=float(input('q='))
          Volt=P*E/q
          print('Voltage is(P*E/q) ',round(Volt, 2),'V')
        if Vnew ==[['q','r']]:
          q=float(input('q='))
          r=float(input('r='))
          Volt=(k)*q/r
          print('Voltage is(k*q/r) ',round(Volt, 2),'V')

if want=='C':
  C=[['q','V'],['A','d'],['U','V'],['U','q'],['n','V'],['r1r2'],['r1r2','l']]
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
          print('Capacitance is(q/V) ',round(Cap, 2),'F')
        if Cnew ==[['U','V']]:
          U=float(input('U='))
          V=float(input('V='))
          Cap=2*U/(V**2)
          print('Capacitance is(2U/(V^2)) ',round(Cap, 2),'F')
        if Cnew ==[['q','U']]:
          q=float(input('q='))
          U=float(input('U='))
          Cap=q**2/(2*U)
          print('Capacitance is(q^2/(2U)) ',round(Cap, 2),'F')
        if Cnew ==[['n','V']]:
          n=int(input('n='))
          V=float(input('V='))
          Cap=n*e/V
          print('Capacitance is(n*e/V) ',round(Cap, 2),'F')
        if Cnew ==[['A','d']]:
          A=float(input('A='))
          d=float(input('d='))
          Cap=e0*A/d
          print('Capacitance is(e0*A/d) ',round(Cap, 2),'F')
        if Cnew ==[['r1r2']]:
          r1=float(input('r1(Outer)='))
          r2=float(input('r2(Inner)='))
          if r1==r2:
              print('Both radius can not have same value ')
          else:
              Cap=(4*(3.14)*e0*r1*r2)/(r1 - r2)
              print('Capacitance is((4π*e0*r1*r2)/(r1 - r2)) ',round(Cap*10**10, 4),'x10^-4 uF')
        if Cnew ==[['l','r1r2']]:
          l=float(input('l='))
          r1=float(input('r1(Outer)='))
          r2=float(input('r2(Inner)='))
          Cap=(2*(3.14)*e0*l)/(math.log(r1/r2))
          print('Capacitance is(2π*e0*l)/log(r2/r1) ',round(Cap*10**10, 4),'x10^-4 uF')
          
          
if want=='vd':
  Vd=[['i','A','q','n'],['l','t'],['j','n']]
  for i in range(0,len(Vd)):
      lst.sort()
      Vd[i].sort()
      if lst == Vd[i]:
        print ("We can find Drift Velocity from Given Information")
        Vdnew=[]
        Vdnew.append(Vd[i])
        if Vdnew ==[['i','A','q','n']]:
          i=float(input('i='))
          A=float(input('A='))
          q=float(input('q='))
          n=int(input('n='))
          Veld=i/(A*q*n)
          print('Drift Velocity is() ',round(Veld, 2),'m/sec')
        if Vdnew ==[['l','t']]:
          l=float(input('Distane='))
          t=int(input('Av. Collision time='))
          Veld=l/t
          print('Drift Velocity is() ',round(Veld, 2),'m/sec')
        if Vdnew ==[['E','t']]:
          E=float(input('E='))
          t=float(input('t='))
          Veld=0.5*(e*E*t/m)
          print('Drift Velocity is((e*E*t/2m)) ',round(Veld, 2),'m/sec')
        if Vdnew ==[['j','n']]:
          j=float(input('j='))
          n=int(input('n='))
          Veld=j/(n*e)
          print('Drift Velocity is(j/(n*e)) ',round(Veld, 2),'m/sec')
      elif lst != Vd[i]:
         print('We cannot find Drift Velocity from Given Information')
      break
          


          
          

