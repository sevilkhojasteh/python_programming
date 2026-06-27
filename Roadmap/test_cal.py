from calculator import square

def main():
    test_square()



def test_square():
    try:
        assert square(2) == 4
        assert square(3) == 9
        assert square(4) == 16
        assert square(5) == 25
    except AssertionError:
        print("3 squared was not 9")

# if the test_square is wrong we have assertionError


if __name__ == "__main__":
    test_square()