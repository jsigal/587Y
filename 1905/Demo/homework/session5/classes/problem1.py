# 1.	Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
from datetime import date


class Person:
    """A class to represent a person with name, country, and date of birth."""
    
    def __init__(self, name, country, date_of_birth):
        """
        Initialize a Person object.
        
        Args:
            name (str): The person's name
            country (str): The person's country
            date_of_birth (date): The person's date of birth as a date object
        """
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def get_age(self):
        """
        Calculate and return the person's age in years.
        
        Returns:
            int: The person's age in years
        """
        today = date.today()
        age = today.year - self.date_of_birth.year
        
        # Adjust age if birthday hasn't occurred this year
        if today.month < self.date_of_birth.month or \
           (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        
        return age
    
    def __str__(self):
        """Return a string representation of the person."""
        return f"{self.name} from {self.country}, born on {self.date_of_birth}"


# Test the implementation
if __name__ == '__main__':
    # Test case 1: Person with birthday already passed this year
    person1 = Person("John Doe", "USA", date(1990, 5, 15))
    print(f"Test 1: {person1}")
    print(f"Age: {person1.get_age()} years")
    print()
    
    # Test case 2: Person with birthday not yet passed this year
    person2 = Person("Jane Smith", "Canada", date(2000, 12, 25))
    print(f"Test 2: {person2}")
    print(f"Age: {person2.get_age()} years")
    print()
    
    # Test case 3: Person born today (edge case)
    person3 = Person("Bob Johnson", "UK", date.today())
    print(f"Test 3: {person3}")
    print(f"Age: {person3.get_age()} years")
    print()
    
    # Test case 4: Person with birthday today
    today = date.today()
    person4 = Person("Alice Brown", "Australia", date(today.year - 25, today.month, today.day))
    print(f"Test 4: {person4}")
    print(f"Age: {person4.get_age()} years")
    print()
    
    # Test case 5: Older person
    person5 = Person("Charlie Wilson", "Germany", date(1985, 3, 10))
    print(f"Test 5: {person5}")
    print(f"Age: {person5.get_age()} years")
