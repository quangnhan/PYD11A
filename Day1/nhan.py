# Bai 1
sum = 0
for i in range(1, 10000, 2):
    sum += i
print(sum)

sum = 0
for i in range(0, 10000):
    if i%2 == 1:
        sum += i
print(sum)
