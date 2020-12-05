#functions
def stairs():
    n = int(input("enter your number :"))
    for i in range(0,n):
        for j in range(0, i+1):
            print("* " , end="")
        print("\r")
        
def pyramid():
      n = int(input("enter your number :"))
      k = 2 * n - 2
      for i in range(0,n):
           for j in range(0,k):
               print(end=" ")
           k = k - 1
           for j in range(0, i+1):
                print("*", end=" ")
           print("\r")

def diamond():
     n=int(input("enter your number :"))
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print("\r")
     k = n - 2
     for i in range(n , -1, -1):
          for j in range(k , 0 , -1): 
               print(end=" ")
          k = k + 1
          for j in range(0 , i + 1):
                print("* ", end="")
          print("\r")

def hourglass():
    n=int(input("enter your number :"))
    k = n - 2
    for i in range(n, -1 , -1):
          for j in range(k , 0 , -1):
               print(end=" ")
          k = k + 1    
          for j in range(0, i+1):
               print("* " , end="")
          print("\r")
    k = 2 * n - 2
    for i in range(0,n):
          for j in range(0,k):
               print(end=" ")
          k = k - 1
          for j in range(0, i+1):
                print("*", end=" ")
          print("\r")
 

#program
while True:

    data = input("([s]stairs, [p]pyramid, [d]diamond, [h]hourglass, [e]exit): ")
    if data == "s":
        stairs()
    elif data == "d":
        diamond()
    elif data == "p":
        pyramid()
    elif data == "h":
        hourglass()    
    elif data == "e":
        input("press enter to exit")
        break
    elif data != ("s", "d", "p", "h", "e"):
        print("not a valid command please try again.")
        break
#program ends