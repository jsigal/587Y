# Problem 3: Character Stats in a Game
# •	Create an Enum: 
# Define an Enum called CharacterClass with members like WARRIOR, MAGE, ARCHER, ROGUE.
# •	Create a Class: 
# Define a class GameCharacter.
# •	It should have instance attributes name (string), health (integer), attack_power (integer), and character_class (an CharacterClass member).
# •	The constructor should take name, character_class, and optionally health and attack_power (with default values).
# •	Implement a method take_damage(damage_amount) that reduces the character's health.
# •	Implement a method attack(other_character) that reduces the other_character's health by the current character's attack_power.
# •	Implement a method display_stats() that prints the character's name, class, health, and attack power.

from enum import Enum


class CharacterClass(Enum):
    WARRIOR = "WARRIOR"
    MAGE = "MAGE"
    ARCHER = "ARCHER"
    ROGUE = "ROGUE"


class GameCharacter:
    def __init__(self, name, character_class, health=100, attack_power=10):
        """
        Initialize a game character.
        
        Args:
            name: The character's name (string)
            character_class: A CharacterClass enum member
            health: The character's health points (default: 100)
            attack_power: The character's attack power (default: 10)
        """
        self.name = name
        self.character_class = character_class
        self.health = health
        self.attack_power = attack_power
    
    def take_damage(self, damage_amount):
        """Reduces the character's health by the damage amount"""
        self.health -= damage_amount
        if self.health < 0:
            self.health = 0
    
    def attack(self, other_character):
        """Attacks another character, reducing their health by this character's attack_power"""
        other_character.take_damage(self.attack_power)
    
    def display_stats(self):
        """Prints the character's name, class, health, and attack power"""
        print(f"Name: {self.name}")
        print(f"Class: {self.character_class.value}")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")


# Test code
if __name__ == "__main__":
    # Create characters with different classes
    warrior = GameCharacter("Conan", CharacterClass.WARRIOR, health=150, attack_power=20)
    mage = GameCharacter("Gandalf", CharacterClass.MAGE, health=80, attack_power=25)
    archer = GameCharacter("Legolas", CharacterClass.ARCHER, health=100, attack_power=15)
    rogue = GameCharacter("Shadow", CharacterClass.ROGUE)
    
    print("="*50)
    print("Initial Character Stats:")
    print("="*50)
    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    archer.display_stats()
    print()
    rogue.display_stats()
    
    print("\n" + "="*50)
    print("Combat Simulation:")
    print("="*50)
    
    # Warrior attacks mage
    print(f"\n{warrior.name} attacks {mage.name}!")
    warrior.attack(mage)
    print(f"{mage.name}'s health after attack: {mage.health}")
    
    # Mage attacks warrior
    print(f"\n{mage.name} attacks {warrior.name}!")
    mage.attack(warrior)
    print(f"{warrior.name}'s health after attack: {warrior.health}")
    
    # Archer attacks rogue
    print(f"\n{archer.name} attacks {rogue.name}!")
    archer.attack(rogue)
    print(f"{rogue.name}'s health after attack: {rogue.health}")
    
    # Rogue takes direct damage
    print(f"\n{rogue.name} takes 30 points of damage from a trap!")
    rogue.take_damage(30)
    print(f"{rogue.name}'s health after trap: {rogue.health}")
    
    print("\n" + "="*50)
    print("Final Character Stats:")
    print("="*50)
    warrior.display_stats()
    print()
    mage.display_stats()
    print()
    archer.display_stats()
    print()
    rogue.display_stats()

