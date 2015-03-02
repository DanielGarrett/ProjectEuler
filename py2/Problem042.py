import EulerRunner
import itertools

wordFile = open('../data/Problem42_words.txt', 'r')
words = wordFile.readlines()[0].replace('"','').split(',')

def prob42iter():
    count = 0
    wordValues = []
    for word in words:
        value = 0
        for letter in word:
            value += ord(letter) - 64
        wordValues.append(value)
    triangles = list(itertools.takewhile(lambda x: x < max(wordValues), EulerRunner.triangle_generator()))
    print triangles
    return len(filter(lambda x: x in triangles, wordValues))

EulerRunner.solve_problem(prob42iter)
