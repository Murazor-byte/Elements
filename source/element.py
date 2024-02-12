from enum import Enum

class ElementGroup(Enum):
    ALKALI_METAL = "Alkali Metal",
    ALKALINE_EARTH_METAL = "Alkaline Earth Metal",
    TRANSITION_METAL = "Transition Metal",
    POST_TRANSITION_METAL = "Post Transition Metal",
    METALLOID = "Metalloid",
    REACTIVE_NONMETAL = "Reactive nonmetal",
    NOBLE_GAS = "Noble Gas",
    LANTHANIDES = "Lanthanide",
    ACTINIDE = "actinide",
    UNKOWN_PROPERTY = "Unkown Property"


class Element:
    element_group = "Alkali Metal"

    def __init__(self, name: str, symbol: str, atomic_number: int, mass: float, element_group: ElementGroup):
        self.name = name,
        self.symbol = symbol,
        self.atomic_numer = atomic_number,
        self.mass = mass,
        self.element_group = element_group