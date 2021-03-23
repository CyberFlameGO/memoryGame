import random

card_kv_store = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7,
                 16: 8}

card_list = list(card_kv_store.values())

random.shuffle(card_list)
print(card_list)
print(
    "{} {} {} {}\n{} {} {} {}\n{} {} {} {}\n{} {} {} {}".format(card_list[0], card_list[1], card_list[2], card_list[3],
                                                                card_list[4], card_list[5], card_list[6], card_list[7],
                                                                card_list[8], card_list[9], card_list[10],
                                                                card_list[11],
                                                                card_list[12], card_list[13], card_list[14],
                                                                card_list[15]))
