#region ========== Imports ==========
from enum import Enum

#endregion

#region ========== Classes ==========

# Fødevarer
class Protein(str, Enum):
    LAKS            = "Laks"
    TUN             = "Tun"
    TEMPURA_REJE    = "Tempura Reje"
    KYLLING         = "Kylling"


class Vegetable(str, Enum):
    AGURK           = "Agurk"
    AVOCADO         = "Avocado"
    FORAARSLOEG     = "Forårsløg"
    GULLEROD        = "Gullerod"


class Sauce(str, Enum):
    TERIYAKI    = "Teriyaki"
    CHILLI_MAYO = "Chilli-mayo"
    SOYA        = "Soya"

# Andet

class SortBy(int, Enum):
    NAME = 1
    PRICE = 2
    NEWEST = 3



# region tests
if __name__ == "__main__":

    fillings = [protein.value for protein in Protein] + [vegetable.value for vegetable in Vegetable]
    print(fillings)

    fil = list(Protein) + list(Vegetable)
    print(fil)

# endregion