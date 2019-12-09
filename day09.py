def setup_input(inputfile):
    with open(inputfile) as f:
        input = f.readline().strip("\n")
        input = [int(x) for x in input.split(",")]
    return input


def intf(input, input_values):
    output_value = 0
    i = 0
    relat_base = 0
    while True:
        opmode = str(input[i]).zfill(5)[::-1]
        opcode, mode1 = int(opmode[1::-1]), int(opmode[2])
        mode2, mode3 = int(opmode[3]), int(opmode[4])
        try:
            index1 = i+1 if mode1 == 1 else input[i+1]
            index2 = i+2 if mode2 == 1 else input[i+2]
            index3 = i+3 if mode3 == 1 else input[i+3]
            if mode1 == 2:
                index1 = input[i+1] + relat_base
            if mode2 == 2:
                index2 = input[i+2] + relat_base
            if mode3 == 2:
                index3 = input[i+3] + relat_base
        except IndexError:
            pass
        if opcode == 1:
            try:
                input[index3] = input[index1] + input[index2]
            except IndexError:
                input.extend([0]*(index3-len(input)+1))
                input[index3] = input[index1] + input[index2]
            i += 4
        elif opcode == 2:
            try:
                input[index3] = input[index1] * input[index2]
            except IndexError:
                input.extend([0]*(index3-len(input)+1))
                input[index3] = input[index1] * input[index2]
            i += 4
        elif opcode == 3:
            try:
                input_num = input_values.pop(0)
                input[index1] = input_num
            except IndexError:
                input.extend([0]*(index1-len(input)+1))
                input[index1] = input_num
            i += 2
        elif opcode == 4:
            yield input[index1]
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
            try:
                input[index3] = 1 if input[index1] < input[index2] else 0
            except IndexError:
                input.extend([0]*(index3-len(input)+1))
                input[index3] = 1 if input[index1] < input[index2] else 0
            i += 4
        elif opcode == 8:
            try:
                input[index3] = 1 if input[index1] == input[index2] else 0
            except IndexError:
                input.extend([0]*(index3-len(input)+1))
                input[index3] = 1 if input[index1] == input[index2] else 0
            i += 4
        elif opcode == 9:
            relat_base += input[index1]
            i += 2
        elif opcode == 99:
            break
        else:
            raise ValueError()
    return output_value


program = setup_input("input09.txt")
program = [109, 1, 204, -1, 1001, 100, 1,
           100, 1008, 100, 16, 101, 1006, 101, 0, 99]
for x in intf(program, [0]):
    print(x)
