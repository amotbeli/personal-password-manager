import random

def main():
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

if __name__ == "__main__":
    main()