def is_prime(x):
  if x < 2:
     return False
  for i in range(2,x):
    if x % i == 0:
      return False
  else:
    return True

x = raw_input("Please enter a number: ")
if is_prime(int(x)):
  print x, "is a prime number"
else:
  print x, "is not a prime number"
