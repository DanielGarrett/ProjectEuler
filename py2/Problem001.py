import EulerRunner

def problem1_iter():
    total = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total

def problem1_func():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


EulerRunner.solve_problem(problem1_iter)
EulerRunner.solve_problem(problem1_func)
