"""Matching game"""
# coding=utf-8

import random
import time


def clear_py_console(sec, lines):
    """

    :param sec: int
    :param lines: int
    """
    time.sleep(sec)
    print("\n" * lines)


card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}
plot_number_translation = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "b1": 5, "b2": 6, "b3": 7, "b4": 8, "c1": 9, "c2": 10,
                           "c3": 11, "c4": 12, "d1": 13, "d2": 14, "d3": 15, "d4": 16}
valid_rows = ["a", "b", "c", "d"]
valid_columns = ["1", "2", "3", "4"]

playing = True

while playing:
    card_list_values = list(card_kv_store.values())
    random.shuffle(card_list_values)

    #    for val in range(len(card_kv_store)):
    #        card_kv_store[val] = card_list_values[val - 1]
    #        print(card_kv_store[val])

    print("A * * * *\n"
          "B * * * *\n"
          "C * * * *\n"
          "D * * * *\n"
          "\u2588",
          1, 2, 3, 4)
    card_kv_store = card_kv_store.fromkeys(card_kv_store, "*")

    row1 = input("Choose a line.").strip().lower()
    column1 = str(input("Choose a column.").strip())
    row2 = input("Choose a line.").strip().lower()
    column2 = str(input("Choose a column.").strip())
    if row1 in valid_rows and column1 in valid_columns:
        pos1 = row1 + column1
        numeric_pos1 = plot_number_translation.get(pos1)
        int(numeric_pos1)
        match1 = card_list_values[numeric_pos1 + 1]
        plot1 = False

    if row2 in valid_rows and column2 in valid_columns:
        pos2 = row2 + column2
        numeric_pos2 = plot_number_translation.get(pos2)
        int(numeric_pos2)
        match2 = card_list_values[numeric_pos2 + 1]

    if match1 == match2:
        print("MATCH!")
        card_kv_store[numeric_pos1] = match1
        card_kv_store[numeric_pos2] = match2
    else:
        print(
            f"{pos2.title()} does not match {pos1.title()} unfortunately.\n{pos1.title()} is {match1} and "
            f"{pos2.title()} "
            f"is {match2} though!")
    print("A {} {} {} {}\n"
          "B {} {} {} {}\n"
          "C {} {} {} {}\n"
          "D {} {} {} {}\n"
          "\u2588".format(card_kv_store.get(1), card_kv_store.get(2), card_kv_store.get(3), card_kv_store.get(4),
                          card_kv_store.get(5), card_kv_store.get(6), card_kv_store.get(7), card_kv_store.get(8),
                          card_kv_store.get(9), card_kv_store.get(10), card_kv_store.get(11), card_kv_store.get(12),
                          card_kv_store.get(13), card_kv_store.get(14), card_kv_store.get(15), card_kv_store.get(16)),
          1, 2, 3, 4)
    if "*" not in card_kv_store:
        print("Well done! Game completed, would you like to play another round?")
