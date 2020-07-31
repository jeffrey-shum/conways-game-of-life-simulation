#board.py
import random

def dead_state(width, height):
    board = []
    for n in range(height):
        row = [0 for x in range(width)]
        board.append(row)
    return board    

def random_state(width, height):
    state = dead_state(width, height)
    for row in state:
        for cell_num, cel in enumerate(row):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 1
            else:
                cell_state = 0 
            row[cell_num] = cell_state
    return state

def main(argv):
    return print(random_state(int(argv[1]),int(argv[2])))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise RuntimeError(f'{sys.argv[0]} usage: width height')
    main(sys.argv)
