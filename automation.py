import time

from game import game_state_hash, is_game_over, next_state

"""
blue - a
brown - b
gray - c
green - d
light green - e
light light green - f
orange - g
pink - h
purple - i
red - j
skyblue - k
yellow - l
"""
game_state = [
    "kkda",
    "cehi",
    "bjig",
    "gjhg",
    "aljd",
    "dbdl",
    "fjib",
    "fhif",
    "akce",
    "eclb",
    "aflc",
    "ghke",
    "",
    "",
]
n_tubes = len(game_state)

# print_game(game_state)
played_game_state_hashes = set()
all_game_states = [[game_state, []]]
all_game_state_hashes = set([game_state_hash(game_state)])

t1 = time.time()
while len(all_game_states):
    print(len(all_game_states), len(played_game_state_hashes), end="\r")
    # get a new game state using BFS
    game_state, game_actions = all_game_states.pop(0)
    current_game_hash = game_state_hash(game_state)
    played_game_state_hashes.add(current_game_hash)
    all_game_state_hashes.remove(current_game_hash)

    for i in range(n_tubes):
        gsi = game_state[i]
        # continue if tube contains no balls or all balls with same color
        if not len(gsi) or (len(gsi) == 4 and len(set(gsi)) == 1):
            continue
        for j in range(n_tubes):
            # skip moving to same tube
            if i == j:
                continue
            new_game_state, is_valid_move = next_state(game_state, i, j)
            if not is_valid_move:
                continue
            if (ngs := game_state_hash(new_game_state)) in played_game_state_hashes:
                continue
            if ngs in all_game_state_hashes:
                continue
            if is_game_over(new_game_state):
                print("\n\n")
                for step, [from_tube, to_tube] in enumerate(game_actions + [[i, j]]):
                    print(f"Step {step + 1:3} From {from_tube + 1} - To {to_tube + 1}")
                print("Found solution in ", time.time() - t1, "seconds")
                input("Press enter for next solution")
                t1 = time.time()
            else:
                all_game_states.append([new_game_state, game_actions + [[i, j]]])
                all_game_state_hashes.add(ngs)
