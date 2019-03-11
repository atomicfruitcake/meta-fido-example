from metaprogramming.fido import Fido

class Anger(type):
    def angry(cls):
        print("{} is angry".format(type(cls())))
        return True

    def __call__(cls, *args, **kwargs):
        this = type.__call__(cls, *args, **kwargs)
        setattr(this, "angry", cls.angry)
        return this

class AngryFido(Fido, metaclass=Anger):
    pass


if __name__ == "__main__":
    angry_fido = AngryFido()
    print(angry_fido.angry())
