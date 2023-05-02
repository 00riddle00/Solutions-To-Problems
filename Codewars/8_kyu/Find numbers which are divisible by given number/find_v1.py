def divisible_by(numbers, divisor):
    if divisor == 1:
        return numbers

    if len(numbers) > 1 and numbers[1] - numbers[0] == 1:
        if numbers[0] == 0:
            return numbers[::divisor]
        else:
            return numbers[divisor-1::divisor]
    else:
        return [x for x in numbers if x % divisor == 0]
