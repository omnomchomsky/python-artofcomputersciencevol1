def min(m, n):
    return m if (m < n) else n


def max(m, n):
    return m if (m > n) else n


#s1e3
def algorithm_f(m, n):
    r = max(m, n) % min(m, n)
    return min(m, n) if (r is 0) else algorithm_f(min(m, n), r)


def algorithm_e(m, n):
    r = m % n
    return n if (r is 0) else algorithm_e(n, r)

