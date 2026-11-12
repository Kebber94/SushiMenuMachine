#region ========== Imports ==========
from datetime import datetime
from model.sushi import Nigiri, Maki, Uramaki

#endregion

#region ========== Classes ==========

# Eksporterer menukortet til en tekstfil
class MenuExport:
    @staticmethod
    def export_menu(machine):
        date = datetime.now().strftime("%d-%m-%Y_%H-%M")

        filename = f'{date} - Sushi menu export'

        menu = machine.get_sorted_menu()

        with open(f'data/{filename}.txt', 'w', encoding='utf-8') as file:
            file.write("=== Sushi Menu Maker 3000 ===\n\n")

            # Holder styr på den forrige sushi-type, så overskrifter ikke gentages
            previous_type = None

            for number, sushi in enumerate(menu, start=1):
                if type(sushi) == Nigiri:
                    if previous_type != Nigiri:
                        file.write("\n🍣 Nigiri:\n")

                    previous_type = Nigiri

                    file.write(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                               f'            {sushi.get_filling().value}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""}\n')

                if isinstance(sushi, Maki):
                    proteins = ', '.join(protein.value for protein in sushi.get_protein_list())
                    vegetables = ', '.join(vegetable.value for vegetable in sushi.get_vegetable_list())
                    all_filling = ', '.join(filter(None, [proteins, vegetables]))

                    if type(sushi) == Maki:
                        if previous_type != Maki:
                            file.write(f'\n🍣 Maki:\n')

                        previous_type = Maki

                        file.write(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                              f'            {all_filling}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""} | Sesam: {"Ja" if sushi.get_sesam() else "Nej"}\n')

                    elif type(sushi) == Uramaki:
                        if previous_type != Uramaki:
                            file.write(f'\n🍣 Uramaki: Inside-Out\n')

                        previous_type = Uramaki

                        file.write(f'    {number}. {sushi.get_name()} - {sushi.get_price()} kr.\n'
                              f'            {all_filling}{" | " + sushi.get_sauce().value if sushi.get_sauce() else ""} | Sesam: {"Ja" if sushi.get_sesam() else "Nej"}\n')

#endregion