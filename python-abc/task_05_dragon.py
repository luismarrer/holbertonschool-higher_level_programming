class SwimMixin:
    """
    Mixin class that provides swim functionality.
    """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """
    Mixin class that provides fly functionality.
    """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swim and fly capabilities from mixins.
    """
    def roar(self):
        print("The dragon roars!")

