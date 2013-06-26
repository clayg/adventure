# (a x_n + c) mod m
seed = 6
for i in range(5):
    print seed % 36
    seed = (69069 * seed + 1) % 2 ** 32

