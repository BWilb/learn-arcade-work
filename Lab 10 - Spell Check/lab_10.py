import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():
    """Open of file into dictionary line"""
    dictionary_list = []
    dictionary_file = open("dictionary.txt")

    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)
    dictionary_file.close()

    print("----Linear Search----")
    alice_file = open("AliceInWonderLand200.txt")
    for index, story_line in enumerate(alice_file):
        word_list = split_line(story_line)
        for word in word_list:
            key = word.upper()
            current_pos = 0
            while current_pos < len(dictionary_list) and dictionary_list[current_pos] != key:
                current_pos += 1
                if current_pos == len(dictionary_list):
                    print(f"Line {index + 1} possible misspelled word: " + key)

    alice_file.close()

    print()
    print("----Binary Search----")
    alice_file = open("AliceInWonderLand200.txt")
    for index, story_line in enumerate(alice_file):
        word_list = split_line(story_line)
        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_position = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_position] < key and dictionary_list[middle_position] != key:
                    lower_bound = middle_position + 1
                elif dictionary_list[middle_position] > key and dictionary_list[middle_position] != key:
                    upper_bound = middle_position - 1
                else:
                    found = True
            if not found:
                print(f"Line {index + 1} possible misspelled word: " + key)

    alice_file.close()
main()