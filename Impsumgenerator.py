# Vytvořte vlastní  projektu Lorem Ipsum generátoru.
# Nastavte uživatelské parametry, tak, aby byl výsledek co nejpodobnější nějaké jazykové variantě apod.

# Co je třeba zhodnotit (pár nápadů...):
# ? délka slabik
# ? délka slov
# ? počet slov / počet odstavců
# ? bonus: vygenerovat text do souboru






import random
import string


seznam_slov = []
prvni_seznam_slabik1 = ["ke", "ča", "buh", "li", "bo", "ce", "ra", "po", "hi", "zy"]
druhy_seznam_slabik1 = ["pat", "tě", "fo", "ni", "jo", "za", "gol", "g", "lu", "x"]

prvni_seznam_slabik2 = ["he", "pla", "bě", "lo", "mo", "šle", "pý"]
druhy_seznam_slabik2 = ["ka", "tu", "je", "do", "dle", "pra", "cha"]
treti_seznam_slabik2 = ["fi", "se", "či", "pak", "gi", "k", "šek"]

prvni_seznam_slabik3 = ["chla", "kro", "ži", "fik", "bor"]
druhy_seznam_slabik3 = ["me", "vy", "po", "je", "pik"]
treti_seznam_slabik3 = ["ny", "rod", "pu", "žiš", "žu"]
ctvrty_seznam_slabik3 = ["c", "vyk", "pi", "mol", "la"]


while True:
    x1 = random.choice(prvni_seznam_slabik1)
    y1 = random.choice(druhy_seznam_slabik1)
    random_slovo1 = x1 + y1
    prvni_seznam_slabik1.remove(x1)
    druhy_seznam_slabik1.remove(y1)
    seznam_slov.append(random_slovo1)
    if prvni_seznam_slabik1 == []:
        break

while True:
    x2 = random.choice(prvni_seznam_slabik2)
    y2 = random.choice(druhy_seznam_slabik2)
    z2 = random.choice(treti_seznam_slabik2)
    random_slovo2 = x2 + y2 +z2
    prvni_seznam_slabik2.remove(x2)
    druhy_seznam_slabik2.remove(y2)
    treti_seznam_slabik2.remove(z2)
    seznam_slov.append(random_slovo2)
    if prvni_seznam_slabik2 == []:
        break

while True:
    x3 = random.choice(prvni_seznam_slabik3)
    y3 = random.choice(druhy_seznam_slabik3)
    z3 = random.choice(treti_seznam_slabik3)
    xy3 = random.choice(ctvrty_seznam_slabik3)
    random_slovo3 = x3 + y3 +z3 + xy3
    prvni_seznam_slabik3.remove(x3)
    druhy_seznam_slabik3.remove(y3)
    treti_seznam_slabik3.remove(z3)
    ctvrty_seznam_slabik3.remove(xy3)
    seznam_slov.append(random_slovo3)
    if prvni_seznam_slabik3 == []:
        break



pocet_slov = random.randint(4,10)
pocet_bloku = int(input("Kolik chcete generovat bloků: "))
pocet_vet_na_blok = int(input("Kolik chcete generovat vět na jeden blok: "))

for x in range(pocet_bloku):
    for y in range(pocet_vet_na_blok):
        veta = " ".join(random.sample(seznam_slov, k = pocet_slov))
        text = veta.capitalize()
        print(text+".", end=" ")
    print()
    print("----------------------------------------")