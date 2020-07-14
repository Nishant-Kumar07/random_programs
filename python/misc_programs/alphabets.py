import string

number = input()


alpha = string.ascii_lowercase

alpha_len = len(alpha)

if number <=26:
    print alpha[number]
else:
    quotient = number/alpha_len
    remainder = number % alpha_len
    print alpha[remainder-1]*quotient + str(alpha[remainder-1])
