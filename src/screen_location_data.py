_obj_y = [
     342,
     429,
     515,
     602,
     689,
     776,
]
_obj_x = [
     749, 
     836, 
     922,
    1009,
    1095,
    1182.
]

OBJ_LOCS = [[(0, 0)] * 6 for _ in range(0, 6)]
for row in range(0, 6):
    for col in range(0, 6):
        OBJ_LOCS[row][col] = (_obj_x[col], _obj_y[row])
        
