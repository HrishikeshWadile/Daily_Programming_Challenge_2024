def find_prime_factors(num):
    prime_factors = []

    # Divide by 2 until num is odd
    while num % 2 == 0:
        prime_factors.append(2)
        num //= 2

    # Check for odd factors from 3 to sqrt(num)
    for i in range(3, int(num ** 0.5) + 1, 2):
        while num % i == 0:
            prime_factors.append(i)
            num //= i

    # If num is still greater than 2, then it is prime
    if num > 2:
        prime_factors.append(num)

    return prime_factors


# Taking input from user or using default values
use_default = input("Do you want to use default value 18? (y/n): ").strip().lower()

if use_default == "n":
    n = int(input("Enter the number you want to find prime factors of: "))
    print(find_prime_factors(n))
else:
    print(find_prime_factors(18))
