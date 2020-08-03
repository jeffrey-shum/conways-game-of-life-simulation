#board.py
import random

def dead_state(width, height):
    board_state = []
    for n in range(height):
        row = [0 for x in range(width)]
        board_state.append(row)
    return board_state    

def random_state(width, height):
    board_state = dead_state(width, height)
    for row in board_state:
        for cell_num, cel in enumerate(row):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = 1
            else:
                cell_state = 0 
            row[cell_num] = cell_state
    return board_state

def render(board_state):
    print('-' * (len(board_state[0]) + 2))
    for row in board_state:
        print('|', end ='')
        for cell in row:
            if cell == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print('|')        
    print('-' * (len(board_state[0]) + 2))

def main(argv):
    return print(random_state(int(argv[1]),int(argv[2])))

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise RuntimeError(f'{sys.argv[0]} usage: width height')
    main(sys.argv)
