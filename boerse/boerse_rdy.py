#! /usr/bin/python3
# -*- coding: utf-8 -*-

# Einbinden von externem Code
import random, os, sys

# Variablen
# *-------*
# colors
rst = "\033[0m"
vsw = "\033[30m"
vro = "\033[31m"
vgr = "\033[32m"
vgl = "\033[33m"
vbl = "\033[34m"
vma = "\033[35m"
vcy = "\033[36m"
vwe = "\033[37m"
# bg-colors
bsw = "\043[30m"
bro = "\043[31m"
bgr = "\043[32m"
bgl = "\043[33m"
bbl = "\043[34m"
bma = "\043[35m"
bcy = "\043[36m"
bwe = "\043[37m"
# game vars
spname = "x"
spgeld = 5000
spakt = [0, 0, 0, 0]
firma = ["LIDL", "ALDI", "PLUS", "REWE"]
aktien = [500, 500, 500, 500]
kurs = [100, 100, 100, 100]
karte = [0, 0, 0, 0]
wert = [-25, -15, -5, 0, 5, 15, 25]
auswahl = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maxkurs = 250
runde = 1

# print headlines
def kopf():
    global spname
    ausgabe = ""
    for i in range(0, 80):
        ausgabe += "*"
    print(vro + ausgabe)
    print("*" + "{0:^78}".format("Börse") + "*")
    print(ausgabe + rst)
    print(vgr)
    print("Guten Tag!\nMöchtest Du dich in die Händlerliste eintragen?")
    print(
        "Wir müssen nur noch Deinen Namen auf die Zulassung schreiben und\nschon steht Dir der Handelsraum offen."
    )
    spname = input("Dein Name? ")
    print("\n=> Trader " + spname + " wurde heute zur Börse zugelassen. <=\n" + rst)
    print(vro + ausgabe + rst)

# player stats
def spkonto():
    ausgabe = ""
    for i in range(0, 30):
        ausgabe += "~"
    print(vcy + ausgabe)
    global spname
    print(vcy + "=> Kontoauszug für " + spname)
    print("Geldeinlage: " + str(spgeld))
    print("{0:5}{1:>7}{2:>11}".format("Firma", "Aktien", "Wert in €"))
    for i in range(0, 4):
        print(
            "{0:>5}{1:>7}{2:>11}".format(
                firma[i], str(spakt[i]), str(spakt[i] * kurs[i]) + " €"
            )
        )
    print(ausgabe + rst)

# view the facts
def show_kurs():
    ausgabe = ""
    for i in range(0, 30):
        ausgabe += "~"
    print(vgr + ausgabe)
    print("=> Aktuelle Aktienkurse!")
    print("{0:5}{1:>7}{2:>7}{3:>11}".format("Firma", "Kurs", "Aktien", "Wert in €"))
    for i in range(0, 4):
        print(
            "{0:>5}{1:>7}{2:>7}{3:>11}".format(
                firma[i], str(kurs[i]), str(aktien[i]), str(aktien[i] * kurs[i]) + " €"
            )
        )
    print(ausgabe + rst)

# take a turn
def zug():
    global runde
    ausgabe = ""
    for i in range(0, 30):
        ausgabe += "~"
    print(vro + "\n#####     #####     #####")
    print("=> Start von Runde " + str(runde) + " <=")
    print(vro + "#####     #####     #####\n" + rst)
    print(vgl + ausgabe)
    print("=> Achtung Kursbewegungen!!!")
    print(vma + "Computer zieht..." + vgl)
    for i in range(0, 4):
        karte[i] = wert[random.randint(0, 6)]
    print("{0:5}{1:>4}{2:>4}{3:>4}".format("Firma", " alt", " +/- ", " neu"))
    for i in range(0, 4):
        print(
            "{0:>5}{1:>4}{2:>4}{3:>4}".format(
                firma[i], str(kurs[i]), str(karte[i]), str(kurs[i] + karte[i])
            )
        )
        kurs[i] = kurs[i] + karte[i]
    print(ausgabe + rst)
    runde += 1
    for a in range(0, 4):
        for b in range(0, 4):
            auswahl[a][b] = wert[random.randint(0, 6)]
    print(vgl + "=> Kurse manipulieren?")
    print(vma + "Du ziehst ..." + vgl)
    print(
        "{0:3}{1:>5}{2:>5}{3:>5}{4:>5}".format(
            "Opt", firma[0], firma[1], firma[2], firma[3]
        )
    )
    for i in range(0, 4):
        print(
            "{0:^3}{1:>5}{2:>5}{3:>5}{4:>5}".format(
                str(i + 1),
                str(auswahl[i][0]),
                str(auswahl[i][1]),
                str(auswahl[i][2]),
                str(auswahl[i][3]),
            )
        )
    kpr = input("Welche Manipulation soll durchgeführt werden? (1-4)")
    s = int(kpr)
    if s in (1, 2, 3, 4):
        s -= 1
        print("{0:5}{1:>4}{2:>4}{3:>4}".format("Firma", " alt", " +/- ", " neu"))
        for i in range(0, 4):
            print(
                "{0:>5}{1:>4}{2:>4}{3:>4}".format(
                    firma[i],
                    str(kurs[i]),
                    str(auswahl[s][i]),
                    str(kurs[i] + auswahl[s][i]),
                )
            )
            kurs[i] = kurs[i] + auswahl[s][i]
    print(ausgabe + rst)

# sell and buy
def handel():
    global spgeld
    ausgabe = ""
    deal = False
    for i in range(0, 30):
        ausgabe += "~"
    print(vgr + ausgabe)
    print("=> Parketthandel!")
    while deal == False:
        print("Welche Firma möchtest du handeln?")
        print(
            "(1) "
            + firma[0]
            + "\n(2) "
            + firma[1]
            + "\n(3) "
            + firma[2]
            + "\n(4) "
            + firma[3]
        )
        kpr = input("1-4? ")
        if kpr in ("1", "2", "3", "4"):
            s = int(kpr) - 1
            print("Von " + firma[s] + " sind " + str(aktien[s]) + " Aktien verfügbar.")
            print("Du besitzt " + str(spakt[s]) + " Aktien und " + str(spgeld) + "€.")
            print(
                "Du kannst max "
                + str(int(spgeld / kurs[s]))
                + " Aktien zu "
                + str(kurs[s])
                + "€ je Aktie kaufen"
            )
            print(
                "Du kannst max "
                + str(spakt[s])
                + " Aktien zu "
                + str(kurs[s])
                + "€ je Aktie verkaufen"
            )
            kpr = input("(k)aufen / (v)erkaufen? (k/v)")
            if kpr == "k":
                amax = int(spgeld / kurs[s])
                print(
                    "=> Du kannst max " + str(int(spgeld / kurs[s])) + " Aktien kaufen."
                )
                kpr = input("Wieviele Aktien möchtest Du kaufen? 1-" + str(amax) + "?")
                if int(kpr) <= amax:
                    aktien[s] = aktien[s] - int(kpr)
                    spakt[s] = spakt[s] + int(kpr)
                    spgeld = spgeld - kurs[s] * int(kpr)
                    print(
                        vro
                        + "Deal! Du besitzt jetzt "
                        + str(spakt[s])
                        + " Aktien und "
                        + str(spgeld)
                        + " €."
                        + vgr
                    )
                deal = True
            if kpr == "v":
                amax = int(spgeld / kurs[s])
                print("=> Du kannst max " + str(spakt[s]) + " Aktien verkaufen.")
                kpr = input(
                    "Wieviele Aktien möchtest Du verkaufen? 1-" + str(spakt[s]) + "?"
                )
                if int(kpr) <= spakt[s]:
                    aktien[s] = aktien[s] + int(kpr)
                    spakt[s] = spakt[s] - int(kpr)
                    spgeld = spgeld + kurs[s] * int(kpr)
                    print(
                        "Deal! Du besitzt jetzt "
                        + str(spakt[s])
                        + " Aktien und "
                        + str(spgeld)
                        + " €."
                    )
                deal = True
    print(ausgabe + rst)

# gameloop
def spiel():
    # m für Menu, i Spielerkonto, k Kurs ,n nächste Runde, h handel
    kpr = ""

    while kpr != "q":
        print(vwe + "Runde: " + str(runde) + rst)
        kpr = input(vwe + "Was tun (m - Menu)? ")
        if kpr == "m":
            print(
                vma
                + "\n m - Menu\n i - Spielerkonto\n k - Kursübersicht\n h - Handel\n n - nächste Runde\n q - Spielende\n"
            )
        if kpr == "i":
            spkonto()
        if kpr == "k":
            show_kurs()
        if kpr == "n":
            zug()
        if kpr == "h":
            handel()
        if kpr == "q":
            kpr = input(vro + "Wirklich aufhören? (j/n)")
            if kpr == "j":
                print(rst)
                break

# main funktion
def main():
    os.system("clear")
    kopf()
    spkonto()
    show_kurs()
    spiel()

# Start point
if __name__ == "__main__":
    main()
