# coding=utf-8  # ^ encoding requested by my IDE
"""Matching game"""  # doctype requested by my IDE
# imports for the project
import random
import time


# a function to clear x amount of lines after a specified period of time (in seconds)


def clear_py_console(sec, lines) -> object:
    """
# doctype recommended by my ide
    :param sec: int
    :param lines: int
    """
    time.sleep(sec)  # sleeps for a period of time specified when the function is called
    print("\n" * lines)  # sends a newline * specified amount (effectively clearing the console)


# Dictionary which stores all the values to be used in the game
card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}
# dictionary to translate all possible plot-points to numbers
plot_number_translation = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "b1": 5, "b2": 6, "b3": 7, "b4": 8, "c1": 9, "c2": 10,
                           "c3": 11, "c4": 12, "d1": 13, "d2": 14, "d3": 15, "d4": 16}
# row letters which are valid in input
valid_rows: list[str] = ["a", "b", "c", "d"]
# win counter (starting at 0)
wins = 0
# main while loop variable
playing = True

# prints board layout to introduce the user to the game
print("Welcome to a game of Memory Game!\nThis is what the board looks like!\n\n"
      "A * * * *\n"
      "B * * * *\n"
      "C * * * *\n"
      "D * * * *\n"
      "\u2588",
      1, 2, 3, 4,
      "\nYou choose a position by its line (row) number and column letter, kinda like in Chess! I hope you enjoy!\n\n")

# loop for the game
while playing:
    # turns the dict into a list
    card_list_values = list(card_kv_store.values())
    # shuffles said list
    random.shuffle(card_list_values)
    # turns all keys into asterisks
    card_kv_store = card_kv_store.fromkeys(card_kv_store, "*")
    # boolean variables for use in 'while' loops
    round_in_progress: bool = True
    error_catching: bool = True
    plotting: bool = True
    identical_plot: bool = True

    # code for each round
    while round_in_progress:
        # prints out the current "board"
        print("A {} {} {} {}\n"
              "B {} {} {} {}\n"
              "C {} {} {} {}\n"
              "D {} {} {} {}\n"
              "\u2588".format(card_kv_store.get(1), card_kv_store.get(2), card_kv_store.get(3), card_kv_store.get(4),
                              card_kv_store.get(5), card_kv_store.get(6), card_kv_store.get(7), card_kv_store.get(8),
                              card_kv_store.get(9), card_kv_store.get(10), card_kv_store.get(11), card_kv_store.get(12),
                              card_kv_store.get(13), card_kv_store.get(14), card_kv_store.get(15),
                              card_kv_store.get(16)),
              1, 2, 3, 4)
        # when the user plots a point (chooses rows and columns)
        while plotting:
            # catches errors (specifically catching integer ValueError)
            while error_catching:
                # asks the user for a row (this is just part of the loop of asking for a plot, invalid input is
                # caught later on
                row1 = input("Please choose a row.\n").strip().lower()
                try:
                    # asks the user for input as an integer (this seems redundant but it means i don't have a
                    # valid_columns list at the top, and allows for easier 'if' statement code
                    column1 = int(input("Please choose a column.\n").strip())
                    error_catching = False  # if there are no errors raised we proceed to the next part of the code
                # catches errors for incorrect datatype
                except ValueError:
                    print("Invalid input! Please use a round number.")  # tells the user they didn't type an integer
            error_catching = True  # changes the variable to True because the code is recycled later on
            # if the inputted rows and columns are valid
            if row1 in valid_rows and 1 <= column1 <= 4:
                # adds the variables into one "word" (the colon after the var-name is for annotation, which was a
                # suggestion from my IDE)
                pos1: str = row1 + str(column1)
                numeric_pos1 = plot_number_translation.get(pos1)  # translates the plotted point into a number
                # gets the shuffled number which corresponds with the translated number (adds a 1 to account for the
                # list starting at 0)
                match1 = card_list_values[numeric_pos1 + 1]
                plotting = False  # plotted position was in correct bounds so we escape the loop
            else:
                print("Invalid input, try again.")  # the user's input was out of bounds

        plotting = True  # beep boop, recycled variable

        while plotting:
            while error_catching:
                row2 = input("Choose a line.").strip().lower()
                try:
                    column2 = int(input("Choose a column.").strip())
                    error_catching = False  # change to error_catching
                except ValueError:
                    print("Invalid input! Please use a round number.")
            error_catching = True
            if row2 in valid_rows and 1 <= column2 <= 4:
                if row1 == row2 and column1 == column2:
                    print("Identical inputs are not allowed.")
                else:
                    pos2: str = row2 + (column2)  # adds the variables into one "word" (the colon after the var-name is
                    # for annotation, which was a suggestion from my IDE)
                    numeric_pos2 = plot_number_translation.get(pos2)  # translates the plotted point into a number
                    # int(numeric_pos2)  # this seems redundant so i'm commenting it out
                    match2 = card_list_values[numeric_pos2 + 1]
                    plotting = False  # plotted position was in correct bounds so we escape the loop
            else:
                print("Invalid input, try again.")
        plotting = True

        if match1 == match2:
            print("MATCH!")
            card_kv_store[numeric_pos1] = match1
            card_kv_store[numeric_pos2] = match2

        else:
            print(
                f"{pos2.title()} does not match {pos1.title()} unfortunately.\n{pos1.title()} is {match1} and "
                f"{pos2.title()} "
                f"is {match2} though!"
                "\n\nWe'll be hiding these values in 3 seconds, so memorize up!")

            clear_py_console(3, 1000)

        if "*" not in card_kv_store.values():
            round_in_progress = False
            # TODO: potentially add a stopwatch
            wins += 1
            print("Looks like you paired up all the numbers!\n"
                  "A {} {} {} {}\n"
                  "B {} {} {} {}\n"
                  "C {} {} {} {}\n"
                  "D {} {} {} {}\n"
                  "\u2588".format(card_kv_store.get(1), card_kv_store.get(2), card_kv_store.get(3),
                                  card_kv_store.get(4),
                                  card_kv_store.get(5), card_kv_store.get(6), card_kv_store.get(7),
                                  card_kv_store.get(8),
                                  card_kv_store.get(9), card_kv_store.get(10), card_kv_store.get(11),
                                  card_kv_store.get(12),
                                  card_kv_store.get(13), card_kv_store.get(14), card_kv_store.get(15),
                                  card_kv_store.get(16)),
                  1, 2, 3, 4)
            round_end = input(
                "Well done! Game completed, would you like to play another round?\nType 'y' to play another round, "
                "or anything else to finish this session.\nInput: ").lower().strip()
            if round_end == "y":
                print("Alright! Next round incoming. . .")
            else:
                print("Your wins this session:", wins)
                playing = False
