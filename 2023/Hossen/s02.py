# input, print, int


##age = int(input("Enter your age: "))
##gender = input("Enter your gender ('Male', Fmale')")
##
##if age > 18 and gender == "Male":
##    print("You can be a soldier.")
##else:
##    print("You cann't be a soldier.")


# -----------------
width = int(input("Width: "))
height = int(input("Height: "))

if width < 0 or height < 0:
    print("Width or height cann't be less than or equal zero.")
else:
    area = width * height
    print("Area is", area)
# 0, 0.0 , "", '', [], (), {}
