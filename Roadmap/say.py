import sys

from sayings import hello, goodbye

if len(sys.argv) ==2:
    name = sys.argv[1]
    hello(name)
    goodbye(name)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    print("Too few command-line arguments")
    sys.exit(1)