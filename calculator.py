loop = True
while loop:
    try:
        Getal1 = int(input(f"Voer Getal nummer een in: \n"))
    except ValueError:
        print("Dat is geen geldige invoer.")
    else:
        loop = False
loop = True

while loop:
    operator = str(input(f"Voeg een operator toe: \n"))
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        loop = False


loop = True
while loop:
    try:
        Getal2 = int(input(f"Voer getal nummer twee in: \n"))
    except ValueError:
        print("Dat is geen geldige invoer.")
    else:
        loop = False

if operator == '+':
    antwoord = (Getal1 + Getal2)
if operator == '-':
    antwoord = (Getal1 - Getal2)
if operator == '*':
    antwoord = (Getal1 * Getal2)
if operator == '/':
    antwoord = (Getal1 / Getal2)

print(f'{Getal1} {operator} {Getal2} = {antwoord}')