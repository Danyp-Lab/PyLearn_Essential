# Not Finished
ArraySize = int(input("Array size :"))
UserArray = []
NotSort = False
for i in range(ArraySize):
    UserArray.append(int(input("Write number:")))

print("UserArray is:", UserArray)

for i in UserArray:
    for j in UserArray:
        if i > j:
            NotSort = True

if NotSort:
    print("its not Sort")
else:
    print("sort")
