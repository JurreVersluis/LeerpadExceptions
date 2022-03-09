# Jurre Versluis Pizza calculator
PizzaHoeveelheden = {"Kleine": 0, "Medium": 0, "Grote": 0}
keys_list = list(PizzaHoeveelheden)
Prijzen = [2.50, 5.30, 10.40]
totaalprijs = 0

print("Welkom bij Jurre's pizza zaak.\n")

for i in range(3):
    print(f"Een {keys_list[i]} pizza kost {Prijzen[i]:.2f}.")


def hoeveelpizzas(pizzatype):
    loop = True
    while loop:
        try:
            hoeveel = int(input(f"\nHoeveel {pizzatype} pizza(s) wilt u bestellen?\n"))
        except ValueError:
            print("Dat is geen geldige invoer.")
        else:
            loop = False

    PizzaHoeveelheden[pizzatype] = hoeveel


def prijzen():
    global totaalprijs
    for b in range(3):
        prijs = (PizzaHoeveelheden.get(keys_list[b]) * Prijzen[b])
        print(f'De prijs van de {PizzaHoeveelheden.get(keys_list[b])} {keys_list[b]} Pizza(s) is bij elkaar: {(prijs):.2f}€')
        totaalprijs += prijs
    print('                                               --------+')
    print(f'De totale prijs is:                             {totaalprijs:.2f}€')


hoeveelpizzas("Kleine")
hoeveelpizzas("Medium")
hoeveelpizzas("Grote")
print('')
prijzen()
