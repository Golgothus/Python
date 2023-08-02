#! /usr/bin/python3

# inventory = {'torch':'1','rope':'0','rations':'3'}
# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inv = {"gold coin": 42, "rope": 1, "torch": 15, "rations": 3}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def display_inventory(inventory):
    itemCount = 0

    for k, v in inventory.items():
        print(f"{v} {k}")
        itemCount += int(v)

    print(f"Total number of items: {itemCount}")


def add_to_inventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory:
            inventory[k] = 1
        else:
            inventory[k] += 1


add_to_inventory(inv, dragonLoot)
display_inventory(inv)
