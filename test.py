from game_of_life import next_board_state, dead_state

# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

def conduct_test(initial_state, expected_next_state):
    actual_next_state = next_board_state(initial_state)
    if expected_next_state == actual_next_state:
        print("PASSED")
    else:
        print("FAILED!")
        print("Expected:")
        print(expected_next_state)
        print("Actual:")
        print(actual_next_state)
        

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    conduct_test(init_state1, expected_next_state1)

    
    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]

    conduct_test(init_state2, expected_next_state2)


    # Test 3: live cells with less than 2 live neighbors
    # should become dead.

    init_state3 = [
        [1,1,0],
        [0,0,0],
        [0,0,0]
    ]
        
    expected_next_state3 = dead_state(3,3)

    conduct_test(init_state3, expected_next_state3)


    # Test 4: live cells with exactly 3 live neighbors
    # should stay alive

    init_state4 = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]

    expected_next_state4 = [
        [1,1,0],
        [1,1,0],
        [0,0,0]
    ]
    
    conduct_test(init_state4, expected_next_state4)

    # Test 5: live cells with exactly 2 live neighbors
    # should stay alive.

    init_state5 = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]

    expected_next_state5 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]

    conduct_test(init_state5, expected_next_state5)

    # Test 6: dead cells with exactly 3 live neighbors
    # should come alive.
    
    init_state6 = [
        [1,0,1],
        [0,0,0],
        [1,0,0]
    ]

    expected_next_state6 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]

    conduct_test(init_state6, expected_next_state6)
