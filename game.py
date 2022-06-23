import copy
from itertools import zip_longest


def is_game_over(game_state: list[str]) -> bool:
    return all(
        (
            len(tube) == 0 or (len(tube) == 4 and len(set(tube)) == 1)
            for tube in game_state
        )
    )


def print_game(game_state: list[str]):
    print("\n")
    for row in reversed(list(zip_longest(*game_state, fillvalue="-"))):
        for ball_color in row:
            print(f"| {ball_color} |", end="  ")
        print("")
    for i in range(len(game_state)):
        print("|___|", end="  ")
    print("")
    for i in range(len(game_state)):
        print(f"  {i}  ", end="  ")
    print("\n")


def read_int(prompt: str) -> int:
    try:
        val = input(prompt)
        val = int(val)
    except TypeError:
        val = 0
    return val


def next_state(
    game_state: list[str], from_tube: int, to_tube: int
) -> tuple[list[str], bool]:
    game_state = copy.copy(game_state)
    # validate the user inputs
    # 1. Must be different tubes
    if from_tube == to_tube:
        # print("Values must be different")
        return game_state, False

    # apply/check the game rules
    # 2. Cannot move from empty tube
    if not len(game_state[from_tube]):
        # print("Cannot move something from empty tube")
        return game_state, False

    # 3. Any color balls can be moved to empty tubes
    # check if the tube is empty
    # or check if the colors match
    if (
        len(game_state[to_tube])
        and game_state[from_tube][-1] != game_state[to_tube][-1]
    ):
        # print("Colors are different on top of the tubes")
        return game_state, False

    # manipulate the game state
    # 4. Cannot put more than 4 balls
    # check the length of to_tube
    if len(game_state[to_tube]) < 4:
        # move the balls
        # remove from from_tube
        # add to to_tube
        ft = game_state[from_tube]
        tt = game_state[to_tube]
        game_state[from_tube], game_state[to_tube] = ft[:-1], tt + ft[-1]
        # ball_color = game_state[from_tube].pop()
        # game_state[to_tube].append(ball_color)
        # game_state.sort()
        while True:
            new_game_state, is_valid_move = next_state(game_state, from_tube, to_tube)
            if not is_valid_move:
                return game_state, True
            else:
                game_state = new_game_state

    return game_state, False


def game_state_hash(game_state: list[str]) -> str:
    return ";".join(sorted(game_state))


def is_same_state(game_state: list[str], other_game_state: list[str]) -> bool:
    return game_state_hash(game_state) == game_state_hash(other_game_state)


def play_game():
    gs = [
        "BRRG",
        "YRBG",
        "GYGY",
        "BYRB",
        "",
        "",
    ]
    gs.sort()

    while not is_game_over(gs):
        print_game(gs)
        ft1 = read_int("From tube:")
        tt1 = read_int("To tube:")
        gs, is_valid_move = next_state(gs, ft1, tt1)
        if not is_valid_move:
            print("Not a valid move")
    print_game(gs)


if __name__ == "__main__":
    play_game()
