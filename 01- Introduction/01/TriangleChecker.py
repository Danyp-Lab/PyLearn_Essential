# Triangle Checker

FirstSide = int(input("Write First side of the triangle"))
SecondSide = int(input("Write Second side of the triangle"))
ThirdSide = int(input("Write Third side of the triangle"))

# check triable a side < sum of two side
if (
    FirstSide + SecondSide > ThirdSide
    and FirstSide + ThirdSide > SecondSide
    and SecondSide + ThirdSide > FirstSide
):
    print("The Triangle Drawable")

else:
    print("The Triangle Can't Draw")
