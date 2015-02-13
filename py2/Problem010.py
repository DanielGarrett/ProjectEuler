import EulerRunner

def problem10iter():
    return sum(EulerRunner.prime_sieve(2000000))

EulerRunner.solve_problem(problem10iter)
