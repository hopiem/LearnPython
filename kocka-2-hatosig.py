import random

dobasokSzama = 0
hatosKijott = 0

while hatosKijott < 2:
    dobas = random.choice(range(1, 7))
    dobasokSzama = dobasokSzama + 1

    print('dobások száma: ' + str(dobasokSzama) + ', dobás száma: ' + str(dobas) + '. 6-osok:' + str(hatosKijott))  
    
    if dobas == 6:
        print('KIJÖTT a 6 -os! :)')
        hatosKijott += 1

print('\n -->> Ennyi dobásból sikerült: ' + str(dobasokSzama) + '\n')
