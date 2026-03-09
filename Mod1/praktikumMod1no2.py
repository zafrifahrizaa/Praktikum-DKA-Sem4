def fibonacci_ke_n(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    a, b = 1, 1
    for i in range(3, n+1):
        a, b = b, a+b
    return b

def cetak_fibonacci(n: int) -> None:
    if n <= 0:
        print(" ")
        return
    
    a, b = 1, 1

    for i in range(1, n+1):
        if i == 1 or i == 2:
            print(1, end=" ")
        else:
            a, b = b, a +b
            print(b, end=" ")
    print()

n = int(input("Masukkan nilai n: "))

hasil = fibonacci_ke_n(n)
print("fibonacci ke ", n, "adalah ", hasil)

print("deret fibonacci dari 1 -", n , ":")
cetak_fibonacci(n)