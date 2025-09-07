x = int(input())
y = int(input())

g = 1
for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        g = i

l = (x * y) // g

print(g)
print(l)
