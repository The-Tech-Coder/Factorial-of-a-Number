def facto(N):
    if (N < 0):
        return 0
    elif (N == 0 or N == 1):
        return 1
    else:
        fact = 1
        for i in range(1, N+1):
            fact = fact * i
        return fact


num = int(input("Enter a number: "))
print("Factorial of", num, "is", facto(num))
