#!/usr/bin/python3
"""
    ZAHLENRATEN
    Mastermindclone
    code style fixed with black
    kopflast, 2023
"""

import random as rd


def main():
    # Kopfausgabe
    print("Willkommen zum Zahlenraten (kopflast '23)")
    regel = """
    5 Zahlen werden aus 0-9 gezogen.
    Gib 5 Zahlen zwischen 0 und 9 ein, dann
    drück "Eingabe".
    Du erhältst einen Hinweis:
            * - kommt nicht vor.
            O - kommt vor.
            X - richtig
    """
    print(regel)

    # Listen anlegen
    gesucht = list()
    eingabe = list()
    
    # Erstelle Liste aus 5 Zufallszahlen (Zahlen können doppelt vorkommen)
    for i in range(1, 6):
        gesucht.append(str(rd.randint(0, 9)))
    print(gesucht)
    
    # Variablen für Schleife vorbereiten
    play = True
    hit = 0
    versuche = 0
    
    # Spielschleife
    while play == True:
        print("Gibt 5 Zahlen ein zwischen 0 und 9")
        check = False
        while check == False:
            ein = input("Eingabe: ")
            if len(ein) == 5:                
                if ein.isdecimal():
                    check = True
            else:
                print("Eingabe ungültig")
                ein = ""
        versuche += 1
        for zeichen in ein:
            eingabe.append(zeichen)
        print(eingabe)
        hinweis = ["*", "*", "*", "*", "*"]
        z1 = 0
        for zeichen in eingabe:
            z2 = 0
            for nummer in gesucht:
                if eingabe[z1] == gesucht[z2]:
                    if z1 == z2:
                        hinweis[z1] = "X"
                        hit += 1
                    else:
                        if hinweis[z1] != "X":
                            hinweis[z1] = "O"
                z2 += 1
            z1 += 1
        print("Versuche:", versuche)
        print(hinweis)

        if hit == 5:
            print("Volltreffer!! in", versuche, "Versuchen!")
            # Ask for repeat
            ask = input("Ende mit x? ").lower()
            if ask == "x":
                play = False            
            else:
                '''
                play = True
                eingabe.clear()
                gesucht.clear()
                hit = 0
                versuche = 0
                '''
                print("\n------------------------------------\n")
                main()
        else:
            hit = 0
            eingabe.clear()

# Start the loop
if __name__ == "__main__":
    main()
