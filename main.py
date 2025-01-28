def main():
    file_content = read_file("./books/frankenstein.txt")
    # word count
    words_count = count_words(file_content)

    # character count
    characters_count = count_characters(file_content)
    sorted_characters = sort_characters(characters_count)

    print(f"{words_count} words found in the document\n")

    for sorted in sorted_characters:
        char = sorted[0]
        count = sorted[1]

        print(f"The '{char}' character was found {count} times")


def read_file(file_path):
    file_contents = None

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def count_words(file_contents):
    return len(file_contents.split())


def count_characters(file_contents):
    characters = {}

    for c in file_contents:
        char = c.lower()
        if char.isalpha() == False:
            continue

        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


def sort_characters(characters):
    return sorted(characters.items(), key=lambda x: x[1], reverse=True)


main()
