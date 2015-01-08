import EulerRunner
import itertools

def problem2_iter():
    total = 0
    fib1 = 0
    fib2 = 1
    while fib2 < 4000000:
        fibtemp = fib1 + fib2
        fib1 = fib2
        fib2 = fibtemp
        if fib1 % 2 == 0:
            total += fib1
    return total

def problem2_func():
    return sum((y for y in itertools.takewhile(lambda x: x < 4000000, EulerRunner.fib_generator()) if y % 2 == 0))
    

EulerRunner.solve_problem(problem2_iter)
EulerRunner.solve_problem(problem2_func)
