# ========== Imports ==========
from model.enums import Sauce, Protein, Vegetable
from model.sushi_machine import SushiMachine
from model.sushi import Nigiri, Maki, Uramaki, Sushi


#region ========== Definitions ==========
def main():
    machine = SushiMachine()

    print("Velkommen til Sushi Maker 3000!")

    machine.add_sushi(Nigiri("Flamberet Laks", 20, Sauce.CHILLI_MAYO, Protein.LAKS))
    machine.add_sushi(Maki(
        "Flamberet Laks",
        20,
        Sauce.CHILLI_MAYO,
        True,
        [Protein.LAKS, Protein.TEMPURA_REJE],
        [Vegetable.AGURK, Vegetable.AVOCADO, Vegetable.FORAARSLOEG]))


    machine.get_sushi(0).set_price(30)

    for sushi in machine.get_menu():
        print(f'{sushi.get_name()} - {sushi.get_price()} kr.')

'''

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
                    create_drink(machine)
                case 2:
                    show_drinks(machine)
                case 3:
                    edit_drink(machine)
                case 4:
                    delete_drink(machine)
                case 5:
                    break
        else:
            print('Ugyldig indtastning. Prøv igen...')
'''

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