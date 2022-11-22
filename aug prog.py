
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]
aug2 = False
if len(aug)==12:
    ev2=True
    print(f'{aug2} ezek havi hőmérséklet!')
else:
    print(f'{aug2} ezek nem havi hőmérsékletek!')


legnagyobb =aug[0]
for i in aug:
    if i>legnagyobb:
        legnagyobb=i
print(f'{legnagyobb} a legnagyobb!')

legkissebb =aug[0]
for i in aug:
    if i<legkissebb:
        legkissebb=i
print(f'{legkissebb} a legkisseb!')

hanyszor=0
for x in aug:
    if x>31:
        hanyszor+=1
print(f'Ennyiszer:({hanyszor}) volt 31 fok')

print(f'A hőmérséklet {aug[21]} volt 20.-án')
atlag=0
for i in aug:
    atlag+=i
ert=atlag/len(aug)
print(f'{ert:0.1f} az átlag hőmérséklet.')
hoing=legnagyobb-legkissebb
print(f'Ekkora volt a hőingadozás: {hoing}')

wr=open('H:\\aug.txt','a')
wr.write(f'{legnagyobb} a legnagyobb\n')
wr.write(f'{legkissebb} a legkissebb\n')
wr.write(f'{aug2} \n')
wr.write(f'{i+1} \n')
wr.write(f'{hanyszor} \n')
wr.write(f'{hoing} a hőingadozás\n')
wr.write(f'{atlag} az átlag hőmérséklet\n')
wr.write(f'{aug[21]} a hőmérséklet 20.-án\n')
wr.close()