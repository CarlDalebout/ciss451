
a, b = 5, 10
c, d = 21, 24

def E(x):
  return (a * x + b) % 26

def D(x):
  return (c * x + d) % 26

if __name__ == "__main__":
  for x in range(26):
    print(x, E(x), D(E(x)))