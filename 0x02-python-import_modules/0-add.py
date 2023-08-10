#!/usr/bin/python3

# Defining  the variables
a = 1
b = 2

def main():
    """Print the sum of 1 and 2."""
    from add_0 import add
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    main()
