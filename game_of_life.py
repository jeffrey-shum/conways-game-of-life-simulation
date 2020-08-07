#board.py
import random
import time

dead = 0
live = 1

def dead_state(width, height):
    '''
    Emits a board state when supplied with a specified board width and height.
    '''
    return [[dead for _ in range(width)] for _ in range(height)]

def random_state(width, height):
    '''
    Emits a board state with randomly generated cell states.
    '''
    board_state = dead_state(width, height)
    for row in board_state:
        for cell_index, cell in enumerate(row):
            random_number = random.random()
            if random_number >= 0.5:
                cell_state = live
            else:
                cell_state = dead 
            row[cell_index] = cell_state
    return board_state

def state_width(state):
    '''
    Emit the width of a board state.
    '''
    return len(state[0])

def state_height(state):
    '''
    Emit the height of a board state.
    '''
    return len(state)

def load_board_state(filepath):
    with open(filepath, 'r') as f:
        lines = [l.rstrip() for l in f.readlines()] # rstrip() to ignore newlines

    width = state_width(lines)
    height = state_height(lines)
    board_state = dead_state(width, height)

    for row_index, row in enumerate(lines):
        for column_index, character in enumerate(row):
            board_state[row_index][column_index] = int(character)
    
    return board_state
def render(board_state):
    '''
    Renders a board in the terminal when supplied with a board state.
    '''
    display_as = {
        dead : ' ',
        live : u"\u2588" # Unicode for filled in square
    }
    width = state_width(board_state)
    print('-' * ((width * 2) + 2))
    for row in board_state:
        print('|', end ='')
        for cell in row:
            if cell == live:
                print(display_as[live] * 2, end='')
            else:
                print(display_as[dead] * 2, end='')
        print('|')        
    print('-' * ((width * 2) + 2))

def next_cell_state(cell_coords, state):
    '''
    Emit the next value of a single cell.
    '''
    height = state_height(state)
    width = state_width(state)
    x = cell_coords[0]
    y = cell_coords[1]
    cell_state = state[x][y]
    num_live_neighbors = 0
    for row_index in range((x-1), (x+1)+1):
        if row_index < 0 or row_index >= height: continue
        for column_index in range((y-1), (y+1)+1):
            if column_index < 0 or column_index >= width: continue
            if row_index == x and column_index == y: continue
            if state[row_index][column_index] == live:
                num_live_neighbors += 1
    if cell_state == live:
        if num_live_neighbors <= 1:
            return dead
        elif num_live_neighbors <= 3:
            return live
        else:
            return dead
    else:
        if num_live_neighbors == 3:
            return live
        else:
            return dead
            
def next_board_state(initial_state):
    width = state_width(initial_state)
    height = state_height(initial_state)
    next_state = dead_state(width, height)
    for row_index in range(0, height):
        for column_index in range(0, width):
            next_state[row_index][column_index] = next_cell_state((row_index,column_index), initial_state)
    return next_state    

def board_generator(state):
    '''
    Generator which continuously generates the next board state.
    '''
    while True:
        next_state = next_board_state(state)
        yield next_state
        state = next_state
        time.sleep(.5)

def run_simulation(state):
    '''
    Renders the game of life simulation continuously.
    '''
    for phase in board_generator(state):
        render(phase)

def main(argv):
    state = (random_state(int(argv[1]),int(argv[2])))
    run_simulation(state)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise RuntimeError(f'{sys.argv[0]} usage: width height')
    main(sys.argv)
