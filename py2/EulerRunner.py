#EulerRunner.py
import datetime
def solve_problem(solve_func):
    start = datetime.datetime.now()
    result = str(solve_func())
    end = datetime.datetime.now()
    print 'The answer is "' + result + '". Solved in ' + str((end - start).total_seconds()) + 's'

def fib_generator():
    fib1, fib2 = 0, 1
    yield fib1
    yield fib2
    while True:
        fibtemp = fib1 + fib2
        fib1 = fib2
        fib2 = fibtemp
        yield fib2
