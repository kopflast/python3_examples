# Import the numpy module
import numpy as np
import os

# Variables

workpath = os.getcwd()
folder_text = "texte"
filelist = [fname for fname in os.listdir(folder_text)]

def mix(a, b):
    words = a
    f = b
    fn = (os.path.join(workpath + '/' + folder_text + '/' + f))
    # Random startpoint for the chain, first Letter Uppercase
    # graped text from Website as txt-file
    # lasswitz = open('lasswitz_text.txt', encoding='utf8').read()
    mytext = open(fn, encoding="utf8").read()
    # split text in words, delete whitespace and leave signs
    corpus = mytext.split()  # lasswitz.split()
    # generate word-pairs
    def make_pairs(corpus):
        for i in range(len(corpus) - 1):
            yield (corpus[i], corpus[i + 1])

    pairs = make_pairs(corpus)
    # create dictonary from word-pairs
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)
    while first_word.islower():
        first_word = np.random.choice(corpus)
    chain = [first_word]
    n_words = words  # 128  Lenght of the result in words
    # generate chain
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))
    ausgabe = " ".join(chain)

    return "Aus " + str(f) + " Anz. Worte " + str(words) + ":\n\n" + ausgabe + "...\n\nZeichen: " + str(len(ausgabe))


# Import the tkinter module
import tkinter as tk
from tkinter import ttk

# GUI


# Erstelle das Hauptfenster
root = tk.Tk()
root.title("Einfache GUI")

# Erstelle einen Textbereich
text_area = tk.Text(root)
text_area.grid(rowspan=4, columnspan=3)
text_area.insert("end", "Hallo, Drücke 'MIX' und freu dich!\n\n")


# Eingabefeld
label = tk.Label(root, text="Eingabe Anzahl Worte:")
label.grid(row=5, column=0)
entry = tk.Entry(root)
entry.insert(0, "24")
entry.grid(row=5, column=1)

# Erstelle einen "MIX"-Button
def on_button_press():
    value = int(entry.get())
    return value


def next_button_clicked():
    filename = optmenu.get()
    out = mix(on_button_press(), filename)
    text_area.insert("end", out + "\n\nNochmal? Drück 'MIX'.\n\n")
    text_area.see("end")

next_button = tk.Button(root, text="MIX", command=next_button_clicked)
next_button.grid(row=5, column=2)


# Erstelle eine Auswahlbox für das Textfile

label1 = tk.Label(root, text="Wähle ein Textfile:")
label1.grid(row=6, column=0)
optmenu = ttk.Combobox(root, values=filelist, state="readonly")
optmenu.set(filelist[0])
optmenu.grid(row=6, column=1)

# Erstelle einen "Programmende"-Button
def exit_button_clicked():
    root.destroy()


exit_button = tk.Button(root, text="Programmende", command=exit_button_clicked)
exit_button.grid(row=7, column=2)

# Starte die GUI-Schleife
root.mainloop()
