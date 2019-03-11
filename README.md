# meta-fido-example
The following files are simple examples to be used as an introduction to metaprogramming
in Python. The examples are written in Python3 but can be run in Python2 with some
modification. Below I've left a brief description of what each file is designed to help
teach.

# dog.py
This gives us our first simple Python class, the `Dog` class. Note the inclusion here
of the `have_birthday` function which changes the internal state of the dog object which
will be important later. Secondly, note that when you run this code, we can see that Fido
and Rover are written to different places in memory (check the hex code on the output
when running the file)

# fido.py
Here we create a new class for a specific dog. Creating a class rather than a new object
can be advantageous to make something more portable to be shared between many modules at
runtime. However note that still `fido1` and `fido2` are distict objects. This means that
when `fido1` has a birthday, `fido2` does not and it's age stays the same. Herein lies a
problem of creating a class for a specific instance of an object.

# angry_fido.py
This is our first introduction to metaprogramming. Here, we define a metaclass. A metaclass
can be considered a class that defines class behaviour rather than what that class is. We
introduce the `Anger` metaclass. Note that this could be applied to any class such as `Cat`
or `Student`. Here, we inject the `Anger` metaclass into `Fido` to create the `AngryFido`
class which has a class property without explicitly defining it.

# single_fido.py
Finally, we will solve the problem found in `fido.py` using metaprogramming. In this module,
we create a metaclass from Singleton. A Singleton is a design pattern that causes only one instance
of a class to exist at any point in time. It is a metaclass since we have described only the
behaviour of a class without encapsulating any properties or functions of a class like we did
with `Dog`.

When we inject our metaclass into `Fido` this time, we can see that there is a single instance
of `PetFido` written to memory even when we instantiate 2 `PetFido` objects. When you run the
module, you will see that even when `fido1` has a birthday, `fido2` will also have a birthday since
they are the same object.

