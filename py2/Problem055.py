import EulerRunner
def is_palindrome(value):
    return (len(value) < 2) or (value[0] == value[-1] and is_palindrome(value[1:-1]))

def number_reverse(number):
    return int(str(number)[::-1])

def is_lychrel(number, count = 50):
    return not is_palindrome(str(number + number_reverse(number))) and (count == 0  or is_lychrel(number + number_reverse(number), count - 1))

def problem55func():
    return len([0 for x in range(10001) if is_lychrel(x)])
        

EulerRunner.solve_problem(problem55func)
