def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))
