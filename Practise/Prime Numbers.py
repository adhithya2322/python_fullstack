count = 0

print("Prime numbers between 1 and 100:")

for n in range(2, 101):
    factors = 0

    for i in range(1, n + 1):
        if n % i == 0:
            factors += 1

    if factors == 2:
        print(n)
        count += 1

print("Total prime numbers:", count)