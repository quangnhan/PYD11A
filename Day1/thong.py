n = int(input("enter number: "))

for i in range(2, n - 1):
    if n % i == 0:
        print("It is NOT a prime number")
        break
else:
    print("prime number")
