from typing import List, Tuple

class Board:
    def __init__(self, 
                 suns: List[Tuple[int, int]] = list(), 
                 moons: List[Tuple[int, int]] = list(), 
                 equals: List[Tuple[Tuple[int, int], Tuple[int, int]]] = list(), 
                 diff: List[Tuple[Tuple[int, int], Tuple[int, int]]] = list()
                )->None:
        
        self.grid = [[0] * 6 for _ in range(0, 6)]
        for (row, col) in suns:
            self.grid[row][col] = 1
        for (row, col) in moons:
            self.grid[row][col] = 2
        
        self.equals = equals
        self.diff = diff
        
    def print(self)->None:
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()