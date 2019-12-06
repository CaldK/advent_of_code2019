sumfuel = 0

with open("input.txt") as f:
    for mass in f:
        sumfuel += int(mass)//3 - 2

print(sumfuel)


def gen_fuel_req(n):
    mass_to_consider = n//3 - 2
    while mass_to_consider > 0:
        yield mass_to_consider
        mass_to_consider = mass_to_consider//3 - 2


sumfuel = 0

with open("input.txt") as f:
    for mass in f:
        sumfuel += sum(gen_fuel_req(int(mass)))

print(sumfuel)
