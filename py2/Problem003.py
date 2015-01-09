import EulerRunner

def problem3_iter():
    to_factor = 600851475143
    gen = EulerRunner.prime_generator()
    current_prime = None
    while to_factor > 1:
        current_prime = gen.next()
        while to_factor % current_prime == 0:
            to_factor /= current_prime
    return current_prime



EulerRunner.solve_problem(problem3_iter)
