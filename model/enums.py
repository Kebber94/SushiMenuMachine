# ========== Imports ==========
from enum import Enum


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
    INGEN       = "Ingen"

# Andet

class SortBy(int, Enum):
    NAME = 1
    PRICE = 2
    NEWEST = 3