def fahr_to_celi(fahr):
    celi  = (fahr - 32) * (5/9)
    return celi

while True:
    try:
        fahr = int(input("Enter fahrenheit: "))
        celi = fahr_to_celi(fahr)

        if celi > 87:
            print("Too hot.")
        elif celi < 82:
            print("Too cold.")
        else:
            print("The tempeture is now just right.")
            break
    except ValueError:
        print("Wrong number.")
        
    
    

