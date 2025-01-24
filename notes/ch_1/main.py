import string


def shift(k, xs): # assume xs list of ints
  return [(_ + k) % 26 for _ in xs]

def combine(zss):
  ret = []
  while len(zss[0]) != 0:
    for i in range(len(zss)):
      if len(zss[i]) != 0:
        ret.append(zss[i][0])
        print("zss: ", zss, "ret: ",ret)
        zss[i].pop(0)
    
  return ret

def main():
  p = "helloworld"
  key = "cat"

  p0 = list(ord(c) - ord('a') for c in p)
  print(p0)

  key0 = list(ord(c) - ord('a') for c in key)
  print(key0)

  y0 = p0[0::3]
  y1 = p0[1::3]
  y2 = p0[2::3]
  print(y0, y1, y2)
  z0 = shift(key0[0], y0)
  z1 = shift(key0[1], y1)
  z2 = shift(key0[2], y2)
  print(z0, z1, z2)
  
  z = list()
  z.append(z0)
  z.append(z1)
  z.append(z2)
  print(z)
  z = combine(z)
  print(z)

if __name__ == "__main__":
  main()