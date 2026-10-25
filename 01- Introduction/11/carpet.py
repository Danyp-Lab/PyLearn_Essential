from termcolor import colored


def generate_rug(n):
    rug = [[" "] * n for _ in range(n)]
    num = n // 2
    color_num = 0
    colors = [
        "black",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
        "grey",
        "orange",
        "pink",
    ]

    for i in range(num + 1):
        for j in range(i, n - i):
            rug[i][j] = colored("■", colors[color_num])
            rug[n - 1 - i][j] = colored("■", colors[color_num])
            rug[j][i] = colored("■", colors[color_num])
            rug[j][n - 1 - i] = colored("■", colors[color_num])

        if color_num < len(colors) - 1:
            color_num += 1
        else:
            color_num = 0

    return rug


def main():
    try:
        n = int(input("Enter an odd number to create a rug: "))
        if n % 2 == 0:
            print("Please enter an odd number.")
        else:
            rug = generate_rug(n)
            for row in rug:
                for col in row:
                    print(col, end=" ")
                print()
    except ValueError:
        print("You must enter an integer number!")


if __name__ == "__main__":
    main()
