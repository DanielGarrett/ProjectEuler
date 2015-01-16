import EulerRunner

def euclid(x,y):
    return y if x % y == 0 else euclid(y, x % y)

def lcm(x,y):
    return (x * y) / (euclid(x,y) if x > y else euclid(y,x))

def problem5_func():
    return reduce(lcm, range(1,21), 1)
        

EulerRunner.solve_problem(problem5_func)
