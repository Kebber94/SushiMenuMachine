# ========== Imports ==========
from model.sushi import Sushi
from model.enums import SortBy


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
    def delete_sushi(self, index):
        return self.__menu.pop(index)

    def delete_drink(self, drink_number):
        if self.is_valid_index(drink_number):
            return self.__drink_list.pop(drink_number)
        else:
            raise ValueError(f'{drink_number} is an invalid drink')

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



#endregion
