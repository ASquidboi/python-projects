arr = input("Input list seperated by spaces. Numbers only:").split()

x = 0
changes = 0

while True:
  
  try:
    a = arr[x]
    b = arr[x + 1]
    #print(a,b,x)
   
  except:
    x = 0
    a = arr[x]
    b = arr[x + 1]
  
  
  
  if a > b:
    arr[x] = b
    arr[x + 1] = a
  print(arr)
  x = x + 1
  
