class Actor:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# test Class:
""" 
actor1 = Actor(name="Tom Hanks", age=65, gender="Male")
print(actor1)  # This will call the __str__ method and display actor1's details
"""
