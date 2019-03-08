from metaprogramming.fido import Fido

class SingleMetaDog(type):

    _instances = {}
    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(SingleMetaDog, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PetFido(Fido, metaclass=SingleMetaDog):
    pass


def fido_example3():
    fido1 = PetFido()
    fido2 = PetFido()
    print(fido1)
    print(fido2)

    print(fido1.get_age())
    fido1.have_birthday()
    print(fido2.get_age())


if __name__ == "__main__":
    fido_example3()
