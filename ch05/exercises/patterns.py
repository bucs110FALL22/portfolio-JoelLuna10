def star_pyramid():
  a = 0
  number = int(input("Type number of star rows: "))
  for i in range(number):
    a += 1
    print("*" * a)

def rstar_pyramid():
  number = int(input("Type number of star rows: "))
  a = number
  for i in range(number):
    print("*" * a)
    a -= 1

star_pyramid()
rstar_pyramid()

