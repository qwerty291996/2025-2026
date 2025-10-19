import math
from functools import lru_cache

M = 2000000
is_prime = [True] * (M + 1)
primes = []
PI = [0] * (M + 1)

def precompute():
    global is_prime, primes, PI
    is_prime[0] = is_prime[1] = False
    for i in range(2, M + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, M + 1, i):
                is_prime[j] = False
    count = 0
    for i in range(1, M + 1):
        if is_prime[i]:
            count += 1
        PI[i] = count

precompute()

def icbrt(x):
    low, high = 1, x
    while low <= high:
        mid = (low + high) // 2
        mid3 = mid * mid * mid
        if mid3 <= x:
            low = mid + 1
        else:
            high = mid - 1
    return high

def phi(x, primes_list):
    V = []
    i = 1
    while i <= x:
        v = x // i
        V.append(v)
        i = x // v + 1
    V.sort()
    idx_map = {}
    for idx, v in enumerate(V):
        idx_map[v] = idx
    F = V.copy()
    for p in primes_list:
        for i in range(len(V) - 1, -1, -1):
            if V[i] < p * p:
                break
            j = V[i] // p
            idx = idx_map[j]
            F[i] -= F[idx]
    return F[idx_map[x]]

@lru_cache(maxsize=None)
def prime_pi(x):
    if x < M:
        return PI[x]
    a = prime_pi(icbrt(x))
    b = prime_pi(math.isqrt(x))
    primes_list = primes[:a]
    ph = phi(x, primes_list)
    result = ph + a - 1
    for i in range(a + 1, b + 1):
        p_i = primes[i]
        result -= (prime_pi(x // p_i) - (i - 1))
    return result

def main():
    n = int(input().strip())
    low, high = 2, 25000000000
    while low <= high:
        mid = (low + high) // 2
        if prime_pi(mid) < n:
            low = mid + 1
        else:
            high = mid - 1
    print(low)

if __name__ == '__main__':
    main()