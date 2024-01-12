#David Johnson 4-17-2020

#function to convert miles to kilometers
def miTOkm(mi):
    km = float(mi * 1.609)
    return km

#while loop to accept user input until valid
while True:
    try:
        mi = float(input("Enter miles: "))
        break
    except:
        print("Invalid input, please try again...")

print("Total miles: ", mi)
print("Total kilometers: ", miTOkm(mi))

