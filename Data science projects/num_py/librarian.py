def librarian():
   x = []

   for i in range (5):
       y = input("write your authors: ")
       z = y.split()
       print(z)
       x.append(z[0])


   x.sort()
   return(x)


print(librarian())

