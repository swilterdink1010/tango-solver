import pyautogui as auto
import numpy as np

from solver import Solver

def capture_board():
    ss = auto.screenshot()
    img = np.array(ss)