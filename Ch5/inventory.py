# https://github.com/Golgothus
# Chapter 5 - Dictionaries

backpack = {'health pots': 20, 'sword': '1', 'mana pots': 2, 'bow': 1}

def display(inventory):
    print('The player currently has these items - ')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v.get(inventory)
    return item_total

print('Total number of items: ' + str(backpack))