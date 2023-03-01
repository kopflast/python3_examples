# Zahlenraten

"""
    Eine zufällige Zahl zwischen 111 und 999 wird gesucht. Der Zufall sucht die Zahl aus.
    Der Spieler/in gibt eine dreistellige Zahl ein und das Programm vergleicht die Eingabe mit
    der ausgesuchten Zahl. Eine Ausgabe verrät ob die Eingabe zu groß zu klein oder treffend ist.
    Zum Ende wird die Anzahl der Versuche und die gespielte Zeit in Sekunden ausgegeben.
    
    
    Eine kleine Übung in Python 3.10 von kopflast 2023 

"""

import random as rd
import time as tm


def zeit():
    zeit = tm.time()
    return zeit


def dauer(start, ende):
    d = ende - start
    return round(d)


zahl = rd.randrange(111, 999)

def main():
    run = True
    print("Start")
    versuche = 0
    start_zeit = zeit()
    while run == True:
        chk = False
        while chk == False:
            eingabe = int(input("Gib eine dreistellige Zahl ein: "))
            if eingabe >= 111 and eingabe <= 999:
                chk = True
        versuche += 1
        if eingabe == zahl:
            run = False
            end_zeit = zeit()
            gebraucht = dauer(start_zeit, end_zeit)
            print(
                "Du hast "
                + str(versuche)
                + " Versuche in "
                + str(gebraucht)
                + " Sekunden gebraucht!"
            )
            print("Ende")
            check = input("\nNochmal y/n? ").lower()
            if check == "y":
                main()            
            else:
                print("Auf Wiedersehen.")
                run = False
        if eingabe > zahl:
            print("Deine Zahl ist zu groß!")
        if eingabe < zahl:
            print("Deine Zahl ist zu klein!")



if __name__ == "__main__":
    main()
