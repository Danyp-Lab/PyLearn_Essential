import os
import random

from clip import Clip
from documentary import Documentary
from film import Film
from media import *
from series import Series

Products = []
# get current path and add DB path to file_path
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "dataset.txt")


def choice(ch):
    actions = {
        1: add,
        2: edit,
        3: remove,
        4: lambda: show_info(input("Search: Enter your Media Name: ")),
        5: lambda: advanced_search(
            input("Please enter the minimum duration you want: "),
            input("Please enter the maximum duration you want: "),
        ),
        6: lambda: download(input("Download Trailer: Please enter media name ")),
        7: suggest_random_media,
        8: lambda: (write_to_database(), exit(0)),
    }
    action = actions.get(ch, lambda: (print("Invalid input, try again"), show_menu()))
    action()


def show_menu():
    options = [
        "Add",
        "Edit",
        "Remove",
        "Show Info",
        "Search by Time",
        "Download Trailer",
        "Suggest Media",
        "Exit",
    ]
    for i, option in enumerate(options, 1):
        print(f"{i}- {option}")


def read_from_database():
    # Mapping of media types to their respective classes and unique attributes
    type_to_class = {
        "film": {"class": Film, "attribute": "genre"},
        "series": {"class": Series, "attribute": "num_episodes"},
        "documentary": {"class": Documentary, "attribute": "topic"},
        "clip": {"class": Clip, "attribute": "category"},
    }

    # Open the database file and read each line
    with open(file_path) as file:
        for line in file:
            # Split the line into db_data and strip whitespace
            db_data = [data.strip() for data in line.split(",")]

            # Skip processing if the line is empty or malformed
            if not db_data or not db_data[0]:
                continue

            # Extract the object type and convert it to lowercase
            obj_type = db_data[0].lower()

            # Check if the object type is supported
            if obj_type in type_to_class:
                # Retrieve the class and unique attribute for the object type
                media_class = type_to_class[obj_type]["class"]
                unique_attribute = type_to_class[obj_type]["attribute"]

                # Create an object of the media class with the provided db_data
                media_object = media_class(
                    obj_type,
                    name=db_data[1],
                    director=db_data[2],
                    imdb_score=db_data[3],
                    url=db_data[4],
                    duration=db_data[5],
                    casts=db_data[6],
                    **{unique_attribute: db_data[7]},
                )

                # Add the created media object to the Products list
                Products.append(media_object)
            else:
                # Print an error message for unsupported media types
                print(f"Unsupported type: {obj_type}")


def add():
    # Prompt for the type of media product and validate input
    obj_type = input("Enter object type (film, series, documentary, clip): ").strip().lower()
    valid_types = {"film", "series", "documentary", "clip"}

    # Check if the entered media type is valid
    if obj_type not in valid_types:
        print(f"Unsupported type: {obj_type}")
        return

    # Mapping of media types to their respective classes and unique attributes
    type_to_class = {
        "film": {"class": Film, "attribute": "genre"},
        "series": {"class": Series, "attribute": "num_episodes"},
        "documentary": {"class": Documentary, "attribute": "topic"},
        "clip": {"class": Clip, "attribute": "category"},
    }

    # Collect common information for all media types
    name = input("Enter name: ")
    director = input("Enter director: ")
    imdb_score = input("Enter IMDB score: ")
    url = input("Enter URL: ")
    duration = input("Enter duration: ")
    casts = input("Enter casts (separated by &): ")

    # Retrieve the class and unique attribute for the entered media type
    media_info = type_to_class[obj_type]
    media_class = media_info["class"]
    unique_attribute = media_info["attribute"]

    # Prompt for the unique attribute of the media type
    additional_info = input(f"Enter {unique_attribute} information: ")

    # Create an instance of the media class with the collected information
    media_object = media_class(
        obj_type,
        name,
        director,
        imdb_score,
        url,
        duration,
        casts,
        **{unique_attribute: additional_info},
    )

    # Add the new media object to the global Products list
    Products.append(media_object)
    print("Item added successfully.")


def show_edit_menu():
    options = {
        "1": "edit name",
        "2": "edit director",
        "3": "edit IMDB score",
        "4": "edit URL",
        "5": "edit duration",
        "6": "edit Casts",
    }

    for number, action in options.items():
        print(f"{number}- {action}")


def edit():
    # Prompt for the name of the media product to edit
    name_to_edit = input("Enter the name of the media you want to edit: ").strip().lower()

    # Search for the media product by name
    for product in Products:
        if product.name.lower() == name_to_edit:
            # Display current information of the media product
            show_info(product.name)

            # Define the edit options based on the product type
            edit_options = {
                "1": ("name", "Enter new name: "),
                "2": ("director", "Enter new director: "),
                "3": ("imdb_score", "Enter new IMDB score: "),
                "4": ("url", "Enter new URL: "),
                "5": ("duration", "Enter new duration: "),
                "6": ("casts", "Enter new casts (separated by &): "),
            }

            # Add specific options for Film, Series, Documentary, and Clip
            if isinstance(product, Film):
                edit_options["7"] = ("genre", "Enter new genre: ")
            elif isinstance(product, Series):
                edit_options["7"] = ("num_episodes", "Enter new number of episodes: ")
            elif isinstance(product, Documentary):
                edit_options["7"] = ("topic", "Enter new topic: ")
            elif isinstance(product, Clip):
                edit_options["7"] = ("category", "Enter new category: ")

            # Show the edit menu and get user choice
            show_edit_menu()
            choice = input("Enter your choice: ")

            # Execute the chosen edit action
            if choice in edit_options:
                attribute, prompt = edit_options[choice]
                new_value = input(prompt)
                setattr(product, attribute, new_value)
                print(f"{attribute} updated successfully.")
            else:
                print("Invalid choice!")
            print("Product edited successfully!✔️")
            break
    else:
        print(f"No media product found with the name: {name_to_edit}")


def remove():
    # Prompt for the name of the media to remove
    media_name = input("Enter the name of the media to remove: ").strip().lower()

    # Attempt to find and remove the specified media
    for product in Products:
        if product.name.lower() == media_name:
            # Display information about the media before removal
            show_info(product.name)

            # Confirm with the user before deletion
            confirmation = input("⚠️ Are you sure you want to delete this media? (Y/n): ").lower()
            if confirmation == "y":
                Products.remove(product)
                print(f"Media '{product.name}' has been deleted successfully!✔️")
                return
            else:
                print("Deletion canceled.❌")
                return

    # Inform the user if the media was not found
    print(f"No media found with the name '{media_name}'.")


def show_info(media_name):
    # Find the media product by name
    for product in Products:
        if product.name.lower() == media_name.lower():
            # Display common information
            print(f"Name: {product.name}")
            print(f"Director: {product.director}")
            print(f"IMDB Score: {product.imdb_score}")
            print(f"URL: {product.url}")
            print(f"Duration: {product.duration} minutes")
            print("Casts:")
            for actor in product.casts.split("&"):
                print(f"- {actor.strip().title()}")

            # Display type-specific information
            if isinstance(product, Film):
                print("Type: Film")
                print(f"Genre: {product.genre}")
            elif isinstance(product, Series):
                print("Type: Series")
                print(f"Number of Episodes: {product.num_episodes}")
            elif isinstance(product, Documentary):
                print("Type: Documentary")
                print(f"Topic: {product.topic}")
            elif isinstance(product, Clip):
                print("Type: Clip")
                print(f"Category: {product.category}")

            return  # Exit after displaying information

    # If the loop completes without finding the media, print not found message
    print(f"Media with name '{media_name}' not found.")


def advanced_search(min_duration, max_duration):
    """
    Search for media products within a specified duration range.

    Parameters:
    min_duration (int): The minimum duration in minutes.
    max_duration (int): The maximum duration in minutes.
    """
    # Initialize a flag to track if any media is found
    is_media_found = False

    # Iterate over the Products list to find matching media
    for product in Products:
        if min_duration <= product.duration <= max_duration:
            is_media_found = True
            show_info(product.name)

    # If no media matches the criteria, inform the user
    if not is_media_found:
        print(f"No media found with duration between {min_duration} and {max_duration} minutes.")


def download(name):
    """
    Offer the user to download a media product by name if it's a film.

    Parameters:
    name (str): The name of the media product to download.
    """
    # Search for the media product by name
    for product in Products:
        if product.name.lower() == name.lower():
            show_info(name)
            user_choice = input("Do you want to download this movie? (y/N): ").strip().lower()

            # If the user confirms, check if the product is a Film and download
            if user_choice == "y":
                if isinstance(product, Film):
                    product.download()
                    print(f"'{name}' is now downloading.")
                else:
                    print("Error: Only films can be downloaded.")
            return  # Exit after handling the download request

    # If the media product is not found, inform the user
    print(f"Product with name '{name}' not found.")


def suggest_random_media():
    """
    Suggest a random media product from the Products list.
    """
    if Products:  # Ensure there is at least one product to suggest
        suggestion_index = random.randrange(len(Products))
        print(f"Suggested Media: {Products[suggestion_index].name}")
    else:
        print("No media products available to suggest.")


def write_to_database(file_path):
    """
    Write the details of all media products to a database file.

    Parameters:
    file_path (str): The path to the database file.
    """
    try:
        with open(file_path, "w") as db_file:
            for product in Products:
                # Prepare the data string based on the product type
                data = (
                    f"{product.type},{product.name},{product.director},"
                    f"{product.imdb_score},{product.url},{product.duration},{product.casts}"
                )

                # Add type-specific data
                if isinstance(product, Film):
                    data += f",{product.genre}"
                elif isinstance(product, Series):
                    data += f",{product.num_episodes}"
                elif isinstance(product, Documentary):
                    data += f",{product.topic}"
                elif isinstance(product, Clip):
                    data += f",{product.category}"
                else:
                    print(f"Unsupported product type: {type(product).__name__}")
                    continue  # Skip writing unsupported product types

                # Write the data to the file
                db_file.write(data + "\n")
    except OSError:
        print("An error occurred while writing to the database.")


# Example usage
print("Welcome to Py MediaClubStore")
# Assume read_from_database() is defined elsewhere and file_path is known
read_from_database()
print("Database loaded successfully!✔️")

while True:
    show_menu()
    choice(int(input("Enter your choice: ")))
    print("debug console")
