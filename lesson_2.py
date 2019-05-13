  def squirrel(self, N):
    s = 1
    factorial = 1
    emerald = 0
    nf = 0
    for i in range(2, N+1):
        factorial *= i
    nf = factorial
    while nf != 0:
        nf = nf//10
        s *= 10
    emerald = factorial//(s / 10)