# Least common multiple(LCM)

# Get numbers
NumA = int(input("Number 1:"))
NumB = int(input("Number 2:"))

# init
MultA = []
MultB = []
LCM = 9999999
FoundLCM = False
# Find coefficients
for i in range(2, NumA):
    if NumA % i == 0:
        MultA.append(i)
for j in range(2, NumB):
    if NumB % j == 0:
        MultB.append(j)
print(MultA)
print(MultB)

# search between coefficients - LCM

for i in MultA:
    for j in MultB:
        if i == j:
            if i < LCM:
                LCM = i

if not LCM:
    print("Not Found")
else:
    print("LCM:", LCM)
