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

    current_line_number = 0

    alice_file = open("AliceInWonderLand200.txt")

    for line in alice_file:
        current_line_number += 1
        word_list = split_line(line)
        for word in word_list:
            current_list_position = 0
            while current_list_position < len(dictionary_list) and word.upper() != dictionary_list[current_list_position]:
                current_list_position += 1

            if current_list_position >= len(dictionary_list):
                print(word, current_line_number)

    alice_file.close()

    print("--- Binary Search ---")

    alice_file = open("AliceInWonderLand200.txt")

    current_line_number = 0

    for line in alice_file:
        current_line_number += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print(word, current_line_number)

    alice_file.close()

    # print(misspelled_list)


if __name__ == "__main__":
    main()
