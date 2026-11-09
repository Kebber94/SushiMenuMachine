#region ========== Imports ==========
from model.sushi import Sushi, Nigiri, Maki, Uramaki
from model.enums import SortBy

#endregion

#region ========== Classes ==========
class SushiMachine:
    def __init__(self):
        self.__menu = []

    # Create
    def add_sushi(self, sushi):
        # Sikre, at vi kun tilføjer objekter baseret på Sushi-klassen
        if isinstance(sushi, Sushi):
            self.__menu.append(sushi)

    # Read
    def get_menu(self):
        return list(self.__menu)

    def get_sushi(self, index):
        return self.__menu[index]


    # Update


    # Delete
    def delete_sushi(self, sushi):
        self.__menu.remove(sushi)
        return sushi


    # Sort
    def sort_menu(self, sort_by):
        if isinstance(sort_by, SortBy):
            match sort_by:
                case SortBy.NAME:
                    return sorted(self.__menu, key=lambda sushi: sushi.get_name())
                case SortBy.PRICE:
                    return sorted(self.__menu, key=lambda sushi: sushi.get_price())
                case SortBy.NEWEST:
                    return list(reversed(self.__menu))

    def get_sorted_menu(self):
        menu = self.get_menu()

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
