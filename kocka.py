#100 dobásból
import random

n = 0#dobások száma

dobás = -1

while n < 100 and dobás != 6:
    n = n + 1

    dobás = random.choice([1, 2, 3, 4, 5, 6])

    print("dobás " + str(dobás) + "-es")


print("Vége")
