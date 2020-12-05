print("enter 'exit' to end program.\n")
while True:
    data = input("enter integer  :")
    sc_data = input("do you want to square it or cube it ? (s/c) :")
    if data == "exit":
        input("press enter to end")
        break
    i = int(data)
    if sc_data == "s":
        print(i, "squared is", i **2, "\n")
    elif sc_data == "c":
        print(i, "cubed is", i **3, "\n")

    
    
