import EulerRunner
import math

def problem39iter():
    maxnum = 0
    maxval = 0
    for p in range(1, 1001):
        count = 0
        for a in range(int(math.floor((p)/3)), 0, -1):
            asquared = a**2
            for b in range(a+1,int(math.floor((p-a)/2))):
                c = p - a - b
                if asquared + b**2 == c**2:
                    count += 1
        if count > maxval:
            maxval = count
            maxnum = p
    return maxnum

EulerRunner.solve_problem(problem39iter)
