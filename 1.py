try:
  c = input("enter all numbers with a space in between").split(" ")
  d = 0
  for i in c:
    d+= int(i)
   print("sum = ",d)
except:
  print("an error occured")
