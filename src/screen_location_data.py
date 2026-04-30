_obj_x = [
     749, 
     836, 
     922,
    1009,
    1095,
    1182,
]
_obj_y = [
     342,
     429,
     515,
     602,
     689,
     776,
]
_comp_h_x = [
     786,
     873,
     960,
    1046,
    1133,
]
_comp_h_y = [
     335,
     422,
     508,
     595,
     682,
     768,
]

OBJ_LOCS = [[(0, 0)] * 6 for _ in range(0, 6)]
for row in range(0, 6):
    for col in range(0, 6):
        OBJ_LOCS[row][col] = (_obj_y[row], _obj_x[col])
        
COMP_LOCS = [
    [[(0, 0)] * 5 for _ in range(0, 6)],
    [[(0, 0)] * 6 for _ in range(0, 5)],
]
for row in range(0, 6):
    for col in range(0, 5):
        COMP_LOCS[0][row][col] = (_comp_h_y[row], _comp_h_x[col])