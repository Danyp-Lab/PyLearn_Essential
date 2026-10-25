# reverse list Without use Function
# init
SampleList = [1, 2, 3, 4, 5, 6]
ReverseList = []
# print
print(SampleList)

for i in SampleList:
    ReverseList.append(SampleList[-i])

print(ReverseList)
