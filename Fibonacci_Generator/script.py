#Chang the rang of fibonacci sequence by changing th loop rang on lin 16.



def fibonacci():
  a = 0
  b = 1
  while True:
    yield a
    a, b = b, a + b

# Generate an infinite sequence of Fibonacci numbers
fibonacci_sequence = fibonacci()

# Print the first 10 Fibonacci numbers
for i in range(10):
  print(next(fibonacci_sequence))
