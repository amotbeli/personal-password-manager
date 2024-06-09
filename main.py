def main():
    print("hello world")

    with open('adjectives.txt', 'r') as file:
        adjectives = file.readlines()
        adjectives = [adjective.strip() for adjective in adjectives]

    with open('nouns.txt', 'r') as file:
        nouns = file.readlines()
        nouns = [noun.strip() for noun in nouns]

    print(adjectives)
    print(nouns)

if __name__ == "__main__":
    main()