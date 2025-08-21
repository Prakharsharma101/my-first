N = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(abs(N)))
print("Sum of digits:", digit_sum)
