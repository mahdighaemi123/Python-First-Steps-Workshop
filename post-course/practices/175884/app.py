# https://quera.org/problemset/175884/

# solution 1
def calculate_floor(floors):
    u_count = 0
    d_count = 0

    for floor in floors:
        if floor == "U":
            u_count += 1

        elif floor == "D":
            d_count += 1

    return u_count - d_count

# solution 2
def calculate_floor(floors):
    floor = 0

    for floor in floors:
        if floor == "U":
            floor += 1

        elif floor == "D":
            floor -= 1

    return floor

# solution 3
def calculate_floor(floors):
    return floors.count("U") - floors.count("D")