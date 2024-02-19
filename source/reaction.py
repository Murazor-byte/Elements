'''
Steps:
1. Identify the type of chemical reaction:
        Single Replacement, Double Replacement, Combustion, Decomposition, Synthesis
2. Write expected results
        Don't forget about the 7 diamotic elements
3. balance element compounds
        Ensure the elements (subscripts) balance for that compound based on charges 
'''
from element import Element, ElementGroup, ElementState
from periodic_table import PeriodicTable
from typing import List
from element import Element

class Reaction:
        
    def __init__(self):
      self.periodic_table = PeriodicTable()


    def add_element(self, element_name):
        index = next(i for i, element in enumerate(self.periodic_table.elements) if element.name == element_name)
        return self.periodic_table.elements[index]


    def add_compound(self, compound: List[str]):
        reactant:List[Element] = []
        for element in compound:
            reactant.append(self.add_element(element))
        return reactant


    def print_all_elements(self):
        for element in self.periodic_table.elements:
            print(f'{element.name} [{element.symbol} {element.charge}]: {element.mass}'.replace('\'', '').replace("(", "").replace(")", "").replace(",", ""))
     # print([element.name for element in self.periodic_table.elements])
        

    def print_all_elements(self, reactants: List[List[Element]]):
        for compound in reactants:
            for element in compound:
                print(f'{element.name} [{element.symbol} {element.charge}]: {element.mass}'.replace('\'', '').replace("(", "").replace(")", "").replace(",", ""))
                # print([element.name for element in self.periodic_table.elements])


    def get_charges(self, reactants: List[List[Element]]):
        num_anions = 0
        num_cations = 0
        anions: List[Element] = []
        cations: List[Element] = []

        for compound in reactants:
            for element in compound:
                if element.charge >= 0:
                    num_cations += 1
                    cations.append(element)
                else:
                    num_anions += 1
                    anions.append(element)
        print(f'Number Cation: {num_cations}, Number Anions: {num_anions}')
        return num_anions, num_cations


    def single_repalcement(self, reactants: List[List[Element]]):

        num_anions, num_cations = self.get_charges(reactants)

        single_reactant = compound_reactant = Element("", "", 0, 0, ElementGroup.UNKOWN_PROPERTY, ElementState.UNKOWN, 0)
        single_reactant_index = compound_index = replacement_compound_element_index= 0

        is_cation_replacement = False

        # see if it's a anionic or cationic replacment
        if num_cations >= num_anions:
            is_cation_replacement = True

        # find which compound has the anion, then flip the single reactant with this accompanying one
        for index, compound in enumerate(reactants):
            if len(compound) > 1:
                for conmpound_index, element in enumerate(compound):
                    if (element.charge >= 0 and is_cation_replacement) or (element.charge < 0 and not is_cation_replacement):
                        #flip elements
                        compound_reactant = element
                        replacement_compound_element_index = conmpound_index
                        compound_index = index
                        print(f'Storing the compound element {element.name} at reactants index: {compound_index}, at reactant index {replacement_compound_element_index}')
            if len(compound) == 1:
                single_reactant = reactants[index][0]
                single_reactant_index = index
                print(f'Storing element {reactants[index][0].name} at reactant index {single_reactant_index}')

        reactants[single_reactant_index][0] = compound_reactant
        reactants[compound_index][replacement_compound_element_index] = single_reactant

    
    def double_replacement(self, reactants: List[List[Element]]):
        num_anions, num_cations = self.get_charges(reactants)

        first_reactant = second_reactant = Element("", "", 0, 0, ElementGroup.UNKOWN_PROPERTY, ElementState.UNKOWN, 0)
        first_reactant_index = first_compound_element_index = second_reactant_index = second_compound_element_index = 0

        is_cation_replacement = is_second_reactant = False

        # if it's a anionic or cationic replacment
        if num_cations >= num_anions:
            is_cation_replacement = True

        # find which compound has the anion, then flip the both reactants in both compounds
        for index, compound in enumerate(reactants):
            for conmpound_index, element in enumerate(compound):
                if (element.charge >= 0 and is_cation_replacement) or (element.charge < 0 and not is_cation_replacement):
                    if not is_second_reactant:
                        is_second_reactant = True
                        first_reactant_index = index
                        first_compound_element_index = conmpound_index
                        first_reactant = element
                    else:
                        second_reactant_index = index
                        second_compound_element_index = conmpound_index
                        second_reactant = element
           
        # flip reactatns
        reactants[first_reactant_index][first_compound_element_index] = second_reactant
        reactants[second_reactant_index][second_compound_element_index] = first_reactant