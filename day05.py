def setup_input(inputfile):
    with open(inputfile) as f:
        input = f.readline().strip("\n")
        input = [int(x) for x in input.split(",")]
    return input


def intf(input, input_value):
    output_value = 0
    i = 0
    while True:
        opmode = str(input[i]).zfill(5)[::-1]
        opcode, mode1 = int(opmode[1::-1]), int(opmode[2])
        mode2, mode3 = int(opmode[3]), int(opmode[4])
        try:
            index1 = i+1 if mode1 else input[i+1]
            index2 = i+2 if mode2 else input[i+2]
            index3 = i+3 if mode3 else input[i+3]
        except IndexError:
            pass
        if opcode == 1:
            input[index3] = input[index1] + input[index2]
            i += 4
        elif opcode == 2:
            input[index3] = input[index1] * input[index2]
            i += 4
        elif opcode == 3:
            input[index1] = input_value
            i += 2
        elif opcode == 4:
            output_value = input[index1]
            if output_value:
                ValueError(
                    f"Check is not 0 - Error Code: {output_value} - on {i}")
            i += 2
        elif opcode == 5:
            i = input[index2] if input[index1] else i+3
        elif opcode == 6:
            i = input[index2] if not input[index1] else i+3
        elif opcode == 7:
            input[index3] = 1 if input[index1] < input[index2] else 0
            i += 4
        elif opcode == 8:
            input[index3] = 1 if input[index1] == input[index2] else 0
            i += 4
        elif opcode == 99:
            break
        else:
            raise ValueError()
    return output_value


assert intf([3, 12, 6, 12, 15, 1, 13, 14, 13,
             4, 13, 99, -1, 0, 1, 9], 42) == 1
assert intf([3, 12, 6, 12, 15, 1, 13, 14, 13,
             4, 13, 99, -1, 0, 1, 9], 0) == 0
assert intf([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 42) == 1
assert intf([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0) == 0


def main():
    input = setup_input("input05.txt")
    print(f"Diagnostic code for Part 1 is: {intf(input, 1)}")
    input = setup_input("input05.txt")
    print(f"Diagnostic code for Part 2 is: {intf(input, 5)}")


if __name__ == "__main__":
    main()
