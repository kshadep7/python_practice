def twoSum(numbers, target):
    i, j = 0, len(numbers)-1

    while(i < j):
        if (numbers[i] + numbers[j]) == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1

    return [-1, -1]


numbers = [2,7,11,15]
print(twoSum(numbers, 9))