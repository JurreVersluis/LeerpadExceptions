punten = 0
gefaald = "Helaas hebben wij geconstanteerd dat u niet de benodigde eisen heeft voor deze baan."

antwoord = input('Wat is uw naam?\n')
if antwoord == 'Mil':
    raise NameError('Je bent aangenomen!')
if antwoord == 'Erdem':
    raise NameError('Je bent aangenomen!')
if antwoord == 'Diemaco':
    raise NameError('Je bent aangenomen!')


vraag1 = input("Hoeveel jaar ervaring heeft u met dieren?\n")
if float(vraag1) > 4:
    punten = punten + 1

vraag2 = input("Hoeveel jaar ervaring heeft u met dressuur?\n")
if float(vraag2) > 4:
    punten = punten + 1

vraag3 = input("Hoeveel jaar ervaring heeft u met jongleren?\n")
if float(vraag3) > 5:
    punten = punten + 1

vraag4 = input("Hoeveel jaar ervaring heeft u met acrobatiek?\n")
if float(vraag4) > 3:
    punten = punten + 1

if punten < 1:
    print (gefaald)
    exit()

punten = 0

vraag5 = input("Heeft u een mbo-4 diploma of hoger?\n 1. Ja \n 2. Nee\n\n")
if float(vraag5) == 1:
    punten = punten + 1

vraag6 = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs?\n 1. Ja \n 2. Nee\n\n")
if float(vraag6) == 1:
    punten = punten + 1

vraag7 = input("Bent u in bezit van een hoge hoed?\n 1. Ja \n 2. Nee\n\n")
if float(vraag7) == 1:
    punten = punten + 1

if punten < 3:
    print (gefaald)
    exit()



vraag8 = input("Watvoor geslacht heeft u?\n 1. man \n 2. vrouw\n\n")
if float(vraag8) == 1:
    vraag8a = input("Heeft u enige gezichtsbeharing?\n 1. Ja ik heb een snor. \n 2. Ja ik heb een baard. \n 3. Nee ik heb geen gezichtsbeharing.\n\n")
    if float(vraag8a) == 1:
        (vraag8aa) = input("Mijn snor is:..cm\n1. 5cm\n2. 10cm of langer\n")
        if float(vraag8aa) == 2:
            punten = punten + 1

else:
    vraag8b = input("Watvoor haar heeft u?\n 1. Ik heb rood gekruld haar. \n 2. Ja ik heb blonde lokken. \n 3. ik heb bruin haar\n\n")
    if float(vraag8b) == 1:
        (vraag8bb) = input("Mijn haar is is:..cm\n1. 10cm\n2. 20cm of langer\n")
        if float(vraag8bb) == 2:
            punten = punten + 1


if punten < 4:
    print(gefaald)
    exit()

vraag9 = input("Hoelang bent u?\n1. 120cm \n 2. 135cm \n 3. 150cm of langer\n")
if float(vraag9) == 3:
    punten = punten + 1

vraag10 = input("Hoe zwaar bent u?\n1. 80kg \n 2. 85kg \n 90kg of meer\n")
if float(vraag10) == 3:
    punten = punten + 1


vraag11 = input("heeft u een van de volgende certficaten?\n1. Overleven met gevaarlijk personeel \n2. hoge houde certificaat \n3. huisdieren certificaat\n 1. Ja\n 2. Nee\n")
if float(vraag11) == 1:
    punten = punten + 1

if punten < 7:
    print(gefaald)
    exit()

input("Heeft u ooit huisdieren gehad?\n 1. Ja\n 2. Nee\n")
input("Bent u ooit naar een circus geweest gehad?\n 1. Ja\n 2. Nee\n")
input("Heeft u ooit goudvissen gehad?\n 1. Ja\n 2. Nee")
input("Vindt u deze laatste 4 vragen niet heel verdacht?\n 1. Ja\n 2. Nee\n")

print("Uw verzoek is vestuurd naar onze medewerkers en u zult snel een antwoord krijgen.\n")