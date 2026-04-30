from typing import List, Tuple
import time
import numpy as np
import pyautogui as auto

from board import Board
from screen_location_data import OBJ_LOCS, COMP_LOCS

from solver import Solver


COLORS = {
    "BLUE":     [  76, 140, 230 ],
    "YELLOW":   [ 255, 179,  30 ],
    "BROWN":    [ 140, 114,  76 ],
    "WHITE":    [ 255, 255, 255 ],
}


def _color_diff(color: List[int], other: List[int])->int:
    diff = 0
    for i in range(0, 3):
        diff += abs(int(other[i]) - int(color[i]))
    return diff


def _detect_obj(color: List[int])->int:
    if _color_diff(color, COLORS["YELLOW"]) < 20:
        return 1
    if _color_diff(color, COLORS["BLUE"]) < 20:
        return 2
    return 0

def _detect_comp(pos: Tuple[int, int], img)->int:
    eq_sum_diff = 0
    df_sum_diff = 0
    
    EQ_OFFSET = [
        (  3,  5 ),
        (  3, -5 ),
        ( -3,  5 ),
        ( -3, -5 ),
    ]
    DF_OFFSET = [
        (  0,  0 ),
        (  3,  3 ),
        (  3, -3 ),
        ( -3,  3 ),
        ( -3, -3 ),
    ]
    
    for offset in EQ_OFFSET:
        eq_sum_diff += _color_diff(img[pos[0]+offset[0]][pos[1]+offset[1]], COLORS["BROWN"])
    for offset in DF_OFFSET:
        df_sum_diff += _color_diff(img[pos[0]+offset[0]][pos[1]+offset[1]], COLORS["BROWN"])
        
    if eq_sum_diff > 1500 and df_sum_diff > 1500:
        return 0
    if eq_sum_diff < 300:
        return 1
    if df_sum_diff < 300:
        return 2
    
    return 0


def capture_board()->Board:
    ss = auto.screenshot()
    img = np.array(ss)
    
    board = Board()
    
    for row in range(0, 6):
        for col in range(0, 6):
            board.grid[row][col] = _detect_obj(img[OBJ_LOCS[row][col][0]][OBJ_LOCS[row][col][1]])
            
    for row in range(0, 6):
        for col in range(0, 5):
            match _detect_comp(COMP_LOCS[0][row][col], img):
                case 0:
                    continue
                case 1:
                    board.equals.append(((row, col), (row, col+1)))
                    continue
                case 2:
                    board.diff.append(((row, col), (row, col+1)))
                    continue
    for row in range(0, 5):
        for col in range(0, 6):
            match _detect_comp(COMP_LOCS[1][row][col], img):
                case 0:
                    continue
                case 1:
                    board.equals.append(((row, col), (row+1, col)))
                    continue
                case 2:
                    board.diff.append(((row, col), (row+1, col)))
                    continue
            
    return board
    

def main():
    time.sleep(1)
    board = capture_board()
    solved = Solver(board)
    solved.backtrack()
    solved.print()
    
if __name__ == "__main__":
    main()