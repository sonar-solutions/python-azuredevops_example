class MyClass(object):
    def __init__(self):
        self.message = 'Hello'
        return self  # Noncompliant: a TypeError will be raised



if not a == 2:        # Noncompliant
    b = not i < 10    # Noncompliant
