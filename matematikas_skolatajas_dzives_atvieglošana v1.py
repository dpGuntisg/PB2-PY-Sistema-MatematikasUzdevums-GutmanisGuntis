"""
Programma, kas palīdz matemātikas skolotājai
Programmu veidojis:
 DP1-2 Audzēknis
 Guntis Gūtmanis
"""

import shutil
from time import sleep
columns = shutil.get_terminal_size().columns


    
########################################################################################################################################    

def teorija():
    print("Teorija".center(columns))
    sleep(1)
    print("Kombinatorikas pamatlikumi".center(columns))
    sleep(2)
    print("1.Saskaitīšanas likums:\n Ja no dotās kopas kādu elementu A var izvēlēties n veidos, bet elementu B – m veidos, tad A vai B var izvēlēties n + m veidos.")
    sleep(3)
    print("2. Reizināšanas likums.\n Ja no dotās kopas kādu elementu A var izvēlēties n veidos, bet elementu B – m veidos, tad elementu pāri A un B var izvēlēties n *  m veidos.\n")
    print("Jūs esat izlasījis teoriju. Vai vēlaties atvērt piemērus, ja jā spiediet 2, ja vēlaties pildīt pārbaudes darbu spiediet 3, bet ja vēlaties izslēgt programmu spiediet 0")
    darbiba = int(input("Izvēle: "))
    if darbiba == 2:
        piemers()
    elif darbiba == 3:
        uzdevumi()
    elif darbiba == 0:
        exit
                
#########################################################################################################################################

def risinajums():    
    print("Risinājums:\n   1)Jāizvēlas ābolu vai bumbieri, tātad 5+4=9 veidos.\n   2)Katram izvēlētajam ābolam varam piekārtot 4 bumbierus no otrā šķīvja. Tātad kopā augļu pāri varam izvēlēties 5⋅ 4 = 20 veidos.")

def piemers():
    print("Kombinatorikas pamatlikuma piemērs\n\n".center(columns))
    print("Piemērs")
    print("Vienā šķīvī 5 dažādu šķirņu āboli, bet otrā – 4 dažādi bumbieri.")
    print("   1) Cik veidos var izvēlēties vienu augli?\n   2) Cik veidos var izvēlēties dažādu augļu pāri?\n\n")
    pirmaatbilde = int(input("1) "))
    otraatbilde = int(input("2) "))
    if pirmaatbilde == 9 and otraatbilde == 20:
        print("Malacis! Tev ir pareizi!")
    elif pirmaatbilde == 9 and otraatbilde != 20:
        print("Tu kļūdijies otrājā piemērā!")
        risinajums()
    elif pirmaatbilde != 9 and otraatbilde == 20:
        print("Tu kļūdījies pirmajā piemērā!")
        risinajums()
    else:
        print("Nepareizi!")
        risinajums()
    print("Jūs esat izpildījis piemērus. Vai vēlaties atvērt teoriju?, ja jā spiediet 1, ja vēlaties pildīt pārbaudes darbu spiediet 3, bet ja vēlaties izslēgt programmu spiediet 0")
    darbiba = int(input("Izvēle: "))
    if darbiba == 1:
        teorija()
    elif darbiba == 3:
        uzdevumi()
    elif darbiba == 0:
        exit 
 
##########################################################################################################################################

punkti = 0
def uzdevumi():
    print("Pārbaudes darbs".center(columns))
    print("Tēma Kombinatorikas pamatlikumi".center(columns))
    print("Uzdevumi:\n")
    print("1. Martai ir 3 šorti, 2 svārki un 4 bikses. Cik dažādu apģērbu komplektu var izveidot ar pelēko topu?\nAtbildes:\n1\nNevar aprēķināt\n9\n24\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 9:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
       
    print("2. Ervīnam ir 5 T-krekli un 4 bikses. Cik dažādu apģērbu komplektu viņš var izveidot?\nAtbildes:\n20\nNevar aprēķināt\n1\n9\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 20:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("3. Cik dažādu 6 ciparu skaitļus var izveidot, ja pirmajam ciparam jābūt 2?\nAtbildes:\n6\n100000\n50\n60\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 100000:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("4. Cik dažādu trīsciparu skaitļu var izveidot, lai cipari neatkārtotos?\nAtbildes:\n3\n30\n100\n648\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 648:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("5. Cik dažādu trīsciparu skaitļu var izveidot?\nAtbildes:\n29\n30\n900\n1000\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 900:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("6. Cik dažādu trīsciparu pāru skaitļu var izveidot?\nAtbildes:\n5\n450\n900\n17\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 450:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("7. Cik dažādu trīs burtu kodu var izveidot no 23 burtiem?\nAtbildes:\n3\n69\n10626\n12167\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 12167:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("8. Cik dažādu piecu burtu “vārdu” var izveidot no burtiem ZEBRA?\nAtbildes:\n120\n25\n3125\n5\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 120:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
        
    print("9. Cik dažādu “vārdu” var izveidot no burtiem ZEBRA, ja burti var atkārtoties?\nAtbildes:\n5\n25\n3125\n120\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 3125:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
    print("10. Cik dažādu 4 burtu “vārdu” var izveidot no vārda ZEMENE burtiem?\nAtbidles:\n24\n16\n4\n256\n")
    atbilde = int(input("Ievadiet atbildi: "))
    if atbilde == 24:
        print("Pareizi!")
        punkti = punkti + 1
    else:
        print("Nepareiza atbilde!")
    print('Tev ir'  , punkti,'/10 punkti' )
    print("Jūs esat izpildījis Pārbaudes darbu. Vai vēlaties atvērt teoriju?, ja jā spiediet 1, ja vēlaties redzēt piemērus spiediet 2, bet ja vēlaties izslēgt programmu spiediet 0")
    darbiba = int(input("Izvēle: "))
    if darbiba == 1:
        teorija()
    elif darbiba == 3:
        uzdevumi()
    elif darbiba == 0:
        exit

###########################################################################################################################################

print("Kombinatorikas pamatlikumi".center(columns))
print("Šajā programma ir 4 iespējas")
print("Ir kombinatorikas pamatlikuma teorija, lai atvērtu spiediet 1")
print("Ir kombinatorikas pamatlikuma piemēri, lai atvērtu spiediet 2")
print("Ir kombinatorikas pamatlikuma pārbaudes darbs, lai atvērtu spiediet 3")
print("Ja vēlieties izslēgt programmu, spiediet 0")
darbiba = int(input("Iespēja: "))
if darbiba == 1:
    teorija()
elif darbiba == 2:
    piemers()
elif darbiba == 3:
    uzdevumi()
