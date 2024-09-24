
def calculate_lcm(N, M):
    factor1 = []
    factor2 = []
    multiple1 = []
    multiple2 = []

    # Finding factors of N
    for i in range(1, N + 1):
        if N % i == 0:
            factor1.append(i)

    # Finding factors of M
    for j in range(1, M + 1):
        if M % j == 0:
            factor2.append(j)

    # Finding first 25 multiples of N
    for k in range(1, 26):
        multiple1.append(N * k)

    # Finding first 25 multiples of M
    for l in range(1, 26):
        multiple2.append(M * l)

    # Finding common multiples
    common_multiple = set(multiple1) & set(multiple2)

    # LCM is the minimum of the common multiples
    LCM = min(common_multiple)
    return LCM


# Taking input from user or using default values
use_default = input("Do you want to use default values (N=4, M=6)? (yes/no): ").strip().lower()

if use_default == "no":
    N = int(input("Enter the first number: "))
    M = int(input("Enter the second number: "))
else:
    N = 4
    M = 6

lcm = calculate_lcm(N, M)
print(f"Least common multiple (LCM) of {N} and {M} is {lcm}")
