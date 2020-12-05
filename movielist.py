#functions    
def addMovie():
    print("adding a movie")
    print()
            
def deleteMovie():
    print("deleting a movie")
    print()
            
def listMovies():
    print("listing all movies")
    print()

while True:
    data = input("([a]add movie, [d]delete movie, [l]list movies, [e]exit): ")
    if data == "a":
        addMovie()
    elif data == "d":
        deleteMovie()
    elif data == "l":
        listMovies()
    elif data == "e":
        input("press enter to exit")
        break
    elif data != ("a", "d", "l", "e"):
        print("not a valid command please try again.")
        break
#program ends