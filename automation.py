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
    [
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
    ],
    [],
]
n_tubes = len(game_state[0])

# print_game(game_state)
played_game_state_hashes = []
all_game_states = [game_state]

t1 = time.time()
while len(all_game_states):
    print(len(all_game_states), len(played_game_state_hashes), end="\r")
    game_state, game_actions = all_game_states.pop(0)
    played_game_state_hashes.append(game_state_hash(game_state))
    for i in range(n_tubes):
        gsi = game_state[i]
        if not len(gsi) or (len(gsi) == 4 and len(set(gsi)) == 1):
            continue
        for j in range(n_tubes):
            if i != j:
                new_game_state, is_valid_move = next_state(game_state, i, j)
                if not is_valid_move:
                    continue
                if (ngs := game_state_hash(new_game_state)) in played_game_state_hashes:
                    continue
                for played_game_state in all_game_states:
                    if ngs == game_state_hash(played_game_state[0]):
                        break
                else:
                    if is_game_over(new_game_state):
                        print("\n\n")
                        for step, [from_tube, to_tube] in enumerate(
                            game_actions + [[i, j]]
                        ):
                            print(
                                f"Step {step + 1:3} From {from_tube + 1} - To {to_tube + 1}"
                            )
                        print("Found solution in ", time.time() - t1, "seconds")
                        input("Press enter for next solution")
                        t1 = time.time()
                    else:
                        all_game_states.append(
                            [new_game_state, game_actions + [[i, j]]]
                        )
