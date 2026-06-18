
class Dog():
    def bark(self):
        return 'woof'
    x='Hello'
Roger=Dog()
print(Roger.bark())
print(Roger.x)
del Roger
#class cannot be empty... so if you want to create an empty class... put pass in the block such as
class People():
    pass
