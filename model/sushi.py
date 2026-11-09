#region ========== Imports ==========
from xxlimited_35 import Null

from model.enums import Protein, Vegetable, Sauce

#endregion

#region ========== Classes ==========

class Sushi:
    # Create
    def __init__(self, name, price, sauce=None):
        self.set_name(name)
        self.set_price(price)
        self.set_sauce(sauce)

    # Properties
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
        if not isinstance(name, str) or len(name.strip()) < 3:
            raise ValueError("Ugyldigt navn")
        self.__name = name.strip()

    def set_price(self, price):
        # type() for at undgå, at True bliver accepteret som en pris, da bool er en underklasse af int.
        if type(price) != int or price < 0:
            raise ValueError("Ugyldig pris. Kun hele positive tal")
        self.__price = price

    def set_sauce(self, sauce):
        if sauce is None:
            self.__sauce = None
        elif not isinstance(sauce, Sauce):
            raise ValueError("Ugyldig sauce")
        self.__sauce = sauce


class Nigiri(Sushi):
    # Create
    def __init__(self, name, price, sauce, filling):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.set_filling(filling)

    # Read
    def get_filling(self):
        return self.__filling

    # Update
    def set_filling(self, filling):
        if not isinstance(filling, (Protein, Vegetable)):
            raise ValueError(f'{filling} er ikke en gyldig topping')

        self.__filling = filling


class Maki(Sushi):
    def __init__(self, name, price, sauce, sesam, protein=None, vegetable=None):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.set_sesam(sesam)
        self.__protein_list = []
        self.__vegetable_list = []

        if protein is not None:
            if not isinstance(protein, list):
                raise ValueError(f'Protein skal være en liste')

            for p in protein:
                self.add_protein(p)

        if vegetable is not None:
            if not isinstance(vegetable, list):
                raise ValueError(f'Vegetable skal være en liste')

            for v in vegetable:
                self.add_vegetable(v)

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
        if not isinstance(sesam, bool):
            raise ValueError(f'{sesam} er ikke en gyldig sesam-værdi')
        self.__sesam = sesam


    def add_protein(self, protein):
        if not isinstance(protein, Protein):
            raise ValueError(f'{protein} er ikke et gyldigt protein')
        self.__protein_list.append(protein)


    def add_vegetable(self, vegetable):
        if not isinstance(vegetable, Vegetable):
            raise ValueError(f'{vegetable} er ikke en gyldig grøntsag')
        self.__vegetable_list.append(vegetable)

    # Delete
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


    nigiri1 = Nigiri(
        "Nigiri",
        20,
        Sauce.TERIYAKI,
        Vegetable.AVOCADO,
    )
    print(nigiri1.get_name(),
          nigiri1.get_price(),
          nigiri1.get_sauce().value,
          nigiri1.get_filling().value
          )


    maki1 = Maki(
        "Lakse Maki",
        50,
        Sauce.SOYA,
        True,
        [Protein.LAKS, Protein.TEMPURA_REJE],
        [Vegetable.AVOCADO, Vegetable.AGURK]
    )
    # Print er ikke pænt da vi printer ENUM objekter i stedet for deres .value
    print(maki1.get_name(),
          maki1.get_price(),
          maki1.get_sauce().value,
          maki1.get_protein_list(),
          maki1.get_vegetable_list(),
          sep=", ")


    uramaki1 = Uramaki(
        "California Roll",
        65,
        Sauce.SOYA,
        True,
        [Protein.TEMPURA_REJE],
        [Vegetable.AVOCADO]
    )

    print(uramaki1.get_name(),
          uramaki1.get_price(),
          uramaki1.get_sauce().value,
          uramaki1.get_protein_list(),
          uramaki1.get_vegetable_list(),
          sep=", "
          )
#endregion