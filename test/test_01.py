import math

total = 1300
count = 6
a = math.floor(total / count)

print(a)

for i in range(count):
    if i == count - 1:
        print(total)
    else:
        print(a)
    total = total - a