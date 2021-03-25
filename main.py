# coding=utf-8
"""imports the random module"""
import random

card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}
plot_number_translation = {"a1": 1, "a2": 2, "a3": 3, "a4": 4, "b1": 5, "b2": 6, "b3": 7, "b4": 8, "c1": 9, "c2": 10,
                           "c3": 11, "c4": 12, "d1": 13, "d2": 14, "d3": 15, "d4": 16}
valid_rows = ["a", "b", "c", "d"]
valid_columns = ["1", "2", "3", "4"]


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
card_kv_store = card_kv_store.fromkeys(card_kv_store, "*")
row = input("Choose a line.").strip().lower()
column = str(input("Choose a column.").strip())
if (row in valid_rows) and (column in valid_columns):
    pos = row + column
    numeric_pos = plot_number_translation.get(pos)
    int(numeric_pos)
    card_kv_store[numeric_pos] = card_list_values[numeric_pos+1]


print("A {} {} {} {}\n"
      "B {} {} {} {}\n"
      "C {} {} {} {}\n"
      "D {} {} {} {}\n"
      "\u2588".format(card_kv_store.get(1), card_kv_store.get(2), card_kv_store.get(3), card_kv_store.get(4),
                      card_kv_store.get(5), card_kv_store.get(6), card_kv_store.get(7), card_kv_store.get(8),
                      card_kv_store.get(9), card_kv_store.get(10), card_kv_store.get(11), card_kv_store.get(12),
                      card_kv_store.get(13), card_kv_store.get(14), card_kv_store.get(15), card_kv_store.get(16)),
      1, 2, 3, 4)
