import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    """The main function"""
    dictionary_file = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    alice_file = open("AliceInWonderLand200.txt")

    for line in alice_file:
        word_list = split_line(line)
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(word_list) and word.upper() == dictionary_list:
                current_list_position += 1

            print(word)

    alice_file.close()

    # print(misspelled_list)


if __name__ == "__main__":
    main()
