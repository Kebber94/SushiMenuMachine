# ========== Imports ==========
from model.enums import Protein, Vegetable, Sauce



#region ========== Classes ==========

class Sushi:
    def __init__(self, name, price, sauce):
        self.__name = name
        self.__price = price
        self.__sauce = sauce

    # Property
    @property
    def rice(self):
        return True

    # Read
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_sauce(self):
        return self.__sauce

    # Update
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_sauce(self, sauce):
        self.__sauce = sauce


class Nigiri(Sushi):
    def __init__(self, name, price, sauce, filling):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.__filling = filling

    # Read
    def get_filling(self):
        return self.__filling

    # Update
    def set_filling(self, filling):
        self.__filling = filling


class Maki(Sushi):
    def __init__(self, name, price, sauce, sesam, protein, vegetables):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.__sesam = sesam

        self.__protein_list = list(protein)
        self.__vegetable_list = list(vegetables)

    # Property
    @property
    def seaweed(self):
        return True

    # Read
    def get_sesam(self):
        return self.__sesam

    def get_protein_list(self):
        return list(self.__protein_list)

    def get_vegetable_list(self):
        return list(self.__vegetable_list)

    # Update
    def set_sesam(self, sesam):
        self.__sesam = sesam

    def add_protein(self, protein):
        self.__protein_list.append(protein)

    def add_vegetable(self, vegetable):
        self.__vegetable_list.append(vegetable)

    def remove_protein(self, protein):
        if protein in self.__protein_list:
            self.__protein_list.remove(protein)
            return True

        return False

    def remove_vegetable(self, vegetable):
        if vegetable in self.__vegetable_list:
            self.__vegetable_list.remove(vegetable)
            return True

        return False


class Uramaki(Maki):

    @property
    def rice_outside(self):
        return True

#endregion


#region tests

if __name__ == "__main__":

    '''
    nigiri = Nigiri("Nigiri", 20, Sauce.TERIYAKI, Vegetable.AVOCADO)
    print(nigiri.get_name(), nigiri.get_price(), nigiri.get_sauce().value, nigiri.get_filling().value)
    
    nigiri = Nigiri("Nigiri", 20, Sauce.TERIYAKI, Protein.LAKS)
    print(nigiri.get_name(), nigiri.get_price(), nigiri.get_sauce().value, nigiri.get_filling().value)
    '''

    maki1 = Maki(
        "Lakse Maki",
        50,
        Sauce.SOYA,
        True,
        [Protein.LAKS],
        [Vegetable.AVOCADO, Vegetable.AGURK]
    )

    maki1.add_protein(Protein.TUN)
    print(", ".join(protein.value for protein in maki1.get_protein_list()))

    maki1.remove_protein(Protein.LAKS)
    print(", ".join(protein.value for protein in maki1.get_protein_list()))


    #print(", ".join(vegetable.value for vegetable in maki1.get_vegetable_list()))


    #print(maki1.get_name(),maki1.get_price(),maki1.get_sauce().value,maki1.get_protein_list(), sep=", ")



    uramaki1 = Uramaki(
        "California Roll",
        65,
        Sauce.SOYA,
        True,
        [Protein.TEMPURA_REJE],
        [Vegetable.AVOCADO]
    )

    print(uramaki1.get_name())
    print(uramaki1.get_protein_list())
    print(uramaki1.rice_outside)

#endregion