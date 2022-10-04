from typing import List


class CodingGuideExample:
    '''
    Coding Guide Example
    -------------

    This example contains:
    - A public function name findSolution function
    - A private function name maxPrice
    - Some examples about comment

    '''
    def __init__(self) -> None:
        pass

    # Annotation data type with : <datatype> 
    # Use -> <datatype> to annotation the return datatype of function
    def findSolution(self, C : int, W : List[int], P : List[int]) -> List[int]:
        '''
        Find a solution of knapsack problem using Dynamic Programing algorithms

        @Parameters:
        ----------
            - C : weight of knapsack
            - W : list weight of items
            - P : list price of items

        @Return
        ----------
        List indexes of selected items
        '''
        return [1, 2, 3]

    # Private function with __ at start of function name
    def __maxPrice(self, P : List[int]) -> int:
        '''
        Find max price of given list prices of items
        '''
        return max(P)