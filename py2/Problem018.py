import EulerRunner

numFile = open('../data/Problem018_numbers.txt', 'r')
nums = [[int(num) for num in line.split(' ')] for line in numFile.readlines()]

def brute_recurse(row, column, total):
    if row == len(nums):
        return total
    total += nums[row][column]
    return max(brute_recurse(row+1, column, total),brute_recurse(row+1, column+1, total))

def problem18_brute():
    return brute_recurse(0, 0, 0)

def problem18_dp():
    totals = []
    for x in range(len(nums)):
        totals.append([])
        for y in range(len(nums[x])):
            totals[x].append(0)
    
    totals[0][0] = nums[0][0]
    for x in range(len(nums)-1):
        for y in range(len(nums[x])):
            totals[x+1][y] = max(nums[x+1][y] + totals[x][y], totals[x+1][y])
            totals[x+1][y+1] = nums[x+1][y+1] + totals[x][y]

    return max(totals[-1])

EulerRunner.solve_problem(problem18_brute)
EulerRunner.solve_problem(problem18_dp)
