#region ========== Imports ==========
from model.enums import Sauce, Protein, Vegetable, SortBy
from model.sushi_menu_machine import SushiMenuMachine
from model.sushi import Nigiri, Maki, Uramaki
from services.menu_export import MenuExport

#endregion

#region ========== Definitions ==========

# ===== Create =====
# Opretter sushi-objekter ud fra brugerinput og tilføjer dem til menukortet
def create_sushi(machine):
    while True:
        print('\n========== Sushi Menu Maker 3000 ==========\n'
              '1. Nigiri\n'
              '2. Maki\n'
              '3. Uramaki')

        choice = input('Hvilken type sushi ønsker du at oprette (Tryk Enter for at afslutte): ')

        if choice == "":
            break

        try:
            choice = int(choice)
        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen!')
            continue

        if 0 < choice < 4:
            match choice:
                case 1:
                    name, price, sauce, filling = get_sushi_input('Nigiri')

                    # Opret Nigiri
                    sushi = Nigiri(
                            name,
                            price,
                            sauce,
                            filling,
                        )

                    machine.add_sushi(sushi)

                    print('\nFølgende sushi blev oprettet:')
                    show_sushi(sushi)

                case 2:
                    name, price, sauce, sesam, protein, vegetable = get_sushi_input('Maki')

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

                    print('Følgende sushi blev oprettet:')
                    show_sushi(sushi)

                case 3:
                    name, price, sauce, sesam, protein, vegetable = get_sushi_input('Uramaki')

                    # Opret Uramaki
                    sushi = Uramaki(
                        name,
                        price,
                        sauce,
                        sesam,
                        protein,
                        vegetable
                    )

                    machine.add_sushi(sushi)

                    print('Følgende sushi blev oprettet:')
                    show_sushi(sushi)
        else:
            print('Ugyldig indtastning. Prøv igen...')

# Indsamler brugerinput til oprettelse af Sushi-objekter
def get_sushi_input(sushi_type: str):
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

    # Returnere forskellige oplysninger afhængigt af sushi-typen
    if sushi_type == 'Nigiri':
        return name, price, sauce, filling

    elif sushi_type == 'Maki' or sushi_type == 'Uramaki':
        sesam = get_sesam()
        if isinstance(filling, tuple):
            proteins, vegetables = filling
            return name, price, sauce, sesam, proteins, vegetables
        else:
            raise ValueError("Maki skal have protein- og grøntsagslister")


# ===== Input =====
# Indsamler og validerer brugerens input

# Sushi navn
def get_sushi_name():
    while True:
        try:
            name = input('Hvad vil du kalde din sushi?: ').strip() # strip'es for at fjerne mellemrum

            if len(name) < 3:
                raise ValueError

            return name

        except ValueError:
            print('Du skal indtaste et gyldigt navn på mindst 3 bogstaver')

# Sushi pris
def get_price():
    while True:
        try:
            price = int(input('Hvad er prisen?: '))
        except ValueError:
            print('Du kan kun indtaste hele ikke-negative tal')
            continue

        if price < 0:
            print('Prisen må ikke være negativ!')
            continue

        return price

# Sushi fyld
def get_filling_number(sushi_type: str):
    # Omdanner begge Enums til lister og samler dem, så brugeren kan vælge alt fyld fra én liste
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

            # Index starter ved 0, derfor trækkes 1 fra brugerens valg
            filling = int(filling) - 1

            if not 0 <= filling < len(all_filling):
                raise ValueError

            selected_filling = all_filling[filling]

            if sushi_type == 'Nigiri':
                return selected_filling

                # Fordeler fyldet i de korrekte lister og forhindrer dubletter
            if isinstance(selected_filling, Protein) and selected_filling not in proteins:
                proteins.append(selected_filling)
            elif isinstance(selected_filling, Vegetable) and selected_filling not in vegetables:
                vegetables.append(selected_filling)
            else:
                raise ValueError

        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen og må ikke vælge det samme topping 2 gange!')
            continue

# Sushi sovs
def get_sauce():
    while True:
        try:
            sauce = input('\nHvilken sovs ønsker du?\n'
                              'Vælg én eller lad feltet være blankt for at vælge ingen sovs: ')
            if sauce == "":
                return None

            # Index starter ved 0, derfor trækkes 1 fra brugerens valg
            sauce = int(sauce) - 1

            if not 0 <= sauce < len(Sauce):
                raise ValueError

        except ValueError:
            print('Du skal indtaste et gyldigt tal fra listen!')
            continue

        # Returnere Enum-medlemmet
        return list(Sauce)[sauce]

# Sushi sesam
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


# ===== Read / Visual =====

# Viser sushi-menuen
def show_menu(machine, menu=None):
    if menu is None:
        menu = machine.get_sorted_menu()

    # Holder styr på den forrige sushi-type, så overskrifter ikke gentages
    previous_type = None

    for number, sushi in enumerate(menu, start=1):

        if type(sushi) == Nigiri:
            if previous_type != Nigiri:
                print(f'\n🍣 Nigiri:')

            previous_type = Nigiri

            print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                  f'            {sushi.get_filling().value}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""}')

        # Anvender isinstance for at ramme både Uramaki og Maki, da Uramaki arver fra Maki
        if isinstance(sushi, Maki):
            proteins = ', '.join(protein.value for protein in sushi.get_protein_list())
            vegetables = ', '.join(vegetable.value for vegetable in sushi.get_vegetable_list())
            all_filling = ', '.join(filter(None, [proteins, vegetables]))

            if type(sushi) == Maki:
                if previous_type != Maki:
                    print(f'\n🍣 Maki:')

                previous_type = Maki

                print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                      f'            {all_filling}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""} | Sesam: {"Ja" if sushi.get_sesam() else "Nej"}')

            elif type(sushi) == Uramaki:
                if previous_type != Uramaki:
                    print(f'\n🍣 Uramaki: Inside-Out')

                previous_type = Uramaki

                print(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                      f'            {all_filling}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""} | Sesam: {"Ja" if sushi.get_sesam() else "Nej"}')

# Viser pænt alle oplysninger for en given sushi
def show_sushi(sushi):
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

# Viser hvilke sovse der kan vælges imellem
def show_sauce():

    for number, sauce in enumerate(Sauce, start=1):
        if number == 1:
            print('Sovs')
        print(f'    {number}. {sauce.value}')

# Viser hvilke fyld der kan vælges imellem
def show_filling():
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


# ===== Update =====

# Redigeringsmenu til bruger
def edit_menu(machine):
    while True:
        menu = machine.get_sorted_menu()
        show_menu(machine)

        choice = input('\nHvilken sushi vil du redigere (Enter for at gå tilbage): ')

        if choice == "":
            return

        try:
            choice = int(choice)
        except ValueError:
            print('Du skal indtaste et gyldigt tal!')
            continue

        if 1 <= choice <= len(menu):
            # Listen er en kopi, men sushi-objekterne er de samme, så ændringerne gemmes i den originale menu
            sushi = menu[choice - 1]
            edit_sushi(sushi)
        else:
            print("Du skal vælge et nummer fra listen!")

# Redigere eksisterende sushi-objekter via deres setters
def edit_sushi(sushi):
    while True:
        print(f'\n========== Rediger {sushi.get_name()} ==========')
        print('1. Navn')
        print('2. Pris')
        print('3. Sauce')
        print('4. Fyld')
        if isinstance(sushi, Maki):
            print('5. Sesam')

        choice = input('Hvad ønsker du at ændre (Enter for at gå tilbage): ')

        if choice == "":
            return

        match choice:
            case "1":
                print(f'\nNavn: {sushi.get_name()}')

                while True:
                    try:
                        sushi.set_name(input('\nIndtast det nye navn: '))
                        break
                    except ValueError as error:
                        print(error)
            case "2":
                print(f'\nPris: {sushi.get_price()}')

                while True:
                    try:
                        sushi.set_price(int(input('\nIndtast den nye pris: ')))
                        break
                    except ValueError as error:
                        print(error)
            case "3":
                sauce = sushi.get_sauce()
                print(f'Sovs: {sauce.value if sauce is not None else "Ingen"}')

                show_sauce()

                while True:
                    try:
                        sushi.set_sauce(get_sauce())
                        break
                    except ValueError as error:
                        print(error)
            case "4":
                if type(sushi) == Nigiri:
                    print(f'\nFyld: {sushi.get_filling().value}')
                    show_filling()

                    while True:
                        try:
                            sushi.set_filling(get_filling_number("Nigiri"))
                            break
                        except ValueError as error:
                            print(error)
                elif isinstance(sushi, Maki):
                    proteins = ', '.join(protein.value for protein in sushi.get_protein_list())
                    vegetables = ', '.join(vegetable.value for vegetable in sushi.get_vegetable_list())
                    filling = ', '.join(filter(None, [proteins, vegetables]))

                    print(f'\nFyld: {filling}')

                    show_filling()

                    while True:
                        try:
                            proteins, vegetables = get_filling_number("Maki")

                            # Fjern de gamle ingredienser
                            for old_protein in sushi.get_protein_list():
                                sushi.remove_protein(old_protein)

                            for old_vegetable in sushi.get_vegetable_list():
                                sushi.remove_vegetable(old_vegetable)

                            # Tilføj de nye ingredienser
                            for protein in proteins:
                               sushi.add_protein(protein)

                            for vegetable in vegetables:
                                sushi.add_vegetable(vegetable)

                            break
                        except ValueError as error:
                            print(error)
            case "5":
                if isinstance(sushi, Maki):
                    # Skifter sesam til det modsatte af, hvad værdien var før, da der kun kan vælges ja eller nej
                    sushi.set_sesam(not sushi.get_sesam())

                    print(f'Sesam ændret til:  {"Ja" if sushi.get_sesam() else "Nej"}')


# ===== Delete =====

# Sletter sushi-objekter fra menuen
def delete_sushi(machine):

    show_menu(machine)
    menu = machine.get_sorted_menu()

    while True:
        choice = input('\nHvilken sushi vil du slette (Enter for at gå tilbage): ')

        if choice == "":
            return

        try:
            choice = int(choice)
        except ValueError:
            print('Du skal indtaste et gyldigt tal!')
            continue

        if 1 <= choice <= len(menu):
            # Finder sushi-objektet i den sorterede liste og sletter det fra den originale menu
            # Index starter ved 0, derfor trækkes 1 fra brugerens valg
            sushi = menu[choice - 1]
            removed_sushi = machine.delete_sushi(sushi)

            print(f'Følgende sushi blev slettet:\n'
                  f'{removed_sushi.get_name()}\n')
            return
        else:
            print('Du skal indtaste et gyldigt tal!')


# ===== Sortering =====

# Sorterer menuen
def sort_menu(machine):
    menu = machine.get_sorted_menu()

    while True:
        print('\n=== Sorter menukort ===')
        print('1. Navn')
        print('2. Pris')
        print('3. Nyeste')
        print('Enter for at gå tilbage')

        choice = input('\nVælg sortering: ')

        if choice == '':
            return

        match choice:
            case "1":
                menu = machine.sort_menu(SortBy.NAME)
            case "2":
                menu = machine.sort_menu(SortBy.PRICE)
            case "3":
                menu = machine.sort_menu(SortBy.NEWEST)
            case _:
                print("Ugyldigt valg. Prøv igen.")
                continue

        # Grupperer den sorterede menu efter sushi-type, inden den vises
        menu = machine.get_sorted_menu(menu)
        show_menu(machine, menu)


# ===== Testdata =====

# Data så menukortet ikke er tomt fra start. Bruges til test og demonstration
def test_data(machine):
    sushis = (
        Nigiri(
            "Laks",
            25,
            Sauce.TERIYAKI,
            Protein.LAKS
        ),
        Nigiri(
            "Den med tun",
            15,
            None,
            Protein.TUN
        ),
        Maki(
            "Ebi",
            45,
            Sauce.TERIYAKI,
            True,
            [Protein.TEMPURA_REJE],
            [Vegetable.AVOCADO, Vegetable.AGURK, Vegetable.FORAARSLOEG]
        ),
        Maki(
            "Dragon roll",
            50,
            Sauce.CHILLI_MAYO,
            True,
            [Protein.TEMPURA_REJE, Protein.LAKS],
            [Vegetable.AVOCADO, Vegetable.FORAARSLOEG]
        ),
        Uramaki(
            "Alaska roll",
            45,
            None,
            False,
            [Protein.LAKS],
            [Vegetable.AGURK]
        )
    )

    for sushi in sushis:
        machine.add_sushi(sushi)


# ===== Main =====
def main():
    # Opretter maskinen og tilføjer testdata ved programmets start
    machine = SushiMenuMachine()
    test_data(machine)

    print("Velkommen til Sushi Menu Maker 3000!")

    while True:
        print('\n========== Sushi Menu Maker 3000 ==========\n'
              '1. Opret ny sushi på menukortet\n'
              '2. Vis menukortet\n'
              '3. Rediger sushi på menukortet\n'
              '4. Fjern sushi fra menukortet\n'
              '5. Sorter menukortet\n'
              '6. Afslut (exporter menukort)\n')

        try:
            choice = int(input('Vælg et nummer: '))

        except ValueError:
            print('Du skal indtaste et tal fra menuen!')
            continue

        if 0 < choice < 7:
            match choice:
                case 1:
                    create_sushi(machine)
                case 2:
                    show_menu(machine)
                case 3:
                    edit_menu(machine)
                case 4:
                    delete_sushi(machine)
                case 5:
                    sort_menu(machine)
                case 6:
                    MenuExport.export_menu(machine)
                    break
        else:
            print('Ugyldig indtastning. Prøv igen...')

#endregion




if __name__ == "__main__":
    main()