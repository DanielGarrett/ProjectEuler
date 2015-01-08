#EulerRunner.py
import datetime
def solve_problem(solve_func):
    start = datetime.datetime.now()
    result = str(solve_func())
    end = datetime.datetime.now()
    print 'The answer is "' + result + '". Solved in ' + str((end - start).total_seconds()) + 's'

