# without using Time lib
# h = 60 min = 3600 s
# // div + round down
# % remaining
hh = 0
UserSecondInput = int(input("Please write second"))
hh = int(UserSecondInput // 3600)
mm = int((UserSecondInput % 3600) // 60)
ss = int((UserSecondInput % 3600) % 60)

print(
    "you Write:",
    UserSecondInput,
    "Seconds\n",
    "Converted to format hh:mm:ss is \n",
    "⏲️",
    hh,
    ":",
    mm,
    ":",
    ss,
)
