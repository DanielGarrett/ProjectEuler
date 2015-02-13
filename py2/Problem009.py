import EulerRunner
import math

def problem9iter():
    for a in range(333, 0, -1):
        asquared = a**2
        for b in range(a+1,int(math.floor((1000-a)/2))):
            c = 1000 - a - b
            if asquared + b**2 == c**2:
                return a*b*c
    return False

EulerRunner.solve_problem(problem9iter)
