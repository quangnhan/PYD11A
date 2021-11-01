sum_number = 0
sum_1 = 0

for i in range(0, 1000):
    if(i%3 == 0 and i%3 == 5):
        sum_number =+ i 
    else:
        sum_1 =+ i

print(sum_number - sum_1)
