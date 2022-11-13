import random

k, m, n = input("Enter 3 values: ").split()
population = k * ["AA"] + m * ["Aa"] + n * ["aa"]
count = 0
for i in range(10000):
  count += 'A' in [random.choice(x) for x in random.sample(population, 2)]
print(count / 10000)
