from cryptography.hazmat.primitives import hashes

"""
Calculator library containing basic math operations.
"""
# My Calculator


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    return first_term // second_term


def divide_fl(first_term, second_term):
    return first_term / second_term


def square(first_term):
    return first_term ** 2


def cube(first_term):
    return first_term ** 3


def power(first_term, second_term):
    return first_term ** second_term


def mod(first_term, second_term):
    return first_term % second_term
    # This is the modulo function that barry asked for


def square_root(first_term):
    return first_term ** (1.0 / 2)


def itob(first_term):
    """convert an int to bin"""
    if type(first_term) == int:
        return bin(first_term)
    else:
        raise TypeError


if __name__ == "__main__":

    FILENAME = "test.txt"
    print("Test hash algorithm MD5 is weak")
    print("Done")
    fileDigest3 = hashes.Hash(hashes.MD5())
    with open(FILENAME, "rb") as reader:
        # Read and add line to fileDigest
        for line in reader:
            fileDigest3.update(line)

    fileProduct3 = fileDigest3.finalize()
    print(fileProduct3.hex())
