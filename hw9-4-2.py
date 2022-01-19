# Author RTS 1/17/22

from itertools import product


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
value = 10
def answers(lst, value):
    answer = []
    for num in lst:
        answer += [num * value]
    print(answer)
product(numbers, value)
