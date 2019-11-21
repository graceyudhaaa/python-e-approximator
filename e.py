import random
import statistics



def e():
    n = input('how many iteration you want?: ')
    steps = []

    for number in range(0,int(n)):
        x = 0
        step = 0

        while x < 1:
            x += random.random()
            # print(x)
            step = step + 1

        steps.append(step)

    print(f"e is approximately {statistics.mean(steps)}")

    return(statistics.mean(steps))


e()