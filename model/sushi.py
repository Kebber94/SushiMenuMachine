#region ========== Imports ==========
from model.enums import Protein, Vegetable, Sauce

#endregion

#region ========== Classes ==========

class Sushi:
    # Create - Initaliserer fælles attributter og bruger setters til at validere værdierne
    def __init__(self, name, price, sauce=None):
        self.set_name(name)
        self.set_price(price)
        self.set_sauce(sauce)

    # Properties - Ris er en fælles skrivebeskyttet egenskab for alle sushi-typer. Dvs. alle har ris
    @property
    def rice(self):
        return True

    # Read - Henter de fælles attributter for et sushi-objekter
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_sauce(self):
        return self.__sauce

    # Update - Validerer input inden det sættes på objektet. Bliver også anvendt ved oprettelse af nye objekter.
    def set_name(self, name):
        if not isinstance(name, str) or len(name.strip()) < 3:
            raise ValueError("Ugyldigt navn. Skal være mindst 3 tegn")
        self.__name = name.strip()

    def set_price(self, price):
        # type() for at undgå, at True bliver accepteret som en pris, da bool er en underklasse af int.
        if type(price) != int or price < 0:
            raise ValueError("Ugyldig pris. Kun hele ikke-negative tal")
        self.__price = price

    def set_sauce(self, sauce):
        if sauce is not None and not isinstance(sauce, Sauce):
            raise ValueError("Ugyldig sauce")
        self.__sauce = sauce


# Nigiri nedarver Sushi-klassens metoder og fælles egenskaber.
# Sushi i parentes angiver, hvilken klasse Nigiri arver fra.
class Nigiri(Sushi):
    # Create - Køres ved oprettelse af nyt objekt i denne klasse.
    def __init__(self, name, price, sauce, filling):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.set_filling(filling)

    # Read - Henter oplysninger om objektet
    def get_filling(self):
        return self.__filling

    # Update - Sikrer at topping er en værdi fra Protein eller Vegetable Enum
    def set_filling(self, filling):
        if not isinstance(filling, (Protein, Vegetable)):
            raise ValueError(f'{filling} er ikke en gyldig topping')
        self.__filling = filling


# Maki arver Sushi-klassens attributter og metoder
class Maki(Sushi):
    # Create - Køres ved oprettelse af nyt objekt i denne klasse.
    def __init__(self, name, price, sauce, sesam, protein=None, vegetable=None):
        # Kalder Sushi-klassens __init__ for at initialisere de fælles attributter
        super().__init__(name, price, sauce)

        self.set_sesam(sesam)
        self.__protein_list = []
        self.__vegetable_list = []

        # Validerer at protein og grøntsager er lister
        if protein is not None:
            if not isinstance(protein, list):
                raise ValueError('Protein skal være en liste')

            for p in protein:
                self.add_protein(p)

        if vegetable is not None:
            if not isinstance(vegetable, list):
                raise ValueError('Vegetable skal være en liste')

            for v in vegetable:
                self.add_vegetable(v)

    # Property - alle makiruller har tang
    @property
    def seaweed(self):
        return True

    # Read - Henter oplysninger om objektet
    def get_sesam(self):
        return self.__sesam

        # Returnerer kopier af listerne for at beskytte de originale lister
    def get_protein_list(self):
        return list(self.__protein_list)

    def get_vegetable_list(self):
        return list(self.__vegetable_list)

    # Update - Validerer input inden det sættes på/tilføjes til objektet. set_sesam anvendes også ved oprettelse af nye objekter.
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

    # Delete - fjerner ingredienser fra objektets lister
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

# Uramaki arver Maki-klassens attributter og metoder
class Uramaki(Maki):

    @property
    def rice_outside(self):
        return True

#endregion

