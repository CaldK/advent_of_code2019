
def setup_input(inputfile):
    with open(inputfile) as f:
        return [line.strip('\n').split(')') for line in f]


def num_of_connections(input, s, level):
    num = 0
    for i in input:
        if s == i[0]:
            num += level + 1 + num_of_connections(input, i[1], level+1)
    return num


def path_to_orbit(input, goal):
    '''returns the unique Path from the innermost orbit to the
       predecessor of the orbit goal'''
    for i in input:
        if goal == i[1]:
            return path_to_orbit(input, i[0]) + [i[0]]
    return []


def main():
    input = setup_input("input06.txt")

    # PART 1 - Number of direct and indirect orbits:
    print(num_of_connections(
        input, path_to_orbit(input, input[0][0])[0], 0))

    # PART 1 - Only with path_to_orbit
    visited = []
    num = 0
    for i in input:
        if i[1] not in visited:
            num += len(path_to_orbit(input, i[1]))
            visited.append(i[1])
    print(num)

    # PART 2 - Minimum number of orbital transfers:
    print(len(set(path_to_orbit(input, 'YOU'))
              ^ set(path_to_orbit(input, 'SAN'))))


if __name__ == "__main__":
    main()
