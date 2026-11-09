#region ========== Imports ==========
from model.enums import Sauce, Protein, Vegetable
from model.sushi_machine import SushiMachine
from model.sushi import Nigiri, Maki, Uramaki, Sushi

#endregion

#region ========== Definitions ==========

# Create
def create_sushi(sushi_type: str):
    print(f'\n========== {sushi_type} ==========')
    # Navn
    name = get_sushi_name()

    # Pris
    price = get_price()

    # Fyld
    show_filling()
    filling = get_filling_number(sushi_type)

    # Sovs
    show_sauce()
    sauce = get_sauce()

    if sushi_type == 'Nigiri':
        return name, price, sauce, filling

    elif sushi_type == 'Maki' or sushi_type == 'Uramaki':
        sesam = get_sesam()
        if isinstance(filling, tuple):
            proteins, vegetables = filling
            return name, price, sauce, sesam, proteins, vegetables
        else:
            raise ValueError("Maki skal have protein- og grøntsagslister")



def create_sushi_menu(machine):
    while True:
        print('\n========== Sushi Maker 3000 ==========\n'
              '1. Nigiri\n'
              '2. Maki\n'
              '3. Uramaki\n'
              '4. Afbryd\n')

        try:
            choice = int(input('Hvilken type sushi ønsker du at oprette:'))
        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen!')
            continue

        if 0 < choice < 5:
            match choice:
                case 1:
                    name, price, sauce, filling = create_sushi('Nigiri')

                    # Opret Nigiri
                    sushi = Nigiri(
                            name,
                            price,
                            sauce,
                            filling,
                        )

                    machine.add_sushi(sushi)

                    # Resultat
                    print('Følgende sushi blev oprettet:')
                    show_sushi(sushi)

                case 2:
                    name, price, sauce, sesam, protein, vegetable = create_sushi('Maki')

                    # Opret Maki
                    sushi = Maki(
                        name,
                        price,
                        sauce,
                        sesam,
                        protein,
                        vegetable
                    )

                    machine.add_sushi(sushi)

                    # Resultat
                    print('Følgende sushi blev oprettet:')
                    show_sushi(sushi)
        else:
            print('Ugyldig indtastning. Prøv igen...')

# Read
def get_sushi_name():
    while True:
        try:
            name = str(input('Hvad vil du kalde din sushi?: '))

            if len(name) < 3:
                raise ValueError

            return name

        except ValueError:
            print('Du skal indtaste et gyldigt navn på mindst 3 bogstaver')


def get_price():
    while True:
        try:
            price = int(input('Hvad er prisen?: '))
        except ValueError:
            print('Du kan kun indtaste hele positive tal')
            continue

        return price


def get_filling_number(sushi_type: str):
    filling_protein = list(Protein)
    filling_vegetable = list(Vegetable)
    all_filling = filling_protein + filling_vegetable

    proteins = []
    vegetables = []

    while True:
        try:
            if sushi_type == 'Nigiri':
                filling = input('Vælg én topping: ')
            else:
                if proteins or vegetables:
                    filling = input('Vælg endnu en topping (Enter for at afslutte): ')
                else:
                    filling = input('Vælg mindst én topping: ')

            if filling == "":
                if sushi_type == 'Nigiri':
                    raise ValueError

                if proteins or vegetables:
                    return proteins, vegetables
                else:
                    raise ValueError

            filling = int(filling) - 1

            if not 0 <= filling < len(all_filling):
                raise ValueError

            selected_filling = all_filling[filling]

            if sushi_type == 'Nigiri':
                return selected_filling

            if isinstance(selected_filling, Protein) and selected_filling not in proteins:
                proteins.append(selected_filling)
            elif isinstance(selected_filling, Vegetable) and selected_filling not in vegetables:
                vegetables.append(selected_filling)
            else:
                raise ValueError

        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen!')
            continue


def get_sauce():
    while True:
        try:
            sauce = input('\nHvilken sovs ønsker du?\n'
                              'Vælg én eller lad feltet være blankt for at vælge ingen sovs: :')
            if sauce == "":
                return None
            else:
                sauce = int(sauce) - 1

            if not 0 <= sauce < len(Sauce):
                raise ValueError

        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen!')
            continue

        return list(Sauce)[sauce]


def get_sesam():

    while True:
        try:
            sesam = input('Ønsker du sesam på toppen? (J)a/(N)ej: ')

            match sesam.upper():
                case "J" | "JA":
                    return True
                case "N" | "NEJ":
                    return False
                case _:
                    raise ValueError
        except ValueError:
            print("Skriv 'Ja' eller 'Nej'...")


def show_sauce():
    for number, sauce in enumerate(Sauce, start=1):
        if number == 1:
            print('Sovs')
        print(f'    {number}. {sauce.value}')


def show_filling():
    # Viser hvilke fyld der kan vælges imellem
    filling_protein = list(Protein)
    filling_vegetable = list(Vegetable)
    all_filling = filling_protein + filling_vegetable

    for number, filling in enumerate(all_filling, start=1):
        if type(filling) is Protein:
            if filling is filling_protein[0]:
                print('🥩 Protein')
            print(f'    {number}. {filling.value}')

        elif type(filling) is Vegetable:
            if filling is filling_vegetable[0]:
                print(f'\n🥬 Grøntsager')
            print(f'    {number}. {filling.value}')


def show_sushi(sushi):
    # Viser pænt alle oplysninger for et given sushi
    sauce = sushi.get_sauce()

    print(f'Navn: {sushi.get_name()}\n'
          f'Pris: {sushi.get_price()} kr.\n'
          f'Sovs: {sauce.value if sauce is not None else "Ingen"}')

    # Nigiri
    if isinstance(sushi, Nigiri):
        print(f'Fyld: {sushi.get_filling().value}')

    # Maki og Uramaki
    if isinstance(sushi, Maki):
        proteins = ', '.join(protein.value for protein in sushi.get_protein_list())
        vegetables = ', '.join(vegetable.value for vegetable in sushi.get_vegetable_list())

        print(f'Protein: {proteins if proteins else "Ingen"}\n'
              f'Grøntsager: {vegetables if vegetables else "Ingen"}\n'
              f'Sesam: {"Ja" if sushi.get_sesam() else "Nej"}')

    # Uramaki
    if isinstance(sushi, Uramaki):
        print(f'Inside-Out: {"Ja" if sushi.rice_outside else "Nej"}')



def show_menu(machine):
    menu = machine.get_menu()

    menu_nigiri = []
    menu_maki = []
    menu_uramaki = []

    for sushi in menu:
        # anvender type i stedet for isinstance så vi rammer præcise klasse og ikke skal tænke på arv og rækkefølge.
        if type(sushi) == Nigiri:
            menu_nigiri.append(sushi)
        elif type(sushi) == Maki:
            menu_maki.append(sushi)
        elif type(sushi) == Uramaki:
            menu_uramaki.append(sushi)

    menu = menu_nigiri + menu_maki + menu_uramaki

    for number, sushi in enumerate(menu, start=1):

        if type(sushi) == Nigiri:
            if sushi is menu_nigiri[0]:
                print(f'🍣 Nigiri:')
            print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n')

        # anvender isinstance for at ramme både Uramaki og Maki, da Uramaki arver fra Maki
        if isinstance(sushi, Maki):
            proteins = ', '.join(protein.value for protein in sushi.get_protein_list())
            vegetables = ', '.join(vegetable.value for vegetable in sushi.get_vegetable_list())
            all_filling = proteins + ", " + vegetables

            if type(sushi) == Maki:
                if sushi is menu_maki[0]:
                    print(f' Maki:')
                print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                      f'            {all_filling}')

            elif type(sushi) == Uramaki:
                if sushi is menu_uramaki[0]:
                    print(f' Uramaki:')
                print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                      f'             {all_filling}')



def main():
    machine = SushiMachine()

    print("Velkommen til Sushi Maker 3000!")

    while True:
        print('\n========== Sushi Maker 3000 ==========\n'
              '1. Opret ny sushi på menukortet\n'
              '2. Vis menukortet\n'
              '3. Rediger sushi på menukortet\n'
              '4. Fjern sushi fra menukortet drik\n'
              '5. Afslut\n')

        try:
            choice = int(input('Vælg et nummer: '))

        except ValueError:
            print('Du skal indtaste et tal fra menuen!')
            continue

        if 0 < choice < 6:
            match choice:
                case 1:
                    create_sushi_menu(machine)
                case 2:
                    show_menu(machine)
                case 3:
                    edit_sushi(machine)
                case 4:
                    delete_sushi(machine)
                case 5:
                    break
        else:
            print('Ugyldig indtastning. Prøv igen...')

#endregion




"""
Velkommen til SushiMaskinen!

1. Opret ny sushi på menukortet
2. Vis menukort
3. Rediger sushi på menukortet
4. Fjern sushi fra menukortet
5. Afslut
"""

if __name__ == "__main__":
    main()