N = int(input("Enter any number: "))


def sum_to_n(N):
    sum = 0
    for i in range(1,N+1):
        sum += i
    print(f"Sum to {N} is {sum}")


sum_to_n(N)
