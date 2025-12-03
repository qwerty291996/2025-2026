#     1-topshiriq

def yosh_turi(yosh):
    if yosh < 7:
        return "Bog‘cha"
    elif 7 <= yosh <= 17:
        return "Maktab o‘quvchisi"
    else:
        return "Katta yoshdagilar"
yosh = int(input())
print(yosh_turi(yosh))

#     2-topshiriq

def fibonachi(n):
    if n <= 0:
        return []

    fib = [0]
    if n == 1:
        return fib

    fib.append(1)

    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib
son = int(input())
print(fibonachi(son))