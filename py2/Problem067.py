import EulerRunner

numFile = open('../data/Problem067_numbers.txt', 'r')
nums = [[int(num) for num in line.split(' ')] for line in numFile.readlines()]
print len(nums)
print len(nums[-1])

def problem67_dp():
    totals = []
    for x in range(len(nums)):
        totals.append([])
        for y in range(len(nums[x])):
            totals[x].append(0)

    print len(totals)
    print len(totals[-1])
    
    totals[0][0] = nums[0][0]
    for x in range(len(nums)-1):
        for y in range(len(nums[x])):
            totals[x+1][y] = max(nums[x+1][y] + totals[x][y], totals[x+1][y])
            totals[x+1][y+1] = nums[x+1][y+1] + totals[x][y]

    print totals[-1]
    return max(totals[-1])

EulerRunner.solve_problem(problem67_dp)
