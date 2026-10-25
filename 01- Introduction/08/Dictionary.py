# bug : because use google text to voice , may freeze
# file.txt download from other git
import gtts


# Main function to handle user interactions
def main():
    while True:
        show_menu()
        try:
            user_input = int(input("Enter Number: "))
            # Translate English to Persian
            if user_input == 1:
                text = input("Please Enter Your Text: ")
                result = translate(text, "fa")
                print(result)
                save_voice_to_file(result)  # no farsi here - finglish
            # Translate Persian to English
            elif user_input == 2:
                text = input("Please Enter Your Text: ")
                result = translate(text, "en")
                print(result)
                save_voice_to_file(result)
            # Add a new word to the dictionary
            elif user_input == 3:
                en = input("Please Enter Your Word (en): ")
                fa = input("Please Enter Your Word (fa): ")
                add_word(en, fa)
            # Exit the program
            elif user_input == 4:
                exit()
            else:
                print("Invalid input. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to display the menu to the user
def show_menu():
    print("1_ Translate English to Persian".title())
    print("2_ Translate Persian to English".title())
    print("3_ Add New Word".title())
    print("4_ Exit".title())


# Function to read the data from the file and return a dictionary
def read_data():
    with open("file.txt") as file:
        data = file.read().split("\n")
    return dict(zip(data[::2], data[1::2]))


# Function to translate the text based on the provided language
def translate(text: str, to):
    dictionary = read_data()
    sentences = text.split(".")
    result = ""
    for sentence in sentences:
        words = sentence.split(" ")
        for word in words:
            word = word.strip()
            if word in [" ", "."]:
                continue
            result += dictionary.get(word, word) + " "
        result += "."
    return result


# Function to add a new word to the file
def add_word(en, fa):
    with open("file.txt", "a") as file:
        file.write(f"\n{en}\n{fa}")


# Function to save the voice to a file
def save_voice_to_file(text):
    voice = gtts.gTTS(text, lang="en", slow=False)
    voice.save("voice.mp3")


if __name__ == "__main__":
    main()
