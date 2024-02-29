english_alphabet_letters_num = 26
possible_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_in_the_word = []
unknown_cells = 5


def count_colors():
    count = {'S': 0, 'N': 0, 'Z': 0}
    for j in range(int(input())):
        word = input()
        colors = input()
        for i, color in enumerate(colors):
            if word[i] in possible_letters:
                if color == 'Z':
                    count['Z'] += 1
                    if word[i] in letters_in_the_word:
                        letters_in_the_word.pop(letters_in_the_word.index(word[i]))
                elif color == 'N':
                    letters_in_the_word.append(word[i])
                    count['N'] += 1
                else:
                    count['S'] += 1
                    possible_letters.pop(possible_letters.index(word[i]))
    return count
