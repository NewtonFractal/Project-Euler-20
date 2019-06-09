import math
import time
start = time.time()

def Factorial_Digit_Sum(y):
    factorial = list(str(math.factorial(100)))
    for x in factorial:
        y += int(x)
    print(y)

Factorial_Digit_Sum(0)
end = time.time()
print(end - start)