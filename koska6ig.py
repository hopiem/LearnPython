

import random

count = 0

for x in range(100):
  rnd = random.choice(range(1, 7))

  print('ciklus ' + str(x) + '. dobás:' + str(rnd))

  if rnd == 6:
    count = count + 1


