from reaction import Reaction
from element import Element
from typing import List

if __name__ == '__main__':
    reaction = Reaction()

    reactants: List[List[Element]] = [[]]
    reactants.pop(0) #remove empty element

    reactants.append(reaction.add_compound(["Carbon", "Hydrogen", "Oxygen"]))
    reactants.append(reaction.add_compound(["Oxygen", "Hydrogen"]))


    for compound in reactants:
        for element in compound:
            print(f'{element.name} ', end="")
        print("\n")

    # single replacement
    reaction.combustion(reactants)


    print("\n")
    for compound in reactants:
        for element in compound:
            print(f'{element.name} ', end="")
        print("\n")
