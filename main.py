import random
import matplotlib.pyplot as plt

benzersizListe = []

def benzersizListeYapıcı():

    global benzersizListe

    x = list(range(8))

    random.shuffle(x)

    benzersizListe = x

def kusur_var_mi(liste):

    for i in range(8):
        for j in range(i + 1, 8):

            x_farki = abs(i - j)

            y_farki = abs(liste[i] - liste[j])

            if x_farki == y_farki:
                return True

    return False

def cozum_bul():

    deneme_sayisi = 0
    while True:
        deneme_sayisi += 1
        benzersizListeYapıcı()

        if not kusur_var_mi(benzersizListe):
            print(f"\n--- ÇÖZÜM BULUNDU! ({deneme_sayisi}. denemede) ---")
            print(f"Kusursuz Dizilim: {benzersizListe}")

            break

cozum_bul()

x_koordinatlari = list(range(1, 9))

y_koordinatlari = [ y+1 for y in benzersizListe]

plt.figure(figsize=(7, 7))
plt.scatter(x_koordinatlari, y_koordinatlari, s=700, c="#ffbd11", marker='*', edgecolors='black')

eksen_etiketleri = list(range(1, 9))
plt.xticks(eksen_etiketleri)
plt.yticks(eksen_etiketleri)

plt.xlim(0, 9)
plt.ylim(0, 9)

plt.grid(True, linewidth=1.5, color='gray', alpha=0.5)

plt.title("8 Vezir Çözümü", fontsize=14)
plt.xlabel("X Ekseni", fontsize=12)
plt.ylabel("Y Ekseni", fontsize=12)

plt.show()