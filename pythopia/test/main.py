# Basic import statement
import math_operations
import sys

print(sys.path)

result = math_operations.add(5, 3)
print(result)  # Output: 8

result = math_operations.sub(10, 4)
print(result)  # Output: 6

result = math_operations.mul(6, 7)
print(result)  # Output: 42


# Different methods to import

# Import entire module
import math_operations

# Import specific functions from the module
from math_operations import add,mul

# Import the entire module with an alias
# rename math_operations to mo
import math_operations as mo
from math_operations import add as a


# Import all Items from a module (use cautiously)
from math_operations import *

"""
Module search path:
1. the directory containing the input script
2. PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$PWD
echo $PYTHONPATH
in terminal
3. Standard library directories
4. Site-packages directories
5. Additional directories specified by the user

"""