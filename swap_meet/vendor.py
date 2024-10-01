class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item_to_remove):
        for item in self.inventory:
            if item == item_to_remove:
                self.inventory.remove(item_to_remove)
                return item_to_remove
        return False

    def get_by_id(self, id_num):
        for item in self.inventory:
            if item.id == id_num:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)
