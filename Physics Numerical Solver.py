print('*______________________________THE BASIC PHYSICS NUMERICAL SOLVER______________________________*')
print("Chapter 1. Electric Charges and Fields")
print("Chapter 2. Electrostatic Potential And Capacitance")
print("Chapter 3. Current Electricity")
print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('For:')
print('Volt=V, Current=I, Resistance=R, Charge=q, Radius=r, Electric Field=E, Power=P, Capacitance=C, Force=F')
print('Area=A, Distance=d, Drift velocity=Vd, Dielectric constant=K, Work done=W, Electric flux=Ef, Length=L')
print("Charge density=p, Induced charge=q', Polarisation=P', Volume=V, Two Charges=q1q2, Two Radius=r1r2")
print('#Note: All value must be in Standard Unit')
data=str(input("Which Values do Question have: "))
lst= data.split(',')
print(lst)
want=str(input("What Do Question want: "))
if want=='V':
  V=[['I','R'],['P','I'],['P','R'],['q','C'],['P','E','q'],['q','r']]
  for i in range(0,len(V)):
      lst.sort()
      V[i].sort()
      if lst == V[i]:
        print ("We can find Voltage from Given Information")
        Vnew=[]
        Vnew.append(V[i])
        if Vnew ==[['I','R']]:
          I=int(input('I='))
          R=int(input('R='))
          Volt=I*R
          print('Voltage is ',Volt,'V')
        if Vnew ==[['I','P']]:
          I=int(input('I='))
          P=int(input('P='))
          Volt=P/I
          print('Voltage is ',Volt,'V')
        if Vnew ==[['P','R']]:
          R=int(input('R='))
          P=int(input('P='))
          Volt=P*R
          print('Voltage is ',Volt,'V')
        if Vnew ==[['I','R']]:
          I=int(input('I='))
          R=int(input('R='))
          Volt=I*R
          print('Voltage is ',Volt,'V')
        if Vnew ==[['P','E','q']]:
          P=int(input('P='))
          E=int(input('E='))
          q=int(input('q='))
          Volt=P*E/q
          print('Voltage is ',Volt,'V')
        if Vnew ==[['q','r']]:
          q=int(input('q='))
          r=int(input('r='))
          Volt=(9*10**9)*q/r
          print('Voltage is ',Volt,'V')
          
          
                

  
  
