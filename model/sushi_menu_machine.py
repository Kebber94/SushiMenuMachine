#region ========== Imports ==========
from model.sushi import Sushi, Nigiri, Maki, Uramaki
from model.enums import SortBy

#endregion

#region ========== Classes ==========
class SushiMenuMachine:
    def __init__(self):
        self.__menu = []
        self.__sort_by = None

    # Create
    def add_sushi(self, sushi):
        # Sikrer, at vi kun tilføjer objekter baseret på Sushi-klassen
        if not isinstance(sushi, Sushi):
            raise ValueError('Ugyldig objekt. Skal være af typen Sushi')
        self.__menu.append(sushi)


    # Read - Returnerer en kopi af listen for at beskytte den originale liste
    def get_menu(self):
        return list(self.__menu)

    def get_sushi(self, index):
        return self.__menu[index]


    # Delete - sletter sushi-objekter fra menuen
    def delete_sushi(self, sushi):
        self.__menu.remove(sushi)
        return sushi


    # Sort - Sorterer menukortet i enten navn, pris eller senest tilføjet
    def sort_menu(self, sort_by):
        if isinstance(sort_by, SortBy):
            self.__sort_by = sort_by

            match sort_by:
                case SortBy.NAME:
                    return sorted(self.__menu, key=lambda sushi: sushi.get_name())
                case SortBy.PRICE:
                    return sorted(self.__menu, key=lambda sushi: sushi.get_price())
                case SortBy.NEWEST:
                    return list(reversed(self.__menu))

    # menu bruges som valgfri parameter, så metoden også kan anvendes på andre menuer
    def get_sorted_menu(self, menu=None):
        # Bruger maskinens menukort, hvis ingen menu angives.
        if menu is None:
            if self.__sort_by is not None:
                menu = self.sort_menu(self.__sort_by)
            else:
                menu = self.get_menu()

        # Grupperer derefter sushi efter type: Nigiri, Maki og Uramaki.
        menu_nigiri = []
        menu_maki = []
        menu_uramaki = []

        for sushi in menu:
            if type(sushi) == Nigiri:
                menu_nigiri.append(sushi)
            elif type(sushi) == Maki:
                menu_maki.append(sushi)
            elif type(sushi) == Uramaki:
                menu_uramaki.append(sushi)

        return menu_nigiri + menu_maki + menu_uramaki

#endregion
