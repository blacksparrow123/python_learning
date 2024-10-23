def calculateSum(numbers):
    if numbers == []:
        return 0
    else:
        sum = 0
        for number in numbers:
            sum += number
    return sum

def calculateProduct(numbers):
    if numbers == []:
        return 1
    else:
        product = 1
        for number in numbers:
            product *= number
    return product