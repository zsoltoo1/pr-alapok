#feladat_025

honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
    # az eredeti listaelem NEM módosul!
    honap = honap.upper()	
    print(honap)
print(honapok)

for index in range(len(honapok)):
    # az eredeti listaelem módosul!
    honapok[index] = honapok[index].upper()    
print(honapok)
