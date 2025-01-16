
def main():
    
  x = list()
  for i in range(135246):
    i3 = i**3
    i2 = i**2

    value = i3 + 425*i2 + 79*i + 42 
    if value % 135246 == 0:
      print("found one i:", i)
      x.append(i)
    with open("test.txt", "a") as f:
      print(value % 135246, file=f)
      f.close()  

  print(x)


if __name__ == "__main__":
  print("test")
  main()