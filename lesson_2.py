  def squirrel(self, N):
    s = 1
    factorial = 1
    emerald = 0
    nf = 0
    if(N == 0 or N == 1):
        emerald = 1
        return emerald
    for i in range(2, N+1):
        factorial *= i
    nf = factorial
    while nf != 0:
        nf = nf//10
        s *= 10
    emerald = int(factorial//(s / 10))
    return (emerald)