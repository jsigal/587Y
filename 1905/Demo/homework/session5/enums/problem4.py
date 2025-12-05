# Problem 4: Inventory Item with Rarity
# •	Create an Enum: 
# Define an Enum called Rarity with members COMMON, UNCOMMON, RARE, EPIC, LEGENDARY, each with an associated integer value representing its rarity level (e.g., COMMON = 1, LEGENDARY = 5).
# •	Create a Class: 
# Define a class InventoryItem.
# •	It should have instance attributes name (string), description (string), and rarity (a Rarity member).
# •	Implement a method get_item_info() that returns a formatted string with the item's name, description, and rarity level.
# •	Implement a method is_higher_rarity(other_item) that takes another InventoryItem as an argument and returns True if the current item's rarity is higher than the other_item's rarity, False otherwise.


from enum import Enum


class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5


class InventoryItem:
    def __init__(self, name, description, rarity):
        """
        Initialize an inventory item.
        
        Args:
            name: The item's name (string)
            description: The item's description (string)
            rarity: A Rarity enum member
        """
        self.name = name
        self.description = description
        self.rarity = rarity
    
    def get_item_info(self):
        """Returns a formatted string with the item's name, description, and rarity level"""
        return f"Item: {self.name}\nDescription: {self.description}\nRarity: {self.rarity.name} (Level {self.rarity.value})"
    
    def is_higher_rarity(self, other_item):
        """
        Returns True if the current item's rarity is higher than the other_item's rarity, False otherwise.
        
        Args:
            other_item: Another InventoryItem instance to compare with
        """
        return self.rarity.value > other_item.rarity.value


# Test code
if __name__ == "__main__":
    # Create items with different rarities
    common_sword = InventoryItem("Iron Sword", "A basic iron sword", Rarity.COMMON)
    rare_staff = InventoryItem("Mystic Staff", "A powerful magical staff", Rarity.RARE)
    legendary_armor = InventoryItem("Dragon Scale Armor", "Armor forged from dragon scales", Rarity.LEGENDARY)
    epic_potion = InventoryItem("Elixir of Power", "A rare potion that increases strength", Rarity.EPIC)
    uncommon_shield = InventoryItem("Steel Shield", "A sturdy steel shield", Rarity.UNCOMMON)
    
    print("="*60)
    print("Inventory Items Information:")
    print("="*60)
    print("\n" + common_sword.get_item_info())
    print()
    print(rare_staff.get_item_info())
    print()
    print(legendary_armor.get_item_info())
    print()
    print(epic_potion.get_item_info())
    print()
    print(uncommon_shield.get_item_info())
    
    print("\n" + "="*60)
    print("Rarity Comparisons:")
    print("="*60)
    
    # Test rarity comparisons
    print(f"\nIs {rare_staff.name} higher rarity than {common_sword.name}? {rare_staff.is_higher_rarity(common_sword)}")
    print(f"Is {common_sword.name} higher rarity than {rare_staff.name}? {common_sword.is_higher_rarity(rare_staff)}")
    print(f"Is {legendary_armor.name} higher rarity than {epic_potion.name}? {legendary_armor.is_higher_rarity(epic_potion)}")
    print(f"Is {epic_potion.name} higher rarity than {legendary_armor.name}? {epic_potion.is_higher_rarity(legendary_armor)}")
    print(f"Is {uncommon_shield.name} higher rarity than {common_sword.name}? {uncommon_shield.is_higher_rarity(common_sword)}")
    print(f"Is {common_sword.name} higher rarity than {uncommon_shield.name}? {common_sword.is_higher_rarity(uncommon_shield)}")
    
    # Test edge case: same rarity
    common_knife = InventoryItem("Iron Knife", "A small iron knife", Rarity.COMMON)
    print(f"\nIs {common_sword.name} higher rarity than {common_knife.name} (same rarity)? {common_sword.is_higher_rarity(common_knife)}")
    
    print("\n" + "="*60)
    print("Rarity Hierarchy (from lowest to highest):")
    print("="*60)
    items = [common_sword, uncommon_shield, rare_staff, epic_potion, legendary_armor]
    sorted_items = sorted(items, key=lambda x: x.rarity.value)
    for item in sorted_items:
        print(f"{item.rarity.name}: {item.name}")

