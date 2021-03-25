# coding=utf-8
"""imports the random module"""
import random

card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}

valid_rows = ["a", "b", "c", "d"]
valid_columns = [1, 2, 3, 4]

card_list_values = list(card_kv_store.values())
random.shuffle(card_list_values)

for val in range(len(card_kv_store)):
    card_kv_store[val] = card_list_values[val - 1]

print("A * * * *\n"
      "B * * * *\n"
      "C * * * *\n"
      "D * * * *\n"
      "\u2588",
      1, 2, 3, 4)

row = input("Choose a line.").strip().lower()
column = int(input("Choose a column.").strip())
# if row in valid_rows and column in valid_columns:


print("A {:.fdict.get[1]} {} {} {}\n"
      "B {} {} {} {}\n"
      "C {} {} {} {}\n"
      "D {} {} {} {}\n"
      "\u2588",
      1, 2, 3, 4)
