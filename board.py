#board.py

def dead_state(width, height):
    board = []
    for n in range(height):
        row = [0 for x in range(width)]
        board.append(row)
    return board    
