from parse_screen import capture_board
import keyboard
from solver import Solver
import pyautogui as auto
from screen_location_data import OBJ_LOCS


auto.PAUSE = 0.0001


def solve_screen():
    board_state = capture_board()
    print("\nStarting State:")
    board_state.print()
    solver = Solver(board_state)
    solver.backtrack()
    print("\nTarget State:")
    solver.print()
    for row in range(0, 6):
        for col in range(0, 6):
            if board_state.grid[row][col] != 0:
                continue
            for _ in range(0, solver.grid[row][col]):   
                auto.leftClick(OBJ_LOCS[row][col][1], OBJ_LOCS[row][col][0])


def main():
    try:
        keyboard.add_hotkey("j", solve_screen)
        print("Press 'J' with board on screen to run solver")
        keyboard.wait("j")
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()