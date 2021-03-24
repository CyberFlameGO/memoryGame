import random

card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}

card_list_values = list(card_kv_store.values())
random.shuffle(card_list_values)
print("1 * * * *\n"
      "2 * * * *\n"
      "3 * * * *\n"
      "4 * * * *\n"
      "\u2588 A B C D")
