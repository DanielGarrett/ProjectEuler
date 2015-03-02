import EulerRunner

total = 0
def add_to_total(digits, number, string_so_far):
    global total
    total += int(str(digits[0]) + str(digits[1]) + string_so_far)
    total += int(str(digits[1]) + str(digits[0]) + string_so_far)

def check_div_17(digits, number, string_so_far):
    remain = (number * -10) % 17
    for x in (set([remain]) & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        add_to_total(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_13(digits, number, string_so_far):
    remain = (number * -10) % 13
    for x in (set([remain]) & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        check_div_17(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_11(digits, number, string_so_far):
    remain = (number * -10) % 11
    for x in (set([remain]) & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        check_div_13(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_7(digits, number, string_so_far):
    sevens = [set([0,7]), set([6]), set([5]), set([4]), set([3]), set([2,9]), set([1,8])]
    for x in (sevens[(number * 10) % 7] & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        check_div_11(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_5(digits, number, string_so_far):
    fives = set([0,5])
    for x in (fives & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        check_div_7(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_3(digits, number, string_so_far):
    trips = [set([0,3,6,9]), set([2,5,8]), set([1,4,7])]
    for x in (trips[number % 3] & set(digits)):
        digits.remove(x)
        new_number = (number * 10 + x) % 100
        new_string_so_far = string_so_far + str(x)
        check_div_5(digits, new_number, new_string_so_far)
        digits.append(x)

def check_div_2(digits, number, string_so_far):
    evens = set([0,2,4,6,8])
    for x in (evens & set(digits)):
        digits.remove(x)
        new_number = number * 10 + x
        new_string_so_far = string_so_far + str(x)
        check_div_3(digits, new_number, new_string_so_far)
        digits.append(x)
    

def problem43_iter():
    global total
    digits = [x for x in range(10)]
    for x in digits[:]:
        digits.remove(x)
        number = x
        string_so_far = str(x)
        check_div_2(digits, number, string_so_far)
        digits.append(x)
    return total
        
EulerRunner.solve_problem(problem43_iter)

