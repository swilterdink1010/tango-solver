from typing import List
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

def capture_board()->Board:
    ss = auto.screenshot()
    img = np.array(ss)
    
    board = Board()
    
    for row in range(0, 6):
        for col in range(0, 6):
            board.grid[row][col] = _detect_obj(img[OBJ_LOCS[row][col][0]][OBJ_LOCS[row][col][1]])
            
    return board
    

def main():
    time.sleep(1)
    capture_board().print()
    
    
if __name__ == "__main__":
    main()