import random
import json

def main():
    print("---")
    print("Personal Password Manager")
    print("---")
    print("Enter 1 to generate random login details.")
    print("Enter 2 to store your login details.")
    print("Enter 3 to recall your login details.")
    print("")
    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        generate_login_details()
    elif user_choice == "2":
        store_login_details()
    elif user_choice == "3":
        recall_login_details()
    else:
        print("Invalid input.")

# GENERATE LOGIN DETAILS

def generate_login_details():
    """
    - this function generates random username and password by calling relevant functions
    - and prints them for the user
    """
    random_username = find_random_username()
    random_password = find_random_password()

    print("---")
    print("Generate Login Details")
    print("---")
    print("Username: ", random_username)
    print("Password: ", random_password)
    print("")

def find_random_username():
    """
    - this funtion generates random username by combining a random adjective and a random noun
        - adjectives and nouns come from local text files 
    - and returns the random username
    """
    with open('adjectives.txt', 'r') as file:
        adjectives = file.readlines()
        adjectives = [adjective.strip() for adjective in adjectives]

    with open('nouns.txt', 'r') as file:
        nouns = file.readlines()
        nouns = [noun.strip() for noun in nouns]

    random.shuffle(adjectives)
    random.shuffle(nouns)

    adjective_index = random.randint(0, len(adjectives) - 1)
    noun_index = random.randint(0, len(nouns) - 1)

    random_username = adjectives[adjective_index] + "_" + nouns[noun_index]
    return random_username

def find_random_password():
    """
    - this function generates random password by combining uppercase and lowecase letters, numbers, and special characters
    - and returns the password
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '>', '.', '?', '/', '|', '`', '~']

    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(special_characters)

    random_password = ""
    password_length = 16

    for i in range(password_length):
        letters_index = random.randint(0, len(letters) - 1)
        numbers_index = random.randint(0, len(numbers) - 1)
        special_characters_index = random.randint(0, len(special_characters) - 1)

        if (i == letters_index):
            password_char = letters[letters_index].upper()
        elif (i == numbers_index):
            password_char = numbers[numbers_index]
        elif (i == special_characters_index):
            password_char = special_characters[special_characters_index]
        else:
            password_char = letters[letters_index]

        random_password += password_char
    
    return random_password

# STORE LOGIN DETAILS

def store_login_details():
    """
    - this function calls relevant functions to store user login details as nested dictionaries in a JSON file
        - gets user login details
        - appends user login details to the existing login details, if any
        - stores total login details in the JSON file again
    """
    existing_logins = read_logins()
    new_logins = get_logins()
    existing_logins.append(new_logins)

    with open('login_details.json', 'w') as file:
        # indent = 4 makes the json file formatting easier to read
        json.dump(existing_logins, file, indent = 4)

def read_logins():
    with open('login_details.json', 'r') as file:
        login_details = json.load(file)
        return login_details

def get_logins():
    login_details = {}

    while True:
        print("---")
        print("Store Login Details")
        print("---")
        website = input("Enter website name (or 'done' to finish): ")
        if website.lower() == "done":
            break
        username = input("Enter email/username: ")
        password = input("Enter password: ")

        if website not in login_details:
            login_details[website] = {}

        login_details[website][username] = password

    return login_details

# RECALL LOGIN DETAILS

def recall_login_details():
    """
    - this function recalls the stored user login details from the JSON file
    """
    found_website = False
    found_username = False

    with open('login_details.json', 'r') as file:
        existing_logins = json.load(file)

    print("---")
    print("Recall Login Details")
    print("---")
    website = input("Enter website name: ")

    for i in range(len(existing_logins)):
        if website in existing_logins[i]:
            found_website = True
            username = input("Enter username/email: ")
            if username in existing_logins[i][website]:
                found_username = True
                password = existing_logins[i][website][username]
                print("Password:", password)
                break

    if (found_website == False) or (found_username == False):
        print("No such login detail found.")

if __name__ == "__main__":
    main()