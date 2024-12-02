# import library for random number of index for secret word
import random
# import library for sleep function for splash screen
import time


# print the Welcome Screen
def splash_screen():
    """This function prints the Welcome screen.
         :type HANGMAN_ASCII_ART: str
         :type num2: int
         :return: None
         :rtype:
         """
    HANGMAN_ASCII_ART = """Welcome to the game Hangman !
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART)
    print("Max Tries:", 6)


# Python code to pick a word from a text file
def choose_word(file_path, index):
    """This function selects a word from a list of word in a text file using an index.
             :type file_path: str
             :type index: int
             :return: word_list[int]
             :rtype: str
             """
    # Open the file in read mode
    with open(file_path, "r") as words_file:
        # reading each line
        word_list = []
        for line in words_file:
            # reading each word
            for word in line.split():
                if word not in word_list:
                    # append the words to list
                    word_list.append(word)
        if len(word_list) == 1:
            return word_list[0]
        elif index > len(word_list):
            loop = index - len(word_list)

            return word_list[loop - 1]
        else:
            return word_list[index - 1]


def print_hangman(num_of_tries):
    """This function consists a dictionary which hangman level photos and print it.
                 :type num_of_tries: int
                 :return: print(HANGMAN_PHOTOS[num_of_tries])
                 :rtype: str
                 """
    HANGMAN_PHOTOS = {1: """    x-------x""", 2: """    x-------x
    |
    |
    |
    |
    |
""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |"""}
    return print(HANGMAN_PHOTOS[num_of_tries])


def show_hidden_word(secret_word, old_letters_guessed):
    """This function returns a string combined the letter guessed and old ones.
                     :type secret_word: str
                     :type old_letters_guessed: list
                     :return: display
                     :rtype: str
                     """
    display = ""

    for index, x in enumerate(secret_word):
        if index == len(secret_word) - 1:
            if x in old_letters_guessed:
                display += x
                return display
            else:
                display += "_"
                return display
        if x in old_letters_guessed:
            display += x
            display += " "
            # print(x, end="")
        else:
            display += "_ "
            # print("_", end="")
    return display


def check_valid_input(letter_guessed, old_letters_guessed):
    """This function check is the input is legal and was not guessed already.
                         :type letter_guessed: str
                         :type old_letters_guessed: list
                         :return: true or false
                         :rtype: bool
                         """
    x = len(letter_guessed)
    letter_guessed = letter_guessed.lower()
    if x > 1 or not (letter_guessed.isalpha()):
        return False
    elif letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """This function check is the input is legal using check_valid_input function
     and prints "X" and a list of guessed letters in case that the input is illegal.
                             :type letter_guessed: str
                             :type old_letters_guessed: list
                             :return: true or false
                             :rtype: bool
                             """
    x = len(letter_guessed)
    letter_guessed = letter_guessed.lower()
    if x > 1 or not (letter_guessed.isalpha()) or letter_guessed in old_letters_guessed:
        old_letters_guessed.sort()
        print("X")
        # print list items horizontally in for loop
        for item in old_letters_guessed:
            print(item, "->", end=' ')
            x -= 1
        return False
    else:
        old_letters_guessed.append(letter_guessed)

        return True


def check_win(secret_word, old_letters_guessed):
    """This function checks if the user guessed all the letters from the secret word.
                                 :type secret_word: str
                                 :type old_letters_guessed: list
                                 :return: true or false
                                 :rtype: bool
                                 """
    counter = 0
    for x in secret_word:
        if x in old_letters_guessed:
            counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False


def hangman():
    """This function is actually the running process of the game.
                                     :type word: str
                                     :type old_letters_guessed: list
                                     :return: None
                                     :rtype: bool
                                     """
    splash_screen()
    time.sleep(2)
    file_path = input("Enter a file path:")
    index = int(input("Enter index:"))
    secret_word = choose_word(file_path, index)
    MAX_TRIES = 6
    num_of_tries = 0
    old_letters = []

    while MAX_TRIES != num_of_tries:
        print("\n")
        # prints the first level photo of Hangman
        print_hangman(num_of_tries + 1)
        # prints the new stats of correct and un-guessed letters of the secret word
        print(show_hidden_word(secret_word, old_letters))
        # constantly checks if the user won
        if check_win(secret_word, old_letters):
            print("WIN")
            return

        x = input("Please enter a letter:")
        if not check_valid_input(x, old_letters):
            try_update_letter_guessed(x, old_letters)

        elif x not in secret_word:
            try_update_letter_guessed(x, old_letters)
            num_of_tries += 1
        else:
            # using the try_update_letter_guessed to add input to old letters list
            try_update_letter_guessed(x, old_letters)



    print("\n")
    print_hangman(num_of_tries + 1)
    print("LOSE")


def main():

    hangman()


if __name__ == "__main__":
    main()
