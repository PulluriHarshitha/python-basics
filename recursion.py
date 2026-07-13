#recursion 1 to n numbers
def print_numbers(n, i=1):
    if i > n:
        return
    print(i)
    print_numbers(n, i + 1)
n = int(input())
print_numbers(n)