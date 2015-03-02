import EulerRunner
import math

def count_factors(num):
    count = 0
    for x in range(1, int(math.floor(math.sqrt(num)))):
        if num % x == 0:
            count += 1
    return count * 2
        

def problem12_iter():
    gen = EulerRunner.triangle_generator()
    while True:
        x = gen.next()
        y = count_factors(x)
        if y > 500:
            return x

EulerRunner.solve_problem(problem12_iter)
