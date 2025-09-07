x = int(input())

if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
    print(x, "is a Leap Year")
else:
    print(x, "is NOT a Leap Year")
