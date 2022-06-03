"""
Programma, kas palīdz matemātikas skolotājai
Programmu veidojis:
 DP1-2 Audzēknis
 Guntis Gūtmanis
"""

import shutil
from time import sleep
columns = shutil.get_terminal_size().columns


def teorija():
    
    print("Teorija".center(columns))
    sleep(1)
    print("Kombinatorikas pamatlikumi".center(columns))
    sleep(2)
    print("1.Saskaitīšanas likums:\n Ja no dotās kopas kādu elementu A var izvēlēties n veidos, bet elementu B – m veidos, tad A vai B var izvēlēties n + m veidos.")
    sleep(3)
    print("2. Reizināšanas likums.\n Ja no dotās kopas kādu elementu A var izvēlēties n veidos, bet elementu B – m veidos, tad elementu pāri A un B var izvēlēties n *  m veidos.")

def piemers():
    print("Kombinatorikas pamatlikuma piemērs\n\n".center(columns))
    print("Piemērs")
    print("Vienā šķīvī 5 dažādu šķirņu āboli, bet otrā – 4 dažādi bumbieri.")
    print("   1) Cik veidos var izvēlēties vienu augli?\n   2) Cik veidos var izvēlēties dažādu augļu pāri?\n\n")

#!!ATGĀDINĀJUMS IELIKT IESPĒJU LIETOTĀJAM IEVADĪT ATBILDI!!!
    
    print("Risinājums:\n   1) Jāizvēlas ābolu vai bumbieri, tātad 5+4=9 veidos.\n   2)Katram izvēlētajam ābolam varam piekārtot 4 bumbierus no otrā šķīvja. Tātad kopā augļu pāri varam izvēlēties 5⋅ 4 = 20 veidos.")

def uzdevumi():
    print("Pārbaudes darbs".center(columns))
    print("Tēma Kombinatorikas pamatlikumi".center(columns))
    print("Uzdevumi:\n")
    print("1. Martai ir 3 šorti, 2 svārki un 4 bikses. Cik dažādu apģērbu komplektu var izveidot ar pelēko topu?\nAtbildes:")
    
uzdevumi()



