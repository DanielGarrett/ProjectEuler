import EulerRunner

def problem48func():
    return str(sum(x**x for x in range(1,1001)))[-10:]
        
EulerRunner.solve_problem(problem48func)
