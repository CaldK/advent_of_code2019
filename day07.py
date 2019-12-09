import day05
from itertools import permutations

orig_program = day05.setup_input("input07.txt")

max_thrust = 0
# for x in permutations([0, 1, 2, 3, 4]):
#     output = 0
#     for elem in x:
#         program = orig_program.copy()
#         output = day05.intf(program, [elem, output])
#         if output > max_thrust:
#             max_thrust = output

print(max_thrust)

for x in permutations([5, 6, 7, 8, 9]):
    output = 0
    inputs = dict(zip(['A', 'B', 'C', 'D', 'E'], [[i] for i in x]))
    amps = dict(zip(['A', 'B', 'C', 'D', 'E'], [day05.intf(
        orig_program.copy(), x) for x in inputs.values()]))
    try:
        output_ampE = 0
        while True:
            for amp in amps:
                inputs[amp].append(output)
                output = next(amps[amp])
            output_ampE = output
    except StopIteration:
        print(f"Done. Code: {x} - Output: {output_ampE}")
    if output_ampE > max_thrust:
        max_thrust = output_ampE

print(max_thrust)
