import time

# -> Votre programme proposera 3 options :

# - Oeufs à la coque : 3 minutes

# - Oeufs mollets : 6 minutes

# - Oeufs durs : 9 minutes


"""def point():
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)


def cuisson(temps):
    d = temps
    min = d//60
    sec = d-min*60
    print(f"{min:02d}")
    print(sec)
    print("cuisson en cours", point())

    # for i in range(10):
    #     time.sleep(1)
    #     print(".", end="", flush=True)
    # print("")
    # print("Fin du programme")"""


print()
print('CUISSON DES OEUFS')
print("-----------------")
print("a - oeufs à la coque: 3 minutes")
print("b - oeufs mollets: 6 minutes")
print("c - oeufs durs 9: minutes")
print()
choix = input("Quel est votre choix ? ")

duree = 0
if choix == "a":
    duree = 3*60
if choix == "b":
    duree = 6*60
if choix == "c":
    duree = 9*60

while True:
    for i in range(10):
        time.sleep(1)
        duree -= 1
        if duree <= 0:
            break
        print(".", end="", flush=True)
    if duree <= 0:
        break
    min = duree//60
    sec = duree-min*60
    print()
    print(f"temps restant:{min:02d}:{sec:02d}", end="", flush=True)
print()
print("Cuisson terminé")
