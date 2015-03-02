import EulerRunner
import math

def problem39iter():
    maxnum = 0
    maxval = 0
    sqr = [x**2 for x in range(1000)]
    for p in range(12, 1001):
        count = 0
        for a in range(1, p/3):
            for b in range(a+1, ((p-a)/2) + 1):
                c = p - a - b
                if sqr[a] + sqr[b] == sqr[c]:
                    count += 1
        if count > maxval:
            maxval = count
            maxnum = p
    return maxnum

EulerRunner.solve_problem(problem39iter)
