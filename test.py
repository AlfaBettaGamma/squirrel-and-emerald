import random
class my_work:
  def squirrel(self, N):
    factorial = 1
    nf = 0
    if(N == 0 or N == 1):
      emerald = 1
      return emerald
    for i in range(2, N+1):
      factorial *= i
    emerald = factorial
    while emerald > 10:
      emerald //= 10
    return emerald

class my_test:
  def test1(self):
    test = my_work()
    print(test.squirrel(0))

  def test2(self):
    test = my_work()
    print(test.squirrel(1))

  def test3(self):
    test = my_work()
    for i in range(10):
      y = random.randint(0,10)
      print(test.squirrel(y))

test = my_test()
test.test3()