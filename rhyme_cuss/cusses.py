from random import randint


PREFIX_FILE = "prefix.txt"
SUFFIX_FILE = "suffix.txt"
OUTPUT_FILE = "cusses.txt"
FIRST_WORDS = "သရေကြိုး တင်းအောင်ကိုင်"
LAST_WORDS = "မအလ မအလ"


def read_from_file(file_name):
    with open(file_name, "r") as input_file:
        lines = [line.rstrip('\n') for line in input_file]
    return lines


def write_to_file(file_name, output_list):
    with open(file_name, "w") as output_file:
        output_file.write("\n".join(output_list))


def get_random_word(lines):
    random_index = randint(0, len(lines) - 1)
    random_word = lines[random_index]
    return random_word


def decorate_with_special_words(output_set, first, last):
    output_set.remove(first)
    output_list = [first] + list(output_set)
    output_list.append(last)
    return output_list


def generate_word_list():
    prefixes = read_from_file(PREFIX_FILE)
    suffixes = read_from_file(SUFFIX_FILE)
    output_set = set()

    while len(output_set) < 100:
        combined = get_random_word(prefixes) + " " + get_random_word(suffixes)
        output_set.add(combined)

    output_list = decorate_with_special_words(output_set, FIRST_WORDS, LAST_WORDS)
    return output_list


def main():
    output_list = generate_word_list()
    write_to_file(OUTPUT_FILE, output_list)


if __name__ == '__main__':
    main()
