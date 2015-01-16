import EulerRunner

def sum_squares(top):
    return sum(x ** 2 for x in range(1, top+1))

def square_sum(top):
    return (top * (top + 1) / 2) ** 2

def problem6_func():
    return square_sum(100) - sum_squares(100)

EulerRunner.solve_problem(problem6_func)
    
