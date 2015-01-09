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

#not a partularly useful generator (keeps things in memory), but making a memory tradeoff for time
def prime_generator():
    primes = []
    current = 2
    while True:
        prime_index = 0
        is_prime = True
        while len(primes) > prime_index and primes[prime_index] ^ 2 <= current:
            if current % primes[prime_index] == 0:
                is_prime = False

                break
            prime_index += 1
        if is_prime:
            primes.append(current)
            yield current
        current += 1
