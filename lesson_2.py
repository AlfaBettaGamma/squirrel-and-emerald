def squirrel(N):
  factorial = 1
  nf = 0
  if(N == 0 or N == 1):
    emerald = 1
    return emerald
  for i in range(2, N+1):
    factorial *= i
  emerald = factorial
  while emerald > 9:
    emerald //= 10
  return emerald