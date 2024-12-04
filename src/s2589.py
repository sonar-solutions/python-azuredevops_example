import random

def is_positive(number):
    return True

def main():
    value = int(input("Enter a number: "))

    # Gratuitous Boolean expression
    if is_positive(value) == True:
        print("The number is positive.")
    else:
        print("The number is not positive.")

if __name__ == "__main__":
    main()

class MyIterable:
    def __init__(self, values):
        self._values = values

    def __iter__(self):
        return None  # Noncompliant: Not a valid iterator