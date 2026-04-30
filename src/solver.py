from copy import deepcopy

from board import Board
import board_history

class Solver:
    def __init__(self, board: Board = Board())->None:
        self.grid = deepcopy(board.grid)
        self.equals = deepcopy(board.equals)
        self.diff = deepcopy(board.diff)
    
    def _match_diff_equals(self)->bool:
        r_val = False
        
        for eq in self.equals:
            first = self.grid[eq[0][0]][eq[0][1]]
            second = self.grid[eq[1][0]][eq[1][1]]
            
            if first == 0 and second != 0:
                self.grid[eq[0][0]][eq[0][1]] = second
                r_val = True
                
            elif first != 0 and second == 0:
                self.grid[eq[1][0]][eq[1][1]] = first
                r_val = True
                
        for df in self.diff:
            first = self.grid[df[0][0]][df[0][1]]
            second = self.grid[df[1][0]][df[1][1]]
            
            if first == 0 and second != 0:
                self.grid[df[0][0]][df[0][1]] = 3 - second
                r_val = True
                
            elif first != 0 and second == 0:
                self.grid[df[1][0]][df[1][1]] = 3 - first
                r_val = True
                
        return r_val
    
    def _check_count(self)->bool:
        r_val = False
        
        for row in range(0, 6):
            suns = 0
            moons = 0
                
            for col in range(0, 6):
                match (self.grid[row][col]):
                    case 0:
                        continue
                    case 1:
                        suns+=1
                        continue
                    case 2:
                        moons+=1
                        continue
                
            if suns == 3 and moons != 3:
                for col in range(0, 6):
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 2
                r_val = True
                
            elif moons == 3 and suns != 3:
                for col in range(0, 6):
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 1
                r_val = True
                
        for col in range(0, 6):
            suns = 0
            moons = 0
                
            for row in range(0, 6):
                match (self.grid[row][col]):
                    case 0:
                        continue
                    case 1:
                        suns+=1
                        continue
                    case 2:
                        moons+=1
                        continue
                
            if suns == 3 and moons != 3:
                for row in range(0, 6):
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 2
                r_val = True
                
            elif moons == 3 and suns != 3:
                for row in range(0, 6):
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 1
                r_val = True
                
        return r_val
                
    def _double_fill(self)->bool:
        r_val = False
        for row in range(0, 6):
            for col in range(0, 5):
                if self.grid[row][col] == 0:
                    continue
                
                if self.grid[row][col] == self.grid[row][col+1]:
                    if col > 0:
                        if self.grid[row][col-1] == 0:
                            self.grid[row][col-1] = 3 - self.grid[row][col]
                            r_val = True
                    if col < 4:
                        if self.grid[row][col+2] == 0:
                            self.grid[row][col+2] = 3 - self.grid[row][col]
                            r_val = True
                            
        for col in range(0, 6):
            for row in range(0, 5):
                if self.grid[row][col] == 0:
                    continue
                
                if self.grid[row][col] == self.grid[row+1][col]:
                    if row > 0:
                        if self.grid[row-1][col] == 0:
                            self.grid[row-1][col] = 3 - self.grid[row][col]
                            r_val = True
                    if row < 4:
                        if self.grid[row+2][col] == 0:
                            self.grid[row+2][col] = 3 - self.grid[row][col]
                            r_val = True
        return r_val
        
    def _gap_fill(self)->bool:
        r_val = False
        
        for row in range(0, 6):
            for col in range(0, 6):
                if self.grid[row][col] != 0:
                    continue
                
                if row > 0 and row < 5:
                    if self.grid[row-1][col] == self.grid[row+1][col] and self.grid[row-1][col] != 0:
                        self.grid[row][col] = 3 - self.grid[row-1][col]
                        r_val = True
                
                if col > 0 and col < 5:
                    if self.grid[row][col-1] == self.grid[row][col+1] and self.grid[row][col-1] != 0:
                        self.grid[row][col] = 3 - self.grid[row][col-1]
                        r_val = True
                
        return r_val
        
    def _solve_trivial(self)->None:
        active = True
        while active:
            if self._match_diff_equals():
                continue
            if self._check_count():
                continue
            if self._double_fill():
                continue
            if self._gap_fill():
                continue
            active = False
        
    def _valid_board(self)->bool:
        for eq in self.equals:
            first = self.grid[eq[0][0]][eq[0][1]]
            second = self.grid[eq[1][0]][eq[1][1]]
            if first != second and first != 0 and second != 0:
                return False
            
        for df in self.diff:
            first = self.grid[df[0][0]][df[0][1]]
            second = self.grid[df[1][0]][df[1][1]]
            if first == second and first != 0 and second != 0:
                return False
            
        for row in range(0, 6):
            suns = 0
            moons = 0
                
            for col in range(0, 6):
                match (self.grid[row][col]):
                    case 0:
                        continue
                    case 1:
                        suns+=1
                        continue
                    case 2:
                        moons+=1
                        continue
                
            if suns > 3 or moons > 3:
                return False
                
        for col in range(0, 6):
            suns = 0
            moons = 0
                
            for row in range(0, 6):
                match (self.grid[row][col]):
                    case 0:
                        continue
                    case 1:
                        suns+=1
                        continue
                    case 2:
                        moons+=1
                        continue
                
            if suns > 3 or moons > 3:
                return False
            
        for row in range(0, 6):
            for col in range(0, 4):
                match = self.grid[row][col]
                if match == 0:
                    continue
                
                if self.grid[row][col+1] == match and self.grid[row][col+2] == match:
                    return False
                
        for col in range(0, 6):
            for row in range(0, 4):
                match = self.grid[row][col]
                if match == 0:
                    continue
                
                if self.grid[row+1][col] == match and self.grid[row+2][col] == match:
                    return False
                
        return True
            
    def backtrack(self)->bool:
        self._solve_trivial()
        
        if not self._valid_board():
            return False
        
        eligible = []
        for row in range(0, 6):
            for col in range(0, 6):
                if self.grid[row][col] == 0:
                    eligible.append((row, col))
        
        if len(eligible) == 0:
            return True
        
        for eq in self.equals: # try equals first to elim most options
            if eq[0] in eligible:
                old_grid = deepcopy(self.grid)
                self.grid[eq[0][0]][eq[0][1]] = 1
                if self.backtrack():
                    return True
                else:
                    self.grid = old_grid
                    self.grid[eq[0][0]][eq[0][1]] = 2
                    if self.backtrack():
                        return True
                    else:
                        return False
                    
        for df in self.diff: # diff as second resort
            if df[0] in eligible:
                old_grid = deepcopy(self.grid)
                self.grid[df[0][0]][df[0][1]] = 1
                if self.backtrack():
                    return True
                else:
                    self.grid = old_grid
                    self.grid[df[0][0]][df[0][1]] = 2
                    if self.backtrack():
                        return True
                    else:
                        return False
                    
        old_grid = deepcopy(self.grid) # if no equals or diffs are eligible
        self.grid[eligible[0][0]][eligible[0][1]] = 1
        if self.backtrack():
            return True
        else:
            self.grid = old_grid
            self.grid[eligible[0][0]][eligible[0][1]] = 2
            if self.backtrack():
                return True
            else:
                return False
            
    def print(self)->None:
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()


def main():
    solver = Solver(board_history.apr_29)
    solver.backtrack()
    solver.print()
    
    
if __name__ == "__main__":
    main()