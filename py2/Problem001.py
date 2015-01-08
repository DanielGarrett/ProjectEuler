import EulerRunner

def problem1_iter():
    sum = 0
    for x in range(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

def problem1_func():
    return reduce((lambda x,y: x+y), [x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


EulerRunner.solve_problem(problem1_iter)
EulerRunner.solve_problem(problem1_func)
