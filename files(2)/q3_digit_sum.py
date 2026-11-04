def digit_sum(number):
    # Base case: a single digit is its own sum
    if number < 10:
        return number
    # Recursive case: last digit + sum of the remaining digits
    digit = number % 10
    return digit + digit_sum(number // 10)


for n in (5824, 7, 0, 1000, 99999):
    print(f"digit_sum({n}) =", digit_sum(n))
