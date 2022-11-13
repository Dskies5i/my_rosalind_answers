
def fibonacci_loop_pythonic(months, offpermat):
    baby, parent = 1, 1

    for i in range(months - 1):
        # this format has a temporary implicit value
        baby, parent = parent, parent + (baby * offpermat)
        print("Baby", baby, end=" ")
        print("Parent", parent)

    return baby


#print(fibonacci_loop_pythonic(4, 5))

def fibonacci_with_lifespan(n, m):
    parent, baby = 1, 1
    offpermat = 2

    for i in range(2, n):
        gen = 0
        if i < m:
            baby, parent = parent, parent + (baby * offpermat)

    return baby


print(fibonacci_with_lifespan(6, 3))


n = 89  # replace input
m = 16  # replace input
bunnies = [1, 1]
months = 2
count = []
while months < n:
    if months < m:
        bunnies.append(bunnies[-2] + bunnies[-1])
    elif months == m or count == m + 1:
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)
    else:
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(
            m + 1)])
    months += 1


def MortalFibonacci(n, m):
    living = [1, 1]
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death
        print(tmp)
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    print(living)
    return living[-1]


# months/generations
n = 87
# survival time
m = 19
