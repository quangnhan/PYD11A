sum = 0
for i in range(1, 1000, 2):
    sum += i
print(sum)


sum_divide_3_5 = 0
tổng_còn_lại = 0
for i in range(1, 1000):
    if i % 3 == 0 and i % 5 == 0:
        sum_divide_3_5 += i
    else:
        tổng_còn_lại += i


print(sum_divide_3_5)
print(tổng_còn_lại)
print(sum_divide_3_5 - tổng_còn_lại)
