digit_input = int(input('Please enter a four-digit number:'))

digit_1 = digit_input // 1000
digit_2 = (digit_input // 100) % 10
digit_3 = (digit_input % 100) // 10
digit_4 = digit_input % 10

print(digit_4, digit_3, digit_2, digit_1)


