a = b = 0
c = ["Fuzz","Buzz"]
for num in range(1,101):
  if (num % 3) == 0 :
    a  = 1
  if (num % 5) == 0 :
    b = 1 
  if (a == 0 and b == 0):
    print(num)
  else:
    print(f"{a * c[0]}{b * c[1]}")   
    a = b = 0
