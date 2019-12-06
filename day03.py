def add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def between(x0, x1, y1):
    ls = [x0, x1, y1]
    ls.sort()
    return ls[1] == x0


def detec_coll(s_1, t_1, s_2, t_2):
    if s_1[0] == t_1[0] and s_2[1] == t_2[1]:
        if between(s_1[0], s_2[0], t_2[0]) and between(s_2[1], s_1[1], t_1[1]):
            return(s_1[0], s_2[1])
    if s_1[1] == t_1[1] and s_2[0] == t_2[0]:
        if between(s_1[1], s_2[1], t_2[1]) and between(s_2[0], s_1[0], t_1[0]):
            return(s_2[0], s_1[1])
    return None


def calc_steps(x, y):
    if x[0] == y[0]:
        return abs(x[1]-y[1])
    elif x[1] == y[1]:
        return abs(x[0]-y[0])
    return None


def import_input(input1='', input2='', data=None):
    if data is not None:
        with open(data) as f:
            input1 = f.readline().strip('\n').split(',')
            input2 = f.readline().strip('\n').split(',')
    else:
        input1 = input1.split(',')
        input2 = input2.split(',')
    return input1, input2


def get_distance_steps(input1, input2):
    position = (0, 0)
    pois = [(0, 0)]
    for x in input1:
        richtung = x[:1]
        strecke = int(x[1:])
        if richtung == 'R':
            po = (strecke, 0)
        elif richtung == 'U':
            po = (0, strecke)
        elif richtung == 'D':
            po = (0, -strecke)
        elif richtung == 'L':
            po = (-strecke, 0)
        new_po = add(position, po)
        pois.append(new_po)
        position = new_po

    position = (0, 0)
    collition = []
    collition_step = []
    steps2 = 0

    for x in input2:
        richtung = x[:1]
        strecke = int(x[1:])
        if richtung == 'R':
            po = (strecke, 0)
        elif richtung == 'U':
            po = (0, strecke)
        elif richtung == 'D':
            po = (0, -strecke)
        elif richtung == 'L':
            po = (-strecke, 0)
        new_po = add(position, po)
        steps1 = 0
        for i in range(len(pois)-1):
            coll = detec_coll(position, new_po, pois[i], pois[i+1])
            if coll is not None:
                collition.append(coll)
                collition_step.append(
                    steps1+calc_steps(position, coll) +
                    steps2+calc_steps(pois[i], coll))
            steps1 += calc_steps(pois[i], pois[i+1])
        steps2 += strecke
        position = new_po

    distances = []
    if (0, 0) in collition:
        collition.remove((0, 0))
    if 0 in collition_step:
        collition_step.remove(0)
    for coll in collition:
        distances.append(abs(coll[0])+abs(coll[1]))

    return min(distances), min(collition_step)


def main():
    input1, input2 = import_input(data="input03.txt")
    distance, steps = get_distance_steps(input1, input2)
    print(
        f"Answer for Day 03 - First Part: {distance} - Second Part: {steps}.")


if __name__ == "__main__":
    main()
