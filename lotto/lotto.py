import random


def kugel():
    return random.randrange(1, 50)


def ziehung():
    zahlen = []
    while len(zahlen) < 7:
        zug = kugel()
        if zug in zahlen:
            pass
        else:
            zahlen.append(zug)
    return zahlen


def main():
    print("Willkommen zum Lotto-Simulator")
    zug = 1
    run = True
    while run == True:
        e = ziehung()
        g = list()
        for i in range(1, 7):
            g.append(e[i])
        g = sorted(g)
        print(
            "Ziehung",
            zug,
            "Zahlen:",
            g[0],
            g[1],
            g[2],
            g[3],
            g[4],
            g[5],
            "Zusatzzahl:",
            e[6],
        )
        # Für unsortierte Ausgabe:     e[0],e[1],e[2],e[3],e[4],e[5]
        check = input("\nNoch eine Ziehung y/n? ").lower()
        if check == "y":
            zug += 1
            run = True
        else:
            print("Auf Wiedersehen.")
            run = False


if __name__ == "__main__":
    main()
