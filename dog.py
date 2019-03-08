class Dog:

    def __init__(self, breed, name, age, owner):
        self.breed = breed,
        self.name = name
        self.age = age
        self.owner = owner


    def speak(self):
        print("Woof!")

    def get_age(self):
        return self.age

    def have_birthday(self):
        print("Pet Dog {name} had a birthday".format(name=self.name))
        self.age += 1

    bark = speak


def pet_dogs_example():
    fido = Dog(breed="labrador", name="Fido", age=2, owner="Alice")
    rover = Dog(breed="spaniel", name=  "Rover", age=3,  owner="Bob")
    print(fido)
    print(rover)


if __name__ == "__main__":
    pet_dogs_example()
