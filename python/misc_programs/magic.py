"""
Recently Oz has found a magical string consisting of single digit "1". After experimenting on the string, Oz found a weird magical property of the string that is whenever he touches the string then each digit "1" of string changed to digit "0" and each digit "0" of string changed to "01". Oz found this property interesting and immediately asked a question to RK : "How many 1's and 0's will be in the magical string if he touches the string M times ?"

Input :

The first line contains the number of test cases T . Each test case consists of a positive integer - M .

Output :

For each test case output two space-separated integers, number of 1's and number of 0's in the magical string if Oz touches the string M times.

Constraints :

1<= T <=20

1<= M <=90

SAMPLE INPUT
2
1
2
SAMPLE OUTPUT
0 1
1 1


HINT - IT becomes a fibonnaci
"""
def fib(n):
    a,b = 0,1
    for i in range(n-1):
      a,b = b,a+b
    return (a,b)

for _ in xrange(input()):
    m = input()
    a,s = fib(m) #a is number of 0 and s is number of 1
    print a,s
