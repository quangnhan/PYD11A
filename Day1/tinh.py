n = int(input())
prime_number = True
if (n < 2):
    prime_number = False
elif (n == 2):
    prime_number = True
elif (n % 2 == 0):
    prime_number = False
else:
    for i in range(3, n, 2):
        if (n % i == 0):
            prime_number = False
 
if prime_number == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")