
ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]
ev2 = False
if len(ev)==12:
    ev2=True
    print(f'ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')
# ----------------------------------------------------------------------
legnagyobb =ev[0]
for i in ev:
    if i>legnagyobb:
        legnagyobb=i
print(f'{legnagyobb} a legnagyobb!')
# ----------------------------------------------------------------------
hely=len(ev)
ker=legnagyobb
z=0
while ev[z] !=ker:
    z+=1
print(f"Hanyadik helyen van: {z+1}")
# ----------------------------------------------------------------------
legkissebb =ev[0]
for i in ev:
    if i<legkissebb:
        legkissebb=i
print(f'{legkissebb} a legkisseb!')
#----------------------------------------------------------------------
összeg=0
for szam in ev:
    összeg+=szam
print(f'{összeg} ennyi van összesen!')
# ----------------------------------------------------------------------
hanyszor=0
for x in ev:
    if x>2400:
        hanyszor+=1
print(hanyszor)  
# ----------------------------------------------------------------------
wr=open('H:\\ev.txt','a')
wr.write(f'{legnagyobb} a legnagyobb\n')
wr.write(f'{legkissebb} a legkissebb\n')
wr.write(f'{ev2} \n')
wr.write(f'{z+1} \n')
wr.write(f'{hanyszor} \n')
wr.write(f'{összeg} az összege\n')
wr.close()