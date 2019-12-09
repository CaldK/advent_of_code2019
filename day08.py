from textwrap import wrap
from collections import Counter


def setup_input(inputfile):
    with open(inputfile) as f:
        return f.readline().strip("\n")


corp = setup_input("input08.txt")
layers = wrap(corp, 150)
print([x.count('1')*x.count('2') for x in layers if x.count('0') == 4])

image = ''
for x in zip(*layers):
    try:
        first_1 = x.index('1')
    except ValueError:
        first_1 = None
    try:
        first_0 = x.index('0')
    except ValueError:
        first_0 = None
    color = None
    if first_1 is None:
        color = '.'
    elif first_0 is None:
        color = ' '
    elif x.index('1') < x.index('0'):
        color = ' '
    elif x.index('0') < x.index('1'):
        color = ','
    image += color

for x in wrap(image, 25):
    print(' '.join(x))
with open("output08.txt", "w") as f:
    f.writelines([(' '.join(x))+'\n' for x in wrap(image, 25)])
