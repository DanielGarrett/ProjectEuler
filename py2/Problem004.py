import EulerRunner

#only accepts strings
def is_palindrome(value):
    return (len(value) < 2) or (value[0] == value[-1] and is_palindrome(value[1:-1]))


def problem4_iter():
    max_num = 0
    for x in range(999, 99, -1):
        for y in range(0, 999-x):
            z = (x+y) * (999-y)
            if z > max_num and is_palindrome(str(z)):
                max_num = z
        if max_num > 0:
            return max_num

def problem4_func()

EulerRunner.solve_problem(problem4_iter)
