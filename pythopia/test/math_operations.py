# Modular programming

# function --> Class --> Module --> Package
"""
this modeul provides basic arithmetic algorithms.
"""


def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

__all__ = ['add', 'sub', 'mul', 'div']

#  Modules are built for import and scripts are built for execusion
# but sometime you want to execute the models too
# When: for testing the module

if __name__ == "__main__":
    assert sub(1, 2) == -1
    assert add(1, 2) == 3
    assert mul(1, 2) == 2
    print("All tests passed")

    