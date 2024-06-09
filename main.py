import random

def main():
    find_random_username()
    find_random_password()

def find_random_username():
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
    print(random_username)

def find_random_password():
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
    
    print(random_password)


if __name__ == "__main__":
    main()