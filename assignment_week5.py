# First, I'm creating the base class "Superhero" to represent general superhero attributes and actions.
class Superhero:
    def __init__(self, name, power, alias):
        # Using a constructor to initialize each superhero object with unique values
        self.name = name
        self.power = power
        self.alias = alias
    
    # Adding a method to describe the superhero's abilities
    def describe(self):
        return f"{self.name}, famously known as {self.alias}, possesses {self.power}!"
    
    # Adding an action method to simulate the superhero saving the day
    def action(self):
        return f"{self.alias} uses {self.power} to save the city!"

# Now I'm building a Kryptonian subclass to demonstrate inheritance and polymorphism.
class Kryptonian(Superhero):
    def __init__(self, name, power, alias, planet):
        # Leveraging the parent class constructor to initialize common attributes
        super().__init__(name, power, alias)
        self.planet = planet  # Adding a unique attribute for Kryptonians
    
    # Overriding the describe method for Kryptonians to highlight their origin
    def describe(self):
        return f"{self.alias}, a Kryptonian from {self.planet}, wields the mighty power of {self.power}!"

# To fulfill the second activity, I'm designing a polymorphism challenge with animals 🐕
class Animal:
    # Defining a generic move method for the parent class
    def move(self):
        return "This animal moves in a unique way."

class Bird(Animal):
    # Customizing the move method for birds
    def move(self):
        return "Soaring through the skies with elegance! 🕊️"

class Fish(Animal):
    # Customizing the move method for fish
    def move(self):
        return "Gliding swiftly in the water! 🐟"

class Dog(Animal):
    # Customizing the move method for dogs
    def move(self):
        return "Running enthusiastically on land! 🐕"

# Now it's time to put everything together in the main program.
if __name__ == "__main__":
    # Creating instances of superheroes to demonstrate inheritance and encapsulation
    superman = Kryptonian("Clark Kent", "Super Strength", "Superman", "Krypton")
    batman = Superhero("Bruce Wayne", "Martial Arts", "Batman")
    
    # Creating instances of animals to showcase polymorphic behavior
    bird = Bird()
    fish = Fish()
    dog = Dog()
    
    # Displaying superhero information
    print(superman.describe())  # Superman's enhanced description
    print(batman.describe())    # Batman's basic description
    print(superman.action())    # Superman in action!
    
    # Demonstrating polymorphism with animal movements
    print(bird.move())  # Bird-specific movement
    print(fish.move())  # Fish-specific movement
    print(dog.move())   # Dog-specific movement