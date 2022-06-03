#Programma, kas palīdz matemātikas skolotājai
#Programmu veidojis DP1-2 Audzēknis Guntis Gūtmanis

import shutil
from time import sleep

def teorija():
    columns = shutil.get_terminal_size().columns
    print("Teorija".center(columns))
    sleep(1)
    print("Kombinatorikas pamatlikums".center(columns))
    sleep(1)
    print("Ja no dotās kopas kādu elementu A var izvēlēties n veidos, bet elementu B – m veidos, tad elementu pāri A un B var izvēlēties n * m veidos.")
    sleep(3)
    print("Piemērs:\n Vienā šķīvī 5 dažādu šķirņu āboli, bet otrā – 4 dažādi bumbieri. Cik veidos var izvēlēties dažādu augļu pāri?  ")
    sleep(10)
    print("Risinājums:\n Katram izvēlētajam ābolam varam piekārtot 4 bumbierus no otrā šķīvja. Tātad kopā augļu pāri varam izvēlēties 5 * 4 = 20 veidos.")
teorija()



