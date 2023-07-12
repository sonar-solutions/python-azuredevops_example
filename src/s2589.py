import random

def is_positive(number):
    return number > 0

def main():
    value = int(input("Enter a number: "))

    # Gratuitous Boolean expression
    if is_positive(value) == True:
        print("The number is positive.")
    else:
        print("The number is not positive.")

if __name__ == "__main__":
    main()

