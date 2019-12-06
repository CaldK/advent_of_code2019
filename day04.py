from collections import Counter

print(sum([1 for i in range(273025, 767254) if (sorted(str(i)) == list(
    str(i)) and any([j >= 2 for j in Counter(str(i)).values()]))]))
