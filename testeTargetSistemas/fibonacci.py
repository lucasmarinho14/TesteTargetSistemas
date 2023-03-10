def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num or num == 0


num = int(input("Digite um número: "))

if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
