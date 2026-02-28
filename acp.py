class Dog:
    """A simple class to represent a dog."""
    # Class variable (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, breed):
        """Initialize name and breed instance variables."""
        # Instance variables (unique to each instance)
        self.name = name
        self.breed = breed

    def display_details(self):
        """Display the details of the dog instance."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        # Accessing the class variable using the class name is a good practice
        print(f"Species: {Dog.species}")
        print("-" * 20)

# Create two instances of the Dog class
dog1 = Dog(name="Buddy", breed="Golden Retriever")
dog2 = Dog(name="Charlie", breed="Poodle")

# Display the details of the two dog breeds
print("Details of the dogs:")
print("-" * 20)
dog1.display_details()
dog2.display_details()
