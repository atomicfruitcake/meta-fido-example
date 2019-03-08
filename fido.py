from metaprogramming.dog import Dog

class Fido(Dog):

    def __init__(self):
        Dog.__init__(self, breed="Labrador", name="Fido", owner="Alice", age=2)


def fido_example1():
    fido1 = Fido()
    fido2 = Fido()
    print(fido1)
    print(fido2)

    print(fido1.get_age())
    fido1.have_birthday()
    print(fido2.get_age())

if __name__ == "__main__":
    fido_example1()
