import EulerRunner

def problem7iter():
    return EulerRunner.prime_sieve(1000000)[10000]

EulerRunner.solve_problem(problem7iter)
