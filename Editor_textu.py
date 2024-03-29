'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: František Kuchta
email: kuchta.f@seznam.cz
discord:FrantisekK #fanyny94

'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
odelovac = "=" * 50
#uzivatele registrovaNI
#user_1 = {"prihlasovaci jmeno" : "bob","heslo": "123"}
#user_2 = {"prihlasovaci jmeno" : "ann","heslo": "pass123"}
#user_3 = {"prihlasovaci jmeno" : "mike","heslo": "password123"}
#user_4 = {"prihlasovaci jmeno" : "liz","heslo": "pass123"}
user = {"bob" : "123",
        "ann" : "pass123",
        "mike" : "password123",
        "liz" : "pas123"}
#prihůaseni uzivatele
prihlasovac_jmeno = input("Zadej své přihlašovací jméno: ")
heslo = input("Zadej heslo: ")
print(odelovac)

if user.get(prihlasovac_jmeno) == heslo:
    print("Zdravím mužes pokračovat dál do programu " + prihlasovac_jmeno)
else:
    print("Zadané udaje nesouhlasí.\nUkončuji program!")
    quit()

#uvítaní v programu
delka_cary = len(odelovac)
pocet_textu = len(TEXTS)
print(f"Máme pro tebe {pocet_textu} texty k analýze.")
print(odelovac)
print("Analyzátoru textu =)".upper().center(delka_cary))
print(odelovac)

#vyber textu

cislo_textu = input(f"Vyber si číslo textu od 1 do {pocet_textu}: ")
if cislo_textu.isalpha():
    print("Zadal jsi pismena, Ukončuji program!")
    quit()
elif 1<= int(cislo_textu) <= pocet_textu :
    vybrany_text = TEXTS[int(cislo_textu) - 1]
    #print("spravně")
else:
    print("Dané číslo neni v razsahu vyběru ukoncuji program!")
    quit()

#práce s textem
#počet slov
slova = []
for slovo in vybrany_text.split():
    slova_v_textu = slovo.strip(",.:-;!?")
    slova.append(slova_v_textu)
# prace s textem
slova_zacatek_velkym_pismeny = []
slova_velka_pismena = []
slova_mala_pismena = []
cisla = []
for slovo in slova:
        if slovo.istitle():
            slova_zacatek_velkym_pismeny.append(slovo)     # velká písmena na zacatku
        elif slovo.isupper() and slovo.isalpha():
             slova_velka_pismena.append(slovo)             # velka pisemna
        elif slovo.islower():
             slova_mala_pismena.append(slovo)              # mala pismena
        elif slovo.isdigit():
             cisla.append(slovo)                           # cisla v textu
# soucet vsech cisel
total = 0
for element in cisla:
     if isinstance(element, int) or element.isdigit():
          total += int(element)

          
print(odelovac)
print(f"V textu je {len(slova)} slov.")
print(f"Počet slov s začínajících velkým písmenem je {len(slova_zacatek_velkym_pismeny)}")
print(f"Počet slov psaných velkým písmem je {len(slova_velka_pismena)} ")
print(f"Počet slov psaných malím písmem je {len(slova_mala_pismena)}")
print(f"Pošet cisel v textu je {len(cisla)}")
print(f"Součet vsech čísel v textu je {total}")


#Grafy
print(odelovac, sep="\n")
print("LEN|\t", "OCCURENCES\t", "|NR.")
print(odelovac, sep="\n")
print(odelovac)
delka_slova = {}
for slovo in slova:
     delka = len(slovo)
     if delka not in delka_slova:
          delka_slova[delka] = 0
     delka_slova[delka] += 1

for delka in sorted(delka_slova):
     print(f'{delka:3}| {"*" * delka_slova[delka]:20}| {delka_slova[delka]:^1}')
  
     
        

 





    



    


