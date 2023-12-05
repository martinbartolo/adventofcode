file = open("day-02.txt", "r")
text = file.read()


#################### Part 1 ####################
def sum_possible_game_ids(text: str):
    games = [line.split(": ")[1].strip("\n") for line in text.split("\n")]

    possible_ids: list[int] = []
    for game_index, game in enumerate(games):
        game_is_possible = True
        for cube_set in game.split("; "):
            num_blue = 0
            num_red = 0
            num_green = 0

            # get number of each color in cube set
            for num_color in cube_set.split(", "):
                num = int(num_color.split(" ")[0])
                color = num_color.split(" ")[1]
                if color == "blue":
                    num_blue = num
                elif color == "red":
                    num_red = num
                elif color == "green":
                    num_green = num

            if num_blue > 14 or num_red > 12 or num_green > 13:
                game_is_possible = False
                break

        if game_is_possible:
            possible_ids.append(game_index + 1)

    return sum(possible_ids)


print("Solution 1: ", sum_possible_game_ids(text))


#################### Part 2 ####################
def sum_game_powers(text: str):
    games = [line.split(": ")[1].strip("\n") for line in text.split("\n")]

    powers: list[int] = []
    for game in games:
        max_num_blue = 0
        max_num_red = 0
        max_num_green = 0
        for cube_set in game.split("; "):
            # get max number of each color in cube set
            for num_color in cube_set.split(", "):
                num = int(num_color.split(" ")[0])
                color = num_color.split(" ")[1]
                if color == "blue":
                    max_num_blue = max(max_num_blue, num)
                elif color == "red":
                    max_num_red = max(max_num_red, num)
                elif color == "green":
                    max_num_green = max(max_num_green, num)
        powers.append(max_num_blue * max_num_green * max_num_red)

    return sum(powers)


print("Solution 2: ", sum_game_powers(text))
